# Rajath Akshay Vanikul (29498724)

# Create a main function to accept input from the user and to create instances to perform
# the class operation defined in decoder, character, word, sentence modules.
# We also create a menu function to perform analysis according to user's choice.

# Create a main function
def main():
# Import the decoder module to decode the morse code.
    import decoder_29498724 as d
# Create an instance of the method "Decoder"
    dd = d.Decoder()
# Display the dictionary stored in decoder module for input reference.
    print(dd)
# Display the instructions for the user's input.
    print("The Morse Code sequences can be of any length but with the minimum of one set of three consecutive ‘*’ \n"
          "Please use displayed Morse code translation table for your reference.\n"
          "Click on <ENTER> twice to terminate and submit your input.")
# Initialising an empty list to store the input from user.
    input_list = []
# Create a loop to accept as many inputs as the user wishes to give.
    while True:
        input_str = input("Enter your Morse Code sequence: ")
# Enter an empty string to exit the input loop.
        if (input_str == ''):
            break
# Importing regular expression to check find all the "*" characters in the input string
        import re
        check = re.findall('\*+',input_str)
# Check if the input has only "*" and "***" for decoding else return an error message.
        try:
            for i in check:
                assert (len(i) == 1 or len(i) == 3)
        except AssertionError:
            print("INVALID INPUT, CHECK THE NUMBER OF '*' IN INPUT")
            continue

# Following code helps us to check the first and last charcter of the input.
        list = input_str.split('*')
        last_character = str(list[len(list) - 1])
# Check if first character in the list belongs to any of the given punctuations and display the error.
        try:
            assert not (list[0] == "010101" or list[0] == "001100" or list[0] == "110011")
        except AssertionError:
            print("INPUT CAN NOT START WITH PUNCTUATION")
            continue
# Check if last character in the list belongs to any of the given punctuations and display the error.
        try:
            assert (last_character == "010101" or last_character == "001100" or last_character == "110011")
        except AssertionError:
            print("INPUT SHOULD TERMINATE WITH A PUNCTUATION")
            continue
# Check for two punctuations in series and display the error.
        try:
            for i in range(len(list) - 1):
                assert not (len(list[i]) == 6 and len(list[i + 1]) == 6)
        except AssertionError:
            print("INPUT CAN NOT HAVE CONSECUTIVE PUNCTUATIONS")
            continue
# Check the input sequences to just contain '0's,'1's and '*'s with a minimum of one "***".
# Store it in to a list for further operations.
        if set(input_str).issubset("1*0") and "***" in input_str:
            input_list.append(input_str)
            print("sequence: ",input_str)
            print("total input sequence : ",input_list)
        else:
            print("INVALID INPUT, PLEASE ENTER AGAIN.")
# Combine every element of the list with "***" in between to a string.
    morse_code_sequence = "***".join(input_list)
    print("final input sequence : ",morse_code_sequence)

    decoded_sequence = dd.decode(morse_code_sequence)
    print("Decoded sequence :",decoded_sequence)
# Check the decoded sequence and run the whole function if the previous input is incorrect.
# Else transfer the sequence to character/word/sentence analysis.
    if decoded_sequence == " ":
        input("Press ENTER to input another sequence")
        main()
    else:
     Menu(decoded_sequence)

# Define a function to access character analysis module and display the result.
def Character(decoded_sequence):
    print("Decoded sequence :", decoded_sequence)
    import character_29498724 as c
    cc = c.CharacterAnalyser()
    cc.analyse_characters(decoded_sequence)
    print("Character analysis :"+'\n',cc)

# Define a function to access word character analysis module and display the result.
def Word(decoded_sequence):
    print("Decoded sequence :", decoded_sequence)
    import word_29498724 as w
    ww = w.WordAnalyser()
    ww.analyse_words(decoded_sequence)
    print("Word analysis :" + '\n', ww)

# Define a function to access sentence analysis module and display the result.
def Sentence(decoded_sequence):
    print("Decoded sequence :", decoded_sequence)
    import sentence_29498724 as s
    ss = s.SentenceAnalyser()
    ss.analyse_sentences(decoded_sequence)
    print("Sentence analysis :" + '\n', ss)


# Create a function named "Menu" to request for user's choice for analysis
def Menu(decoded_sequence):
    print("Enter 1 to check for character analysis on your input")
    print("Enter 2 to check for word analysis on your input")
    print("Enter 3 to check for sentence analysis on your input")
    print("Enter 4 to exit")
    print("Enter 0 to input another sequence")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("PLEASE ENTER A VALID CHOICE")
        choice = int(input("Enter your choice: "))
    if choice == 1:
        Character(decoded_sequence)
        input("Press enter to go back to the Menu")
        Menu(decoded_sequence)
    if choice == 2:
        Word(decoded_sequence)
        input("Press enter to go back to the Menu")
        Menu(decoded_sequence)
    if choice == 3:
        Sentence(decoded_sequence)
        input("Press enter to go back to the Menu")
        Menu(decoded_sequence)
    if choice == 4:
        exit()
    if choice == 0:
        main()
    else:
        print("Invalid choice")
        input("Press enter to go back to the Menu")
        Menu(decoded_sequence)

# This statement confirms that main function should only be executed if the program is executed as a standalone program.
# It will not be executed if the program is imported as a module.
if __name__ == "__main__":
    main()

#0000*0*1011***110011***0000*111*011***01*010*0***1011*111*001***001100
#0000*00***110011***00*01*11***110*111*111*100***010101
#0000*111*011***01*010*0***1011*111*001***001100
