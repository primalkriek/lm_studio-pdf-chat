"""
model.py — talks to LM Studio.
"""
import lmstudio as lms


def list_models():
    """Return a list of model keys for every LLM downloaded in LM Studio."""
    models = lms.list_downloaded_models("llm")
    return [m.model_key for m in models]


def ask(model_key, question, document_text):
    """Ask a question about a document. Returns the model's answer as a string."""
    model = lms.llm(model_key)

    prompt = (
        "Answer the question using only the document below. "
        "If the answer is not in the document, say so.\n\n"
        f"Document:\n{document_text}\n\n"
        f"Question: {question}"
    )

    result = model.respond(prompt)
    return str(result)
