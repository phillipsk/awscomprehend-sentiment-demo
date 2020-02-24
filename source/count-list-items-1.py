# count-list-items-1.py
# https://programminghistorian.org/en/lessons/counting-frequencies

import sys
import source.classifiers as classifiers

filename = "../TXT_asrOutput.txt"
with open(filename, 'r') as f:
    read_data = f.read()

wordstring = read_data

wordlist = wordstring.split()
#
# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))
#

# one liner
wordfreq = [wordlist.count(w) for w in wordlist] # a list comprehension

# print("String\n" + wordstring +"\n")
# print("List\n" + str(wordlist) + "\n")
# print("Frequencies\n" + str(wordfreq) + "\n")
# print("Pairs\n" + str(list(zip(wordlist, wordfreq))))

# Given a list of words, return a dictionary of
# word-frequency pairs.

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# Given a list of words, remove any that are
# in a list of stop words.

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]


# response = urllib.request.urlopen(url)
# html = response.read()
#
# text = obo.stripTags(html).lower()
# fullwordlist = obo.stripNonAlphaNum(text)
# wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
# dictionary = obo.wordListToFreqDict(wordlist)
# sorteddict = obo.sortFreqDict(dictionary)
#
# for s in sorteddict: print(str(s))


def run_demo():
    fullwordlist = read_data
    wordlist = removeStopwords(fullwordlist, classifiers.stopwords)
    dictionary = wordListToFreqDict(wordlist)
    sorteddict = sortFreqDict(dictionary)

    for s in sorteddict: print(str(s))


if __name__ == '__main__':
    run_demo()