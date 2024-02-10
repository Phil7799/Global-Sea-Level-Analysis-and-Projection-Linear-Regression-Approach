#first question

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Assuming the 'epa-sea-level.csv' file is in the same directory
data = pd.read_csv('epa-sea-level.csv')
# print(data.head())
print(data)

#second question

# Extracting the 'Year' and 'CSIRO Adjusted Sea Level' columns
year = data['Year']
sea_level = data['CSIRO Adjusted Sea Level']

# Creating a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(year, sea_level, color='blue', label='CSIRO Adjusted Sea Level')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level (inches)')
plt.title('Global Average Sea Level Change (1880-2022)')
plt.grid(True)
plt.legend()
plt.show()

#third question

# Extracting the 'Year' and 'CSIRO Adjusted Sea Level' columns
year = data['Year']
sea_level = data['CSIRO Adjusted Sea Level']

# Performing linear regression to get the slope, intercept, and other statistics
slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

# Creating a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(year, sea_level, color='blue', label='CSIRO Adjusted Sea Level')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level (inches)')
plt.title('Global Average Sea Level Change (1880-2022)')

# Creating the line of best fit
x_values = year.append(pd.Series([2050]))  # Extend the x-axis to 2050
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='red', label=f'Line of Best Fit (Slope: {slope:.4f})')

plt.grid(True)
plt.legend()
plt.show()

#fourth question

# Filtering the data to include only years from 2000 and onwards
recent_data = data[data['Year'] >= 2000]

# Extracting the 'Year' and 'CSIRO Adjusted Sea Level' columns
year = recent_data['Year']
sea_level = recent_data['CSIRO Adjusted Sea Level']

# Performing linear regression on the recent data to get the slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

# Creating a scatter plot of the recent data
plt.figure(figsize=(12, 6))
plt.scatter(year, sea_level, color='blue', label='CSIRO Adjusted Sea Level (2000 and onwards)')
plt.xlabel('Year')
plt.ylabel('CSIRO Adjusted Sea Level (inches)')
plt.title('Global Average Sea Level Change (Year 2000 and onwards)')

# Creating the new line of best fit, extending it to 2050
x_values = year.append(pd.Series([2050]))  # Extend the x-axis to 2050
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='red', label=f'Line of Best Fit (Slope: {slope:.4f})')

plt.grid(True)
plt.legend()
plt.show()

#fifth question

# Filtering the data to include only years from 2000 and onwards
recent_data = data[data['Year'] >= 2000]

# Extracting the 'Year' and 'CSIRO Adjusted Sea Level' columns
year = recent_data['Year']
sea_level = recent_data['CSIRO Adjusted Sea Level']

# Performing linear regression on the recent data to get the slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)

# Creating a scatter plot of the recent data
plt.figure(figsize=(12, 6))
plt.scatter(year, sea_level, color='blue', label='CSIRO Adjusted Sea Level (2000 and onwards)')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Creating the new line of best fit, extending it to 2050
x_values = year.append(pd.Series([2050]))  # Extend the x-axis to 2050
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='red', label=f'Line of Best Fit (Slope: {slope:.4f})')

plt.grid(True)
plt.legend()
plt.show()


