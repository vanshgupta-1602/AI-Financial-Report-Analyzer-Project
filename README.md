# AI-Financial-Report-Analyzer-Project
# AI Financial Report Analyzer

A Python-based web application that extracts text and key financial figures from PDF reports using Streamlit and pypdf.

## Features

* Upload financial reports in PDF format.
* Extract readable text from PDFs.
* Display key metrics such as revenue, net profit, assets, and debt.
* View and download extracted report text.

## Technologies Used

* Python
* Streamlit
* pypdf
* Regular Expressions

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install streamlit pypdf
```

### 5. Run the application

If your main file is `dashboard.py`, run:

```bash
python -m streamlit run dashboard.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## How to Use

1. Start the application.
2. Upload a financial report in PDF format.
3. View the extracted financial figures and report text.
4. Download the extracted text if required.

## Limitations

Metric extraction depends on the PDF's text formatting. Verify extracted figures against the original report. The current version does not provide full AI-generated financial analysis.

## Future Improvements

* AI-generated financial summaries.
* Year-over-year financial comparisons.
* Financial charts and risk analysis.

## Author

Vansh Gupta
