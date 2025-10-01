# Smart ATS Resume Analyzer 🚀

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-FF4B4B?style=for-the-badge&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_API-4285F4?style=for-the-badge&logo=google)

An intelligent Applicant Tracking System (ATS) that helps you tailor your resume to a specific job description. This tool leverages the power of Google's Gemini Pro model to provide a detailed analysis, including a match percentage, missing keywords, and actionable feedback for improvement.

### [➡️ View the Live App Here!](https://smart-ats-analyzer-yaqhsg6g8ahbj27py4bavg.streamlit.app/)

---

## 📸 App Demo


<img width="1905" height="885" alt="Screenshot 2025-10-01 124953" src="https://github.com/user-attachments/assets/81dcaf9e-e742-42ba-9604-021788a2251d" />
<img width="1909" height="686" alt="Screenshot 2025-10-01 125016" src="https://github.com/user-attachments/assets/12def785-94cd-4862-8977-3d7de4d91a82" />


---

## ✨ Key Features

* **🎯 JD Match Percentage:** Get an instant percentage score on how well your resume aligns with the job description.
* **🔑 Missing Keywords Analysis:** Uncover crucial keywords and skills that are missing from your resume but are vital for the role.
* **📝 Profile Summary & Improvement:** Receive an AI-generated summary of your profile and concrete suggestions on what to improve to better fit the job requirements.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **LLM:** [Google Gemini Pro](https://ai.google.dev/)
* **Programming Language:** Python
* **PDF Processing:** PyPDF2

---

## 💻 How to Run This Project Locally

Follow these steps to set up and run the project on your own machine.

### **1. Clone the Repository**

```bash
git clone [https://github.com/blu-Niranjan/smart-ats-app.git](https://github.com/blu-Niranjan/smart-ats-app.git)
cd smart-ats-app
```
### **2. Create a Virtual Environment**

```bash
It's recommended to use a virtual environment to keep dependencies isolated.
On macOS/Linux:
Bash
python3 -m venv venv
source venv/bin/activate
On Windows:
Bash
python -m venv venv
.\venv\Scripts\activate
```
### **3. Install Dependencies**

```bash
Install all the required libraries from the requirements.txt file.
Bash
pip install -r requirements.txt
```
### **4. Set Up Environment Variables**

```bash
Create a file named .env in the root of the project folder and add your Google API Key.
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY_HERE"
```
### **5. Run the Streamlit App**

```bash
Launch the application using the Streamlit CLI.
Bash
streamlit run app.py
```
The application should now be running on your local machine, typically at http://localhost:8501.
