#!/usr/bin/env/ python

#Created by ADrunkRussian
#Github.com/ADrunkRussian
#Contact me on twitter @ADrunkRussian1
# V1.2

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
	print("0. The Harvester - Collects Emails from google and bing\n")
	print("1. Dmitry - Searches for Subdomains, Emails, TCP port scans and does whois lookups\n")
	print("2. Metagoofil- Tool for extraction of metadata from public documents belonging to a target company\n")	
	#print("3. MSFConsole Search_email_Collector - Collects Emails from Google, Bing and PGP")
	print("8. Download or update modules\n")
	ans=raw_input(
"""Which tool would you like to use? (Select Your tool)
""")
	
	if ans=="0":
		os.system('cls' if os.name == 'nt' else 'clear')

		ans=True
		while ans:
			try:
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
			except:
				print 'You do not The Harvester installed.'
				break 	
#This is the beginning for Metagoofil
	if ans=="2":
		os.system('cls' if os.name == 'nt' else 'clear')

		ans=True	
		while ans:
			print 
			print '=============================================='
			print '#                 Metagoofil                 #'
			print '=============================================='
			print 
			limit="200"
			MDomain=raw_input("What is the website you would like to search?\n")
			filetype=raw_input("What is the filetype you would like to download? (pdf, doc, xls, ppt, odp, ods, docx, xlsx, pptx)\n")
			limit=raw_input("To how many searches would you like to limit your search to? (Default 200)\n")
			dllim=raw_input("Limit of files to download\n")
			wdir=raw_input("What would you like your working directory to be?\n")
			outf=raw_input("Would you like to output a file? (Y/N)\n")
			if outf=="Y":
					outf="-f"
			os.system("sudo metagoofil " + "-d "+ MDomain + " -t " + filetype + " -l "+ limit + " -n "+ dllim + " -o " + wdir + " -f " + outf) 

#This is beginning for updates and installation	
	
	if ans=="1":
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

	if ans=="8":
		os.system('cls' if os.name == 'nt' else 'clear')
	
		ans=True
		while ans:
			
			print 
			print '=============================================='
			print '#          Public Information Search         #'
			print '#             Tool For Collecting            #'
			print '#                   Emails                   #'	
			print '=============================================='
			print '0. The Harvester'
			print '1. Dmitry'
			print '2. Metagoofil'
			#print '2. Metasploit'
			print '9. Return to Main Menu'
			upgrade=raw_input("What would you like to update or download?\n")
#Updates The Harvester
			if upgrade=="0":
					os.system("sudo apt-get install theharvester")
					print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGreat! Everything is installed now!'
					break
#Updates Dmitry
			if upgrade=="1":
					os.system("sudo apt-get install dmitry")
					print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGreat! Everything is installed now!'
					break
#Updates Metagoofil
 			if upgrade=="2":
					os.system("sudo apt-get install metagoofil")
					print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nGreat! Everything is installed now!'
					break
#Main Menu
			if upgrade=="9":
					os.system('cls' if os.name == 'nt' else 'clear')
					break
					
			#if upgrade=="2":
					#os.system('cls' if os.name == 'nt' else 'clear')
					#print '\n\n\n\nWe currently are not supporting Metasploit installations. Sorry'
				
