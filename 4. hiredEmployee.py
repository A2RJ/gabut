import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='adventureworks'
)

query = """
    SELECT TIMESTAMPDIFF(YEAR, BirthDate, HireDate) AS AgeAtHire, 
       SUM(CASE WHEN Gender = 'F' THEN 1 ELSE 0 END) AS Female,
       SUM(CASE WHEN Gender = 'M' THEN 1 ELSE 0 END) AS Male
    FROM employee
    GROUP BY AgeAtHire
    ORDER BY AgeAtHire
"""
df = pd.read_sql_query(query, conn)

df = pd.DataFrame({
    "HiredEmployee": df['AgeAtHire'],
    "Female": df['Female'],
    "Male": df['Male']
})

fig, ax = plt.subplots()
df.plot(x="HiredEmployee", y=["Female", "Male"], ax=ax, kind='line')
plt.xlabel("Hired Employee Age")
plt.ylabel("Total Employee")
plt.title("Total Female and Male Hired Employees by Age")
plt.legend(["Female", "Male"])
ax.grid(True)
plt.show()
conn.close()
