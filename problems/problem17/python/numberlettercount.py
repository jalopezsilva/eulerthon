#!/usr/bin/env python
"""
Number letters count 

    Module sums the length of the word representation of 
    all numbers between 1 and a given number.

    Pre:
        Number must be greater than 1 and less than 1001

"""
import sys

GLUE = 'and'
MAX_LIMIT = 1000
MIN_LIMIT = 1 

def number_letter_count( max_number ):
    D = get_dictionary()
    count = 0
    for i in range( MIN_LIMIT, max_number + 1 ):
        remainder = i
        word = ''
        while remainder != 0:
            if remainder >= 1000:
                multiple, remainder = divmod( remainder, 1000 )
                word += D[multiple] + D[1000]
            elif remainder >= 100:
                multiple, remainder = divmod( remainder, 100 )
                word += D[multiple] + D[100] 
                word += GLUE if remainder != 0 else ''
            elif remainder >= 20:
                multiple, remainder = divmod( remainder, 10 )
                word += D[multiple*10] 
            else:
                multiple, remainder = divmod( remainder, 1 )
                word += D[multiple]
        count += len(word)
    return count

def get_dictionary():
    D = {
        1    : 'one',
        2    : 'two',
        3    : 'three',
        4    : 'four',
        5    : 'five',
        6    : 'six',
        7    : 'seven',
        8    : 'eight',
        9    : 'nine',
        10   : 'ten',
        11   : 'eleven',
        12   : 'twelve',
        13   : 'thirteen',
        14   : 'fourteen',
        15   : 'fifteen',
        16   : 'sixteen',
        17   : 'seventeen',
        18   : 'eighteen',
        19   : 'nineteen',
        20   : 'twenty',
        30   : 'thirty',
        40   : 'forty',
        50   : 'fifty',
        60   : 'sixty',
        70   : 'seventy',
        80   : 'eighty',
        90   : 'ninety',
        100  : 'hundred',
        1000 : 'thousand'
    }
    return D

if __name__ == '__main__':
    if len( sys.argv ) == 1:
        raise Exception('Please indicate the upper limit for counting')

    max_number = int(sys.argv[1])
    if max_number > MAX_LIMIT or max_number < MIN_LIMIT:
        limit_string_max = str(MAX_LIMIT)
        limit_string_min = str(MIN_LIMIT)
        raise Exception('Invalid limit - ' +
                        'Numbers from ' + limit_string_min + ' to ' +
                         limit_string_max + ' are valid' )
    print number_letter_count( max_number )

