
# Text Summarization with BART

This project demonstrates an **abstractive text summarization** system using the **BART** (Bidirectional and Auto-Regressive Transformers) model. The model has been fine-tuned to generate concise and coherent summaries from long text inputs.

## Project Overview

The goal of this project is to create an API that can summarize any given text. The BART model has been fine-tuned on a text summarization dataset, and the model is deployed as a web API using Flask.

### Key Features:
- **Abstractive Summarization:** The BART model is used to generate summaries that are more human-like and coherent, rather than just extracting key phrases.
- **User Interface:** A web interface is provided where users can paste text and get the summary instantly.

## Setup Instructions

### Prerequisites
- Python 3.6+
- Git (to clone the repository)

### Clone the Repository

```bash
git clone https://github.com/arbhavana/Text_suumarization_BART.git
cd Text_suumarization_BART
python main.py
'''
#The API will be accessible at http://localhost:5000
