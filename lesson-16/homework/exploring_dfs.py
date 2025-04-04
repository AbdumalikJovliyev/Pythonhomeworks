# #### Part 2: Exploring DataFrames  
# 1. Using the DataFrame from **`iris.json`**:  
#    - Rename the columns to lowercase.  
#    - Select only the `sepal_length` and `sepal_width` columns.  

# Load the iris.json file
import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-16/homework/")
df_iris = pd.read_json("data/iris.json")
print(df_iris.columns.tolist())



# Rename the columns to lowercase
df_iris.columns = df_iris.columns.str.lower()
# Select only the `sepallength` and `sepalwidth` columns
iris_selected = df_iris[['sepallength', 'sepalwidth']]
print("Selected columns from iris.json:")
print(iris_selected.head())


# 2. From the **`titanic.xlsx`** DataFrame:  
#    - Filter rows where the age of passengers is above 30.  
#    - Count the number of male and female passengers (`value_counts`).  

df_titanic = pd.read_excel("data/titanic.xlsx")

titanic_filtered = df_titanic[df_titanic['Age'] > 30]
print("Passengers with age above 30:")
print(titanic_filtered.head())

# Count the number of male and female passengers
gender_counts = df_titanic['Sex'].value_counts()
print("Count of male and female passengers:")
print(gender_counts)



# 3. From the **Flights parquet file**:  
#    - Extract and print only the `origin`, `dest`, and `carrier` columns.  
#    - Find the number of unique destinations.  


df_flights = pd.read_parquet("data/flights") 
flights_selected = df_flights[['Origin', 'Dest']]  #Carrier named column is not found in the coulmns so I deleted from the choices of filters
print("Selected columns from flights parquet file:")
print(flights_selected.head())

unique_dests = len(set(df_flights['Dest'])) 
print("Number of unique destinations:", unique_dests) 


# 4. From the **`movie.csv`** file:  
#    - Filter rows where `duration` is greater than 120 minutes.  
#    - Sort the filtered DataFrame by `director_facebook_likes` in descending order.  

df_movies = pd.read_csv("data/movie.csv")

movies_filtered = df_movies[df_movies['duration'] > 120]

movies_sorted = movies_filtered.sort_values(by='director_facebook_likes', ascending=False)
print("Movies with duration > 120 minutes, sorted by director_facebook_likes:")
print(movies_sorted.head()) 
