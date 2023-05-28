# Create the years and durations lists
years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90]

# Create a dictionary with the two lists
movie_dict = {
              "years":years,
              "durations":durations
             }

# Print the dictionary
print("movie_dict")
print(movie_dict)
print()


# Import pandas under its usual alias
from cgi import print_directory
from lib2to3.pgen2.token import RPAR
import pandas as pd

# Create a DataFrame from the dictionary
durations_df=pd.DataFrame(movie_dict)


# Print the DataFrame
print("durations_df : ")
print(durations_df)
print()
import matplotlib.pyplot as plt
fig = plt.figure()

#----------------- A visual inspection of our data -------------------------------

# A line plot of release_years and durations

plt.plot(years,durations)

# Create a title
plt.title("Netflix Movie Durations 2011-2020" )

# Show the plot
plt.show()


#--------------------------- Loading the rest of the data from a CSV ------------------------------

"""
Well, it looks like there is something to the idea that movie lengths have decreased over the past ten years! But equipped only with our friend's aggregations, we're limited in the further explorations we can perform. There are a few questions about this trend that we are currently unable to answer, including:

1-What does this trend look like over a longer period of time?
2-Is this explainable by something like the genre of entertainment?

We now have access to the CSV file, available at the path "netflix_data.csv". 
Let's create another DataFrame, this time with all of the data.

"""
# Read in the CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# the first five rows of the DataFrame
print("the first five rows of the DataFrame netflix_df: ")
print(netflix_df[0:5])
print()

#----------------------------  Filtering for movies! ------------------------------------------
"""
Okay, we have our data! Now we can dive in and start looking at movie lengths.

"""
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"]=="Movie"]

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[["title","country","genre","release_year","duration"]]

#  the first five rows of the new DataFrame
print("the first five rows of the new DataFrame netflix_movies_col_subset :")
print(netflix_movies_col_subset.iloc[0:5])
print()

#------------------------------------ Creating a scatter plot -------------------------------
'''
Okay, now we're getting somewhere
.We've read in the raw data, selected rows of movies, and have limited our DataFrame to our columns of interest.
Let's try visualizing the data again to inspect the data over a longer range of time.

'''
# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[["release_year"]],netflix_movies_col_subset[["duration"]])

# Create a title
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.show()

#--------------------------------- Digging deeper ------------------------------------

# Filter for durations shorter than 60 minutes
short_movies=netflix_movies_col_subset[ netflix_movies_col_subset['duration'] < 60 ]


# Print the first 20 rows of short_movies
print("the first 20 rows of short_movies : ")
print(short_movies.iloc[0:20])
print()

#-------------------------------- Plotting with color! -------------------------------
# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for lab, rows in netflix_movies_col_subset.iterrows() :
    if rows["genre"]=="Children":
        colors.append("red")
    elif rows["genre"]=="Documentaries":
        colors.append("blue")
    elif rows["genre"]=="Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset[["release_year"]],netflix_movies_col_subset[["duration"]],c=colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()        


'''

100/1OO --->1234
        ---> 12


'''