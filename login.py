import streamlit as st
# import mysql.connector
import pandas as pd
# import requests
from streamlit_lottie import st_lottie
import app as ap

def login():
    """Login page for authentication."""
    st.title("Login")
    username = st.text_input("Username",key="usn")
    password = st.text_input("Password", key="pw",type="password")

    if st.button("Login"):
        # Validate the credentials
        try:
            db=ap.create_connection()
            cursor = db.cursor()
            cursor.execute("SELECT username, password FROM user_details WHERE username = %s AND password = %s", (username, password))
            result=cursor.fetchone()
            if result:
                st.success("Login successful!")
                st.session_state.loggedin=True
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")
        except (Exception) as error:
            st.error(error)

def main():
    if 'loggedin' not in st.session_state:
        st.session_state.loggedin=None

    if st.session_state.loggedin:
        return ap.main()
    else:
        login()

if __name__ == "__main__":
    main()
