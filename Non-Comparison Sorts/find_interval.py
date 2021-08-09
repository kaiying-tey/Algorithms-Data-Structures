""" 
Sort a list of integers using Radix Sort algorithm.

Time complexity : O(kN) where k is greatest number of digits in element, 
                        N is the length of the input list
Space complexity : total - O(kN)
                   auxiliary - O(N)
                   where k is greatest number of digits in element,
                   N is the length of the input list

Parameters : new_list - a list of integers
            max_item - the maximum element in the list
Output : a sorted list of integers
"""
def radix_sort(new_list, max_item):
    if len(new_list) <= 1:
        return new_list
    base = 10
    column = 0
    while max_item > 0:      # number of digits of maximum elem
        # initialise count array
        count_array = [None] * base
        for i in range(len(count_array)):
            count_array[i] = []
        # append item to count array
        for item in new_list:
            index = item // (base**column) % base
            count_array[index].append(item)
        # update new_list
        index = 0
        for i in range(len(count_array)):
            frequency = len(count_array[i])  # number of items in linked list
            for j in range(frequency):
                new_list[index] = count_array[i][j]
                index += 1
        column += 1
        max_item = max_item // base

    return new_list

"""
Finds the interval with most number of elements from minimal start time to given t. 

Time complexity : O(kN) where k is greatest number of digits in element, 
                        N is the length of the input list
Space complexity : Auxiliary - O(N) where N is the length of the input list

Parameters : transactions - an unsorted list of non-negative integers
             t - a non-negative integer (length of time)
Output : A tuple (best_t, count) where best_t is the minimal start time
                                    count is the number of elements in interval
"""
def best_interval(transactions, t):
    # find the maximum item
    max_item = transactions[0]
    for item in transactions:
        if item > max_item:
            max_item = item

    transactions = radix_sort(transactions, max_item)  # Time: O(kN)
    result = (0, 0, 0) # (start, count, max_item)
    next_item = (0,0)  # pointer indicates where to start counting (position, value)
    last_item = 0
    i = 0
    while i < len(transactions):            # Time: O(N+N)
        if i == 0 or transactions[i] != transactions[i-1]:
            endpoint = transactions[i] + t
            if endpoint >= max_item:            # until end of list
                count = len(transactions) - i
                last_item = max_item
            elif endpoint < next_item[1]:       # smaller than next item in last iteration
                count = next_item[0] - i
                last_item = next_item[1]
            else:
                index = next_item[0]
                count = next_item[0] - i        # count from where last iteration stopped
                while index < len(transactions) and transactions[index] <= endpoint:
                    count += 1
                    last_item = transactions[index]
                    index += 1
                if index < len(transactions):
                    next_item = (index, transactions[index])
            # update result to highest number of count
            if count > result[1]:
                result = (transactions[i], count, last_item)
        i += 1

    # Get minimum start time
    minimum = result[2] - t
    if minimum < result[0]:
        result = (max(minimum, 0), result[1], result[2])

    return (result[0], result[1])
