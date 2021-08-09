""" Question 2 Open reading frames """

class NodeOrf: 
    """
    Initialisation of node for question 2. Index is a list
    that helps to track the first index of suffix of current node.

    Time complexity : O(1) 
    Space complexity : auxiliary - O(1) since the size of link is constant
    Parameters : None
    Return : None
    """
    def __init__(self):
        self.link = [None] * 5
        self.index = []

class OrfFinder:
    """
    Reverse a given string. 

    Time complexity : O(N) where N is the length of input string
    Space complexity : auxiliary - O(N) where N is the length of input string
    Parameters : genome - a single string
    Return : a string in reversed
    """
    def reverse(self, genome):
        res = ""
        for i in range(len(genome)-1, -1, -1):
            res += genome[i]    
        return res

    """
    Initialisation of the OrfFinder with a given genome string. Call function insert() to 
    insert letters into the trie. There are two tries, one can find the prefix of a 
    given pattern, and another can find suffixes of a given pattern.

    Time complexity : O(N^2) where N is the length of input string
    Space complexity : auxiliary - O(N^2) where N is the length of input string
    Parameters : genome - a single string of letters in [A-D]
    Return : None
    """
    def __init__(self, genome):
        self.root1 = NodeOrf()     # a suffix trie of prefixes
        self.root2 = NodeOrf()     # a prefix trie of suffixes
        self.word = genome
        reverse_genome = self.reverse(genome)    # reverse the genome 
        self.insert(self.root1, genome)
        self.insert(self.root2, reverse_genome)

    """
    Insert the suffixes of a given string into the trie, letter by letter. 
    Call the function insert_aux() as helper function. 

    Time complexity : O(N^2) where N is the length of input string
    Space complexity : auxiliary - O(N^2) where N is the length of input string
    Parameters : root - root of the trie, indicates which trie to be inserted
                 genome - a single string of letters in [A-D]
    Return : None
    """
    def insert(self, root, genome):
         for i in range(len(genome)):
            char = genome[i]
            index = ord(char) - 64
            if root.link[index] is None:
                root.link[index] = NodeOrf()
            current = root.link[index]
            current.index.append(i+1)
            self.insert_aux(current, genome, i+1)

    """
    Insert a given string into the trie, letter by letter using recursion.

    Time complexity : O(N) where N is the length of j until length of genome
    Space complexity : auxiliary - O(N) where N is the length of j until length of genome
    Parameters : current - node pointed at
                 genome - a single string of letters in [A-D]
                 j - position pointed at the genome string 
    Return : None
    """
    def insert_aux(self, current, genome, j):
        if j == len(genome):    # base case when j reaches end, insert terminal char
            index = 0
            if current.link[index] is None:   # if path does not exist
                current.link[index] = NodeOrf()
        else:
            char = genome[j]
            index = ord(char) - 64 
            if current.link[index] is None:   # if path does not exist
                current.link[index] = NodeOrf()          
            current = current.link[index]
            current.index.append(j+1)         # record down the first index of suffix
            self.insert_aux(current, genome, j+1)   # continue inserting

    """
    Find all substrings of genome which have start as a prefix and end as a suffix.
    Call function find_aux() to get index list. 

    Time complexity : O(len(start) + len(end) + U) where U is number of characters in the output list
    Space complexity : auxiliary - O(len(start) + len(end) + U) where U is number of characters in the output list 
    Parameters : start - single non-empty string of letters in [A-D]
                 end - single non-empty string of letters in [A-D]
    Return : a list of strings which have start as a prefix and end as a suffix
    """
    def find(self, start, end):
        res = []      # contains all the substrings required
        new_end = []   
        start_by = self.find_aux(start, self.root1)    # find all suffixes index 
        reverse_end = self.reverse(end)            # reverse the end string
        end_by = self.find_aux(reverse_end, self.root2)  # find all prefixes index

        if start_by == [] or end_by == []:   # no substring found that has start as prefix or end as suffix
            return res
        # reverse back all the indices so that they point correctly to original genome
        for index in end_by:
            new_end.append(len(self.word) - index)
        # find the subtrings between start and end
        for e in range(len(new_end)):
            s = 0
            while s < len(start_by):
                if start_by[s] <= new_end[e]:    # prefix must not start after the end index
                    seq = start + self.word[start_by[s] : new_end[e]] + end   
                    res.append(seq)  
                else: 
                    break
                s += 1
        return res
    
    """
    Find the list of indices correspond to a given pattern in given trie. 

    Time complexity : O(M) where M is the length of the pattern
    Space complexity : auxiliary - O(1)
    Parameters : pattern - a sequence of letters to be matched 
                 current - root pointed at, indicates which trie to search 
    Return : a list of indices that is either prefix or suffix of the pattern
    """
    def find_aux(self, pattern, current):
        for char in pattern:   
            index = ord(char) - 64
            if current.link[index] is None:   # no path mathces the pattern
                return []
            current = current.link[index]    
        return current.index


