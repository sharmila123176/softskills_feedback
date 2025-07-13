import streamlit as st

def main():
    st.title("📝 Soft Skills + Teamwork Feedback Form")

    name = st.text_input("Enter your name")

    st.markdown("### Rate the following from 1 (Strongly Disagree) to 5 (Strongly Agree):")

    questions = {
        "1. Demonstrates clear and respectful communication": 0,
        "2. Listens actively and considers team members’ input": 0,
        "3. Shows initiative and takes ownership of tasks": 0,
        "4. Cooperates well in group discussions and projects": 0,
        "5. Handles feedback positively and works on improvements": 0,
        "6. Demonstrates problem-solving and conflict resolution skills": 0
    }

    responses = {}

    for question in questions:
        responses[question] = st.slider(question, 1, 5, 3)

    comments = st.text_area("Additional comments or suggestions (optional)")

    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback!")
        st.markdown("---")
        st.markdown("### 🧾 Feedback Summary")
        st.write(f"**Name:** {name}")
        for q, r in responses.items():
            st.write(f"**{q}**: {r}")
        if comments.strip():
            st.write(f"**Comments:** {comments}")
        else:
            st.write("No additional comments provided.")

if __name__ == "__main__":
    main()
