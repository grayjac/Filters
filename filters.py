#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 4
# Programmer: Jacob Gray
# Last Edit: 4/21/2020


from statistics import mean


def mean_filter(data, filter_width=3):
    """
    This function replaces each sensor reading with the mean of itself and the readings on either side of itself.
    :param data: Data to be filtered. Should be an even length.
    :param filter_width: How many values are averaged. Must be positive and odd.
    :return: Filtered data.
    """
    step = round((filter_width - 1) / 2)
    filtered_data = []

    if filter_width < 0 or filter_width % 2 == 0:
        raise ValueError

    for i in range(0, len(data) - filter_width + 1):
        filtered_data.append(mean(data[i:filter_width + i]))

    return filtered_data
