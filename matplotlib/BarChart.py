# BarChart
# Good to use when viewing data on discrete set of items

# Import pyplot form matplotlib
from matplotlib import pyplot as plt

movies = ["Superwomen", "Iron Man", "X-Men", "Ant Man", "Superman", "Spider-Man"]
overallRatings = [9.9, 9.5, 9.8, 9.7, 9.9, 9.8]

# Adding padding to the bar in bar chart
xs = [i + 0.1 for i, _ in enumerate(movies)]

# Plot Barchart
plt.bar(xs, overallRatings)

# Label x-axis with movie names at bar centers
plt.ylabel("Overall Ratings")
plt.xlabel("Movies")
plt.title("Marvel Movies")
plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

plt.show()
