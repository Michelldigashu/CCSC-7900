# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:45:05 2024

@author: m.digashu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the contents of the CSV file into a dataframe

df= pd.read_csv('C:/Users/Admin/Downloads/FAOSTAT_data(1).csv')

# Check and clean the column names
df.columns = df.columns.str.strip()  # Trim whitespaces

# Step 2: Extract the Apple data
apples_df = df[df['Item'] == 'Apples']

# Step 3: Extract the "Area harvested" and "Yield" for Apples
area_harvested_df = apples_df[apples_df['Element'] == 'Area harvested'][['Year', 'Value']]
yield_df = apples_df[apples_df['Element'] == 'Yield'][['Year', 'Value']]

# Merge the two dataframes on 'Year'
merged_df = pd.merge(area_harvested_df, yield_df, on='Year', suffixes=('_Area', '_Yield'))

# Rename columns for clarity
merged_df.columns = ['Year', 'Area harvested', 'Yield']

# Step 4: Convert the filtered data to a NumPy array
apples_harvest_yield_array = merged_df.to_numpy()

# Step 5: Identify the years with the maximum and minimum yield
max_yield_index = np.argmax(apples_harvest_yield_array[:, 2])
min_yield_index = np.argmin(apples_harvest_yield_array[:, 2])
max_yield_year = apples_harvest_yield_array[max_yield_index]
min_yield_year = apples_harvest_yield_array[min_yield_index]

print("Max yield year:", max_yield_year[0], "with yield:", max_yield_year[2])
print("Min yield year:", min_yield_year[0], "with yield:", min_yield_year[2])

# Step 6: Calculate the annual deviations (anomalies) for "Yield"
mean_yield = np.mean(apples_harvest_yield_array[:, 2])
yield_anomalies = apples_harvest_yield_array[:, 2] - mean_yield

# Save the yield anomalies to a new CSV file with proper formatting
anomalies_df = pd.DataFrame({
    'Year': apples_harvest_yield_array[:, 0],
    'Yield Anomaly': yield_anomalies
})
anomalies_df.to_csv('apples_yield_anomalies.csv', index=False)

# Step 7: Plot a time series of the area harvested
plt.figure(figsize=(10, 5))
plt.plot(apples_harvest_yield_array[:, 0], apples_harvest_yield_array[:, 1], marker='o')
plt.xlabel('Year')
plt.ylabel('Area harvested')
plt.title('Apples Area Harvested Over Time')
plt.grid()
plt.show()

# Step 8: Plot a time series of yield anomalies
plt.figure(figsize=(10, 5))
plt.plot(apples_harvest_yield_array[:, 0], yield_anomalies, marker='o', color='orange')
plt.xlabel('Year')
plt.ylabel('Yield Anomalies')
plt.title('Apples Yield Anomalies Over Time')
plt.grid()
plt.show()
