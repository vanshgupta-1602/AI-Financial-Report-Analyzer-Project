import streamlit as st
import re
from pypdf import PdfReader
st.set_page_config(page_title="AI Financial Report Analyzer", page_icon="📊", layout="wide")
st.title("📊 AI Financial Report Analyzer")
st.caption("Upload a financial PDF to extract figures and review key performance indicators.")
def extract_pdf(file):
    reader = PdfReader(file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)
def numbers(text):
    return [
        float(x.replace(",", ""))
        for x in re.findall(r"(?<![A-Za-z])\d[\d,]*(?:\.\d+)?", text)
    ]
def metric(text, name):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(name, line, re.I):
            section = " ".join(lines[i:i+3])
            vals = numbers(section)
            vals = [v for v in vals if v > 0]
            if vals:
                return vals[-1]
    return None
def fmt(value):
    return f"₹{value:,.2f} crore" if value is not None else "Not found"
pdf = st.file_uploader("Upload annual report (PDF)", type=["pdf"])
if pdf:
    try:
        text = extract_pdf(pdf)
        if not text.strip():
            st.error("No selectable text found. This PDF may be scanned.")
            st.stop()
        st.success("Report uploaded and extracted successfully.")
        revenue = metric(text, r"\bRevenue\b")
        profit = metric(text, r"\bNet Profit\b")
        assets = metric(text, r"\bTotal Assets\b")
        debt = metric(text, r"\bTotal Debt\b")
        cash = metric(text, r"Cash\s*(?:&|and)\s*Equivalents")
        st.header("Financial Overview")
        c1, c2, c3 = st.columns(3)
        c1.metric("Revenue", fmt(revenue))
        c2.metric("Net Profit", fmt(profit))
        c3.metric("Total Assets", fmt(assets))
        c4, c5 = st.columns(2)
        c4.metric("Total Debt", fmt(debt))
        c5.metric("Cash & Equivalents", fmt(cash))
        st.header("Key Insights")
        if revenue is not None and profit is not None:
            st.write(f"- Reported revenue: **{fmt(revenue)}**")
            st.write(f"- Reported net profit: **{fmt(profit)}**")
        if debt is not None and cash is not None:
            st.write(f"- Debt: **{fmt(debt)}**")
            st.write(f"- Cash and equivalents: **{fmt(cash)}**")
        st.info("These figures are extracted from PDF text. Verify them against the original report before making financial decisions.")
        with st.expander("View extracted report text"):
            st.text(text)
        st.download_button(
            "Download extracted text",
            text,
            file_name="financial_report.txt",
            mime="text/plain"
        )
    except Exception as e:
        st.error(f"Could not read this PDF: {e}")
else:
    st.write("### What this app does")
    st.markdown("- Extracts readable text from financial PDFs\n- Displays key financial figures\n- Provides a downloadable text extract")
