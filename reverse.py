#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 2
# Programmer: Jacob Gray
# Last Edit: 4/21/2020


from random import choice
from random import randint
from sum import compare_test
from string import ascii_letters


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


def random_string(lower_bound, upper_bound):
    """
    Generates a random string of upper and lowercase letters of random length between two limits.
    :param lower_bound: Lower letter limit length.
    :param upper_bound: Upper letter limit length.
    :return: A random string of letters.
    """
    rand_length = randint(lower_bound, upper_bound)
    return ''.join(choice(ascii_letters) for i in range(rand_length))


if __name__ == '__main__':
    for i in range(0, 999):
        test_string = random_string(5, 15)
        compare_test(reverse_i(test_string), reverse_r(test_string))
    else:
        print('No errors found')
