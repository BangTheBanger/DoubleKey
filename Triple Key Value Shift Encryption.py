#'origin' will be used to refer to the matrix of values and their respective characters.
#This function is used to get the key for a value from the 'origin' dictionary. 
def getkey(origin, val):
    for key, value in origin.items():
         if val == value:
             return key

#This is the function where the magic happens, the code could be better optimized, for runtime and all that. But I haven't done that yet.
def encode(origin, message, masterkey, fkey, fakey):
    #Here I set the necessary variables. I will return 'new' as the encrypted code.
    new = ""
    #total_reps is where the numbers in the encrypted message come from. 
    #They are the number of times the value has gone past the limit of the origin.
    total_reps = ""
    #count is needed simply to not have a comma after the final value. I don't use it for anything else.
    count = 0
    
    #this loop is where the encryption begins 'x' here represents the index of the string 'message'
    for x in message:
        
        #index is the key for the current 'x' character. This is the number that will be shifted.
        index = getkey(origin, x)
        #Here I change the number by the master key. The very first key that is provided.
        index *= masterkey
        #This sequence makes it so that the master key shifts by the secondary key (named fkey)
        masterkey += fkey
        #Then the secondary key is also shifted so that the next time it loops around the rate of change doesn't stay constant. 
        #Third key is named fakey.
        fkey += fakey
        
        #count for the amount of times the value has gone past the origin max. (aka repetitions; reps)
        reps = 0
        #The counter to check if it's the last character in the message goes up.
        count += 1
        
        #This loop is what calculates the reps, subtracting 95 from the number until we get a shifted value in the origin.
        while True:
            #Check if we need a rep
            if (index > 95):
                index -= 95
                reps += 1
            #If the number falls into range of the origin then...
            else:
                #This if is to make sure the last number doesn't include a comma.
                if (count == len(message)):
                    total_reps += str(reps)
                else:
                    total_reps += str(reps) + ","
                #This is what appends the new, encrypted, text into 'new'
                new += origin[index]
                #Then breaks the while loop, sending the code back to the for loop, for the next character.
                break
    #Then we return the encrypted message, with a linebreak between the encrypted message and the reps
    return (new + '\n' + total_reps)


#The decode function is a lot shorter, probably because I made it after knowing how it works, instead of messing around.
#This function is a lot more compact and does the job nicely, I might use this is a base to compact the encode function too.
def decode(origin, message, masterkey, fkey, fakey):
    #new serves the same function to the 'new' in encode.
    new = ""
    #Here we fetch the reps off of the string provided by the user. We use the linebreak as the delimiter.
    reps = message.split('\n')[1]
    #Then we split the reps into the numbers they represent, rather than using a single string. ex: ["1", "2", "3"] rather than ["1,2,3"]
            #This helps with numbers with more than a single digit.
    reps = reps.split(',')
    #Then we fetch the actual encrypted text from the message.
    message = message.split('\n')[0]
    #repkey is used to navigate the reps array
    repkey = 0
    
    #The loop that will decode the messages
    for x in message:
        #index here serves the same function as in encode. But this time it's going to fetch the value of the encrypted number from the origin
        index = getkey(origin, x)
        #then it's going to go back to the original number before it got subtracted by 95
        index += (95*int(reps[repkey]))
        #then it will divide by the masterkey (as opposed to multiply, in encode)
        index //= masterkey
        #then we will follow the same process of changing the keys than in encode.
        masterkey += fkey
        fkey += fakey
        #Now we should have prepared the keys for the next character, and already got the decrypted character. So we append to new.
        new += origin[index]
        #add the repkey, so that the next character is correctly paired with it's reps, then back to the start of the loop.
        repkey += 1
        
    #finally we return the decrypted message.
    return new


#This is the origin I'm currently using. The keys can't start after 1, because of the nature of the shift. I'd have to spend days figuring out
#how to make it rep nicely without causing troubles. Though, I guess a good start would be index-(originmax+originmin)
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

#This is the rudimentary system I use to run the code in a way the user can interact with.
#This is encode
message = input("What is the message you want to encode: ")
mkey = int(input("What is master key: "))
fkey = int(input("What is your fkey: "))
fakey = int(input("What is your fakey: "))
code = encode(origin, message, mkey,fkey,fakey)
print(code)

#This is decode
message = input("What is the message you want to decode: ")
message += "\n"
message += input("What is the message you want to decode: ")
mkey = int(input("What is master key: "))
fkey = int(input("What is your fkey: "))
fakey = int(input("What is your fakey: "))
code = decode(origin, message, mkey,fkey,fakey)
print(code)

#Making sure the code doesn't just quit the console as soon as it's done. In case you're not running in an IDE.
input("Press anything to exit")

#This is what I used to test the code before. Now it's obsolete.
"""
code = encode(origin, "This is my message, I hope it's encrypted", 5, 2, 10)
print("\nFinal ==" + code)
print()
decoded = decode(origin, code, 5, 2, 10)
print("\nFinal ==" + decoded)
"""