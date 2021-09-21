from Def_GetKey import getkey
def decode(origin, message, masterkey, fkey, fakey):
    new = ""
    t = True
    reps = message.split('\n')[1]
    #print("\nDecode Reps ==" + reps)   #-- Debug line to figure out what's inside $reps


            #Start Decoding
    for x in message:
        index = getkey(origin, x)
        index *= masterkey
        
        if (ord(x) == 10):
            pass
        else:
            pass

    return new