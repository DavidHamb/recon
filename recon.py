#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Based on Vickie Li's book 'Bug Bounty Bootcamp' and translated from bash scripting

# Function library
from doctest import master
import scan
import os
import argparse
import datetime
import re

# Defining options
parser = argparse.ArgumentParser()
parser.add_argument('--mode', help = 'Choose the tools you want to use : nmap-only, dirb-only, cert-only, all', required = True, dest = 'mode')
args = parser.parse_args()
mode = args.mode

domain =''

while domain != 'quit': # repeat the program until the user wants to quit

    domain = input('Please enter a new domain (or quit)! ')

    if domain != 'quit':
        directory = domain + '_recon'

        def master_report(): # preparing a master report
            print('Generating output report for ' + domain)
            date = datetime.datetime.now()
            date = date.strftime('%Y-%m-%d')

            path = directory + '/report'

            with open(path, 'a') as report:
                report.write('This scan was created on ' + date + '\n') # Adding the date of the scan to the output
                if os.path.exists('./' + directory + '/nmap'):
                    report.write('\nResults for nmap : \n')
                    with open(directory + '/nmap') as nmap_result:
                        nmap_result = nmap_result.read()
                        parsed_nmap = re.findall(r'\d{1,5}/\w+\s+\w+\s+\w+', nmap_result) # Parsing the results
                        for element in parsed_nmap:
                            report.write(element + '\n')

                if os.path.exists('./' + directory + './dirb'):
                    report.write('\nResults for dirb : \n')
                    with open(directory + '/dirb') as dirb_result:
                        dirb_result = dirb_result.read()
                        report.write(dirb_result)

                if os.path.exists('./' + directory + '/crt'):
                    report.write('\nResults for crt.sh : \n')
                    with open(directory + '/crt') as crt_result:
                        crt_result = crt_result.read()
                        report.write(crt_result)
     
        if not os.path.exists('./'+directory): # Only execute when directory doesn't exists
            print('Creating directory ' + directory)
            os.mkdir('./'+directory) 

        # performing recon
        if os.path.exists(directory + '/report'):
            os.remove(directory + '/report')

        if mode == 'nmap-only':
            scan.nmap_scan(directory, domain)
            master_report()
        elif mode == 'dirb-only':
            scan.dirb_scan(directory, domain)
            master_report()
        elif mode == 'cert-only':
            scan.crt_scan(directory, domain)
            master_report()
        elif mode == 'all':
            scan.nmap_scan(directory, domain)
            scan.dirb_scan(directory, domain)
            scan.crt_scan(directory, domain)
            master_report()
        else : 
            print('Please specify a valid mode!') # TODO automatically terminate the process
    else:
        print('Thanks for using our recon program and see you next time!')