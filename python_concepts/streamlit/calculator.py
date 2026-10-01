import streamlit as st
import math

st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e293b);
    }

    .calculator {
        max-width: 430px;
        margin: auto;
    }

    .title {
        text-align: center;
        color: #f8fafc;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }

    .display {
        background: #020617;
        color: #f8fafc;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 22px;
        text-align: right;
        font-size: 2.2rem;
        font-weight: 600;
        margin-bottom: 15px;
        min-height: 45px;
        overflow-x: auto;
    }

    div.stButton > button {
        width: 100%;
        height: 58px;
        border-radius: 14px;
        border: 1px solid #334155;
        background: #1e293b;
        color: white;
        font-size: 1.25rem;
        font-weight: 600;
        transition: all 0.15s ease;
    }

    div.stButton > button:hover {
        background: #334155;
        border-color: #64748b;
        transform: translateY(-2px);
    }

    div.stButton > button:active {
        transform: scale(0.96);
    }

    .history-title {
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 25px;
    }
</style>
""", unsafe_allow_html=True)


# ---------- State ----------
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "result" not in st.session_state:
    st.session_state.result = ""

if "history" not in st.session_state:
    st.session_state.history = []


# ---------- Functions ----------
def add(value):
    st.session_state.expression += value


def clear():
    st.session_state.expression = ""
    st.session_state.result = ""


def backspace():
    st.session_state.expression = st.session_state.expression[:-1]


def calculate():
    expression = st.session_state.expression

    if not expression:
        return

    try:
        # Replace calculator symbols with Python equivalents
        safe_expression = expression.replace("×", "*")
        safe_expression = safe_expression.replace("÷", "/")
        safe_expression = safe_expression.replace("^", "**")

        # Basic safe math namespace
        allowed = {
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "round": round
        }

        result = eval(
            safe_expression,
            {"__builtins__": {}},
            allowed
        )

        if isinstance(result, float):
            result = round(result, 10)

            if result.is_integer():
                result = int(result)

        st.session_state.result = str(result)

        st.session_state.history.insert(
            0,
            f"{expression} = {result}"
        )

        # Keep only latest 10 calculations
        st.session_state.history = st.session_state.history[:10]

    except Exception:
        st.session_state.result = "Error"


def use_result():
    if st.session_state.result and st.session_state.result != "Error":
        st.session_state.expression = st.session_state.result
        st.session_state.result = ""


# ---------- UI ----------
st.markdown(
    '<div class="title">🧮 Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Simple • Fast • Modern</div>',
    unsafe_allow_html=True
)

# Display
display_value = (
    st.session_state.result
    if st.session_state.result
    else st.session_state.expression
)

if not display_value:
    display_value = "0"

st.markdown(
    f'<div class="display">{display_value}</div>',
    unsafe_allow_html=True
)


# ---------- Calculator Buttons ----------
rows = [
    ["AC", "⌫", "(", ")"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
]

for row in rows:
    cols = st.columns(4)

    for col, button in zip(cols, row):
        with col:
            if st.button(button, key=f"btn_{button}_{row[0]}"):
                if button == "AC":
                    clear()

                elif button == "⌫":
                    backspace()

                elif button == "%":
                    add("/100")

                elif button == "=":
                    calculate()

                else:
                    add(button)

                st.rerun()


# ---------- Equal Button ----------
if st.button("=", key="equals", use_container_width=True):
    calculate()
    st.rerun()


# ---------- Scientific Functions ----------
with st.expander("🔬 Scientific Functions"):
    sci_cols = st.columns(4)

    functions = [
        ("√", "sqrt("),
        ("sin", "sin("),
        ("cos", "cos("),
        ("tan", "tan("),
        ("log", "log("),
        ("ln", "ln("),
        ("π", "pi"),
        ("e", "e"),
        ("^", "^")
    ]

    for i, (label, value) in enumerate(functions):
        with sci_cols[i % 4]:
            if st.button(label, key=f"sci_{label}"):
                add(value)
                st.rerun()


# ---------- Use Result ----------
if st.session_state.result and st.session_state.result != "Error":
    if st.button("↩️ Use Result", use_container_width=True):
        use_result()
        st.rerun()


# ---------- History ----------
if st.session_state.history:
    st.markdown(
        '<div class="history-title">🕘 Calculation History</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.history:
        st.info(item)

    if st.button("🗑️ Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
