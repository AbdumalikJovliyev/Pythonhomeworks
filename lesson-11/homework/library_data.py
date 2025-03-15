# ### Task 2

# 1. **Database Creation**:
#    - Create a new SQLite database named `library.db`.
#    - Define a table called **Books** with the following schema:
#      - **Title**: TEXT
#      - **Author**: TEXT
#      - **Year_Published**: INTEGER
#      - **Genre**: TEXT

import sqlite3
con=sqlite3.connect("library.db")
cursor=con.cursor()

cursor.execute("""
Create table if not exists Books
    (Title TEXT,
    Author TEXT,
    Year_pub INTEGER,
    Genre TEXT);
""") 

# 2. **Insert Data**:
#    - Populate the **Books** table with the following entries:

# | Title                  | Author          | Year_Published | Genre      |
# |------------------------|-----------------|----------------|------------|
# | To Kill a Mockingbird  | Harper Lee      | 1960           | Fiction    |
# | 1984                   | George Orwell   | 1949           | Dystopian  |
# | The Great Gatsby       | F. Scott Fitzgerald | 1925        | Classic    |

cursor.executemany("""
Insert into Books (Title,Author,Year_pub,Genre) Values(?,?,?,?);""",
    [
        ('To Kill a Mockingbird', 'Harper Lee',1960,'Fiction'),
        ('1984', 'George Orwell',1949,'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald',1925,'Classic'),
    ])
con.commit()

# 3. **Update Data**:
#    - Update the `Year_Published` of **1984** to **1950**.

cursor.execute("""
UPDATE Books
SET Year_pub = 1950
WHERE Title = '1984';              
""")
con.commit()

# 4. **Query Data**:
#    - Retrieve and display the **Title** and **Author** of all books where the `Genre` is **Dystopian**.

cursor.execute("""
SELECT Title, Author FROM Books WHERE Genre='Dystopian';""")
print("Books that are Dystopian genre: ")
print(cursor.fetchall())

# 5. **Delete Data**:
#    - Remove all books published before the year 1950 from the table.

cursor.execute("""
DELETE FROM Books WHERE Year_pub < 1950;
""")
con.commit()

# 6. **Bonus Task**:
#    - Add a new column called `Rating` to the **Books** table and update the data with the following values:

# | Title                  | Rating |
# |------------------------|--------|
# | To Kill a Mockingbird  | 4.8    |
# | 1984                   | 4.7    |
# | The Great Gatsby       | 4.5    |

cursor.execute("""
ALTER TABLE Books ADD COLUMN Rating FLOAT;
""")

cursor.executemany("""
UPDATE Books SET Rating = ? WHERE Title = ?; 
""", [
    (4.8, 'To Kill a Mockingbird'),
    (4.7, '1984'),
    (4.5, 'The Great Gatsby')
])

con.commit()


# 7. **Advanced Query**:
#    - Retrieve all books sorted by their `Year_Published` in ascending order.

cursor.execute("""
SELECT * FROM Books ORDER BY Year_pub ASC;
""")
print("\nBooks sorted by their year of publishment (Ascending):")
print(cursor.fetchall())

# Close the connection
con.close()


