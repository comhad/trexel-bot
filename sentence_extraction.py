import nltk.tokenize as nt
import nltk
from sys import argv
import csv
import re

def process(text, wordType) : 
    ss = nt.sent_tokenize(text)
    tokenizedSent = [nt.word_tokenize(sent) for sent in ss]
    posSentences = [nltk.pos_tag(sent) for sent in tokenizedSent]
    wordCollection = []
    for i in posSentences :
        for a in i :
            if a[1] == wordType :
                wordCollection.append(a[0])
    bufferWords = []
    for word in wordCollection :
        if any(regex.search(word) for regex in bannedRegex) :
            print(word + " has been blocked")
        else :
            bufferWords.append(word)
    return bufferWords


words = csv.reader(open("vocab.csv"))

singleNouns = next(words)
puralNouns = next(words)
singleVerbs = next(words)
puralVerbs = next(words)
adjectives = next(words)

#This is a blacklist to prevent the bot outputting letters on their own

blackList = []
with open("blacklist.txt", "r") as bannedRegex :
    blackList = bannedRegex.readlines()

bannedRegex = []
for regex in blackList :
    bannedRegex.append(re.compile(regex.strip()))

contents = open(argv[1], "r")
script = contents.readlines()

print("Beginning processing " + str(len(script)) + " line(s)...")
for line in script :
    line = line[8:] # Remove the prompt

    for word in process(line, "NNP") : # Append first variation of single nouns
        if len(word) > 1 and word not in singleNouns : # Avoid puncuation and little things like that
            singleNouns.append(word) # This is stupid, but i can't think of a better way to do it
    for word in process(line, "NN") : # Append second variation of single nouns
        if len(word) > 1 and word not in singleNouns :
            singleNouns.append(word)

    for word in process(line, "NNS") : # Append first variation of pural nouns
        if len(word) > 2 and word not in puralNouns : # Avoid 've' and words like that
            puralNouns.append(word)
    for word in process(line, "NNPS") : # Append second variation of pural nouns
        if len(word) > 2 and word not in puralNouns :
            puralNouns.append(word)

    for word in process(line, "VB") :
        if len(word) > 2 and word not in puralVerbs :
            puralVerbs.append(word)
    for word in process(line, "VBP") :
        if len(word) > 2 and word not in puralVerbs :
            puralVerbs.append(word)
    
    for word in process(line, "VBZ") :
        if len(word) > 2 and word not in singleVerbs :
            singleVerbs.append(word)

    for word in process(line, "JJS") :
        if word not in adjectives :
            adjectives.append(word)

def status():
    print("Single nouns : ", end='') 
    print(str(len(singleNouns)))
    print("Pural nouns : ", end='')  
    print(str(len(puralNouns)))
    print("Pural verbs : ", end='') 
    print(str(len(puralVerbs)))
    print("Single verbs : ",end='') 
    print(str(len(singleVerbs)))

status()
print()

with open("vocab.csv", "w") as wordFile :
    fileWrite = csv.writer(wordFile) 
    fileWrite.writerow(singleNouns)
    fileWrite.writerow(puralNouns)
    fileWrite.writerow(puralVerbs)
    fileWrite.writerow(singleVerbs)
    fileWrite.writerow(adjectives)
