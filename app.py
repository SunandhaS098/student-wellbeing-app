import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Well-Being App", layout="centered")

st.title("Student Well-Being & Productivity Explorer")

st.write("""
This web app explores student mental health data to understand
how depression, anxiety, panic attacks, and academic performance
are related.
""")

# Load dataset
df = pd.read_csv("Student_Mental_health.csv")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---------------------------
# Depression Chart
# ---------------------------
st.subheader("Depression Status Among Students")

depression_counts = df["Do you have Depression?"].value_counts()

fig1, ax1 = plt.subplots()
depression_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Depression")
ax1.set_ylabel("Number of Students")

st.pyplot(fig1)

st.write("""
**Insight:**  
A significant portion of students report experiencing depression,
highlighting the importance of mental health awareness.
""")

# ---------------------------
# Anxiety Chart
# ---------------------------
st.subheader("Anxiety Status Among Students")

anxiety_counts = df["Do you have Anxiety?"].value_counts()

fig2, ax2 = plt.subplots()
anxiety_counts.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Anxiety")
ax2.set_ylabel("Number of Students")

st.pyplot(fig2)

st.write("""
**Insight:**  
Anxiety is commonly reported among students, indicating it as a
major mental health concern.
""")

# ---------------------------
# CGPA vs Depression
# ---------------------------
st.subheader("CGPA Distribution Among Students with Depression")

depressed_students = df[df["Do you have Depression?"] == "Yes"]
cgpa_counts = depressed_students["What is your CGPA?"].value_counts()

fig3, ax3 = plt.subplots()
cgpa_counts.plot(kind="bar", ax=ax3)
ax3.set_xlabel("CGPA Range")
ax3.set_ylabel("Number of Students")

st.pyplot(fig3)

st.write("""
**Insight:**  
Students with higher CGPA tend to report lower levels of depression,
but depression is present across all academic performance levels.
""")

# ---------------------------
# Panic Attack Chart
# ---------------------------
st.subheader("Panic Attack Status Among Students")

panic_counts = df["Do you have Panic attack?"].value_counts()

fig4, ax4 = plt.subplots()
panic_counts.plot(kind="bar", ax=ax4)
ax4.set_xlabel("Panic Attack")
ax4.set_ylabel("Number of Students")

st.pyplot(fig4)

st.write("""
**Insight:**  
A noticeable number of students experience panic attacks, emphasizing
the need for accessible mental health support.
""")

# ---------------------------
# Future Scope
# ---------------------------
st.subheader("Future Improvements")

st.write("""
- Add interactive filters (year of study, course)
- Provide personalized well-being tips
- Convert into a full interactive dashboard
""")
st.header("🧠 Mental Health Self-Check Tool")

st.write("Answer the questions below to assess your current mental wellbeing.")

# User Inputs
sleep_hours = st.slider("How many hours do you sleep per day?", 0, 12, 6)
study_hours = st.slider("How many hours do you study per day?", 0, 12, 4)
feeling_stressed = st.selectbox("Do you often feel stressed?", ["No", "Sometimes", "Yes"])
panic_attacks = st.selectbox("Have you experienced panic attacks?", ["No", "Yes"])

# Simple Risk Logic
risk_score = 0

if sleep_hours < 5:
    risk_score += 1

if study_hours > 8:
    risk_score += 1

if feeling_stressed == "Yes":
    risk_score += 2
elif feeling_stressed == "Sometimes":
    risk_score += 1

if panic_attacks == "Yes":
    risk_score += 2

# Result
if st.button("Check My Mental Health Status"):

    if risk_score >= 4:
        level = "High Risk"
        message = "⚠️ High Stress Risk. Please consider speaking to a counselor."
    elif risk_score >= 2:
        level = "Moderate Risk"
        message = "⚠️ Moderate Stress Level. Try relaxation and time management."
    else:
        level = "Low Risk"
        message = "✅ You seem to be managing well. Keep maintaining balance!"

    st.subheader("Your Mental Health Assessment Result")
    st.write(message)

    # Pie Chart
    import matplotlib.pyplot as plt

    labels = ['Stress Score', 'Remaining Balance']
    values = [risk_score, max(6 - risk_score, 0)]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title("Stress Level Distribution")

    st.pyplot(fig)

    # Suggestions
    st.subheader("💡 Suggested Actions")

    if risk_score >= 4:
        st.markdown("""
        - Talk to a counselor or trusted person  
        - Reduce study overload  
        - Practice breathing exercises daily  
        - Ensure 7–8 hours sleep  
        - Take short breaks every 1 hour  
        """)

    elif risk_score >= 2:
        st.markdown("""
        - Improve time management  
        - Exercise 30 minutes daily  
        - Limit screen time before sleep  
        - Try journaling your thoughts  
        """)

    else:
        st.markdown("""
        - Maintain your routine  
        - Keep a healthy sleep schedule  
        - Continue balanced study habits  
        - Stay socially connected  
        """)


