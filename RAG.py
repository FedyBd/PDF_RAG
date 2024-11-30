from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings


# Charger la base de données Chroma
persist_directory = "./chroma_db"  # Vérifiez que le chemin est correct
vector_db = Chroma(
    collection_name="local-rag",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text", show_progress=True),
    persist_directory=persist_directory
)

# Initialiser le modèle de chat
local_model = 'llama3.1'
llm = ChatOllama(model=local_model)

# Définir le template de prompt pour la génération de multiples questions
Query_prompt = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your role is to generate 
    five different versions of the given user question to retrieve relevant documents 
    from a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based similarity
    search. Provide these alternative questions separated by newline. 
    Original question: {question}"""
)

# Configurer le récupérateur de requêtes multiples
retriever = MultiQueryRetriever.from_llm(
    retriever=vector_db.as_retriever(),
    llm=llm,
    prompt=Query_prompt
)

# Définir le prompt principal pour la génération de réponses
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# Définir la chaîne de traitement
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Exemple de requête
query = "comment protéger les mots de passe des utilisateurs ?"

# Invocation de la chaîne pour obtenir la réponse
response = chain.invoke({"question": query})
print(response)