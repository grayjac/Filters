#!/usr/bin/env python3


# ME499-S20 Python Lab 2 Problem 3
# Programmer: Jacob Gray
# Last Edit: 4/19/2020

from sensor import generate_sensor_data
from filters import mean_filter
import csv

test_data = generate_sensor_data(1000)
filtered_test_data = mean_filter(test_data, 17)

with open('sensor_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(test_data)
    writer.writerow(filtered_test_data)
