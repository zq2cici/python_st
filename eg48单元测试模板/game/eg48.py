# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:05:24 2017

@author: pc-541
"""
'''
class Lexicon(object):
 
    def __init__(self):
        self.direction=[('direction','north'),
                         ('direction','south'),
                         ('direction','east')]
        self.verb = [('verb','go'),
                     ('verb','kill'),
                     ('verb','eat')]
        self.stop = [('stop','the'),
                     ('stop','in'),
                     ('stop','of')]
        self.noun = [('noun','bear'),
                     ('noun','princess')]
        self.error= [('error','ASDFADFASDF'),
                     ('error', 'IAS')]
        self.WORD = self.direction+self.verb+self.stop+self.noun+self.error
       
    def scan(self,inputData):
        result =[]
        input_data = inputData.split()
        for word in input_data:
            try:
                result.append(('number',int(word)))
            except ValueError:    
                for i in range(len(self.WORD)):
                    if word == self.WORD[i][1]:
                         result.append(self.WORD[i])
                         
        return result
    
lexicon = Lexicon()
'''      
'''
print("result = {} ".format(lexicon.scan('44 55')) ) 
print("result = {} ".format(lexicon.scan('in')) )     
'''
class Lexicon(object):
 
    def __init__(self):
        self.direction=[('north','south','east')]
        self.verb = [('go','kill','eat')]
        self.stop = [('the','in','of')]
        self.noun = [('bear','princess')]
        self.error= [('ASDFADFASDF','IAS')]
        self.WORD = self.direction+self.verb+self.stop+self.noun+self.error
        self.ACTION =['direction','verb','stop','noun','error']
    def scan(self,inputData):
        result =[]
        input_data = inputData.split()
        for word in input_data:
            try:
                result.append(('number',int(word)))
            except ValueError:    
                for i in range(len(self.WORD)):
                    if word in self.WORD[i]:
                         result.append((self.ACTION[i],word))
                         break
        return result
    
lexicon = Lexicon()
'''
print("WORD= {} ".format(lexicon.WORD) )
print("result = {} ".format(lexicon.scan('44 55')) ) 
print("result = {} ".format(lexicon.scan('north of go')) )
print("result = {} ".format(lexicon.scan('of 44 55 IAS')) )      
'''



