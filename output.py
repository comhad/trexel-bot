import random
import csv

class generator :
    csvFile = csv.reader(open("vocab.csv"))
    s_nouns = next(csvFile)
    p_nouns = next(csvFile)
    s_verbs = next(csvFile)
    p_verbs = next(csvFile)
    adjectives = next(csvFile)
    lines = open("lines.txt").readlines()
    
    def format(self, text) : # This function will replace all pre-defined string patterns with a specified type of word
        newString = text.rstrip()
        newString = newString.replace("%s_noun", random.choice(self.s_nouns))
        newString = newString.replace("%p_noun", random.choice(self.p_nouns))
        newString = newString.replace("%s_verb", random.choice(self.s_verbs))
        newString = newString.replace("%p_verb", random.choice(self.p_verbs))
        newString = newString.replace("%adj", random.choice(self.adjectives))
        newString = newString.replace("%d_rand", str(random.randint(10, 50)))
        return newString
    
    def scriptLine(self) : # Replace words with string patterns so the format function can use it
        newString = random.choice(self.lines)
        return self.format(newString)