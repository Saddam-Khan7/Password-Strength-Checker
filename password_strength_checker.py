import streamlit as st
import re  


def check_password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")


    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")


    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")


    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")


    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character like !@#$%^&*.")


    if score == 5:
        strength = "✅ Your password is strong!"
    elif score >= 3:
        strength = "⚠️ Your password is moderate."
    else:
        strength = "❌ Your password is weak."

    return strength, feedback


st.title("🔐 Password Strength Meter")

st.sidebar.markdown("Developed by **Saddam Khan**")


password = st.text_input("Enter your password:")


if password:
    strength, suggestions = check_password_strength(password)
    st.subheader(strength)

    if suggestions:
        st.markdown("**Suggestions to improve your password:**")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")
