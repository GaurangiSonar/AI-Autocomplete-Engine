import streamlit as st
from src.preprocess import load_dataset
from src.trie import Trie
from src.autocomplete import rank_suggestions
from st_keyup import st_keyup
# Page settings
st.set_page_config(
    page_title="AI Autocomplete Engine",
    page_icon="🔎",
    layout="centered"
)

# Load dataset
@st.cache_data
def get_dataset():
    return load_dataset()

df = get_dataset()

# Build Trie
@st.cache_resource
def build_trie(df):

    trie = Trie()

    for word in df["word"].dropna():
        trie.insert(str(word).lower().strip())

    return trie
trie = build_trie(df)

@st.cache_data(show_spinner=False)
def get_fast_results(_trie, _df, q):
    node = _trie.search_prefix(q.lower())
    res = []
    if node:
        _trie.collect_words(node, q.lower(), res)
    return rank_suggestions(res, _df)[:10]


# Title section
st.markdown(
    """
    <h1 style='text-align: center; color:#4CAF50;'>
    🔎 AI Autocomplete Engine
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Type a prefix to see intelligent suggestions.</p>",
    unsafe_allow_html=True
)

st.divider()

# Input
prefix = st_keyup("Start typing:", placeholder="Example: ap", key="search", )

# Search logic
if prefix:

    node = trie.search_prefix(prefix.lower())

    results = []

    if node:
        trie.collect_words(node, prefix.lower(), results)

    suggestions = rank_suggestions(results, df)

    st.subheader("Suggestions")

    for s in suggestions:
        st.markdown(
            f"""
            <div style="
                padding:10px;
                margin:5px;
                border-radius:8px;
                font-size:18px;">
                {s}
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.divider()

st.markdown(
    """
    <p style='text-align:center; font-size:14px;'>
    Built with Python • Trie Data Structure • Streamlit
    </p>
    """,
    unsafe_allow_html=True
)