# 1. Import pandas
import pandas as pd


# 2. Read the "metacritic2.csv" file, and save the data in a dataframe variable. Print the data
question_2 = pd.read_csv('metacritic2.csv', index_col = 2)


# 3. Create a new dataframe with only Mario Games. Save that in a new dataframe variable and print that data (this will involve Boolean indexing)
question_3 = question_2[question_2['Game'].str.contains('Mario')]


# 4. Sort the Mario data by release year in descending order. (a .sort_values() function exists)
question_4 = question_3.sort_values('Release Year', ascending = False)


# 5. Last time we used a loop to find individual data on different platforms, years, etc. There is a .groupby() function that exists as well. Let's start by grouping by Release Year. Run the following code:
# <var> = <dataframe>.groupby("Release Year").count()
# What does it seems like count presents?
question_5 = question_2.groupby('Release Year').count()
##Count represents no. of hits##


# 6. Use groupby again, but this time on Platform. Afterwards, run .count(), .mean(), and .median(). Which platform looks like it has the best games?
question_6 = question_2.groupby('Platform')
question_6a = question_6.count()
question_6b = question_6.mean()
question_6c = question_6.median()


# 7. Create a new dataframe from the HunterAMC.csv file.
question_7 = pd.read_csv('HunterAMC.csv', sep = '\t')


# 8. In that csv, contest 0 is the AMC 10, and contest 2 is the AMC 12. Create two separate dataframes containing data from the two different contests.
question_8a = question_7[question_7['contest'] == 0]
question_8b = question_7[question_7['contest'] == 2]


# 9. Find the average scores for each contest.
question_9a = question_8a.mean()
question_9b = question_8b.mean()
print(question_9a)
print(question_9b)


# 10. For each column, count how often each answer choice was selected.
