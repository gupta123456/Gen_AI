import streamlit as st

st.title("Price calculator")
original_price = st.number_input("Enter product price",min_value=0.0,value=1000.0,step=1.0)
discount_pct = st.slider("Select Discount price",min_value=0,max_value=50,value=10)

if st.button("Calculate Discount"):
    discount_amount = (discount_pct / 100) *original_price
    final_price = original_price - discount_amount

    st.success(f"The Final price after a {discount_pct}% discount is: {final_price}")

    st.write("Comparison Table")

    data = [
        ["Original Price",original_price],
        ["DIscount",f"{discount_pct}%"],
        ["Final Price",final_price]
    ]

    st.table(data)