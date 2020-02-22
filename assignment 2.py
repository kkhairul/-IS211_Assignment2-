#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib
import csv
import argparse
import sys
import datetime
import logging
import urllib2


persons={}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', 
                        by_default = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv', 
                        type = str)
    args = parser.parse_args()
    if args.input == None:
        sys.exit()
        
# PART II

def downloadData(url):  
    dwnld = url
    urllib.request.urlretrieve(dwnld, 'data.csv')
    
# PART III

def processData(data):
    
    logging.basicConfig(filename = 'errors.log', 
                    format = '%(asctime)s %(message)s', 
                    filemode = 'w') 
  
    #Creating an object 
    assignment2 = logging.getLogger() 
  
    #Setting the threshold of logger to DEBUG 
    assignment2.setLevel(logging.DEBUG) 

    reader = csv.DictReader(data)
    n = 1
    pid = 0
    for raw in reader:
        try:            
            pid = int(raw['id'])
            name = raw['name']
            dob = datetime.datetime.strptime(raw['birthday'], "%d/%m/%Y").strftime("%d/%m/%y")
            persons[pid] = (name, dob)
            n += 1
        except:
           
            assignment2.error("Error processing line %i for ID  %i", n, pid) 
            n += 1   
            
# PART IV
                 
def displayPerson(pid,dic):
    if pid in dic:
         print("Person #", pid, "is", dic[pid][0], "with a birthday of", dic[pid][1])    
    else:
         print("No user found with that ID")           
            
def main():
    url = str(input("Enter Url: "))
    downloadData(url)
    fp = open('data.csv')
    processData(fp)
    
    while True:
        pid = int(input("Enter ID: "))
        if pid >= 1:
            displayPerson(pid, persons)
        else:
            sys.exit()
    
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




