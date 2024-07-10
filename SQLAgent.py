from langchain_google_genai import GoogleGenerativeAI
# from secret_key import *
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from operator import itemgetter
import streamlit as st
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableMap, RunnableLambda
from langchain.memory import ChatMessageHistory
import os


class DatabaseQueryExecutor:
    def __init__(self):
        self.llm = None
        self.db = None

    def func_llm(self,api_key):
        try:
            self.llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.2)
            
        except:
            self.llm = "error"

    def func_db(self,db_uri):
        try:
            self.db = SQLDatabase.from_uri(db_uri)
            
        except :
            self.db = "error"


    def get_schema(self,_):
        return {"table_info": self.db.table_info}
    
    
    def get_chain(self):

        answer_prompt = ChatPromptTemplate.from_template(
        """
            Based on the table schema below,question,sql query, and sql response, write a 
            natural language response in a proper format:
            {table_info}
    
         Question: {question}
         SQL Query: {query}
         SQL Result: {result}
         Answer: """
        )
        get_schema_runnable = RunnableLambda(self.get_schema)
        db = self.db

        execute_query = QuerySQLDataBaseTool(db=db)

        write_query = create_sql_query_chain(self.llm, self.db)

        rephrase_ans = answer_prompt | self.llm | StrOutputParser()
        chain = (
            RunnablePassthrough.assign(table_info= get_schema_runnable).assign(query=write_query ).assign(
                result=itemgetter("query") | execute_query)
            | rephrase_ans
        )    
        
        return chain 
    

    
    def invoke_chain(self, question):
        chain = self.get_chain()
        response = chain.invoke({"question": question})
        return response
    
    
    


