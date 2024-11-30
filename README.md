# RAG-Based Model with LangChain, Chroma DB, and LLaMA 3.1
This mini-project demonstrates how to build a Retrieval-Augmented Generation (RAG) system using LangChain, Chroma DB, and LLaMA 3.1. The model is designed to answer user questions based on the content of a previously uploaded PDF file.

## Project Overview
### Data Preparation & Database Setup:

Prepares the data by extracting content from the uploaded PDF.  
Embeds the extracted data using a specified embedding model.  
Stores the embedded data in a persistent Chroma DB instance for efficient retrieval.  
### Model Implementation & Querying:

Implements the RAG model using LangChain and LLaMA 3.1.  
Queries the Chroma DB to retrieve relevant information for answering user questions.    
Generates responses based on the retrieved context using LLaMA 3.1.  
### Project Structure  
📁 project-root/  
├── 📄 DB_creation.py     # Handles PDF extraction, embedding, and Chroma DB setup.  
├── 📄 RAG.py       # Implements the RAG model to answer user questions.  
└── 📄 README.md               # Project documentation (this file).  
## Installation
Clone the repository: 
git clone https://github.com/FedyBd/PDF-RAG.git  
cd PDF_RAG   
### Install the required dependencies:  

pip install -r requirements.txt  
Ensure the following are installed and properly configured:  

LangChain  
Chroma DB  
LLaMA 3.1 Model  
### Usage  
Prepare the Database: Run the data_preparation.py script to upload and process the PDF file.  
python DB_creation.py  
Query the Model: Use the model_querying.py script to ask questions based on the uploaded PDF.  
python model_querying.py  
#### Example Query
User Question: "How does the system ensure data security?"   
Model Response: "Based on the provided document, data security is achieved through encryption using JSON Web Token"   
