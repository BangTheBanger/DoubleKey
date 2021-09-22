from Def_GetKey import getkey
def decode(origin, message, masterkey, fkey, fakey):
    new = ""
    t = True
    reps = message.split('\n')[1]
    reps = reps.split(',')
    message = message.split('\n')[0]

    """
    #-- Debug loop to figure out what's inside $reps
    #a = ""
    #for x in reps:
        #print(x)
        #a += str(x)
    #print("\nDecode Reps ==" + a)
    #-- Debug loop finish
    """

    #Start Decoding
    repkey = 0
    for x in message:
        index = getkey(origin, x)
        index += (95*int(reps[repkey]))
        index //= masterkey
        masterkey += fkey
        fkey += fakey
        new += origin[index]
        repkey += 1



        
    return new