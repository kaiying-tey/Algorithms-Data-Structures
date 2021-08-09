""" Question 2: Anagrams"""

""" 
Sort a given string into alphabetical order.

Time complexity : O(M) where M is the length of string 
Space complexity : Auxiliary - O(M) where M is the length of input string

Parameter : a_string - a lowercased string
Output : a sorted string in alphabetical order
"""
def counting_sort_str(a_string):
    # initialise count array
    count_array = [0] * (26)
    # update count array with frequency
    for char in a_string:
        position = ord(char) - 97
        count_array[position] = count_array[position] + 1
    # generate a sorted string
    new_string = ""
    for i in range(len(count_array)):
        frequency = count_array[i]
        for _ in range(frequency):
            new_string += chr(i + 97)
    return new_string

""" 
Sort the list based on the first element of each tuple which is 
a string with left-alignment using Radix Sort algortihm
 
Time complexity : O(LM) where L is the length of input list, 
                              M is the length of longest string in list
Space complexity : Auxiliary - O(L) where L is the length of input list

Parameter : a_list - a list of tuples (word, index) 
Output : a sorted list of tuples with left-alignment
                    
"""
def radix_sort_str(a_list):
    # Find maximum length of word in tuple
    max_length = 0
    for tuples in a_list:
        if len(tuples[0]) > max_length:
            max_length = len(tuples[0])

    total_col = 27  # a-z + an additional char
    column = max_length - 1

    while column >= 0:
        # initialise count array
        count_array = [None] * (total_col + 1)
        for i in range(len(count_array)):
            count_array[i] = []
        # update count_array based on ASCII
        for i in range(len(a_list)):
            word = a_list[i][0]
            if column >= len(word): # word has no char at that column
                index = 0              # taken as special char 
            else:
                index = ord(word[column]) - 96
            count_array[index].append((word, a_list[i][1]))
        # update the list to sorted one
        position = 0
        for i in range(len(count_array)):
            frequency = len(count_array[i])
            for j in range(frequency):
                a_list[position] = count_array[i][j]
                position += 1
        # from right to left
        column -= 1

    return a_list

"""
Find a list of strings from list1 which have anagram in list2. 

Time complexity : O(L1M1 + L2M2) where 
                    L1 is length of list1
                    L2 is length of list2
                    M1 is number of characters in the longest string in list1
                    M2 is number of characters in the longest string in list2                 
Space complexity : Auxiliary - O(L1M1 + L2M2) where
                    L1 is length of list1
                    L2 is length of list2
                    M1 is number of characters in the longest string in list1
                    M2 is number of characters in the longest string in list2

Parameters : list1 - a list of lowercased strings with no duplicates
             list2 - a list of lowercased strings with no duplicates
Output : a list of strings from list1
"""
def words_with_anagrams(list1, list2):
    # sort every word to anagram in list1 and mark down index - O(L1M1)
    sorted_list1 = []
    for i in range(len(list1)):
        sorted_str = counting_sort_str(list1[i])
        sorted_list1.append((sorted_str, i))
    # sort every word to anagram in list2 and mark down index - O(L2M2)
    sorted_list2 = []
    for j in range(len(list2)):
        sorted_str = counting_sort_str(list2[j])
        sorted_list2.append((sorted_str, j))
    # sort both lists
    sorted_list1 = radix_sort_str(sorted_list1)
    sorted_list2 = radix_sort_str(sorted_list2)

    res = []
    last_found = ""    # anagram found in previous iteration
    i = 0     # pointer in list1
    j = 0     # pointer in list2
    while i < len(list1):
        word = sorted_list1[i][0]
        if word == last_found:   # anagram already found previously
            res.append(sorted_list1[i])
            i += 1
        # continue from where last iteration stopped
        elif j < len(list2) and word > sorted_list2[j][0]:    # pointed word in list1 greater
            j += 1
        elif j < len(list2) and word == sorted_list2[j][0]:
            res.append(sorted_list1[i])
            last_found = word
            j += 1
            i += 1
        else:
            i += 1
    # Get the strings based on index stored in res
    for i in range(len(res)):
        res[i] = list1[res[i][1]]

    return res
