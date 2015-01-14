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
         
cc = CodeChallenge();
print cc.reverseString()
         
         

