import subprocess
import optparse

#linux System Mac address changer;

def Mac_Changer(interface,mac):
    #instead of use list to prevent the command execution
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

    print("[+] Your Mac Address is changed.new Mac Address is"+mac)

parser=optparse.OptionParser() #give commandline arguments

parser.add_option("-i","--interface",dest="interface",help="Interface to change mac Address") #that's help to set a flags
parser.add_option("-m","--mac",dest="mac",help="set mac address to change mac Address")


(options,arguments)=parser.parse_args() #parser understand the user input

interface=options.interface

mac=options.mac
Mac_Changer(interface,mac)

