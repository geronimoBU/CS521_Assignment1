'''
Simple MadLibs

Created by Alex Geronimo
Last Modified: 5/30/17
 '''

import sys # Use sys.exit to exit Game loop
while True: # Game Loop

    print("Welcome to Mad Libs"'\n')
    print("Instructions:\nEnter an integer (whole number) between the values specified."'\n'
                        "Program will give you a sentence based on the input value."'\n'
                        "If you would like to continue playing, enter 'y' when prompted."'\n'
                        "Enter a different number to display another madlib sentance."'\n'
                        "The program will compile all of your unique sentences (if the sentence is already used it will ask you to enter another number)."'\n'
                        "To exit and print the full list, enter 'n' when prompted"'\n')

    madlib_final = []
    userinput = []

# Create Lists for MadLib Game (Nouns, Verbs, Adjectives)

    nouns = ["dude","cat","Abe Lincon","Chuck Norris","actor","actress","devil","God","student"]   # Index length: 9 [0:8]
    verbs = ["swat","flap","fight","medicate","propel","splatter"]                                 # Index length: 6 [0:5]
    adjs = ["boring","creepy","naked","sick","gentile","fluffy","drunken"]                          # Index length: 7 [0:6]

# MadLib Sentences:  {0} = adjs , {1} = nouns , {2} = verbs

    sentences = ["The {0} {1} would always {2} on the way to work",                                 # Index length: 8 [0:7]
             "At work, the {0} {1} ended up having to {2} a lot to go home early.",
             "A man {2} on a {0} {1}.",
             "{1} {2} to the {0} ground.",
             "All of the king's {0} horses and all of the king's dainty {1}s could not {2} the egg man back together again",
             "When the {0} {1} went to the store, they wanted to {2} at the cashier",
             "I asked {0} {1} to take out the garbage, but they ended up wanting to {2} instead...",
             "On the train ride, Jake saw a {1}, {0} as that is, Jake did not want to {2}"]

# Function for User Input & Validation - input arg = prompt text to user. body = check if positive, integer, and index bounds. return = userinput
    def inputNumber_Val(num_prompt):
        while True:
            try:
                userinput = int(input(num_prompt))

                # Check if integer is positive or zero
                if userinput >= 0:
                    userinput = userinput
                else:
                    num_prompt = ("Error: Please enter a positive number: "'\n')
                    continue

                # Check that the user input does not exceed index in either sentences, nouns, verbs or adjs
                if userinput < len(sentences) or userinput < len(nouns) or userinput < len(verbs) or userinput < len(adjs):
                    userinput = userinput
                else:
                    num_prompt = ("Error: Please enter a number less than " + str(max((len(sentences),len(nouns),len(verbs),len(adjs))))+": "'\n')
                    continue

            except ValueError:
                num_prompt = ("Not an integer! Try again: "'\n')
                continue

            else:
                return int(userinput)

# Inner game loop - as long as user input DOES NOT EQUAL "n" continue writing to madlib final list
    while userinput != "n":
        ind_max = max((len(sentences),len(nouns),len(verbs),len(adjs)))-1
        userinput = inputNumber_Val("Please enter a integer between 0 and " + str(ind_max) + ": "'\n')

        def madlib_index(list,): # If user input exceeds index dimensions of list, use remainder as index number
            if userinput < (len(list)):
                ind_var = userinput
                return ind_var
            else:
                ind_var = userinput % len(list)
                return ind_var

        sent_ind = madlib_index(sentences)
        noun_ind = madlib_index(nouns)
        verb_ind = madlib_index(verbs)
        adj_ind = madlib_index(adjs)

    # Insert selected noun, verb, and adj into sentence
        madlib = (sentences[int(sent_ind)].format(adjs[int(adj_ind)],nouns[int(noun_ind)],verbs[int(verb_ind)]))

    # Check if the resulting sentence is unique
        if not madlib_final:
            madlib_final = [madlib]
        elif madlib in madlib_final:
            if len(madlib_final)-1 == ind_max:
                print("All possible sentences created"'\n')
                break
            else:
                print("This sentence has been used already, enter another number: ")
                continue
        else:
            madlib_final.append(madlib)  # Add current madlib to madlib_final list

    # Print current mad lib to user: elem on separate lines
        print("Current MadLib: "'\n')
        for elem in madlib_final:
            print(elem)

    # Ask user if they would like to continue playing & validate input
        print("")
        next = input("Would you like to keep playing? (enter 'y' or 'n'): "'\n')
        while next != "n" and next != "y":
            next = input("Please enter either 'y' to continue playing or 'n' to exit: "'\n')
        if next == "n":
            userinput = "n"
        else:
            continue

    # Print Final Mad Lib and Exit
    print("Your Final MadLib: "'\n')
    for sent in madlib_final:
        print(sent)
    print("")
    print("Thanks for playing")
    sys.exit()
