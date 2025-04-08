# 1. **Grouped Aggregations on Titanic**

#    - Group passengers by `Pclass` and calculate the following:
#      - Average age.
#      - Total fare.
#      - Count of passengers.
#    - Save the results to a new DataFrame.

import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-17/homework/")
df_titanic=pd.read_excel('data/titanic.xlsx')

titanic_grouped = df_titanic.groupby('Pclass').agg({
    'Age': 'mean',          # Average age
    'Fare': 'sum',          # Total fare
    'PassengerId': 'count'  # Count of passengers
}).reset_index()

print("Titanic Grouped Aggregations:")
print(titanic_grouped)

# 2. **Multi-level Grouping on Movie Data**

#    - Group the movies by `color` and `director_name`.
#    - Find:
#      - Total `num_critic_for_reviews` for each group.
#      - Average `duration` for each group.

df_movie = pd.read_csv('data/movie.csv')
movie_grouped = df_movie.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',  # Total number of critic reviews
    'duration': 'mean'               # Average duration
}).reset_index()

print("\nMovie Multi-level Grouping:")
print(movie_grouped)


# 3. **Nested Grouping on Flights**

#    - Group flights by `Year` and `Month` and calculate:
#      - Total number of flights.
#      - Average arrival delay (`ArrDelay`).
#      - Maximum departure delay (`DepDelay`).

df_flights = pd.read_parquet('data/flights')

def avg_arrival_delay(n):
    return sum(n) / len(n) if len(n) > 0 else 0  # Avoid division by zero

def max_departure_delay(n):
    return max(n) if len(n) > 0 else None  # Handle empty groups

def total_flights(n):
    return len(n)

flights_grouped = df_flights.groupby(['Year', 'Month']).agg({
    'FlightNum': total_flights,       # Custom function for total number of flights
    'ArrDelay': ['mean', avg_arrival_delay],  # Built-in and custom function for average arrival delay
    'DepDelay': ['max', max_departure_delay]  # Built-in and custom function for max departure delay
}).reset_index()

print("\nFlights Nested Grouping:")
print(flights_grouped)