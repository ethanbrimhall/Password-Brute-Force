import time, math
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
found = False

def main():
    global found
    password = input('Input a 1-6 letter password: ')
    print("\n")
    start_time = time.time()
    oneLetter(password)
    if found == False:
        twoLetter(password)
        if found == False:
            threeLetter(password)
            if found == False:
                fourLetter(password)
                if found == False:
                    fiveLetter(password)
                    if found == False:
                        sixLetter(password)
    total_time = time.time() - start_time
    print("in " + str(math.ceil(total_time * 100)/100) + " seconds")
                    
def oneLetter(password):
    global found
    for x in range(len(letters)):
        #print(letters[x])
        if letters[x] == password:
            print('Found Password: ' + letters[x])
            found = True
            break

def twoLetter(password):
    global found
    for x in range(len(letters)):
        for y in range(len(letters)):
            #print(letters[x] + letters[y])
            if letters[x] + letters[y] == password:
               print('Found Password: ' + letters[x] + letters[y])
               found = True
               break
            
        if found == True:
            break

def threeLetter(password):
    global found
    for x in range(len(letters)):
        for y in range(len(letters)):
            for z in range(len(letters)):
                #print(letters[x] + letters[y] + letters[z])
                if letters[x] + letters[y] + letters[z] == password:
                    print('Found Password: ' + letters[x] + letters[y] + letters[z])
                    found = True
                    break
            if found == True:
                break
        if found == True:
            break

def fourLetter(password):
    global found
    for x in range(len(letters)):
        for y in range(len(letters)):
            for z in range(len(letters)):
                for w in range(len(letters)):
                    #print(letters[x] + letters[y] + letters[z] + letters[w])
                    if letters[x] + letters[y] + letters[z] + letters[w] == password:
                        print('Found Password: ' + letters[x] + letters[y] + letters[z] + letters[w])
                        found = True
                        break
                if found == True:
                    break
            if found == True:
                break
        if found == True:
                break

def fiveLetter(password):
    global found
    for x in range(len(letters)):
        for y in range(len(letters)):
            for z in range(len(letters)):
                for w in range(len(letters)):
                    for q in range(len(letters)):
                        #print(letters[x] + letters[y] + letters[z] + letters[w] + letters[q])
                        if letters[x] + letters[y] + letters[z] + letters[w] + letters[q] == password:
                            print('Found Password: ' + letters[x] + letters[y] + letters[z] + letters[w] + letters[q])
                            found = True
                            break
                    if found == True:
                        break
                if found == True:
                    break
            if found == True:
                break
        if found == True:
                break

def sixLetter(password):
    global found
    for x in range(len(letters)):
        for y in range(len(letters)):
            for z in range(len(letters)):
                for w in range(len(letters)):
                    for q in range(len(letters)):
                        for v in range(len(letters)):
                            #print(letters[x] + letters[y] + letters[z] + letters[w] + letters[q] + letters[v])
                            if letters[x] + letters[y] + letters[z] + letters[w] + letters[q] + letters[v] == password:
                                print('Found Password: ' + letters[x] + letters[y] + letters[z] + letters[w] + letters[q] + letters[v])
                                found = True
                                break
                        if found == True:
                            break
                    if found == True:
                        break
                if found == True:
                    break
            if found == True:
                break
        if found == True:
                break
   
if __name__ == "__main__":
    main()
