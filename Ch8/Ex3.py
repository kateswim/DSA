import string

def findMissingLetters(s):
    alphabet=set(string.ascii_lowercase) #attribute of string module containing alphabet set lowercase
    s=set(s.lower()) #make input set lowercase
    missing_Letters=alphabet-s #provide set with letters that not in alphabet

    return missing_Letters

print(findMissingLetters('the quick brown box jumps over a lazy dog'))