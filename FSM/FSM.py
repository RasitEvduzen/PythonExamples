# -*- coding: utf-8 -*-
#!/usr/bin/python3    # Shebang! for Unix
"""
Created on %(date) s
@author: %(Rasit Evduzen)s
"""

#%%%
class StateMachine:
    def __init__(self):
            self.handlers = {}
            self.startState = None
            self.endStates = []
            
    def addState(self,name,handler,endState = 0):
        name = name.upper()
        self.handlers[name] = handler
        if endState:
            self.endStates.append(name)
            
    def setState(self,name):
        self.startState = name.upper()
    
    def runFSM(self,cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise ValueError("At Least One State Must be and End State")
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print(f"reached -> {newState}")
                break
            else:
                handler = self.handlers[newState.upper()]
                
                
positive = ["great","super", "fun", "entertaining", "easy"]
negative = ["boring", "difficult", "ugly", "bad"]               
        
def startTransitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "Python":
        newState = "PythonState"
    else:
        newState = "errState"
    return (newState, txt)
        

def pythonStateTransition(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "is":
        newState = "isState"
    else:
        newState = "errState"     
    return (newState, txt)          

def isStateTransitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "not":
        newState = "notState"
    elif word in positive:
        newState = "posState"
    elif word in negative:
        newState = "negState"
    else:
        newState = "errState"
    return (newState, txt)

def notStateTransitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word in positive:
        newState = "negState"
    elif word in negative:
        newState = "posState"
    else:
        newState = "errState"
    return (newState, txt)

def negState(txt):
    print("Hello World!")
    return ("negState", "")

FSMexample = StateMachine()
FSMexample.addState("Start", startTransitions)
FSMexample.addState("PythonState", pythonStateTransition)
FSMexample.addState("isState", isStateTransitions)
FSMexample.addState("notState", notStateTransitions)
FSMexample.addState("negState", None, endState=1)
FSMexample.addState("posState", None, endState=1)
FSMexample.addState("errState", None, endState=1)
FSMexample.setState("Start")
FSMexample.runFSM("Python is great")
FSMexample.runFSM("Python is difficult")
FSMexample.runFSM("Perl is ugly")


#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%



