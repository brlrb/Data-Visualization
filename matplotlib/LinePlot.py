# Plot using a simple Line Plot

# Import pyplot form matplotlib
from matplotlib import pyplot as plt

# Prepare data
years = [
    1990,
    1991,
    1992,
    1993,
    1994,
    1995,
    1996,
    1997,
    1998,
    1999
]

average_weather = [
    77.1,
    71.2,
    76.7,
    78.2,
    73.4,
    77.6,
    76.4,
    77.8,
    77.1,
    79.2
]

# Prepare to create a line chart
plt.plot(years, average_weather, color = 'blue', marker = 'o', linestyle = 'dashed')

# Add labels
plt.title("Average weather from 1990 <-> 1999")
plt.ylabel("Weather")
plt.xlabel("Year")
plt.show()