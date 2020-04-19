#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 2
# Programmer: Jacob Gray
# Last Edit: 4/19/2020


def reverse_i(character_list):
    """
    This function takes the input character list and returns a new list with all the elements in reverse order by
    use of a for loop.
    :param character_list: List of numbers or characters.
    :return: New list containing all elements of input character list, but in reverse order.
    """

    new_list = []

    for i in range(1, len(character_list) + 1):
        new_list.append(character_list[-i])

    return new_list


def reverse_r(character_list):
    """
    This function takes the input character list and returns a new list with all the elements in reverse order by
    use of recursion.
    :param character_list:
    :return:
    """

    if len(character_list) == 0:
        return []
    else:
        return [character_list[-1]] + reverse_r(character_list[:-1])
