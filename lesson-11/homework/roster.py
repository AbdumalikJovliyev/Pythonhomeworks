# ### Task 1

# 1. **Database Creation**:
#    - Create a new SQLite database named `roster.db`.
#    - Define a table called **Roster** with the following schema:
#      - **Name**: TEXT
#      - **Species**: TEXT
#      - **Age**: INTEGER

# 2. **Insert Data**:
#    - Populate the **Roster** table with the following entries:

# | Name           | Species  | Age |
# |----------------|----------|-----|
# | Benjamin Sisko | Human    | 40  |
# | Jadzia Dax     | Trill    | 300 |
# | Kira Nerys     | Bajoran  | 29  |

# 3. **Update Data**:
#    - Update the `Name` of **Jadzia Dax** to **Ezri Dax**.

# 4. **Query Data**:
#    - Retrieve and display the **Name** and **Age** of all characters where the `Species` is **Bajoran**.

# 5. **Delete Data**:
#    - Remove all characters aged over 100 years from the table.

# 6. **Bonus Task**:
#    - Add a new column called `Rank` to the **Roster** table and update the data with the following values:
   
# | Name           | Rank       |
# |----------------|------------|
# | Benjamin Sisko | Captain    |
# | Ezri Dax       | Lieutenant |
# | Kira Nerys     | Major      |

# 7. **Advanced Query**:
#    - Retrieve all characters sorted by their `Age` in descending order.

import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 1. Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);
""")

# 2. Insert data into the Roster table
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?);
""", [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
])

conn.commit()

# 3. Update Data: Change "Jadzia Dax" to "Ezri Dax"
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';
""")
conn.commit()

# 4. Query Data: Retrieve Name and Age of Bajoran species
cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran';
""")
print("Bajoran Characters:")
print(cursor.fetchall())

# 5. Delete Data: Remove characters aged over 100 years
cursor.execute("""
DELETE FROM Roster WHERE Age > 100;
""")
conn.commit()

# 6. Bonus Task: Add a new column 'Rank' and update values
cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT;
""")

cursor.executemany("""
UPDATE Roster SET Rank = ? WHERE Name = ?; 
""", [
    ('Captain', 'Benjamin Sisko'),
    ('Lieutenant', 'Ezri Dax'),
    ('Major', 'Kira Nerys')
])
conn.commit()

# 7. Advanced Query: Retrieve all characters sorted by Age in descending order
cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC;
""")
print("\nCharacters sorted by Age (Descending):")
print(cursor.fetchall())

# Close the connection
conn.close()
