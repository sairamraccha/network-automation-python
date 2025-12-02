import argparse, yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler

def render_template(template_path, variables):
    env = Environment(loader=FileSystemLoader('.'))
    tmpl = env.get_template(template_path)
    return tmpl.render(**variables)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--template', required=True)
    parser.add_argument('--vars', default='')
    args = parser.parse_args()

    vars_map = {}
    if args.vars:
        for pair in args.vars.split(','):
            if ':' in pair:
                k, v = pair.split(':', 1)
                vars_map[k.strip()] = v.strip()

    device = {
        'device_type': 'cisco_ios',
        'host': args.host,
        'username': vars_map.get('username'),
        'password': vars_map.get('password'),
    }

    config = render_template(args.template, vars_map)
    conn = ConnectHandler(**device)
    output = conn.send_config_set(config.splitlines())
    print(output)
    conn.save_config()
    conn.disconnect()
