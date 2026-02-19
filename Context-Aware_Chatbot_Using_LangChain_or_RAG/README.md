# Custom Website RAG Chatbot (Context-Aware)

A powerful, context-aware conversational chatbot built using LangChain and Retrieval-Augmented Generation (RAG). This application allows users to input any website URL, vectorizes its content, and enables an interactive chat interface to retrieve accurate information directly from the provided source.

## Objective
To build a conversational chatbot that can remember context and retrieve external information during conversations dynamically from any given website URL.

## Key Features
* **Dynamic Knowledge Base:** Input any valid URL (e.g., Wikipedia, custom blogs, internal docs) to instantly create a custom corpus.
* **Retrieval-Augmented Generation (RAG):** Combines the reasoning capabilities of Google's Gemini 2.5 Flash with real-time data retrieval.
* **Context Memory:** Utilizes Streamlit's session state to maintain conversational history for a seamless chat experience.
* **Local Embeddings:** Uses HuggingFace's `all-MiniLM-L6-v2` for fast, cost-free, and API-independent text vectorization.
* **Vector Search:** Powered by FAISS (Facebook AI Similarity Search) for blazing-fast similarity matching.
* **Clean UI:** Fully deployed with a user-friendly Streamlit interface.

## Tech Stack
* **Frontend/Deployment:** Streamlit
* **Framework:** LangChain (`langchain-community`, `langchain-core`)
* **LLM:** Google Gemini (`gemini-2.5-flash` via `langchain-google-genai`)
* **Embeddings:** HuggingFace Sentence Transformers
* **Vector Store:** FAISS
* **Web Scraping:** BeautifulSoup4

## How It Works
1.  **Document Loading:** The app uses `WebBaseLoader` to scrape text from the user-provided URL.
2.  **Text Splitting:** The content is broken down into smaller, manageable chunks (1000 characters) with overlap to maintain context.
3.  **Vectorization & Storage:** Chunks are converted into vector embeddings using a HuggingFace model and stored locally in a FAISS vector database.
4.  **Retrieval & Generation:** When a user asks a question, the system searches FAISS for the top 3 most relevant chunks. These chunks are injected into the LLM prompt as context to generate an accurate, hallucination-free response.

## Installation & Setup

**1. Clone the repository:**
**Step 1**
```bash
pip install gitdir
```
**Step 2**
```bash
gitdir clone https://github.com/arsalan-khatri/DevelopersHub-Internship-Tasks/tree/main/Context-Aware_Chatbot_Using_LangChain_or_RAG
