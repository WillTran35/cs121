import re
import sys
def tokenizeline(line:str) -> list:
    """Helper function to tokenize an individual line."""
    # This function runs in O(n) time complexity, where n is the length of the line.
    # It must iterate through the entire string getting each letter.
    result = []
    string = ""
    line = line.lower()
    pattern = "[a-zA-Z0-9]"
    for i in line:
        if re.search(pattern, i):
            string += i
        else:
            if string != "":
                result.append(string)
            string = ""
    if string != "":
        result.append(string)
    return result
def tokenize(file_path:str) -> list:
    """Write a method/function that reads in a text file and returns a list of the tokens
    in that file. For the purposes of this project, a token is a sequence of alphanumeric characters,
    independent of capitalization (so Apple, apple, aPpLe are the same token).
    You are allowed to use regular expressions if you wish to (and you can use some regexp engine,
    no need to write it from scratch), but you are not allowed to import a tokenizer (e.g. from NLTK),
    since you are being asked to write a tokenizer."""

    # This function runs in O(n) time complexity because it takes each line and passes into tokenizeline() which runs in
    # O(n) complexity
    result = []
    with open(file_path, "r") as line:
        for i in line:
            result += tokenizeline(i)
    return result

def computeWordFrequencies(token:list) -> dict:
    """Write another method/function that counts the number of occurrences of each token in the token list.
    Remember that you should write this assignment yourself from scratch, so you are not allowed to import
    a counter when the assignment asks you to write that method."""

    # This function runs in O(n) time where n is the length of the list. It iterates through the list and adds
    # itself to the dictionary.
    resultdict = {}
    for i in token:
        resultdict[i] = resultdict.setdefault(i, 0) + 1

    return resultdict

def print_frequencies(mydict:str) -> None:
    """Finally, write a method/function that prints out the word frequency count onto the screen.
     The printout should be ordered by decreasing frequency (so, the highest frequency words first;
     if necessary, order the cases of ties alphabetically). """
    sorteditems = sorted(mydict.items(), key = lambda kv: (kv[1], kv[0]))
    # This function runs in O(n) time where n is the length of the list that holds all the dictionary items.
    # Sorting does take O(logn) time but we must iterate through the entire list to print out the results.
    for i in sorteditems:
        print(f"{i[0]} - {i[1]}")

if __name__ == "__main__":
    file = sys.argv[1]
    tokenlist = tokenize(file)
    tokendict = computeWordFrequencies(tokenlist)
    print_frequencies(tokendict)




