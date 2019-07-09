# Rajath Akshay Vanikul (29498724)

# Create a class 'WordAnalyser' which contains methods to count occurrence each word in decoded sequence.
class WordAnalyser:
# Initiate the reference dictionary to store the output of word analysis.
    def __init__(self):
        self.occurrence_dict = {}
        self.ref = ""

# Overload the print function to display the occurrence dictionary in readable format.
    def __str__(self):
        for key, value in self.occurrence_dict.items():
            self.ref += ("{}  word occurred  {}  time(s)\n".format(key,value))
        return (self.ref)

# Define a method to analyse the count of occurrence of each word in the decoded sequence and
# return the occurrence as a dictionary.
    def analyse_words(self,decoded_sequence):
        words_list = decoded_sequence.split(" ")
        for each in words_list:
            if each != "." and each != "," and each != "?" and each != "":
                if each in self.occurrence_dict:
                    self.occurrence_dict[each] += 1
                else:
                    self.occurrence_dict[each] = 1
        return (self.occurrence_dict)