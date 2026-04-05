import streamlit as st

def set_professional_dark_theme():
    st.markdown("""
    <style>
    /* Main background – deep dark blue */
    .stApp {
        background-color: #0e1117;
    }
    .main {
        background-color: #0e1117;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1a1c23;
        border-right: 1px solid #2a2e3d;
    }
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    p, li, .stMarkdown, .stText, label, .stTextInput label, .stSelectbox label {
        color: #e0e0e0 !important;
    }
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #00b4d8, #0077b6);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(0,180,216,0.3);
        background: linear-gradient(90deg, #00c8ff, #0088cc);
    }
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1e1e2e;
        color: #00b4d8;
        border-radius: 8px;
        font-weight: 500;
    }
    .streamlit-expanderContent {
        background-color: #1a1c23;
        border-radius: 0 0 8px 8px;
        border: 1px solid #2a2e3d;
        border-top: none;
        padding: 1rem;
    }
    /* Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #1e1e2e;
        color: #ffffff;
        border: 1px solid #2a2e3d;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
        border-color: #00b4d8;
        box-shadow: 0 0 0 1px #00b4d8;
    }
    /* File uploader */
    .stFileUploader > div > div {
        background-color: #1e1e2e;
        border: 1px dashed #00b4d8;
        border-radius: 12px;
        padding: 1rem;
    }
    /* Alerts */
    .stAlert {
        background-color: #1e1e2e;
        border-left: 4px solid;
        border-radius: 8px;
    }
    .stAlert[data-baseweb="notification"] {
        background-color: #1e1e2e;
    }
    .stAlert.success {
        border-left-color: #00b4d8;
        color: #b0f0ff;
    }
    .stAlert.error {
        border-left-color: #ff4d4d;
        color: #ffb3b3;
    }
    .stAlert.info {
        border-left-color: #00b4d8;
    }
    /* Spinner */
    .stSpinner > div {
        border-top-color: #00b4d8 !important;
    }
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background-color: #1a1c23;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #2a2e3d;
        border-radius: 6px;
        color: #e0e0e0;
        padding: 0.5rem 1rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00b4d8;
        color: #ffffff;
    }
    /* Dataframes */
    .dataframe {
        background-color: #1e1e2e;
        color: #e0e0e0;
        border-radius: 8px;
    }
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #1a1c23;
    }
    ::-webkit-scrollbar-thumb {
        background: #00b4d8;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #0077b6;
    }
    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #1e1e2e;
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid #2a2e3d;
    }
    </style>
    """, unsafe_allow_html=True)