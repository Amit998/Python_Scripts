import subprocess
import optparse 

# interface="wlan0"
# interface2="eth"


# new_mac="00:11:22:33:44:55"

# parser=optparse.OptionParser()
# parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
# parser.add_option("-m","--mac",dest="new_mac",help="New Mac Address")
# (options,arguments)=parser.parse_args()


# interface=input("interface >")
# # interface2=input("new MAC >")


# new_mac="00:11:22:33:44:55"


# interface=options.interface
# new_mac=options.new_mac

# print("[+] chaning mac address for "+interface +" to "+new_mac)

# subprocess.call(f"ifconfig {interface} down",shell=True)
# subprocess.call(f"ifconfig {interface} hw ether {new_mac}",shell=True)
# subprocess.call(f"ifconfig {interface} up",shell=True)


# subprocess.call(['ifconfig',interface,"down"])
# subprocess.call(['ifconfig',interface,"hw","ether",new_mac])
# subprocess.call(['ifconfig',interface,"up"])


# def get_arguments():
#     parser=optparse.OptionParser()
#     parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
#     parser.add_option("-m","--mac",dest="new_mac",help="New Mac Address")
#     return parser.parse_args()



# def change_mac(interface,new_mac):
#     print("[+] chaning mac address for "+interface +" to "+new_mac)
#     subprocess.call(['ifconfig',interface,"down"])
#     subprocess.call(['ifconfig',interface,"hw","ether",new_mac])
#     subprocess.call(['ifconfig',interface,"up"])

# (options,arguments)=get_arguments()
# change_mac(options.interface,options.new_mac)


def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m","--mac",dest="new_mac",help="New Mac Address")
    (options,arguments)= parser.parse_args()

    if not options.interface:
        parser.error(f"[-] please specify an interface , use --help for more info")
    
    elif not options.new_mac:
        parser.error(f"[-] please specify an mac address , use --help for more info")
    
    return options




def change_mac(interface,new_mac):
    print("[+] chaning mac address for "+interface +" to "+new_mac)
    subprocess.call(['ifconfig',interface,"down"])
    subprocess.call(['ifconfig',interface,"hw","ether",new_mac])
    subprocess.call(['ifconfig',interface,"up"])

options=get_arguments()
change_mac(options.interface,options.new_mac)

