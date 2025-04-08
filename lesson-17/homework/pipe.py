# #### **Using `pipe`**

# 1. **Pipeline on Titanic**

#    - Create a pipeline to:
#      - Filter passengers who survived (`Survived == 1`).
#      - Fill missing `Age` values with the mean.
#      - Create a new column, `Fare_Per_Age`, by dividing `Fare` by `Age`.

import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-17/homework/")
df_titanic = pd.read_excel('data/titanic.xlsx')

def filter_survived(df):
    return df[df['Survived'] == 1].copy()

def fill_missing_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

df_titanic_pipeline = (
    df_titanic
    .pipe(filter_survived)
    .pipe(fill_missing_age)
    .pipe(add_fare_per_age)
)

print(df_titanic_pipeline[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())


# 2. **Pipeline on Flights**

#    - Create a pipeline to:
#      - Filter flights with a departure delay greater than 30 minutes.
#      - Add a column `Delay_Per_Hour` by dividing the delay by the scheduled flight duration.



df_flights = pd.read_parquet('data/flights')

def filter_delayed_flights(df):
    df['DepDelay'] = pd.to_numeric(df['DepDelay'], errors='coerce')  # Convert to numeric
    return df[df['DepDelay'] > 30].copy()  # Filter and create a copy

def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['AirTime']
    return df

df_flights_pipeline = (
    df_flights
    .pipe(filter_delayed_flights)
    .pipe(add_delay_per_hour)
)

print(df_flights_pipeline[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())
