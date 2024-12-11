# RAG-Based Model with LangChain, Chroma DB, and LLaMA 3.1

This mini-project demonstrates how to build a Retrieval-Augmented Generation (RAG) system using LangChain, Chroma DB, and LLaMA 3.1. The model is designed to answer user questions based on the content of a previously uploaded PDF file.

## Project Overview

### Data Preparation & Database Setup:
- Prepares the data by extracting content from the uploaded PDF.
- Embeds the extracted data using a specified embedding model.
- Stores the embedded data in a persistent Chroma DB instance for efficient retrieval.

### Model Implementation & Querying:
- Implements the RAG model using LangChain and LLaMA 3.1.
- Queries the Chroma DB to retrieve relevant information for answering user questions.
- Generates responses based on the retrieved context using LLaMA 3.1.

## Project Structure

```
🗁 project-root/
├── 🗌 DB_creation.py       # Handles PDF extraction, embedding, and Chroma DB setup.
├── 🗌 RAG.py              # Implements the RAG model to answer user questions.
└── 🗌 README.md          # Project documentation (this file).
```

## End-to-End Guide
The repository includes a detailed end-to-end Jupyter notebook, which provides a comprehensive guide on:
- Setting up all project requirements.
- Implementing the user interface (UI) for the system.

Make sure to review the notebook for step-by-step instructions and additional insights into the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FedyBd/PDF-RAG.git
   cd PDF-RAG
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following are installed and properly configured:
   - **LangChain**
   - **Chroma DB**
   - **LLaMA 3.1 Model**

## Usage

### Prepare the Database:
Run the `DB_creation.py` script to upload and process the PDF file.
```bash
python DB_creation.py
```

### Query the Model:
Use the `RAG.py` script to ask questions based on the uploaded PDF.
```bash
python RAG.py
```

## Example Query

**User Question:** "How does the system ensure data security?"

**Model Response:** "Based on the provided document, data security is achieved through encryption using JSON Web Token."

---

For additional details, please refer to the included Jupyter notebook or raise an issue in the repository.

