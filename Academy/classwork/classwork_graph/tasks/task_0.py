# Python3 program to find length of the
# shortest chain transformation from source
# to target
from collections import deque

# Returns length of shortest chain
# to reach 'target' from 'start'
# using minimum number of adjacent
# moves. D is dictionary
def shortestChainLen(start, target, D):

    if start == target:
      return 0
    # If the target is not
    # present in the dictionary
    if target not in D:
        return 0

    # To store the current chain length
    # and the length of the words
    level, wordlength = 0, len(start)

    # Push the starting word into the queue
    Q =  deque()
    Q.append(start)

    # While the queue is non-empty
    while (len(Q) > 0):

        # Increment the chain length
        level += 1

        # Current size of the queue
        sizeofQ = len(Q)

        # Since the queue is being updated while
        # it is being traversed so only the
        # elements which were already present
        # in the queue before the start of this
        # loop will be traversed for now
        for _ in range(sizeofQ):
            # Remove the first word from the queue
            word = list(Q.popleft())
            #Q.pop()

            # For every character of the word
            for pos in range(wordlength):

                # Retain the original character
                # at the current position
                orig_char = word[pos]

                # Replace the current character with
                # every possible lowercase alphabet
                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)

                    # If the new word is equal
                    # to the target word
                    if ("".join(word) == target):
                        return level + 1

                    # Remove the word from the set
                    # if it is found in it
                    if ("".join(word) not in D):
                        continue

                    del D["".join(word)]

                    # And push the newly generated word
                    # which will be a part of the chain
                    Q.append("".join(word))

                # Restore the original character
                # at the current position
                word[pos] = orig_char

    return 0

# Driver code
if __name__ == '__main__':

    # Make dictionary
    D = {}
    D["poon"] = 1
    D["plee"] = 1
    D["same"] = 1
    D["poie"] = 1
    D["plie"] = 1
    D["poin"] = 1
    D["plea"] = 1
    start = "toon"
    target = "plea"

    print("Length of shortest chain is: ",
    shortestChainLen(start, target, D))

# This code is contributed by mohit kumar 29