# #### Part 3: Challenges and Explorations  
import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-16/homework/")
# - From **`iris.json`**: Calculate the mean, median, and standard deviation for each numerical column.  
df_iris = pd.read_json("data/iris.json")
mean_values = df_iris.mean(numeric_only=True)
median_values = df_iris.median(numeric_only=True)
std_values = df_iris.std(numeric_only=True)

print("Mean for each numerical column:\n", mean_values)
print("\nMedian for each numerical column:\n", median_values)
print("\nStandard deviation for each numerical column:\n", std_values)


# - From **`titanic.xlsx`**: Find the minimum, maximum, and sum of passenger ages.  
df_titanic=pd.read_excel('data/titanic.xlsx')
df_titanic['Age'] = df_titanic['Age'].fillna(0)  # Replace NaN with 0
minm=df_titanic["Age"].min()
maxm=df_titanic["Age"].max()
summa=df_titanic["Age"].sum()

print("\nMinimum age: ", minm)
print("\nMaximum age: ", maxm)
print("\nSum of passenger ages: ", summa)


# - From **`movie.csv`**:  
#     - Identify the director with the highest total `director_facebook_likes`.  
#     - Find the 5 longest movies and their respective directors.  
df_movie=pd.read_csv('data/movie.csv')
max_likes = df_movie['director_facebook_likes'].max()  # Find the maximum likes
director_highest = df_movie[df_movie['director_facebook_likes'] == max_likes]['director_name'].iloc[0]  # Get the director's name
print("Director with the highest total `director_facebook_likes`:", director_highest)


longest_movies = df_movie.nlargest(5, 'duration')[['movie_title', 'director_name', 'duration']]
print("\nThe 5 longest movies and their respective directors:")
print(longest_movies.to_string(index=False))  


# - From **Flights parquet file**:  
#     - Check for missing values in the dataset. Fill missing values in a numerical column with the column’s mean.  

df_flights = pd.read_parquet("data/flights")
missing_values = df_flights.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)


for numerical_column in df_flights.columns.values: 
    df_flights[numerical_column] = df_flights[numerical_column].fillna(df_flights[numerical_column].mean())
