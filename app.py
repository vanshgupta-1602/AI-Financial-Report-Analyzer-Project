import streamlit as st
from pypdf import PdfReader

st.title("AI Financial Report Analyzer")

uploaded_file = st.file_uploader(
    "Upload Financial Report",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    st.success(f"PDF loaded: {len(pages)} pages")

    question = st.text_input(
        "Ask something about the financial report:"
    )

    if question:

        found = False

        for page in pages:

            if question.lower() in page["text"].lower():

                st.subheader("Result")

                st.write(page["text"][:2000])

                st.caption(
                    f"Source: Page {page['page']}"
                )

                found = True
                break

        if not found:
            st.warning(
                "I couldn't find an exact match in the report."
            )

            
    