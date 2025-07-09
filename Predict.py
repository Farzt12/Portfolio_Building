import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def proses():
    st.set_page_config(page_title="Retail Transactions Dashboard", layout="wide")
    # Load dataset
    df = pd.read_csv('data/Retail_Transactions_Dataset.csv')
    # Display title
    st.title("Retail Transactions Dashboard")
    
    # Show raw data
    if st.checkbox("Show raw data"):
        st.write(df.head())
    
    # Data summary
    st.subheader("Data Summary")
    st.write(df.describe())
    
    # Top products by transaction count
    st.subheader("Top Products by Transaction Count")
    top_products = df['product_name'].value_counts().head(10)
    st.bar_chart(top_products)
    
    # Transaction trends over time
    st.subheader("Transaction Trends Over Time")
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df['month'] = df['transaction_date'].dt.to_period('M')
    monthly_trends = df.groupby('month').size()
    st.line_chart(monthly_trends)
    
    # Top customers
    st.subheader("Top Customers")
    top_customers = df['customer_id'].value_counts().head(10)
    st.write(top_customers) 
# Load data
df = pd.read_csv('data/Retail_Transactions_Dataset.csv')

# Title
st.title("Retail Transactions Dashboard")

# Show raw data
if st.checkbox("Show raw data"):
    st.write(df.head())

# Ringkasan data
st.subheader("Ringkasan Data")
st.write(df.describe())

# Produk terlaris
st.subheader("Top Produk Berdasarkan Jumlah Transaksi")
top_produk = df['product_name'].value_counts().head(10)
st.bar_chart(top_produk)

# Tren transaksi
st.subheader("Tren Transaksi per Bulan")
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['bulan'] = df['transaction_date'].dt.to_period('M')
bulanan = df.groupby('bulan').size()
st.line_chart(bulanan)

# Pelanggan terbanyak
st.subheader("Top Pelanggan")
top_customers = df['customer_id'].value_counts().head(10)
st.write(top_customers)
