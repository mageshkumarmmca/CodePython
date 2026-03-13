import pdfplumber
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

OPENAI_API_KEY = "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"

st.header("Medi Group Insurance Policy")

with st.sidebar:
    st.title("Medi Group Insurance Policy")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

# Extract contents from the PDF and chunk it
if file is not None:
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    #st.write(text)

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY
    )

    vector_store = FAISS.from_texts(chunks, embeddings)

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    user_question = st.text_input("Type your question here")

    retriever = vector_store.as_retriever(
        search_type="mar",
        serarch_knargs={"k": 4}
    )
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        max_tonkens=1000,
        openai_api_key=OPENAI_API_KEY
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "you are a helpful assistant answering questions about a PDF document.\n\n"
         , "Guidelines:\n"
         , "1. Provide complete, well-explained answers using the context below.\n"),
        ("human", "{question}")
    ])

    chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )

    if user_question:
        response = chain.invoke(user_question)
        st.write(response)
