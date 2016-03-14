#!/usr/bin/env/ python

#Created by ADrunkRussian
#Github.com/ADrunkRussian
#Contact me on twitter @ADrunkRussian1
# V1

import os
import urllib2
import json
import codecs

os.system('cls' if os.name == 'nt' else 'clear')

ans=True
while ans:
	print 
	print '==========================='
	print '#   Public Email Search   #'
	print '#   Tool For Collecting   #'
	print '#          Emails         #'	
	print '==========================='
	print("1. The Harvester - Collects Emails from google and bing")
	#print("2. MSFConsole Search_email_Collector - Collects Emails from Google, Bing and PGP")
	ans=raw_input("Which tool would you like to use? \(Select Your tool)")
	
	if ans=="1":
		os.system('cls' if os.name == 'nt' else 'clear')

		ans=True
		while ans:
		
			print 
			print '==========================='
			print '#      The Harvester      #'
			print '==========================='
			domain=raw_input("What is your domain? (i.e google.com)"
)

			os.system('cls' if os.name == 'nt' else 'clear')
			engine=raw_input("What data source would you like to use? (google, googlecse, bing, bingapi, pgp, linkedin, google-profiles, people123, jigsaw, twitter, googleplus, all)")
			os.system('cls' if os.name == 'nt' else 'clear')
			limit=raw_input("Limit the number of results to work with. (enter a number)")
			os.system("sudo theharvester" + " -d " + domain+ " -l " + limit+ " -b " +engine)
			
			print """If you do not see any results above, The Harvester did not find anything. Don\'t give up, there are other methods."""
			break

