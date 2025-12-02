import argparse, os, yaml
from netmiko import ConnectHandler
from datetime import datetime

def load_inventory(path):
    with open(path) as f:
        return yaml.safe_load(f)

def backup_device(hostname, hostdata, output_dir):
    device = {
        'device_type': 'cisco_ios',
        'host': hostdata['hostname'],
        'username': hostdata.get('username'),
        'password': hostdata.get('password'),
    }
    conn = ConnectHandler(**device)
    running = conn.send_command('show running-config')
    conn.disconnect()
    filename = f"{hostname}_running_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.cfg"
    with open(os.path.join(output_dir, filename), 'w') as fh:
        fh.write(running)
    print(f"Backed up {hostname}")

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--inventory', required=True)
    p.add_argument('--output', default='backups')
    args = p.parse_args()
    inv = load_inventory(args.inventory)
    os.makedirs(args.output, exist_ok=True)
    for name, meta in inv.get('hosts', {}).items():
        try:
            backup_device(name, meta, args.output)
        except Exception as e:
            print(f"Failed {name}: {e}")
