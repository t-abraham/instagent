# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:48:17 2022

@author: Tahasanul Abraham
"""

#%% Initialization of Libraries and Directory

from pytimedinput import timedInput
import sys

#%% __userInput__

class __userInput__(object):
    def __init__(self):
        super().__init__()

    def ___userInput___(self, answers: list=[], retrys: int=3, prompt="", default=""):
        answers = [str(x).lower() for x in answers]
        for retry in range(retrys):
            ans = self._timedinput(prompt, default)
            if len(answers) == 0 or str(ans).lower() in answers:
                break
            else:
                self.___printout___ ("Wrong entry. Please select from these {} options:\n".format(answers), self.RED)
        return ans
    
    def _timedinput(self, prompt="", default=""):
        if len(prompt) > 0:
            prompt = str(prompt) + " [{} seconds timeout] >> ".format(self.timeout)
        else:
            prompt = "[{} seconds timeout] >> ".format(self.timeout)
        
        if sys.__stdin__.isatty():
            userText, timedOut = timedInput(prompt=prompt, timeout=self.timeout)
        
            if timedOut is True:
                self.___printout___ ("Timed out when waiting for input.", self.RED)
        else:
            userText = input(">> ")
            
        if len(userText) == 0:
            userText = default
            
        return userText
            
#%% Standalone Run    
if __name__ == "__main__":
    pass

