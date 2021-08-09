""" Question 1 DNA fragments """

class Node: 
    """
    Initialisation of node for question 1. 

    Time complexity : O(1) 
    Space complexity : auxiliary - O(1) since the size of link is constant
    Parameters : None
    Return : None
    """
    def __init__(self):
        self.link = [None] * 5
        self.freq = 0
        self.high_freq = 0
        self.char = -1
        self.word = None

class SequenceDatabase:
    """
    Initialisation of SequenceDatabase. 

    Time complexity : O(1) 
    Space complexity : auxiliary - O(1)
    Parameters : None
    Return : None
    """
    def __init__(self):
        self.root = Node()
        self.count = 0      # number of strings in the database
    
    """
    Update a given node's data. 

    Time complexity : O(1) 
    Space complexity : auxiliary - O(1)
    Parameters: None
    Return: None
    """
    def update(self, current, comp, key):
        current.word = key
        current.high_freq = comp[0]
        current.char = comp[1]

    """
    Insert a single string into the SequenceDatabase by calling 
    a helper function : addSequence_aux()

    Time complexity : O(N) where N is the length of input string 
    Space complexity : auxiliary - O(N) where N is the length of input string
    Parameters: key - a single non-empty string of uppercase letters from [A-D]
    Return: None
    """
    def addSequence(self, s):
        self.count += 1       # increment number of strings in the trie
        current = self.root
        comp = self.addSequence_aux(current, s, 0)      
        # update root data based on the result returned
        if comp[0] > current.high_freq:
            self.update(current, comp, s)
        elif comp[0] == current.high_freq and comp[1] < current.char:
            self.update(current, comp, s)
        elif comp[1] == current.char and comp[2]:
            self.update(current, comp, s)

    """
    Insert a single string into the SequenceDatabase in a recursive way, and 
    record the frequency it has been added and the least lexicographical.

    Time complexity : O(N) where N is the length of input string 
    Space complexity : auxiliary - O(N) where N is the length of input string
    Parameters: current - current node pointed at
                key - a single non-empty string of uppercase letters from [A-D]
                pos - position pointed to specific letter of string
    Return: a tuple (key frequency, current letter in integer, boolean of updated)
    """
    def addSequence_aux(self, current, key, pos):
        # base case when it reaches end
        if pos == len(key):
            index = 0      # insert a terminal character
            if current.link[index] is None:
                current.link[index] = Node()
            current = current.link[index]
            current.freq += 1
            current.char = index
            return (current.freq, index, False)
                
        char = key[pos]       # letter pointed at
        index = ord(char) - 64       
        if current.link[index] is None:   # if path does not exist
            current.link[index] = Node()          
        current = current.link[index]
        comp = self.addSequence_aux(current, key, pos+1)    # insert next letter

        # update current node's data based on result returned
        updated = True
        if comp[0] > current.high_freq:
            self.update(current, comp, key)
        elif comp[0] == current.high_freq and comp[1] < current.char:   # compare for least lexicographical
            self.update(current, comp, key)  
        elif comp[1] == current.char and comp[2]:    # string updated in deeper node
            self.update(current, comp, key)   
        else:
            updated = False
        return (comp[0], index, updated)
    
    """
    Retrieve a string with given pattern(q) as prefix and higher frequency by 
    calling a helper function: query_aux()

    Time complexity : O(M) where M is the length of input string 
    Space complexity : auxiliary - O(1) 
    Parameters: q - a single string of uppercase letters in [A-D]
    Return: None if no string with q as prefix exists, else string with highest frequency with q 
            as prefix. If two or more strings with prefix q have same freq, return the least lexicographical one
    """
    def query(self, q):
        if self.count == 0:
            return None
        current = self.root
        return self.query_aux(current, q, 0)
    
    """
    A helper function that finds a string with given pattern(q) as prefix. 

    Time complexity : O(M) where M is the length of input string 
    Space complexity : auxiliary - O(1)
    Parameters: current - current node pointed at
                key - prefix pattern to be matched
                pos - position pointed to in key
    Return - a string with key as prefix and match the conditions
    """
    def query_aux(self, current, key, pos):
        # base case where it reaches the end
        if pos == len(key):
            return current.word   
        char = key[pos]
        index = ord(char) - 64
        if current.link[index] is not None:    # if path exists
            current = current.link[index]
            return self.query_aux(current, key, pos+1)
        return None   # no string exists
