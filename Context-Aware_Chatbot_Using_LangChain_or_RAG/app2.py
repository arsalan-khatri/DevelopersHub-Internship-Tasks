import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. STREAMLIT CONFIG
st.set_page_config(page_title="Custom URL RAG Chatbot", page_icon="🔗")
st.title("🔗 Custom Website RAG Chatbot")

# 2. SIDEBAR - CONFIGURATION & URL INPUT
st.sidebar.title("🔑 Configuration")
api_key = st.sidebar.text_input("Enter your Google API Key", type="password")

if not api_key:
    st.warning("Please enter your Google API Key in the sidebar to start.")
    st.stop()

# Set Environment Variable
os.environ["GOOGLE_API_KEY"] = api_key

st.sidebar.divider()
st.sidebar.header("🌐 Knowledge Source")
target_url = st.sidebar.text_input("Enter Website URL:", placeholder="https://example.com")

if not target_url:
    st.info("👈 Please enter a URL in the sidebar to load the knowledge base.")
    st.stop()

# URL change hone par chat history clear karne ka logic
if "current_url" not in st.session_state:
    st.session_state.current_url = target_url
elif st.session_state.current_url != target_url:
    st.session_state.messages = []  # Clear history for new URL
    st.session_state.current_url = target_url

# 3. KNOWLEDGE BASE LOADING
# sat.cache_resource will track the argument (URL),
# As soon as the URL changes, it will fetch the new data.
@st.cache_resource(show_spinner=False) 
def load_and_process_data(url):
    with st.spinner(f"Fetching data from {url}..."):
        # Load Data
        loader = WebBaseLoader(url)
        data = loader.load()
        
        # Split Data
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(data)
        
        # Create Embeddings & Vector Store
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(chunks, embeddings)
        
        return vector_store

# Loading data
try:
    vector_db = load_and_process_data(target_url)
    st.sidebar.success("✅ AI Memory Ready for this URL!")
except Exception as e:
    st.error(f"Error loading data from the URL: {e}")
    st.stop()

# 4. CHAT INTERFACE
st.divider()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask something about the provided URL..."):
    # User message dikhana
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Getting a response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # 1. Similarity Search (Retriever)
                relevant_docs = vector_db.similarity_search(prompt, k=3)
                context = "\n\n".join([doc.page_content for doc in relevant_docs])

                # 2. LLM Chain
                llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
                
                template = """Answer the question based ONLY on the following context:
                {context}
                
                Question: {question}
                """
                
                qa_prompt = ChatPromptTemplate.from_template(template)
                chain = qa_prompt | llm | StrOutputParser()
                
                response = chain.invoke({"context": context, "question": prompt})
                
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Error generating response: {e}")