import streamlit as st

def main():
    st.title("Welcome to Streamlit!")

user_name = st.text_input("Enter your name:")
if st.button("Greet me"):
    st.write(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()