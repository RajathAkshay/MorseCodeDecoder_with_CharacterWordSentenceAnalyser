# Rajath Akshay Vanikul (29498724)

# Create a class 'Decoder' which contains methods to decode the morse code inserted.
class Decoder:
# Initiate the reference morse code dictionary under the constructor for this class.
    def __init__(self):
        self.morse_dict = {'01': 'A', '1000': 'B', '1010':'C', '100':'D','0':'E','0010':'F',
              '110':'G','0000':'H','00':'I','0111':'J','101':'K','0100':'L',
              '11':'M','10':'N','111':'O','0110':'P','1101':'Q','010':'R',
              '000':'S','1':'T','001':'U','0001':'V','011':'W','1001':'X','1011':'Y','1100':'Z'
              ,' ':' ',
              '11111':'0','01111':'1','00111':'2','00011':'3','00001':'4','00000':'5',
              '10000':'6','11000':'7','11100':'8','11110':'9',
              '010101':'.','110011':',','001100':'?' }
# Overload the print function to display the morse code dictionary in readable format.
    def __str__(self):
# Initiate a variable to use the variable as a return item.
        ref = ""
        for key, value in self.morse_dict.items():
            ref += str(key +'   \t    '+ value+ '\n')
        return ref

# Define a method called 'decode' which accepts the input string to produce a decoded sentences.
    def decode(self,morse_code_sequence):
# Splitting the input sequence where all '***' occur.
        input_list = morse_code_sequence.split('***')
# Initialise a list to store decoded sequence.
        morseout_list = []
# Check for each character in dictionary and append the corresponding decoded value.
# return a space if you cant find the sequence in dictionary with an error output.
        try:
            for i in input_list:
                input_word = i.split('*')
                for each in input_word:
                    assert (each in self.morse_dict)
                    morseout_list.append(self.morse_dict[each])
                morseout_list.append(" ")
            decoded_sequence = "".join(morseout_list)
        except AssertionError:
            print("INVALID CHARACTER IN INPUT")
            decoded_sequence = " "
        return decoded_sequence