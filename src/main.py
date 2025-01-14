def tokenize(file_path):
    """Write a method/function that reads in a text file and returns a list of the tokens
    in that file. For the purposes of this project, a token is a sequence of alphanumeric characters,
    independent of capitalization (so Apple, apple, aPpLe are the same token).
    You are allowed to use regular expressions if you wish to (and you can use some regexp engine,
    no need to write it from scratch), but you are not allowed to import a tokenizer (e.g. from NLTK),
    since you are being asked to write a tokenizer."""
    result = []
    resultdict = {}
    string = ""
    file_path = file_path.lower()
    for i in file_path:
        if i.isalnum():
            string += i
        else:
            # resultdict[string] = resultdict.setdefault(string, 0) + 1

            result.append(string)
            string = ""
    if string != "":
        # resultdict[string] = resultdict.setdefault(string, 0) + 1

        result.append(string)
    return result

def computeWordFrequencies(token):
    """Write another method/function that counts the number of occurrences of each token in the token list.
    Remember that you should write this assignment yourself from scratch, so you are not allowed to import
    a counter when the assignment asks you to write that method."""
    resultdict = {}
    for i in token:
        resultdict[i] = resultdict.setdefault(i, 0) + 1

    return resultdict

def printFrequency(mydict):
    for i in mydict:
        print(f"{i} - {mydict[i]}")

if __name__ == "__main__":
    tokenlist = tokenize("Hi there hi")
    tokendict = computeWordFrequencies(tokenlist)
    printFrequency(tokendict)



