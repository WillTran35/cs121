import PartA as A
import sys

"""Write a program that takes two text files from the command line as arguments
and outputs the number of tokens they have in common. Here is an example of input/output:"""

def findCommonTokens() -> int:
    token1 = A.tokenize(sys.argv[1])
    token2 = A.tokenize(sys.argv[2])

    token1dict = A.computeWordFrequencies(token1)
    token2dict = A.computeWordFrequencies(token2)

    count = 0

    for key in token1dict.keys():
        if key in token2dict:
            print(key)
            count += 1

    print(count)
    return count

if __name__ == "__main__":
    findCommonTokens()
