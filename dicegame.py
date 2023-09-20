import pandas as pd
import numpy as np
import matplotlib as plt

die = pd.DataFrame(np.arange(1, 7))  # Create a DataFrame with values 1 to 6

sum_of_dice = die.sample(2, replace=True).sum().iloc[0]  # Sample 2 values and calculate their sum

results = []  # Create an empty list to store the results

for x in range(50):
    result = die.sample(2, replace=True).sum().iloc[0]  # Simulate rolling 2 dice and calculate the sum
    results.append(result)

freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()

sort_freq.plot()

