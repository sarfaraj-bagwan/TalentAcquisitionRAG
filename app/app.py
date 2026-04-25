import streamlit as st
import pandas as pd

st.title("AI Talent Assistant")

st.sidebar.header("Candidate Pipeline")
st.sidebar.metric("Resumes", 500)
st.sidebar.metric("Top Matches", 12)

st.write("### Recommended Candidates")
data = {
    "Name": ["Laura S.", "James T.", "Priya N.", "Daniel R."],
    "Role": ["Product Manager", "Solutions Architect", "Marketing Specialist", "Data Analyst"],
    "Attrition Risk": ["Low", "Medium", "Low", "High"],
    "Skills": ["Agile, Cloud, Leadership", "DevOps, AWS, Python", "SaaS, SEO, Communication", "SQL, ML"]
}
df = pd.DataFrame(data)
st.table(df)
