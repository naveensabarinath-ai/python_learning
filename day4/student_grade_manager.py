import pandas as pd
import requests
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="📘",
    layout="wide",
)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: #f4f7f5;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2rem;
    }

    .hero {
        background: #e5eee8;
        border-left: 6px solid #c5a65a;
        border-radius: 8px;
        color: #234638;
        padding: 22px 26px;
        margin-bottom: 22px;
    }

    .hero h1 {
        color: #234638;
        margin: 0;
    }

    .hero p {
        color: #587265;
        margin: 6px 0 0;
    }

    [data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #dce6df;
        border-radius: 8px;
        padding: 14px 16px;
    }

    div[data-testid="stForm"] {
        background: #ffffff;
        border: 1px solid #dce6df;
        border-radius: 8px;
        padding: 18px;
    }

    .stButton > button,
    .stDownloadButton > button {
        background: #557d68;
        border: 1px solid #557d68;
        border-radius: 6px;
        color: #ffffff;
        min-height: 40px;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #416651;
        border-color: #416651;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def clear_entries() -> None:
    for key in list(st.session_state):
        if key.startswith(("student_name_", "student_mark_")):
            del st.session_state[key]

    st.session_state.pop("grade_results", None)
    st.session_state.pop("grade_summary", None)
    st.session_state.pop("csv_data", None)
    st.session_state["student_count"] = 1


st.markdown(
    """
    <div class="hero">
        <h1>Student Grade Manager</h1>
        <p>Class gradebook</p>
    </div>
    """,
    unsafe_allow_html=True,
)

count_col, clear_col = st.columns([3, 1])

with count_col:
    student_count = st.number_input(
        "Number of students",
        min_value=1,
        max_value=30,
        value=1,
        step=1,
        key="student_count",
    )

with clear_col:
    st.write("")
    st.button(
        "Clear entries",
        on_click=clear_entries,
        use_container_width=True,
    )

with st.form("student_grades"):
    st.subheader("Student entries")

    for index in range(int(student_count)):
        name_col, mark_col = st.columns([2, 1])

        name_col.text_input(
            f"Student {index + 1}",
            placeholder="Enter student name",
            key=f"student_name_{index}",
        )

        mark_col.number_input(
            "Mark (0–100)",
            min_value=0.0,
            max_value=100.0,
            step=0.5,
            key=f"student_mark_{index}",
        )

    submitted = st.form_submit_button(
        "Calculate grades",
        type="primary",
        use_container_width=True,
    )

if submitted:
    students = [
        {
            "name": st.session_state.get(f"student_name_{index}", "").strip()
            or f"Student {index + 1}",
            "mark": st.session_state.get(f"student_mark_{index}", 0.0),
        }
        for index in range(int(student_count))
    ]
    payload = {"students": students}

    try:
        grade_response = requests.post(
            f"{API_BASE_URL}/grades/calculate",
            json=payload,
            timeout=10,
        )
        grade_response.raise_for_status()
        grade_data = grade_response.json()

        csv_response = requests.post(
            f"{API_BASE_URL}/grades/csv",
            json=payload,
            timeout=10,
        )
        csv_response.raise_for_status()

        st.session_state["grade_results"] = grade_data["results"]
        st.session_state["grade_summary"] = grade_data
        st.session_state["csv_data"] = csv_response.content
    except requests.RequestException as error:
        st.session_state.pop("grade_results", None)
        st.session_state.pop("grade_summary", None)
        st.session_state.pop("csv_data", None)
        st.error(f"Could not reach the Grade API: {error}")

results = st.session_state.get("grade_results", [])

if results:
    results_df = pd.DataFrame(results)
    marks = results_df["Mark"]
    summary = st.session_state["grade_summary"]

    st.subheader("Class overview")
    average_col, highest_col, lowest_col = st.columns(3)

    average_col.metric("Class average", f"{summary['average_mark']:.1f}")
    average_col.caption(f"Average grade: {summary['average_grade']}")
    highest_col.metric("Highest mark", f"{marks.max():.1f}")
    lowest_col.metric("Lowest mark", f"{marks.min():.1f}")

    st.subheader("Grade report")
    st.dataframe(
        results_df,
        hide_index=True,
        use_container_width=True,
    )

    csv_data = st.session_state.get("csv_data")
    if csv_data:
        st.download_button(
            "Download CSV",
            data=csv_data,
            file_name="student_results.csv",
            mime="text/csv",
            use_container_width=True,
        )

# Need to run the FastAPI server before using this Streamlit app. Use the following command to start the server:
# python -m uvicorn grade_api:app --reload
# Need to run the Streamlit app with the following command: 
# streamlit run day4/student_grade_manager.py