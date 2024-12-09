# Cover Letter Generator using AI and LangChain

This project provides a powerful tool to generate personalized cover letters based on your resume, job role, company details, and optional coursework information. It uses AI models from OpenAI (GPT-4) along with LangChain for document processing and similarity search. The system leverages PDF extraction, embeddings, and retrieval-augmented generation (RAG) to craft customized cover letters tailored to the job you're applying for.

## Features

- **Resume Parsing**: Extracts and processes information from a resume (PDF format).
- **Job Description**: Takes the job role and company context to personalize the cover letter.
- **Relevant Coursework** (optional): Includes relevant coursework or projects to make the cover letter more compelling.
- **AI-Powered**: Uses OpenAI GPT-4 for generating a professional, customized cover letter.
- **Vector Search**: Utilizes embeddings and FAISS for similarity search on your resume and coursework.

## Project Structure

```plaintext
Cover-Letter-Generator/
├── app.py              # Main script to run the cover letter generator
├── requirements.txt    # List of required Python dependencies
└── README.md           # Project documentation
```

## Requirements

To run this project locally, you need to install the required dependencies.

### Prerequisites

- Python 3.7 or higher
- OpenAI API key (you need to set your own key for the OpenAI model)

### Steps to Set Up

1. **Clone the repository:**

   ```bash
   git clone https://github.com/phantom2810/cover-letter-generator.git
   cd cover-letter-generator
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required dependencies:**

   You can install the dependencies using `pip` by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key:**

   Make sure to have your OpenAI API key. Set it as an environment variable:

   ```bash
   export OPENAI_API_KEY="your-api-key-here"  # On Windows use set instead of export
   ```

5. **Run the Application:**

   Now, you can run the application with:

   ```bash
   python app.py
   ```

6. **Access the Gradio Interface:**

   Once the app is running, open the Gradio interface in your web browser. The app will be available at:

   ```plaintext
   http://127.0.0.1:7860/
   ```

7. **Generate Your Cover Letter:**

   - Upload your resume in PDF format.
   - Enter the job role you're applying for.
   - Provide the company name and a brief company description along with the job role description.
   - Optionally, upload a file containing relevant coursework or projects.
   - Click "Submit" to generate the cover letter.

## Project Dependencies

This project uses the following libraries:

- **gradio**: For creating the web interface.
- **PyMuPDF (fitz)**: For extracting text from PDFs.
- **langchain**: For document processing, embeddings, and vector search.
- **openai**: For generating text using OpenAI's GPT models (e.g., GPT-4).
- **sentence-transformers**: For creating text embeddings.
- **faiss-cpu**: For creating the FAISS index for similarity search.

You can install these dependencies by running:

```bash
pip install -r requirements.txt
```

## Troubleshooting

- **Missing API key**: Ensure that your OpenAI API key is set as an environment variable.
- **File upload issues**: The app only accepts PDF files for the resume and coursework. Ensure your files are in PDF format.
- **Error with dependencies**: If you encounter errors during the installation, try updating `pip` and reinstalling the dependencies:

  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain**: A framework for building applications with LLMs (Large Language Models).
- **OpenAI**: For providing GPT-4 models for generating human-like text.
- **FAISS**: A library for efficient similarity search and clustering of dense vectors.

---

Feel free to contribute to this project or open an issue if you encounter any problems.
