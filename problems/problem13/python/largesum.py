"""
Problem 13  - Large Sum
    Find the first ten digits of the sum of the following one-hundred 50-digit numbers

    Although the instance of the problem given in PE can be solved only the sum
    for at most 11 digits, the general case fails.
"""
import sys

# We need 10 digits,
precision_needed = 10

def solve_large_sum(file_name):
    numbers = read_numbers(file_name)
    sum = compute_sum(numbers)
    string_int = str(sum)
    return string_int[0:precision_needed]

def read_numbers(file_name):
    lines = []
    with open(file_name, 'r') as f:
        content = f.read()
    lines = content.split()
    numbers = [ int(number) for number in lines ]
    return numbers

def compute_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    if len( sys.argv ) == 1:
        raise Exception('Please provide input file for problem..')
    file_path = sys.argv[1]
    print solve_large_sum(file_path)
