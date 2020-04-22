#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 1
# Programmer: Jacob Gray
# Last Edit: 4/21/2020


from random import randint


def sum_i(numbers_list):
    """
    Calculates and returns the sum of all numbers in its argument by use of a for loop.
    :param numbers_list: List of numbers you want to sum.
    :return: Sum of all arguments in nums list.
    """

    loop_sum = 0

    for i in range(0, len(numbers_list)):
        loop_sum += numbers_list[i]

    return loop_sum


def sum_r(numbers_list):
    """
    Calculates and returns the sum of all numbers in its argument by use of recursion.
    :param numbers_list: List of numbers you want to sum.
    :return: Sum of all arguments in nums list.
    """

    if len(numbers_list) == 1:
        return numbers_list[0]
    else:
        return numbers_list[0] + sum_r(numbers_list[1:])


def compare_test(a, b):
    """
    Compares integers a and b and raises ValueError if they're not equal.
    :param a: Integer.
    :param b: Integer.
    :return: Raises ValueError if integers a and b are not equal, does nothing otherwise.
    """
    if a != b:
        raise ValueError


if __name__ == '__main__':
    for i in range(0, 999):
        rand_integer_a = randint(-10000, 10000)
        rand_integer_b = randint(-10000, 10000)
        compare_test(sum([rand_integer_a, rand_integer_b]), sum_i([rand_integer_a, rand_integer_b]))
        compare_test(sum([rand_integer_a, rand_integer_b]), sum_r([rand_integer_a, rand_integer_b]))
    else:
        print('No errors found')
