#Evangelista Chicheko
#Code2040 API Challenge

import requests
import json
import httplib

class CodeChallenge:

     def __init__(self):
         self.token = "EbuXdMtJm3"
         self.email = "echicheko@css.edu"
         self.github ="https://github.com/evangelista94/CODE2040-API-Challenge"
         self.params = {"email": "echicheko@css.edu", "github": "https://github.com/evangelista94/CODE2040-API-Challenge", "token": "EbuXdMtJm3"}
         self.output ={};
        
     def sendPost(self,stage,params):         
         httpServ = httplib.HTTPConnection("challenge.code2040.org", 80)        
         
         stringParams = json.dumps(params)
         httpServ.request('POST', '/api/' +stage, stringParams)
         response = httpServ.getresponse()
         print str(response.status)
         if response.status == httplib.OK:
             print "Output from CGI request"
             self.output = response.read();
             print self.output
             
         httpServ.close()
     def printText(self, txt):
         lines = txt.split('\n')
         for line in lines:
             print line.strip()
     #problem 1 reversing the string####################################################################################################################
     def reverseString(self):
         self.sendPost('getstring',self.params)#get the word to be reversed from the server
         word = json.loads(self.output)["result"]#converting the returned string to json
         reversedWord = ""
         length = len(word)
         print word
         for i in range(length):
             reversedWord = reversedWord + word[length - i -1]
         
         #sending back the response to the server
         self.sendPost('validatestring',{"email": "echicheko@css.edu", "github": "https://github.com/evangelista94/CODE2040-API-Challenge", "token": "EbuXdMtJm3","string":reversedWord})
 
     #problem 2 finding a string in an array ############################################################################################################
     def needleHaystack(self):
         self.sendPost('haystack',self.params)#get the dictionary from the server
         dictionary = json.loads(self.output)["result"];
         needleValue = dictionary["needle"] # value of the needle in the returned dictionary
         hayStackArray = dictionary["haystack"]
         position = hayStackArray.index(needleValue)
         #sending back the response to the server
         self.sendPost('validateneedle',{"email": "echicheko@css.edu", "github": "https://github.com/evangelista94/CODE2040-API-Challenge", "token": "EbuXdMtJm3","needle":position})

     #problem 3 Prefix #############################################################333
     def prefixFree(self):
         self.sendPost('prefix',self.params)#get the dictionary from the server
         dictionary = json.loads(self.output)["result"]        
         array = dictionary["array"]       
         prefix = dictionary["prefix"]         
         lengthPrefix = len(prefix)
         
         
         prefixFreeArray = [i for i in array if (i[0:lengthPrefix]!= prefix)]
         
         self.sendPost('validateprefix',{"email": "echicheko@css.edu", "github": "https://github.com/evangelista94/CODE2040-API-Challenge", "token": "EbuXdMtJm3","array":prefixFreeArray})

          
          
         
cc = CodeChallenge();
print cc.reverseString()
print cc.needleHaystack()
print cc.prefixFree()

         

