from Def_GetKey import getkey
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
        fkey += fakey
        #print("i = " + str(index))
        reps = 0
        count += 1
        
        while t:
            if (index > 95):
                index -= 95
                reps += 1

            else:
                #print("Character added = " + str(index) + " - " + origin[index])
                #print("Reps = " + str(reps))
                if (count == len(message)):
                    total_reps += str(reps)
                else:
                    total_reps += str(reps) + ","
                new += origin[index]
                copies += str(reps)
                break
    
    #print("\nCopies = " + copies)
    return (new + '\n' + str(total_reps))
