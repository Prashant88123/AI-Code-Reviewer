import streamlit as st
import time
import os

from code_parser import parse_code
from style_checker import show_style_corrected
from error_detector import detect_errors
from ai_suggester import get_ai_suggestions


# ------------------ HELPERS ------------------

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


# ------------------ STREAMLIT CONFIG ------------------

st.set_page_config(
    page_title="AI Code Reviewer Application",
    layout="wide"
)

if os.path.exists("logo-ai.jpg"):
    col_logo, col_title = st.columns([1, 8])

    with col_logo:
        # 🔧 CHANGE THESE VALUES
        st.markdown("<div style='height: 55px;'></div>", unsafe_allow_html=True)
        st.image("logo-ai.jpg", width=320)

    with col_title:
        # 🔧 CHANGE THESE VALUES
        st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
        st.markdown("<h1 style='margin:0;'>AI Code Reviewer</h1>", unsafe_allow_html=True)
else:
    st.title("AI Code Reviewer")


# ------------------ SESSION STATE ------------------

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = {}

if "ai_suggestions" not in st.session_state:
    st.session_state.ai_suggestions = None

if "rerun_analysis" not in st.session_state:
    st.session_state.rerun_analysis = False



# ------------------ INPUT SECTION ------------------

st.markdown(
    "Paste your Python code below and click **Analyze** "
    "to get feedback on errors, style, and AI suggestions."
)

code = st.text_area("Code Input:", height=240,width=800)


# ------------------ ANALYSIS ------------------

def run_analysis(code):
    result = {}

    parse_result = parse_code(code)
    if not parse_result["success"]:
        result["parse_error"] = parse_result["error"]["message"]
        return result

    result["parse_success"] = True
    result["errors"] = detect_errors(code)
    result["style"] = show_style_corrected(code)
    result["ai"] = get_ai_suggestions(code)

    return result


# ------------------ ANALYZE BUTTON------------------

st.markdown("---")

analyze_clicked = st.button("Analyze code", type="primary")

if analyze_clicked or st.session_state.rerun_analysis:
    if not code.strip():
        st.warning("Please enter some code first!")
    else:
        with st.spinner("Analyzing your code..."):
            st.session_state.analysis_result = run_analysis(code)
            st.session_state.ai_suggestions = st.session_state.analysis_result.get("ai")
            st.session_state.analysis_done = True


# ------------------ TABS AT VERY BOTTOM ------------------

st.markdown("---")
tab1, = st.tabs(["Suggestions"])
if analyze_clicked or st.session_state.rerun_analysis:
    st.session_state.rerun_analysis = False
    # ---------- TAB 1 ----------
    with tab1:
        result = st.session_state.analysis_result
        if result:
            if "parse_error" in result:
                st.error("Your code has syntax errors!")
                st.code(result["parse_error"])
            else:
                st.success("Code parsed successfully!")

                st.subheader("Error Detection Results")
                error_result = result["errors"]

                if error_result["success"]:
                    if error_result["error_count"] == 0:
                        st.info("No static errors found! Your code looks clean.")
                    else:
                        for error in error_result["errors"]:
                            with st.expander(error["type"], expanded=True):
                                st.write(f"**Message:** {error['message']}")
                                st.info(f"**Suggestion:** {error['suggestion']}")

        st.subheader("Analysed Code")

        suggestions = st.session_state.ai_suggestions
        if not suggestions:
            st.info("No AI suggestions available.")
        else:
            for suggestion in suggestions:
                if suggestion["type"] == "AISuggestion":
                    with st.chat_message("assistant"):
                        st.write_stream(stream_data(suggestion["message"]))
                else:
                    st.error(suggestion["message"])

                    #-----Referesh------

if st.button("Refresh"):
    st.session_state.rerun_analysis = True
    st.rerun()
