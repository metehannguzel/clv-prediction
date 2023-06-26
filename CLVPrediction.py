import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Online Retail.xlsx")

df.head()

df.info()

# drop null values

df.dropna(subset="CustomerID", inplace=True)

# keep positive values for Quantity and UnitPrice

df = df.loc[df["Quantity"] > 0]

df = df.loc[df["UnitPrice"] > 0]

# ignore records for incomplete month

df = df.loc[df["InvoiceDate"] < "2011-12-01"]

# calculate total sales

df["Sales"] = df["Quantity"] * df["UnitPrice"]

# dataframe with orders

df_orders = df.groupby(["CustomerID", "InvoiceNo"]).agg({"Sales": sum, "InvoiceDate": max})

df_orders.head(8)
