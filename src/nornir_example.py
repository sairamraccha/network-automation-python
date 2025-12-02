import argparse
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--inventory', required=True)
    args = parser.parse_args()

    nr = InitNornir(config_file=None, inventory={'plugin': 'nornir.plugins.inventory.simple.SimpleInventory', 'options': {'hosts_file': args.inventory}})

    def show_config(task):
        r = task.run(task=netmiko_send_command, command_string='show running-config')
        task.host['running'] = r.result

    results = nr.run(task=show_config)
    print_result(results)
