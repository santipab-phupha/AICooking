import streamlit as st
from aift.multimodal import textqa
from aift import setting

# Set your API key
setting.set_api_key('T69FqnYgOdreO5G0nZaM8gHcjo1sifyU')

# Define available language regions for selection
regions = ["อีสาน", "ใต้", "เหนือ"]

# Streamlit app interface
st.title("Language Translator Demo")
st.write("Translate words or phrases into selected regional dialects.")

# Sidebar or main area input fields
selected_region = st.selectbox("Choose a Region", regions)
phrase = st.text_input("Enter a word or phrase to translate:")

if phrase:
    # Prepare context and call textqa API
    context = f"แปลภาษา{selected_region}"
    try:
        response = textqa.chat(
            instruction=phrase, 
            sessionid='YOUR_SESSION', 
            context=context, 
            temperature=0.2, 
            return_json=False
        )
        st.write("### Translation Result:")
        st.write(response)
    except Exception as e:
        st.write("Error:", e)
