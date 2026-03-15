import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="ScriptSage.AI | Dark Edition", 
    page_icon="🧠", 
    layout="wide"
)

# 2. Professional Dark Theme CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    
    /* Input Boxes */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #4B4B4B !important;
        border-radius: 10px !important;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(45deg, #FF4B4B, #FF8E53);
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    
    /* Header & Cards */
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .stInfo {
        background-color: #1E1E1E !important;
        border: 1px solid #333 !important;
        color: #FF4B4B !important;
    }
    
    /* Sidebar Dark Mode */
    [data-testid="stSidebar"] {
        background-color: #050505;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Setup Groq Client
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 4. Brand Header (Dark Styled)
with st.container():
    st.markdown("<h1 style='text-align: center;'>🧠 ScriptSage.AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>The Dark Mode Viral Content Engine</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #333;'>", unsafe_allow_html=True)

# 5. User Input Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("### 🎬 Content Configuration")
    topic = st.text_input("Enter Video Topic:", placeholder="e.g. 10 AI Secrets for 2026")
    
    c1, c2 = st.columns(2)
    with c1:
        tone = st.selectbox("Select Tone:", ["Professional", "High Energy", "Storytelling", "Funny"])
    with c2:
        duration = st.selectbox("Video Length:", ["Shorts", "5-10 Mins", "10-20 Mins"])

    # Magic Button
    if st.button("Generate Strategy Kit 🚀"):
        if topic:
            with st.spinner("ScriptSage is decrypting viral trends..."):
                prompt = f"""
                Act as a Viral Content Strategist. Create a professional English content kit for:
                Topic: {topic} | Tone: {tone} | Duration: {duration}
                
                Format the output beautifully with titles, hook, bullet points for script, SEO tags, and thumbnail idea.
                """
                
                try:
                    chat_completion = client.chat.completions.create(
                        messages=[{"role": "user", "content": prompt}],
                        model="llama-3.3-70b-versatile",
                    )
                    
                    result = chat_completion.choices[0].message.content
                    
                    st.success("Kit Generated!")
                    st.markdown("---")
                    st.markdown(result)
                    
                    # Download Feature
                    st.download_button("Download Strategy", result, file_name="script_sage_strategy.txt")
                    
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Bhai, topic toh likho pehle!")

# 6. Sidebar Branding
st.sidebar.markdown("## ⚙️ App Settings")
st.sidebar.write("Model: **Llama-3.3-70B**")
st.sidebar.markdown("---")
st.sidebar.write("Developed by **Tushar**")
st.sidebar.caption("PIET AI & DS Student")