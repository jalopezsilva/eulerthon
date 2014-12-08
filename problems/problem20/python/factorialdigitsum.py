#!/usr/bin/env python

import sys


def factorial_digit_sum(integer_n, calculation_method):
    factorial = calculation_method(integer_n)
    digit_sum = 0
    factorial_string = str(factorial)
    for digit in factorial_string:
        digit_sum += int(digit)
    return digit_sum


def brute_force_calculate_factorial(integer_n):
    result = integer_n
    while integer_n > 1:
        integer_n -= 1
        result *= integer_n
    return result


def trimming_factorial(integer_n):
    trimmed_factorial = integer_n
    while integer_n > 1:
        integer_n -= 1
        trimmed_factorial *= integer_n
        if trimmed_factorial % 10 == 0:
            trimmed_factorial = _reduce_multiples(trimmed_factorial, 10)
    return trimmed_factorial


def _reduce_multiples(number, multiple):
    while number % multiple == 0:
        number = number / multiple
    return number


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Please provide a integer n and a' +
                        ' calculation method ' + ' (ie. brute, trimmed)')

    integer_n = int(sys.argv[1])
    method = sys.argv[2]
    calculation_method = brute_force_calculate_factorial
    if method == 'trimmed':
        calculation_method = trimming_factorial

    print factorial_digit_sum(integer_n, calculation_method)
