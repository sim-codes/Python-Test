import csv
from collections import Counter
import numpy as np

# Reading the file and saving each occurence
with open("survey.csv", "r") as file:
    count = Counter()
    read = csv.DictReader(file)

    for i in read:
        count.update(i["COLOURS"].split(","))


# Sorting the colors by value
sorted_colors = sorted(count.items(), key=lambda x: x[1])
dic = {k: v for k, v in sorted_colors}

# Calculating the mean
mean = np.mean(list(dic.values()))

# Calculating the Median
half_values = sum(dic.values()) // 2

# Calculating Variance
squared_diff = [(x - mean) ** 2 for x in dic.values()]
sum_squared_diff = sum(squared_diff)
variance = sum_squared_diff // len(dic.values())


# Calculation the probability of choosing red
color_list = list(dic.keys())
red_count = color_list.count("RED")
total_count = sum(dic.values())
probability_red = red_count / sum(dic.values())

# Calculating the cummulative frequency
value = list(dic.values())
cum_val = np.cumsum(value)
cum_colors = {key: value for key, value in zip(dic.keys(), cum_val)}


def find_colour(n):
    """Function to return color using value"""
    for color, value in cum_colors.items():
        if value >= n:
            return color


median = find_colour(half_values)
mean = find_colour(mean)
mode = max(dic, key=dic.get)
variance = find_colour(variance)

# The result
print(f"Which color of shirt is the mean color?-> {mean}")
print(f"Which color is mostly worn throughout the week?-> {mode}")
print(f"Which color is the median?-> {median}")
print(f"Get the variance of the colors: -> {variance}")
print(
    f"If a colour is chosen at random, what is the probability that the color is red? -> {probability_red}"
)
