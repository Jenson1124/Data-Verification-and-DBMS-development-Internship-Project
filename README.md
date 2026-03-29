AI-Based Material Data Verification and Extraction System
Overview

This project implements an AI-assisted pipeline for extracting engineering material properties from technical PDF reference documents.

Engineering datasets are often stored in semi-structured or unstructured PDFs, making manual extraction slow and error-prone. This system automates the process by combining Python-based text extraction with Large Language Model (LLM) APIs to identify and structure key material properties.

The project demonstrates how AI and NLP techniques can assist in material data verification workflows, reducing manual effort and enabling structured data generation for engineering analysis.

Problem Statement

Material property data (such as Yield Strength, Density, Young’s Modulus, etc.) is typically stored in technical datasheets and research PDFs. Extracting this data manually is:

Time-consuming
Prone to human error
Difficult to standardize across different document formats

This project automates the extraction, validation, and formatting of material properties from reference PDFs.

Features
Automated PDF text extraction from technical reference documents
AI-powered material property identification using LLM APIs
Conversion of unstructured text → structured property data
Modular pipeline for processing multiple material reference PDFs
Standardized formatting of extracted results
Error handling and logging for missing or inconsistent data
Technologies Used
Programming Language
Python
Libraries
PyPDF2 – PDF text extraction
re (Regular Expressions) – pattern matching and property detection
requests – API communication
APIs / AI Models
Hugging Face Inference API
Together AI API
Data Format
JSON for structured data representation
Project Architecture
PDF Reference Files
        │
        ▼
PDF Text Extraction (PyPDF2)
        │
        ▼
Text Processing & Prompt Creation
        │
        ▼
LLM-Based Property Extraction
(Hugging Face API)
        │
        ▼
Structured Property Data (JSON)
        │
        ▼
Output Formatting
(Together AI API)
        │
        ▼
Readable Material Property Report
Example Output
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
Installation

Clone the repository:

git clone https://github.com/Jenson1124/Data-Verification-and-DBMS-development-Internship-Project.git
cd material-data-verification

Install dependencies:

pip install PyPDF2 requests
Configuration

Update the API keys in the script:

HUGGINGFACE_API_KEY = "your-huggingface-api-key"
TOGETHER_API_KEY = "your-together-ai-api-key"

Set the path to your reference PDFs:

PDF_FOLDER = "path/to/reference/pdfs"
Running the Project

Run the script:

python main.py

The system will process the PDFs and print extracted material properties.

Use Cases
Engineering material data verification
Automated datasheet analysis
AI-assisted technical document processing
Preprocessing data for material databases
Future Improvements
Support for additional material properties
Improved accuracy with fine-tuned LLM prompts
Integration with structured material databases
Web or GUI interface for easier interaction
Batch processing of large material datasets
Author

Jenson Antony
Data Verification and Database Development Internship Project
