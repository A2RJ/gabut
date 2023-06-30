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
    SELECT p.ProductID, p.Name AS ProductName, ROUND(SUM(poh.TotalDue), 2) AS TotalAmountDue
    FROM purchaseorderdetail pod
    JOIN product p ON pod.ProductID = p.ProductID
    JOIN purchaseorderheader poh ON pod.PurchaseOrderID = poh.PurchaseOrderID
    WHERE YEAR(poh.OrderDate) = 2001
    GROUP BY p.ProductID, p.Name
    ORDER BY TotalAmountDue DESC
    LIMIT 5;
"""
df_top = pd.read_sql_query(query, conn)

query = """
    SELECT p.ProductID, p.Name AS ProductName, ROUND(SUM(poh.TotalDue), 2) AS TotalAmountDue
    FROM purchaseorderdetail pod
    JOIN product p ON pod.ProductID = p.ProductID
    JOIN purchaseorderheader poh ON pod.PurchaseOrderID = poh.PurchaseOrderID
    WHERE YEAR(poh.OrderDate) = 2001
    GROUP BY p.ProductID, p.Name
    ORDER BY TotalAmountDue ASC
    LIMIT 5;
"""
df_bottom = pd.read_sql_query(query, conn)

conn.close()

df_top = pd.DataFrame({
    "ProductName": df_top['ProductName'],
    "TotalAmountDue": df_top['TotalAmountDue'],
})

df_bottom = pd.DataFrame({
    "ProductName": df_bottom['ProductName'],
    "TotalAmountDue": df_bottom['TotalAmountDue'],
})

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

ax[0].bar(df_top['ProductName'], df_top['TotalAmountDue'])
ax[0].set_ylabel("Total Amount")
ax[0].set_title("The 5 products with the largest purchases in 2001")
ax[0].grid(True)

ax[1].bar(df_bottom['ProductName'], df_bottom['TotalAmountDue'])
ax[1].set_xlabel("Product Name")
ax[1].set_ylabel("Total Amount")
ax[1].set_title("The 5 products with the smallest purchases in 2001")
ax[1].grid(True)

plt.tight_layout()
plt.show()
