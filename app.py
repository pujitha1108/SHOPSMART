import streamlit as st
import requests
import pandas as pd

st.title("Data from Flask API")

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# UOM Data
uom_data = fetch_data("http://127.0.0.1:5000/getUOM") # Replace with your URL
if uom_data:
    st.subheader("Units of Measure (UOM)")
    if isinstance(uom_data, list):  # Check if it's a list of dictionaries
        df_uom = pd.DataFrame(uom_data)
        st.dataframe(df_uom)
    else:
        st.write("UOM data is not in the expected format.")

# Product Data
product_data = fetch_data("http://127.0.0.1:5000/getProducts") # Replace with your URL
if product_data:
    st.subheader("Products")
    if isinstance(product_data, list): # Check if it's a list of dictionaries
        df_products = pd.DataFrame(product_data)
        st.dataframe(df_products)
    else:
        st.write("Product data is not in the expected format.")