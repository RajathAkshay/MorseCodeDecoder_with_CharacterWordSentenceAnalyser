# Rajath Akshay Vanikul (29498724)

# Create a class 'SentenceAnalyser' which contains methods to count occurrence each sentence in decoded sequence.
class SentenceAnalyser:
# Initiate the reference dictionary to store the output of sentence analysis.
    def __init__(self):
        self.occurrence_dict = {}
        self.ref = ""

# Overload the print function to display the occurrence dictionary in readable format.
    def __str__(self):
        for key, value in self.occurrence_dict.items():
            if key == ".":
                self.ref += ("Full sentences occurred {} time(s)\n".format(value))
            if key == ",":
                self.ref += ("Clauses occurred {} time(s)\n".format(value))
            if key ==  "?":
                self.ref += ("Questions occurred {} time(s)\n".format(value))
        return (self.ref)

# Define a method to analyse the count of occurrence of each sentence in the decoded sequence and
# return the occurrence as a dictionary.
    def analyse_sentences(self, decoded_sequence):
        for each in decoded_sequence:
            if each == "." or each == "," or each == "?":
                if each in self.occurrence_dict:
                    self.occurrence_dict[each] += 1
                else:
                    self.occurrence_dict[each] = 1
        return self.occurrence_dict