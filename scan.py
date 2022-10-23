#!/usr/bin/python3
import subprocess
import re

# different tools
def nmap_scan(directory, domain):

    path = directory + '/nmap'

    with open(path, 'w') as nmap_file:
        cmd=['nmap',domain]
        subprocess.run(cmd, stdout=nmap_file) # writing tool output to a file
    print('The results of nmap are stored in ' + directory + '/nmap')

def dirb_scan(directory, domain):

    path = directory + '/dirb'
    url = 'http://' + domain

    with open(path, 'w') as dirb_file:
        cmd=['dirb', url, '/usr/share/dirb/wordlists/small.txt']
        subprocess.run(cmd, stdout=dirb_file) # writing tool output to a file    
    print('The results of dirb are stored in ' + directory + '/dirb')

def crt_scan(directory, domain):

    path = directory + '/crt'
    domain_regex = re.compile(r'^[a-z]?\.[a-z]{2,4}$')

    if re.match( r'^[a-z]*\.[a-z]{2,4}$', domain) != None: # check if input domain matches with a domain name and not a subdomain
        with open(path, 'w') as crt_file:
            cmd_url = 'https://crt.sh/?q=' + domain + '&output=json'
            output_file = directory + '/crt'
            cmd=[cmd_url, '-o', output_file]
            subprocess.run(cmd, stdout=crt_file, shell=True) # writing tool output to a file
        print('The results of cert parsing are stored in ' + directory + '/crt') 
    else:
        print('Certificate parsing is only performed on valid domain names, not on subdomains!')  
