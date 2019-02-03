import json,string,sys,os,re

FILE = "/etc/passwd"

def main():
 f_in = open (FILE,'r')
 pwd_data = []
 pwd_ent = {}

 for line in f_in:
  line_element = line.split(":")
  linelen = len(line_element)
  if linelen<=1:
   # its not likely valid
   continue
  if int(line_element[2])<1000:
   # its probably a system user
   continue
  if int(line_element[2])>65000:
   # probably not a user either
   continue
  pwd_ent = {
   'name':line_element[0],
   'passwd':line_element[1],
   'uid':int(line_element[2]),
   'gid':int(line_element[3]),
   'gecos':line_element[4],
   'dir':line_element[5],
   'shell':line_element[6]
   }
  pwd_data.append(pwd_ent)
    
 print("%s" % json.dumps(pwd_data))

main()
