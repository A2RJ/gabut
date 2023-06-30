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
        YEAR(poh.OrderDate) AS OrderYear,
        ROUND(SUM(poh.TotalDue), 2) AS TotalDue
    FROM purchaseorderheader poh
    GROUP BY YEAR(poh.OrderDate)
    ORDER BY YEAR(poh.OrderDate);
    """
df = pd.read_sql_query(query, conn)
df = pd.DataFrame({
    "OrderYear": df['OrderYear'],
    "TotalDue": df['TotalDue'],
})

fig, ax = plt.subplots()
df.plot(x="OrderYear", y="TotalDue", kind='bar', ax=ax)
plt.xlabel("Order Year")
plt.ylabel("Total Transaction")
ax.yaxis.set_major_formatter('{x:,.2f}')
ax.grid(True)
plt.title('Sales data')
plt.show()
conn.close()
