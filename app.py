import pandas as pd
import streamlit as st
import joblib

model=joblib.load("student_performance_predictor.pkl")
def score_to_grade(score):
  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'
st.title("Student Performance Predictor")

Gender=st.selectbox("Gender",["Male","Female"])
University_Type=st.selectbox("University_Type",["Private","Public"])
Department=st.selectbox("Department",["CSE","CSE(DS)","CIVIL","EEE","ECE"])
Assignment_Score=st.number_input("Assignment_Score(out of 10)",min_value=0,max_value=10)
Midterm_Score=st.number_input("Midterm_Score(out of 30)",min_value=0,max_value=30)
Final_Exam_Score=st.number_input("Final_Exam_Score(out of 60)",min_value=0,max_value=60)

input_data={
  "Gender":[Gender],
  "University_Type":[University_Type],
  "Department":[Department],
  "Assignment_score":[Assignment_Score],
  "Midterm_score":[Midterm_Score],
  "Final_exam_score":[Final_Exam_Score]
}
input_df=pd.DataFrame(input_data)

if st.button("Predict Performance"):
  try:
    prediction_label=model.predict(input_df)[0]
    total_score=Assignment_Score+Midterm_Score+Final_Exam_Score
    prediction_grade=score_to_grade(total_score)

    result ="PASS" if prediction_grade != "F" else "FAIL"
    st.success(f"Predicted Grade:{prediction_grade}")
    st.success(f"Result:{result}")
  except Exception as e:
    st.error(f"Prediction failed:{e}")
