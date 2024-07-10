import streamlit as st
import os
from SQLAgent import DatabaseQueryExecutor
import pandas as pd
import time



# Set page layout
st.set_page_config(layout="wide", page_title="Natural Language to SQL")

# Title and description
st.title("NaturalQuery")


# Sidebar
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Execute Query", "About"])

# About tab content
if navigation == "About":
        st.markdown("""
    ### About
    
    This web app enables you to execute SQL queries on a MySQL Workbench database by converting natural language queries to SQL commands using Google Generative AI. Simply add your DB details of MySQL Workbench database , provide your Google API key, and write your natural language query to get started.
    
    **How it Works:**
    - The app uses Google Generative AI to convert your natural language query into an SQL command.
    - The converted SQL command is then executed on the MySQL Workbench database.
    
    **Instructions:**
    1. Enter your Google API key in the provided text box.
    2. Enter your DB details in the provided text box.
    3. Write your natural language query in the text area.
    4. Click the "Execute Query" button to see the results.
    
    **Disclaimer:**
    - Not all converted SQL commands may be accurate or suitable for execution.
    - Always review and verify the converted SQL command before executing it on your database.
    
    For any queries or feedback, please contact 030esharpreetsingh@gmail.com.
    """)
else:

    # Sidebar settings
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter your Google API Key:", "", type="password")
    
    # Query execution tab content
    st.sidebar.title("DB MYSQL Workbench")
    db_user = st.sidebar.text_input("DB Username")
    db_password = st.sidebar.text_input("DB Password", "", type="password")
    db_host = st.sidebar.text_input("DB Host", value="localhost")
    db_port = st.sidebar.text_input("DB Port", value="3306")
    db_name = st.sidebar.text_input("DB Name")

    submit = st.sidebar.button(label="Submit", type="secondary")
    
    

    if submit:
        # Database and API key validation
        if api_key and db_user and db_password and db_host and db_port and db_name:

            # Initialize DatabaseQueryExecutor with API key and database URI
            db_uri = f"mysql+pymysql://mysql:{db_user}{db_password}@{db_host}:{db_port}/{db_name}"
          
            with st.spinner('Building connection...'):
                executor = DatabaseQueryExecutor()
                executor.func_db(db_uri)
                executor.func_llm(api_key=api_key)
                time.sleep(1)

                if executor.llm == "error":
                    st.sidebar.error("Failed to initialize LLM. Check API key.")
                elif executor.db == "error":
                    st.sidebar.error("Failed to connect to the database. Check details.")
                else:
                    st.sidebar.success("Connected to Database successfully.")
                    st.session_state.executor = executor


# Query Execution
if 'executor' in st.session_state:
    st.header("Query Execution")
    query = st.text_input("Enter your query")
    if st.button("Submit Query"):
        with st.spinner("Executing query..."):
            response = st.session_state.executor.invoke_chain(query)
            # st.write("Generated SQL Query:")
            # st.code(response["query"], language="sql")
            
        
            container = st.container(border=True)
            container.write(response)
    
            # st.write("Query Result:")
            # st.write(response["query"])
