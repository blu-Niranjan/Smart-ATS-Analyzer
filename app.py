import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get the response from the Gemini model
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)

    # Basic check for content
    if not response.candidates or not response.candidates[0].content.parts:
        return "⚠ No response from Gemini. The prompt might be blocked or empty."
    return response.text
# Function to extract text from an uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or "" # Add a fallback for empty pages
    return text

# The prompt template for the Gemini model
input_prompt = """
Hey, act like a highly skilled and experienced ATS (Applicant Tracking System) with deep expertise in software engineering, data science, data analysis, and big data engineering. Your job is to evaluate the given resume against the provided job description in the context of a highly competitive job market. You must provide the most accurate analysis possible, including: 
1) JD Match percentage based on skills, experience, and keywords.
2) Missing keywords that are critical for ATS ranking.
3) A concise profile summary with suggestions for improvement.

Return the response strictly as one single JSON-formatted string with no extra text, using this exact structure:
{{"JD Match": "Value%", "MissingKeywords": ["Keyword1", "Keyword2"], "Profile Summary": "Your summary here."}}

Resume: {text}
Description: {jd}
"""

# Set up the page configuration
st.set_page_config(page_title="Smart ATS", page_icon="📄", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .keyword-pill {
        display: inline-block;
        background-color: #E8F5E9; /* A light green background */
        color: #388E3C; /* A dark green text color */
        padding: 5px 12px;
        margin: 5px;
        border-radius: 16px;
        font-weight: 500;
        border: 1px solid #C8E6C9;
    }
</style>
""", unsafe_allow_html=True)


# Header 
st.title("🚀 Smart ATS Resume Analyzer")
st.write("Optimize your resume to get past automated screeners and land your dream job!")
st.markdown("---")


# Input Fields
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Job Description")
    jd = st.text_area("Paste the complete job description here.", height=300)

with col2:
    st.header("📄 Your Resume")
    uploaded_file = st.file_uploader("Upload your resume in PDF format.", type="pdf")


# --- Submit Button ---
submit = st.button("Analyze My Resume")

# --- Processing and Output ---
if submit:
    if uploaded_file is not None and jd.strip() != "":
        with st.spinner("Analyzing... Our AI is hard at work! 🧠"):
            try:
                # Extract text and generate the response
                resume_text = input_pdf_text(uploaded_file)
                final_prompt = input_prompt.format(text=resume_text, jd=jd)
                response_text = get_gemini_response(final_prompt)

                # Safely parse the JSON response
                try:
                    # The response might be in a Markdown code block, so we clean it
                    if "```json" in response_text:
                        response_text = response_text.split("```json")[1].split("```")[0]
                    
                    response_data = json.loads(response_text)
                    
                    st.markdown("---")
                    st.success("Analysis Complete!")

                    # --- Display Results ---
                    
                    # Column layout for results
                    res_col1, res_col2 = st.columns(2)

                    with res_col1:
                        # 1. JD Match Percentage
                        st.subheader("🎯 Job Description Match")
                        match_percentage = int(response_data["JD Match"].replace('%', ''))
                        st.progress(match_percentage)
                        st.markdown(f"<h2 style='text-align: center;'>{response_data['JD Match']}</h2>", unsafe_allow_html=True)

                    with res_col2:
                         # 2. Missing Keywords
                        st.subheader("🔑 Missing Keywords")
                        keywords = response_data.get("MissingKeywords", [])
                        if keywords:
                            # Display keywords as pills
                            pills_html = "".join([f"<span class='keyword-pill'>{kw}</span>" for kw in keywords])
                            st.markdown(pills_html, unsafe_allow_html=True)
                        else:
                            st.info("Great job! No critical keywords seem to be missing.")

                    # 3. Profile Summary
                    st.subheader("📝 Profile Summary & Improvements")
                    st.markdown(response_data["Profile Summary"])

                except (json.JSONDecodeError, KeyError) as e:
                    st.error("Error parsing the response. The AI might have returned an unexpected format.")
                    st.write("Raw AI Response:")
                    st.code(response_text)

            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

    else:
        st.warning("Please upload your resume and paste the job description before submitting.")