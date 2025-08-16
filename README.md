# Natural-Language-To-SQL-Query

# Natural Query: NL → SQL with RAG

### Overview

Natural Query enables users to interact with a SQL database using plain English.
It uses Retrieval Augmented Generation (RAG) with Google Generative AI (text-bison-001) and LangChain to:

Convert natural language queries → SQL commands

Execute queries on a database (MySQL)

Return results in natural language format

This project simplifies database interaction for non-technical users.

### Tech Stack

Python

LangChain

Google Generative AI (PaLM API / text-bison-001)

MySQL (PyMySQL for DB connection)

Streamlit (Frontend UI)

### Features

✅ Converts plain English → SQL query
✅ Executes SQL queries on MySQL database
✅ Returns results in human-readable natural language
✅ Streamlit interface for user-friendly interaction


### Workflow

<!-- 🔹 Add RAG system architecture diagram here -->
<img width="1778" height="593" alt="image" src="https://github.com/user-attachments/assets/8abcd915-3d03-4a4a-8bab-6d5621b50c7d" />


Pipeline:

User inputs query in natural language

LLM (Google Generative AI) parses intent & generates SQL

SQL executed on MySQL DB

Results formatted into natural language output

Displayed via Streamlit app


### Streamlit App
Input Screen

<img width="1320" height="616" alt="image" src="https://github.com/user-attachments/assets/d1309a20-a7ba-481d-bc73-d6590ce8a821" />


Output

<img width="1547" height="304" alt="image" src="https://github.com/user-attachments/assets/76b0fd6e-6505-492a-b6be-1517196ba10b" />


