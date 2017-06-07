#!/usr/bin/python3
##########################################################
#       All                                              #
# Author: BAHATI Phill                                   #
# E-mail: bahatiphill@protonmail.com                     #
# Twitter: @bahatiphill                                  #
#                                                        #
##########################################################

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
from termcolor import colored, cprint


def do_scan(targets, options):
    parsed = None
    nmproc = NmapProcess(targets, options)
    rc = nmproc.run()
    if rc != 0:
        cprint("nmap scan failed", 'red')
        print("\n")
        print("{0}".format(nmproc.stderr))
    print(type(nmproc.stdout))

    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except NmapParserException as e:
        print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed


# print scan results from a nmap report
def print_scan(nmap_report):
    print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(
        nmap_report.version,
        nmap_report.started))

    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)


def onStart():

    print("\n")
    print("\n")

    cprint("#############  HERE A LIST OF RWANDAN ISP!  #################",'green')
    cprint("You choose a number of which ISP u want to scan its customers", 'green')
    print("\n")
    print("1. Olleh Rwanda")
    print("2. MTN RwandaCell")
    print("3. New Artel")
    print("4. Rwanda Ministry of Education")
    print("5. Airtel")
    print("6. BSC(BroadBand System Corporation)")
    print("\n")

    choosenISP = input("Chose a number: ")
    print("\n")
    try:
        choosenISP = int(choosenISP)
    except:
        cprint("SORRY, You didn't enter a number",'red')

    ISPsIP= ["41.74.160-175.0-255 105.178-179.0-255.0-255", "41.186.0-255.0-255 196.44.240-255.0-255","41.197.0-255.0-255","154.68.64-127.0-255","197.157.128-191.0-255","197.243.0-127.0-255"]
    
    if choosenISP <= len(ISPsIP) and choosenISP >= 1:
        choosenISP = ISPsIP[choosenISP - 1]
        report = do_scan(choosenISP, "-sn")
        if report:
            print_scan(report)
        else:
            cprint("No results returned",'red')
    else:
        cprint("SORRy, choose a number on the ISPs list",'green')



if __name__ == "__main__":
    onStart()