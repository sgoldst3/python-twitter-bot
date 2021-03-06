"""
This function takes in text1, text2, and n
    text1: base text to generate the leading phrases
    text2: corrolary text to append to end of t1 phrases
    n: the size of the tokens generated
"""


from random import *
import re

def generatePhrase(t1, n):
    # print T1[:5], "more: ", len(T2)
    ls1 = t1.split()

    # Find a location that is between zero and
    # n places from the end of the list
    location = randrange(0, len(ls1)-n)

    phrase = ' '.join(ls1[location:location+n])
    return phrase



def phraseInCorpus(phrase, corpus, n):
    corpus = corpus.lower()


    #Perform some regex to clean up this data
    phraseList = phrase.lower().split()
    if len(phraseList)> n:
        phraseList = phraseList[-n:]

    #TODO: may need the below...
    elif len(phraseList) < n:
        n = len(phraseList)

    lcPhrase = " ".join(phraseList)
    location = corpus.find( " "+lcPhrase+" " )

    if location>0:
        return lcPhrase

    elif n>0:
        return phraseInCorpus(" ".join(phraseList[1:]), corpus, n-1)

    else:
        return False



def getSubset(foundString, corpus):
    """
    foundString: a STRING that has been proven to exist inside the corpus
    corpus: a STRING that contains the full corpus

    """
    corpus_ls = corpus.split()
    found_str_ls = foundString.split()
    len_fsl = len(found_str_ls)

    found_matches = []
    to_end = 10
    for i in range(len(corpus_ls)- (len_fsl+to_end)):
        if " ".join(corpus_ls[i:i+len_fsl]) == foundString:
            new_str = " ".join(corpus_ls[i+len_fsl: i+len_fsl+to_end])
            found_matches.append(new_str)


    # print "\nMATCHES: ", found_matches
    return found_matches[randrange(0,len(found_matches))]




def getFullString(file1, file2, n1, n2):
    phrase = generatePhrase(file1, n1)
    count = 0
    val = False

    while (val==False and count<200):
        val = phraseInCorpus(phrase, file2, n2)
        if val is not False:
            second_string = getSubset(val, file2)
            phrase = phrase + " "+second_string
            return phrase
        count += 1

    return


if __name__ == '__main__':
    b_fl = open('data/bspears_sample.txt','r').read()
    s_fl = open('data/full_shakespeare.txt', 'r').read()
    n=8

    print '\n'+ '*'*20

    print getFullString(b_fl, s_fl, 8, 3)

    print '\n'+ '*'*20
