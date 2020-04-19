#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 1
# Programmer: Jacob Gray
# Last Edit: 4/19/2020


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
