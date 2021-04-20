# Spell Check Starter

import re

def Linearsearch(anArray, item):
  
    for i in range(len(anArray)):
  
        if (anArray[i] == item):
            return i
      
    return -1


def binarysearch(anArray, item):
    low = 0
    high = len(anArray) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if anArray[mid] < item:
            low = mid + 1
 

        elif anArray[mid] > item:
            high = mid - 1

        else:
            return mid
 
    return -1 





def alicedictionary():
    alicechoice = input("what selection would you like to be used? [linear][binary] ")
    alicechoice = alicechoice.lower()
    if (alicechoice =="linear"): 
        wordmatch = 0
        for i in range(len(aliceWordsFull)):
         linearresult = Linearsearch(dictionary,aliceWordsFull[i].lower()): 
         if (linearresult == -1): 
             wordmatch +=1
             print(aliceWordsFull.lower() + " is not in the dictionary")
        print (wordmatch + " words were not found in the dictionary") 
    elif (alicechoice == "binary"):
        wordmatch = 0  
        for i in range (len(aliceWordsFull)): 
            binaryresult = binarysearch(dictionary, aliceWordsFull[i].lower())
            if (binaryresult == -1):
                wordsmatch +=1 
                print(aliceWordsFull.lower()+ " is not in the dictionary")
        print(wordmatch + " words were not found in the dictionary")


    

def searchDictionary ():
    userword = input ("what word would you like to search")
    searchchoice = input("what search would you like to do [linear][binary]")
    if (searchchoice == "linear"):
        results = Linearsearch(dictionary,userword)
        if (results == -1):
            print(userword + " is not in the dictionary")
        else: 
            print(userword + " is in the dictionary at " + word)
    if (searchchoice == "binary"): 
        result = binarysearch(dictionary,userword)
        if (result == -1):
            print (userword + " is not in the dictionary")
        else: 
            print(userword + "is in the dictionary at " + word)





def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    print ("what dictionary would you like to access? [Alice][Regular]?")
    dictionarychoice = input(" ")
    dictionarychoice = dictionarychoice.lower()
    if (dictionarychoice == "alice"): 
        alicedictionary()
    elif (dictionarychoice == "regular"):
        regulardictionary()




# end main()


def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w]+", textData)


# Call main() to begin program 


main()

def searchDictionary