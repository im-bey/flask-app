# app.py
from flask import Flask, render_template, request, jsonify
from main import generate_cover_letter  # Import the function from main.py
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF  # PDF generation library
from docx import Document  # DOCX generation library

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask Application for Cover Letter Generator!"

@app.route('/api/letter', methods=['GET'])
def generate():
    try:
        # Retrieve JSON data sent in the request
        data = request.json
        job_title = data.get('job_title')
        job_specifications = data.get('job_specifications')
        candidate_name = data.get('candidate_name')
        candidate_qualifications = data.get('candidate_qualifications')

        # Check if all required fields are present
        if not all([job_title, job_specifications, candidate_name, candidate_qualifications]):
            return jsonify({'error': 'All fields are required!'}), 400

        # Generate the cover letter using the imported function
        cover_letter = generate_cover_letter(
            job_title, job_specifications, candidate_name, candidate_qualifications
        )
        
        # Render the template and pass the generated cover letter to be displayed
        return render_template('index.html', cover_letter=cover_letter)
        # Return the generated cover letter as JSON response
        return jsonify({'cover_letter': cover_letter})
    

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)

# app.py
from flask import Flask, render_template, request, jsonify
from main import generate_cover_letter  # Import the function from main.py
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF  # PDF generation library
from docx import Document  # DOCX generation library

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask Application for Cover Letter Generator!"

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Retrieve JSON data sent in the request
        data = request.json
        job_title = data.get('job_title')
        job_specifications = data.get('job_specifications')
        candidate_name = data.get('candidate_name')
        candidate_qualifications = data.get('candidate_qualifications')

        # Check if all required fields are present
        if not all([job_title, job_specifications, candidate_name, candidate_qualifications]):
            return jsonify({'error': 'All fields are required!'}), 400

        # Generate the cover letter using the imported function
        cover_letter = generate_cover_letter(
            job_title, job_specifications, candidate_name, candidate_qualifications
        )
        
        # Render the template and pass the generated cover letter to be displayed
        return render_template('index.html', cover_letter=cover_letter)
        # Return the generated cover letter as JSON response
        return jsonify({'cover_letter': cover_letter})
    

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
