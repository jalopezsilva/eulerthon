"""
 Problem 14 - Longest Collatz Sequence
    The module calculates the longest collatz sequence in a set of integers. 
    It uses a simple recursive algorithm with memoization 

    Params:
        max_limit - All numbers from 1 to max_limit will be considered.

    Returns:
        The steps in the maximum sequence, the number with that sequence

"""
import sys

def longest_collatz_sequence(max_limit):
    maximum_sequence = -1
    maximum_sequence_number = None

    # Initializes memory set with base cases
    memory_set = { 2:2, 1:1 }

    if max_limit in memory_set:
        maximum_sequence = memory_set[max_limit]
        maximum_sequence_number = max_limit
    else:
        for i in range(1, max_limit+1):
            sequence_length = calculate_collatz_sequence(i, memory_set)
            if sequence_length > maximum_sequence:
                maximum_sequence = sequence_length
                maximum_sequence_number = i

    return maximum_sequence, maximum_sequence_number

def calculate_collatz_sequence(number, memory_set):
    sequence_length = 0
    next_number = -1

    if number % 2 == 0:
        next_number = number / 2
    else:
        next_number = (number * 3) + 1

    if next_number in memory_set:
        sequence_length = memory_set[next_number]
    else:
        sequence_length = calculate_collatz_sequence(next_number, memory_set) 

    sequence_length += 1
    memory_set[number] = sequence_length
    return sequence_length

if __name__ == '__main__':
    if len( sys.argv ) == 1:
        raise Exception('Enter maximum number to calculate collatz sequence.')

    max_limit = int(sys.argv[1])
    print longest_collatz_sequence(max_limit)
