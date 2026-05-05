# AI-Based Material Data Verification & Extraction System

## Overview

Engineering material properties are often stored in semi-structured technical PDFs, making manual extraction slow and error-prone.

This project implements an **AI-assisted material data extraction and verification pipeline** that automatically processes technical PDF documents and extracts structured engineering property data.

The system combines **Python-based PDF processing with Large Language Model (LLM) APIs** to identify and structure key material properties such as:

* Density
* Yield Strength
* Young's Modulus
* Thermal Properties

The goal is to **automate material data verification workflows** and reduce the time required to collect engineering data from reference documents.

---

## Problem Statement

Material property data is commonly distributed across:

* Technical datasheets
* Research papers
* Engineering reference documents

Extracting this information manually is:

* Time-consuming
* Inconsistent across formats
* Prone to human error

This system **automates material property extraction, formatting, and verification from reference PDFs.**

---

## Key Features

* Automated PDF text extraction from technical documents
* AI-powered property extraction using LLM APIs
* Conversion of **unstructured PDF text → structured property data**
* Processing of multiple material reference documents
* Standardized formatting of extracted properties
* Modular architecture for extending to additional material datasets

---

## Technologies Used

### Programming Language

* Python

### Libraries

* **PyPDF2** – PDF text extraction
* **re (Regex)** – Pattern matching and property detection
* **requests** – API communication

### APIs / AI Models

* Hugging Face Inference API
* Together AI API

### Data Format

* JSON for structured material data representation

---

## System Architecture

```
PDF Reference Files
        │
        ▼
PDF Text Extraction (PyPDF2)
        │
        ▼
Text Processing & Prompt Generation
        │
        ▼
LLM-Based Property Extraction
(Hugging Face API)
        │
        ▼
Structured JSON Property Data
        │
        ▼
Output Formatting
(Together AI API)
        │
        ▼
Readable Material Property Output
```

---

## Example Output

```
Processing PDFs and formatting extracted material properties...

Titanium ref 1.pdf → Titanium Grade 2

Extracted Properties:

Density: 4.51 g/cm3
Yield Strength: 275 MPa
Ultimate Strength: 344 MPa
Elongation: 20 %
Poisson's Ratio: 0.37
Young's Modulus: 105 GPa
Thermal Conductivity: 16.4 W/mK
Thermal Expansion Coefficient: 8.6 m/mC
```

---

## Project Structure

```
material-data-verification/
│
├── main.py
├── references/
│   ├── Titanium ref 1.pdf
│   ├── Titanium ref 2.pdf
│   └── ...
│
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Jenson1124/Data-Verification-and-DBMS-development-Internship-Project.git
cd material-data-verification
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install PyPDF2 requests
```

---

## Configuration

Create a `.env` file to store API keys securely:

```
HUGGINGFACE_API_KEY=your-huggingface-api-key
TOGETHER_API_KEY=your-together-ai-api-key
```

Update the path to the reference PDFs inside the script:

```python
PDF_FOLDER = "path/to/reference/pdfs"
```

---

## Running the Project

Run the main script:

```bash
python main.py
```

The system will process the reference PDFs and print extracted material properties.

---

## Use Cases

* Engineering material data verification
* Automated datasheet processing
* AI-assisted document analysis
* Preprocessing material datasets for databases

---

## Future Improvements

* Support for additional material properties
* Improved extraction accuracy using advanced NLP pipelines
* Integration with engineering material databases
* Development of a web or GUI interface
* Large-scale batch processing for material libraries

---

## Author

**Jenson Antony**

Data Verification and Database Development Internship Project

---

## Contributions by R Roshini Devi
- Worked on data validation and DBMS-related tasks
- Contributed to implementation and testing
