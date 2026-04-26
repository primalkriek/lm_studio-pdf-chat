"""
view.py — Streamlit UI. Run with:  streamlit run view.py
"""
import streamlit as st
import controller

st.set_page_config(page_title="PDF Chat", layout="wide")

# Keep chat history and document text across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

# --- Sidebar: pick a model + upload a PDF ---
with st.sidebar:
    st.header("Setup")

    models = controller.list_models()
    if not models:
        st.warning("No models found. Open LM Studio and download a model first.")
        model_key = None
    else:
        model_key = st.selectbox("Model", models)

    pdf_file = st.file_uploader("Upload a PDF", type="pdf")
    if pdf_file is not None:
        st.session_state.document_text = controller.read_pdf(pdf_file.getvalue())
        st.success(f"Loaded {pdf_file.name}")

# --- Main pane: chat ---
st.title("Chat with your PDF")

# Show all previous messages.
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle a new question.
question = st.chat_input("Ask a question about the PDF")
if question:
    if not model_key:
        st.error("Pick a model first.")
    elif not st.session_state.document_text:
        st.error("Upload a PDF first.")
    else:
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = controller.ask(
                    model_key, question, st.session_state.document_text
                )
            st.write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
