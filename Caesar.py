# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:38:05 2021
@author: BangTheBanger

references:
ord > ascii
chr > char
"""
origin = {1: ' ', 2: '!', 3: '"', 4: '#', 5: '$', 6: '%', 7: '&', 8: "'", 9: '(', 10: ')',
          11: '*', 12: '+', 13: ',', 14: '-', 15: '.', 16: '/', 17: '0', 18: '1', 19: '2', 20: '3',
          21: '4', 22: '5', 23: '6', 24: '7', 25: '8', 26: '9', 27: ':', 28: ';', 29: '<', 30: '=',
          31: '>', 32: '?', 33: '@', 34: 'A', 35: 'B', 36: 'C', 37: 'D', 38: 'E', 39: 'F', 40: 'G',
          41: 'H', 42: 'I', 43: 'J', 44: 'K', 45: 'L', 46: 'M', 47: 'N', 48: 'O', 49: 'P', 50: 'Q',
          51: 'R', 52: 'S', 53: 'T', 54: 'U', 55: 'V', 56: 'W', 57: 'X', 58: 'Y', 59: 'Z', 60: '[',
          61: '\\', 62: ']', 63: '^', 64: '_', 65: '`', 66: 'a', 67: 'b', 68: 'c', 69: 'd', 70: 'e',
          71: 'f', 72: 'g', 73: 'h', 74: 'i', 75: 'j', 76: 'k', 77: 'l', 78: 'm', 79: 'n', 80: 'o',
          81: 'p', 82: 'q', 83: 'r', 84: 's', 85: 't', 86: 'u', 87: 'v', 88: 'w', 89: 'x', 90: 'y',
          91: 'z', 92: '{', 93: '|', 94: '}', 95: '~'}
def getkey(origin, val):
    for key, value in origin.items():
         if val == value:
             return key

def encode(origin, message, masterkey, fkey, fakey):
    new = ""
    copies = ""
    t = True
    total_reps = ""
    count = 0
    
    
    for x in message: #for item in message
        index = getkey(origin, x)
        index *= masterkey
        masterkey += fkey
        print("i = " + str(index))
        reps = 0
        count += 1
        
        while t:
            if (index > 95):
                index -= 95
                reps += 1

            else:
                print("Character added = " + str(index) + " - " + origin[index])
                print("Reps = " + str(reps))
                if (count == len(message)):
                    total_reps += str(reps)
                else:
                    total_reps += str(reps) + ","
                new += origin[index]
                copies += str(reps)
                break
    
    #print("\nCopies = " + copies)
    return (new + '\n' + str(total_reps))

code = encode(origin, "message", 5, 2, 10)
print("\nFinal ==" + code)

def decode(origin, message, masterkey, fkey, fakey):
    new = ""
    t = True

    for x in message:
        index = getkey(origin, x)
        index *= masterkey
        
        if (ord(x) == 10):
            pass
        else:
            pass