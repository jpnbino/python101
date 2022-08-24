import serial.tools.list_ports

ports = sorted(serial.tools.list_ports.comports())

def print_com_details(i):
        print("------------------------------------------") 
        print(f"device: \t{ports[i].device}")
        print(f"name: \t\t{ports[i].name}")
        print(f"description: \t{ports[i].description}")
        print(f"hwid: \t\t{ports[i].hwid}")
        print(f"vid: \t\t{ports[i].vid}")
        print(f"serial_number: \t{ports[i].serial_number}")
        print(f"location: \t{ports[i].location}")
        print(f"manufacturer: \t{ports[i].manufacturer}")
        print(f"product: \t{ports[i].product}")
        print(f"interface: \t{ports[i].interface}")



#prints short list
for port, desc, hwid in ports:
        print("{}: {} [{}]".format(port, desc, hwid))

#prints detailed list
for x in range(0, len(ports)):
        print(x)
        print_com_details(x)

print(help(ports[1]))