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
    SELECT
    edh.DepartmentID,
    d.Name AS DepartmentName,
    AVG(DATEDIFF(IF(edh.EndDate = 0, NOW(), edh.EndDate), edh.StartDate) / 30) AS AverageTenureInMonths
    FROM employeedepartmenthistory edh
    JOIN department d ON edh.DepartmentID = d.DepartmentID
    WHERE edh.EndDate != 0
    GROUP BY edh.DepartmentID, d.Name;
    """
df = pd.read_sql_query(query, conn)
df = pd.DataFrame({
    "DepartmentName": df['DepartmentName'],
    "AverageTenureInMonths": df['AverageTenureInMonths'],
})

fig, ax = plt.subplots()
df.plot(y="AverageTenureInMonths", kind='bar', ax=ax)
ax.set_xticklabels(df['DepartmentName'], rotation='horizontal')
plt.xlabel("Department Name")
plt.ylabel("Average Tenure In Months")
plt.title("The average duration of employees working in a department")
ax.grid(True)
plt.show()
conn.close()
