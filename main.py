# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

#Making the Welcome function
def Welcome():
    print("\n\n                            Welcome to the Anagram Checker!! \n" )
    select = input("Press 1 to Begin or 2 to Quit: ")
    try:
        select = int(select)
        if select == 1:
            find_anagram()
        
        elif select == 2:
            print ("Thank you. Bye for now!")
        
        else:
            print ("\n The number selected is invalid, try again.")
            Welcome()

    except ValueError:
        print("\n Error due to invalid entry! Select a number!!")
        Welcome()


#Making the anagram function
def find_anagram():
    firstEntry = input("\n Input First String: \n ")
    secondEntry = input("\n Input Second String: \n ")

    #changing letters of the inputs to uppercase
    firstEntry = firstEntry.upper()
    secondEntry = secondEntry.upper()

    num1 = list(firstEntry)
    num2 = list(secondEntry)

    #trying to remove the spaces
    strippedNum1 = []
    for i in num1:
        i.strip()
        strippedNum1.append(i)

    strippedNum2 = []
    for i in num2:
        i.strip()
        strippedNum2.append(i)

    #Now for the final check, I will try to sort the list of letters
    input1 = sorted(strippedNum1)
    input2 = sorted(strippedNum2)
    
    if len(strippedNum1) != len(strippedNum2):
        print ("\n   False")
        again()
    
    elif input1 == input2:
        print ("\n   True")
        again()
    
    else:
        print ("\n   False")
        again()


#Making the final function for if the user wants to reuse the checker
def again():
    choice = input("\n Would you like to try again? Yes or no:  ")
    choice = choice.upper()

    if choice == "YES":
        find_anagram()

    elif choice == "NO":
        print ("Thank you. Bye for now!")

    else:
        print ("Invalid Entry! I'll ask again \n\n")
        again()


Welcome()
