# #### **Applying Functions**

import pandas as pd
import os
os.chdir("c:/Users/acer nitro/OneDrive/Desktop/Data_science/Pythonhomeworks/lesson-17/homework/")
# 1. **Apply a Custom Function on Titanic**

#    - Write a function to classify passengers as `Child` (age < 18) or `Adult`.
#    - Use `apply` to create a new column, `Age_Group`, with these values.
# Load the Titanic dataset

df_titanic = pd.read_excel('data/titanic.xlsx')
def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

df_titanic['Age_Group'] = df_titanic['Age'].apply(classify_age)  # Apply the function to create a new column `Age_Group`
print(df_titanic[['Age', 'Age_Group']].head(20))



# 2. **Normalize Employee Salaries**

#    - Load the `employee.csv` file.
#    - Normalize the salaries within each department.
# Load the employee dataset

df_employee = pd.read_csv('data/employee.csv')
def normalize_salary(salaries):
    return (salaries - salaries.min()) / (salaries.max() - salaries.min())

df_employee['Normalized_Salary'] = df_employee.groupby('DEPARTMENT')['BASE_SALARY'].transform(normalize_salary)
print(df_employee[['DEPARTMENT', 'BASE_SALARY', 'Normalized_Salary']].head(20))

# 3. **Custom Function on Movies**

#    - Write a function that returns `Short`, `Medium`, or `Long` based on the duration of a movie:
#      - `Short`: Less than 60 minutes.
#      - `Medium`: Between 60 and 120 minutes.
#      - `Long`: More than 120 minutes.
#    - Apply this function to classify movies in the `movie.csv` dataset.


df_movie = pd.read_csv('data/movie.csv')
def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long' 

df_movie['Duration_Category'] = df_movie['duration'].apply(classify_duration)
print(df_movie[['duration', 'Duration_Category']].head(20))