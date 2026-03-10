import streamlit as st

st.title("Product Management")

with st.sidebar:
    st.header("Add new product")

    product_name = st.text_input("Enter product name")

    categories = ["Electronics","clothing","Home & Ktchen","Books"]
    category = st.selectbox("Category",categories)

    price = st.number_input("Price",min_value=0.0,format="%.2f")
    add_button = st.button("Add Product")

    if add_button:
        if product_name:

            st.success("Product added successfully")

            st.subheader("Product details")
            st.write(f"*Name:**{product_name}")
            st.write(f"*Category:**{category}")
            st.write(f"**Price:**{price:.2f}")
        else:
            st.error("Please enter a product name")
    st.divider()
    st.subheader("Product List (Before | After)")
    data = [
        ["Current Entry",product_name if add_button else "None",f"${price:.2f}" if add_button else "$0.00"]
    ]
    st.table(data)