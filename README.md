# 🧠 TIA Backend

> AI-powered backend for the Thyroid Intelligent Assistant (TIA)

The TIA Backend is the core engine behind the Thyroid Intelligent Assistant. It processes thyroid lab reports, extracts medical data using OCR and AI, performs thyroid health analysis, detects trends and risk factors, and exposes APIs consumed by the frontend application.

---

## ✨ Features

- 📄 OCR & AI-powered thyroid report extraction
- 🤖 LLM-assisted structured data parsing
- 🩺 Thyroid health analysis
- 📈 Historical trend analysis
- ⚠️ Risk score calculation
- 🚩 Red flag detection
- 💡 Personalized recommendations
- 🔗 FastAPI REST APIs
- 🗂 Modular architecture
- ☁️ Supabase integration

---

## 🔄 Processing Pipeline

TIA processes thyroid laboratory reports through a multi-stage pipeline that combines document extraction, OCR, AI-assisted parsing, validation, and health analysis.

```text
                    ┌──────────────────────┐
                    │  Thyroid Lab Report  │
                    │     PDF / Image      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     File Upload      │
                    │       FastAPI        │
                    └──────────┬───────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │      Document Extraction       │
              │                                │
              │     PDF → pdfplumber / fitz    │
              │       Image → PaddleOCR        │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │      AI-Assisted Parsing       │
              │                                │
              │        Google Gemini           │
              │                                │
              │   Extract thyroid biomarkers   │
              │ and relevant report information│
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │      Data Validation           │
              │                                │
              │  • Validate extracted values   │
              │  • Normalize data              │
              │  • Validate expected structure │
              │  • Handle extraction errors    │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │        Health Analysis         │
              │                                │
              │ • Thyroid value interpretation │
              │ • Risk indicators              │
              │ • Red flag detection           │
              │ • Trend analysis               │
              │ • Personalized insights        │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │       Structured Response      │
              │                                │
              │        Pydantic Schemas        │
              │                                │
              │  Structured health information │
              │  + analysis + insights         │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌──────────────────────┐
                    │       Supabase       │
                    │                      │
                    │ Reports • Results    │
                    │ Health Data • History│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     TIA Frontend     │
                    │                      │
                    │ Patient-friendly     │
                    │ health insights      │
                    └──────────────────────┘


```

---

## 🏗️ Architecture

TIA follows a modular backend architecture that separates API handling, report processing, AI processing, health analysis, validation, and data management.

```text
                         ┌─────────────────────────┐
                         │       TIA Frontend      │
                         │    React + TypeScript   │
                         └────────────┬────────────┘
                                      │
                                      │ REST API
                                      ▼
                         ┌─────────────────────────┐
                         │        FastAPI          │
                         │        API Layer        │
                         └────────────┬────────────┘
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
    ┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
    │ Report Processing│     │  AI Processing   │     │  Health Analysis │
    │                  │     │                  │     │                  │
    │ • OCR            │     │ • Gemini LLM     │     │ • Risk Analysis  │
    │ • PDF Extraction │     │ • Data Parsing   │     │ • Red Flags      │
    │ • File Handling  │     │ • Structuring    │     │ • Trend Analysis │
    └────────┬─────────┘     └────────┬─────────┘     │ • Recommendations│
             │                        │               └────────┬─────────┘
             │                        │                        │
             └────────────────────────┼────────────────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │   Validation & Schemas  │
                         │                         │
                         │        Pydantic         │
                         │                         │
                         │ • Data Validation       │
                         │ • Type Validation       │
                         │ • Response Schemas      │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │        Supabase         │
                         │        Database         │
                         │                         │
                         │ • Reports               │
                         │ • Health Data           │
                         │ • Historical Data       │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       TIA Frontend      │
                         │                         │
                         │ Patient-friendly health │
                         │insights & visualizations│
                         └─────────────────────────┘
```

## 🔗 API Overview

The backend exposes REST APIs for:

| Area | Purpose |
|---|---|
| Report Processing | Upload and process thyroid laboratory reports |
| Data Extraction | Return structured thyroid biomarkers |
| Clinical Analysis | Generate health and risk insights |
| Trend Analysis | Analyze historical thyroid measurements |
| Recommendations | Generate personalized health guidance |
| Health Tracking | Manage relevant patient health information |

--- 

## 🏗 Project Structure

```text
tia-backend/
│
├── ai/
├── analysis/
├── api/
├── config/
├── constants/
├── database/
├── docs/
├── exceptions/
├── pipeline/
├── schemas/
├── scripts/
├── services/
├── tests/
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

- Python
- FastAPI
- Google Gemini API
- PaddleOCR
- pdfplumber
- Supabase
- Pydantic
- Uvicorn

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/aamina-codes/tia-backend.git
cd tia-backend
```

### Create virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file.

Example:

```env
GEMINI_API_KEY=your_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

API will be available at

```
http://127.0.0.1:8000
```

Interactive documentation

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📌 Current Capabilities

- Upload thyroid reports
- Extract lab values
- Analyze thyroid-related laboratory values
- Generate risk indicators based on available health data
- Generate recommendations
- Detect abnormal trends
- Return structured API responses

---

## 🔮 Future Improvements

- More robust authentication and authorization
- Dedicated doctor-facing APIs
- Expanded patient profile management
- Advanced longitudinal report comparison
- Multi-language support
- Improved clinical rule validation
- Fine-tuned domain-specific AI models
- Expanded automated testing and monitoring

---

## ⚠️ Medical Disclaimer

TIA is an educational and decision-support project intended to help users understand thyroid-related health information.

AI-generated outputs should not be treated as medical diagnoses or as a substitute for professional medical advice, diagnosis, or treatment.

Clinical decisions should always be made in consultation with a qualified healthcare professional.

---

## Related Repository

🎨 **TIA Frontend:**  
https://github.com/aamina-codes/tia-frontend

---

## 👩‍💻 Author

**Aamina Shaik**

Data Science Graduate • AI Engineer • Product Builder

---

## 📄 License

This project is licensed under the MIT License.
