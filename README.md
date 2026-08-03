## Related Repository

🎨 Frontend

https://github.com/aamina-codes/tia-frontend


# 🧠 TIA Backend

> AI-powered backend for the Thyroid Intelligent Assistant (TIA)

The TIA Backend is the core engine behind the Thyroid Intelligent Assistant. It processes thyroid lab reports, extracts medical data using OCR and AI, performs clinical analysis, detects trends and risk factors, and exposes APIs consumed by the frontend application.

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

## 🏗 Project Structure

```text
TIA/
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
- Analyze thyroid function
- Calculate health risks
- Generate recommendations
- Detect abnormal trends
- Return structured API responses

---

## 🔮 Future Improvements

- Authentication
- Doctor Portal
- Patient Dashboard APIs
- Multi-language support
- Fine-tuned medical AI model
- Report comparison across years

---

## 👩‍💻 Author

**Aamina Shaik**

Data Science Graduate • AI Engineer • Product Builder

---

## 📄 License

This project is licensed under the MIT License.
