#!/usr/bin/env/ python

#Created by ADrunkRussian
#Github.com/ADrunkRussian
#Contact me on twitter @ADrunkRussian1
# V1.1

import os
import urllib2
import json
import codecs

os.system('cls' if os.name == 'nt' else 'clear')
ans=True
while ans:
	print 
	print '=============================================='
	print '#          Public Information Search         #'
	print '#             Tool For Collecting            #'
	print '#                   Emails                   #'	
	print '=============================================='
	print("1. The Harvester - Collects Emails from google and bing")
	print("2. Dmitry - Searches for Subdomains, Emails, TCP port scans and does whois lookups")	
	#print("3. MSFConsole Search_email_Collector - Collects Emails from Google, Bing and PGP")
	print("0. Download or update modules")
	ans=raw_input(
"""
Which tool would you like to use? (Select Your tool)
""")
	
	if ans=="1":
		os.system('cls' if os.name == 'nt' else 'clear')

		ans=True
		while ans:
		
			print 
			print '=============================================='
			print '#               The Harvester                #'
			print '=============================================='
			domain=raw_input("""What is your domain? (i.e google.com)
"""
)

			os.system('cls' if os.name == 'nt' else 'clear')
			engine=raw_input("""What data source would you like to use? (google, googlecse, bing, bingapi, pgp, linkedin, google-profiles, people123, jigsaw, twitter, googleplus, all)
""")
			os.system('cls' if os.name == 'nt' else 'clear')
			limit=raw_input("""Limit the number of results to work with: (enter a number)
""")
			os.system("sudo theharvester" + " -d " + domain+ " -l " + limit+ " -b " +engine)
			
			print """

If you do not see any results above, The Harvester did not find anything. Don\'t give up, there are other methods."""
			

			break

	if ans=="0":
		os.system('cls' if os.name == 'nt' else 'clear')
	
		ans=True
		while ans:
			print 
			print '=============================================='
			print '#          Public Information Search         #'
			print '#             Tool For Collecting            #'
			print '#                   Emails                   #'	
			print '=============================================='
			print '1. The Harvester'
			#print '2. Metasploit'
			print '9. Return to Main Menu'
			upgrade=raw_input("What would you like to update or download?")
			if upgrade=="1":
					os.system("sudo apt-get install theharvester")
					print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGreat! Everything is installed now!'
					break
					
			#if upgrade=="2":
					#os.system('cls' if os.name == 'nt' else 'clear')
					#print '\n\n\n\nWe currently are not supporting Metasploit installations. Sorry'
				
	if ans=="2":
		os.system('cls' if os.name == 'nt' else 'clear')
	
		ans=True
		while ans:
			print 
			print '=============================================='
			print '#                   Dmitry                   #'
			print '=============================================='
			print 'Searches for Emails, Subdomains, Performs TCP '
			print 'port scans and WHOIS lookups\n'
			ddomain=raw_input("What is the domain you would like to search?\n")
			options=raw_input("""\nWhat are the options you would like to include in your search?
-i WhoIs lookup
-n NetCraft.com information
-p TCP port scan on a host
-f TCP Filtered scan 
-b Read in the banner recieved
-s Possible Subdomains
-e Possible Email addresses
-t Set TTL in seconds for port scanning (Default 2)

Seperate all options with a space. (I.e -i -n -p)
""")
			os.system("sudo dmitry "  + options + " " + ddomain)
			break
