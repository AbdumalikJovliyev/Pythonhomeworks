#### Part 1: Reading Files  
# 1. **`chinook.db`**  
#    - Use the `sqlite3` library to connect to the database.  
#    - Read the `customers` table into a pandas DataFrame. Display the first 10 rows.  
import sqlite3
import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-16/homework/")
db_path = os.path.abspath("data/chinook.db")  # Convert relative to absolute path
with sqlite3.connect(db_path) as connection:
    df_employee = pd.read_sql_query("SELECT * FROM customers", con=connection)
print(df_employee.head(10))


# 2. **`iris.json`**  
#    - Load the JSON file into a DataFrame. Show the shape of the dataset and the column names.  

df_iris=pd.read_json("data/iris.json")
print("Shape of the dataset iris.json: ", df_iris.shape)
print("Columns of the dataset: ",df_iris.columns)

# 3. **`titanic.xlsx`**  
#    - Load the Excel file into a DataFrame. Use `head` to display the first 5 rows.  
df_xlsl=pd.read_excel("data/titanic.xlsx")
print("The first 5 rows of the titanic.xlsx file: ", df_xlsl.head(5))

# 4. **Flights parquet file**  
#    - Read the Parquet file into a DataFrame and use `info` to summarize it.  
flights=pd.read_parquet("data/flights")
print(flights.info)

# 5. **`movie.csv`**
#   
#    - Load the CSV file into a DataFrame and display a random sample of 10 rows.
movies=pd.read_csv("data/movie.csv")
print(movies.sample(10))


#Extra html task
df_riches=pd.read_html(r"http://en.wikipedia.org/wiki/The_World%27s_Billionaires")
print(df_riches)