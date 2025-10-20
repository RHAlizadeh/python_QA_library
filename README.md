# python-qa-library
Practice Codes

A simple Persian Question Answering (QA) desktop application using Hugging Face Transformers and Tkinter.

## Features
- Answer questions based on a preloaded text file (laptop.txt)
- Persian language support
- Simple graphical interface with Tkinter
- Press Enter or click the button to get an answer

## How to Use
1. Run the application:
- python qa_library.py
2. Type your question in the input box
3. Press Enter or click "بپرس" to get the answer
- The answer will appear in the text box below
4. Click "خروج" to exit the application

## Installation
- Clone the repository:
- git clone https://github.com/RHAlizadeh/python_QA_library
- cd python_QA_library
- Install dependencies:
- pip install -r requirements.txt
- (Note: You need transformers, torch, and Tkinter installed)

## Files
- qa_library.py — main QA library code and GUI
- laptop.txt — the text file used as the knowledge base
- model_cache/ — cached Persian QA model files (ignored if added to .gitignore)
- README.md — this file

License
MIT (or your preferred license)
