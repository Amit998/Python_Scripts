import subprocess
import optparse 
import re



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

if_config_result=subprocess.check_output(["ifconfig",options.interface])

mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:",if_config_result)
if mac_address_search_result.group(0):
    print(mac_address_search_result.group(0))
else:
    print("[ - ] could ot read MAC address")