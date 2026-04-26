# PDF Chat

Three files: `view.py` (Streamlit UI), `controller.py` (controller), `model.py` (model using LM Studio).

## Setup

1. Download **LM Studio** [here](https://lmstudio.ai) if it is not installed
2. Check the sidebar on the right and choose model search and download a model.
Make sure that the model you want to download fits the size of your system RAM
5. Install Python dependencies:
   ```bash
   pip install streamlit lmstudio pypdf
   ```
6. Run:
   ```bash
   streamlit run view.py
   ```

## How to use

- Sidebar: pick a model, upload a PDF.
- Main window: type a question.

## If the model dropdown is empty

It means the SDK couldn't talk to LM Studio. Two things to check:

1. Is LM Studio running, and is the local server on? (Developer tab in LM Studio, the toggle has to be green.)
2. Do you have a model downloaded? Open the model search tab in LM Studio and download one (e.g. `qwen/qwen3-4b-2507`).
3. Check in the server settings that the authentication is off for this example

You can verify from a terminal:
```bash
lms ls
```
If that shows models, the dropdown should show them too.
