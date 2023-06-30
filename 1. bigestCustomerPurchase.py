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
    SELECT CONCAT(c.FirstName, ' ', c.LastName) AS FullName, ROUND(SUM(p.TotalDue), 2) AS Amount
    FROM contact c
    JOIN employee e ON c.ContactID = e.ContactID
    JOIN purchaseorderheader p ON e.EmployeeID = p.EmployeeID
    GROUP BY e.EmployeeID
    ORDER BY Amount DESC;
"""
df = pd.read_sql_query(query, conn)
df = pd.DataFrame({
    "FullName": df['FullName'],
    "Amount": df['Amount'],
})

fig, ax = plt.subplots()
df.plot(x="FullName", y="Amount", kind='barh', ax=ax)
ax.set_xticklabels(df['Amount'], rotation='horizontal')
plt.xlabel("Total Purchased Amount")
plt.ylabel("Fullname")
plt.title("The 5 customers with the biggest purchases")
ax.grid(True)
plt.show()
conn.close()
