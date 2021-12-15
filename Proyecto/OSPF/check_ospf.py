from netmiko import ConnectHandler
import colorama
from colorama import Fore, Style


devices = '''
R1
R2
R3
R4
R5
R6
R7
R8
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'admin'
password = '1234'
verbose = True

for device in devices:
        print(" " * 18 + " Conectando con el dispositivo: " + device)
        print(Style.RESET_ALL)
        net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()

        output = net_connect.send_command('show run | sec ospf')
        ospf_commands = ['router ospf 1', 'net 0.0.0.0 255.255.255.255 area 0']
        if not 'router ospf' in output:
            print("\n")
            print(' ' * 15 + Fore.WHITE + 'OSPF esta ' + Fore.RED + 'no' + Fore.WHITE + ' habilitado en el dispositivo: ' + device +'!' + Style.RESET_ALL)
            print("\n")
            answer = input('Quiere habilitar la configuracion OSPF en: ' + device + ' <y/n> ')
            if answer == 'y':
                output = net_connect.send_config_set(ospf_commands)
                print(output)
                print("\n")
                print(' ' * 20 + Fore.GREEN + 'OSPF configurado correctamente' + Style.RESET_ALL)
                print("\n")
            else:
                print("\n")
                print(' ' * 15 + Fore.RED + 'No se ha configurado OSPF correctamente' + Style.RESET_ALL)
                print("\n")

        else:
            print("\n")
            print( " " * 10 + " Ya esta configurado OSPF en este dispositivo:  " + device + "!")
            print("\n")
            print(Style.RESET_ALL)