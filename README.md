# 📚 Flashcards Generator (LLM-Powered)

This Streamlit app generates intelligent Q&A flashcards from any educational text. Just upload your study material and get downloadable flashcards instantly — perfect for revision or import into tools like Anki.

---
Live at: https://flashcards-generator-by-arun-kumar.streamlit.app/

## 🚀 Features

- 📄 Upload PDF or TXT files  
- 🧠 AI-generated flashcards (Q/A format)  
- 📥 Export flashcards as CSV or JSON  
- 🧪 Filter by subject, difficulty, and language  
- 🤖 Uses OpenAI's GPT-3.5 Turbo for generation  

---

## 📦 Tech Stack

- Python 3.13  
- Streamlit  
- OpenAI API  
- Pandas  
- Regex  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Arun979321/Flashcards-Generator.git
cd Flashcards-Generator
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Set up the API Key

#### Option A: Local Development
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key_here
```

#### Option B: Streamlit Cloud Deployment
Go to `Manage App > Settings > Secrets` and add:
```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

---

## 📤 Output Formats

- CSV (open with Excel, Google Sheets)  
- JSON (for integration or APIs)  

---

## 🧠 Future Improvements

- [ ] Add Hugging Face model option (no API key)  
- [ ] Support for more file formats (DOCX, EPUB)  
- [ ] Export flashcards in Anki `.apkg` format  

---

## 📸 Screenshot

> ![Screenshot 2025-06-16 221737](https://github.com/user-attachments/assets/b3bc4e9a-8a3a-4652-82e0-7884221678be)
> ![Screenshot 2025-06-16 221649](https://github.com/user-attachments/assets/81f40a86-2644-46f0-89b0-e72b2a1a8ffb)
> ![Screenshot 2025-06-16 221700](https://github.com/user-attachments/assets/f9ecaac8-42c8-4dfb-98d1-b0ae711926ed)
> ![Screenshot 2025-06-16 221710](https://github.com/user-attachments/assets/79ba1d8d-4528-44fb-8ff1-f7fa4ec2c02b)
> ![Screenshot 2025-06-16 221726](https://github.com/user-attachments/assets/3c4e2ba2-7f3c-46b2-98bd-ef5a1f4410d8)
> ![Screenshot 2025-06-16 221737](https://github.com/user-attachments/assets/773c30ec-b23a-432f-9fe1-7b5415790235)







---

## 👤 Author

**Arun979321**  
GitHub: [github.com/Arun979321](https://github.com/Arun979321)

---


