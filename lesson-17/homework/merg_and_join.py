# #### **Merging and Joining**

# 1. **Inner Join on Chinook Database**
import pandas as pd
import os
import sqlite3
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-17/homework/")

#    - Load the `chinook.db` database.
#    - Perform an inner join between the `customers` and `invoices` tables on the `CustomerId` column.
#    - Find the total number of invoices for each customer.

conn = sqlite3.connect('data/chinook.db')
query = """
SELECT c.CustomerId, c.FirstName, c.LastName, COUNT(i.InvoiceId) AS TotalInvoices
FROM customers c
INNER JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName
"""
df_inner_join = pd.read_sql_query(query, conn)
conn.close()
print(df_inner_join)

# 2. **Outer Join on Movie Data**

#    - Load the `movie.csv` file.
#    - Create two smaller DataFrames:
#      - One with only `director_name` and `color`.
#      - Another with `director_name` and `num_critic_for_reviews`.
#    - Perform a left join and then a full outer join on `director_name`.
#    - Count how many rows are in the resulting DataFrames for each join type.
df_movie = pd.read_csv('data/movie.csv')
df_director_color = df_movie[['director_name', 'color']]
df_dir_name_num_critic = df_movie[['director_name', 'num_critic_for_reviews']]
result1 = pd.merge(df_director_color, df_dir_name_num_critic, on='director_name', how='left')
result2 = pd.merge(df_director_color, df_dir_name_num_critic, on='director_name', how='outer')
print("Left Join Result:")
print(result1)
print("\nFull Outer Join Result:")
print(result2)