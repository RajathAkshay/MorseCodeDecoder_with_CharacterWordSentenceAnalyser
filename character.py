# Rajath Akshay Vanikul (29498724)

# Create a class 'CharacterAnalyser' which contains methods to count each character in decoded sequence.
class CharacterAnalyser:
# Initiate the reference dictionary to store the output of character analysis.
    def __init__(self):
        self.occurrence_dict = {}
        self.ref = ""

# Overload the print function to display the occurrence dictionary in readable format.
    def __str__(self):
        for key, value in self.occurrence_dict.items():
            self.ref += ("{}  character occurred   {}  time(s)\n".format(key, value))
        return (self.ref)

# Define a method to analyse the count of each character in the decoded sequence and
# return the occurrence of each character as a dictionary.
    def analyse_characters(self,decoded_sequence):
        for each in decoded_sequence:
            if set(each).issubset(" ,.?"):
                continue
            else:
                if each in self.occurrence_dict:
                    self.occurrence_dict[each] += 1
                else:
                    self.occurrence_dict[each] = 1
        return (self.occurrence_dict)