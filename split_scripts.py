import sys
import nltk
import re

dontBreak = re.compile("([\"?’,!\.]|m|re|s|t|ll)") # All the characters we shouldn't have a space before
script = open(sys.argv[1], "r")

buffer = []

for line in script :
    if len(line) < 260 :
        sentence = line
        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)
        processed = ""
        for each in tagged :
            word = each[0]

            if dontBreak.fullmatch(word) :
                processed = processed[:-1] # Remove the last character
            else :
                if each[1] in ["NNP"] :
                    word = "%s_noun"
                elif each[1] in ["NNS"] :
                    word = "%p_noun"
                elif each[1] in ["VB"] :
                    word = "%p_verb"
                elif each[1] in ["VBZ"] :
                    word = "%s_verb"
            
            processed += word + " "

        if "%" in processed :
            buffer.append(processed) # Don't append unaltered lines

outputFile = open("lines.txt", "a")

for line in buffer :
    outputFile.write(line.strip() + "\n")

outputFile.close()