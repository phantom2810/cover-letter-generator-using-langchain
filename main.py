import gradio as gr
import os
import fitz  # PyMuPDF
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"]  # Ensure OPENAI_API_KEY is set in your environment

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text("text")
    return text

# Function to split text into chunks
def split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200):
    """Split the extracted text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create vector store
def create_vector_store(chunks):
    """Create a vector store for similarity search."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_texts(chunks, embeddings)
    return vector_store

# Function to perform retrieval-augmented generation (RAG)
def perform_rag(vector_store, query):
    """Retrieve relevant documents from the vector store."""
    retriever = vector_store.as_retriever()
    docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in docs])
    return context

# Create the Gradio interface function
def generate_cover_letter(pdf_path, job_role, company_name, company_context, course_file):
    # Extract text from resume (PDF)
    resume_text = extract_text_from_pdf(pdf_path.name)  # `.name` gives the file path
    # Split text into chunks for resume
    resume_chunks = split_text_into_chunks(resume_text)
    # Create vector store for resume
    resume_vector_store = create_vector_store(resume_chunks)
    # Perform RAG to get candidate profile
    candidate_profile = perform_rag(resume_vector_store, job_role)

    # Extract text from course information file (PDF or text) if available
    course_text = ""
    if course_file:
        course_text = extract_text_from_pdf(course_file.name)  # Assuming it's a PDF
        # Split text into chunks for course info
        course_chunks = split_text_into_chunks(course_text)
        # Create vector store for course info
        course_vector_store = create_vector_store(course_chunks)
        # Perform RAG to get relevant course context
        course_context = perform_rag(course_vector_store, job_role)
    else:
        course_context = ""

    # Load the OpenAI chat model
    chat = ChatOpenAI(
        temperature=0.5,
        model="gpt-4",  # Use gpt-4 or gpt-3.5-turbo as required
    )

    # Create messages using LangChain's message schema
    messages = [
        SystemMessage(content="You are a seasoned career coach, helping to craft personalized, professional cover letters that highlight the candidate’s strengths and experience."),
        HumanMessage(content=f"""
        I am applying for the {job_role} position at {company_name}.
        ==================
        Company Overview:
        {company_context}
        ==================
        Candidate Profile:
        {candidate_profile}
        ==================
        Relevant Coursework (if any):
        {course_context if course_context else "None"}
        ==================
        From the above information, please write a compelling, customized cover letter. Ensure the tone is professional and matches the job description, company values, and my skills and experiences.
        """)
    ]

    # Generate the response
    response = chat(messages)
    return response.content

# Create Gradio interface
gr.Interface(
    fn=generate_cover_letter,
    inputs=[
        gr.File(label="Upload Your Resume (PDF)", file_types=[".pdf"]),
        gr.Textbox(label="Job Role", placeholder="E.g., Data Scientist, Fullstack Developer, etc."),
        gr.Textbox(label="Company Name", placeholder="Enter the name of the company you are applying to"),
        gr.Textbox(label="Company Context & Job Description", placeholder="Provide a brief description of the company and the job role description"),
        gr.File(label="Upload Relevant Coursework (PDF)", file_types=[".pdf"]),  
    ],
    outputs=gr.Textbox(label="Generated Cover Letter", show_copy_button=True),
    title="Cover Letter Generator",
    description="Generate a personalized cover letter using your resume, the job description, company details, and relevant coursework or projects."
).launch()
