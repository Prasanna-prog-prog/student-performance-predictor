import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="📚",
    layout="centered"
)

# --- Page Header ---
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            color: #4CAF50;
            font-weight: bold;
        }
        .sub-title {
            font-size: 18px;
            color: #555;
        }
        .result-label {
            font-size: 20px;
            margin-bottom: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">📊 Student Performance Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Evaluate a student’s academic performance based on subject scores</p>', unsafe_allow_html=True)

# --- Subject Dropdown ---
subject = st.selectbox("📘 Select Subject", ["Java", "python", "English", "BEE", "DBMS","operating Systems","Software Engineering","Matrices and Cauclus","Engineering chemistry","Computer Aided Engineering Graphics","Applied physics","Data Structures","Digital Electronics"])

# --- Input Fields ---
st.markdown("### ✏️ Enter Marks:")
col1, col2, col3 = st.columns(3)

with col1:
    midterm = st.number_input("Midterm (out of 30)", min_value=0, max_value=30, step=1)
with col2:
    assignment = st.number_input("Assignment (out of 10)", min_value=0, max_value=10, step=1)
with col3:
    final_exam = st.number_input("Final Exam (out of 60)", min_value=0, max_value=60, step=1)

# --- Prediction Logic ---
if st.button("🎯 Predict Performance"):
    total_score = midterm + assignment + final_exam

    # Grade logic
    if total_score >= 90:
        grade = "A"
    elif total_score >= 80:
        grade = "B"
    elif total_score >= 70:
        grade = "C"
    elif total_score >= 60:
        grade = "D"
    else:
        grade = "F"

    result = "Pass" if total_score >= 40 else "Fail"
    result_color = "green" if result == "Pass" else "red"

    # --- Display Results ---
    st.markdown("---")
    st.markdown(f"<p class='result-label'>📘 Subject: <strong>{subject}</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-label'>📊 Total Score: <span style='color:#007BFF; font-weight:bold;'>{total_score}/100</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-label'>🏅 Grade: <span style='color:green; font-weight:bold;'>{grade}</span></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='result-label'>📋 Result: <span style='color:{result_color}; font-weight:bold;'>{result}</span></p>", unsafe_allow_html=True)
