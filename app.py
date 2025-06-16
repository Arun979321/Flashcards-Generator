
import streamlit as st
import pandas as pd
import json
from parser_utils import extract_text_from_file
from llm_utils import generate_flashcards
from flashcard_utils import parse_flashcards

st.set_page_config(page_title="📚 LLM Flashcard Generator")

st.title("📚 LLM-Powered Flashcard Generator")
st.markdown("Generate smart Q&A flashcards from educational content using AI.")

# 🔁 Use session_state to preserve flashcards across reruns
if "flashcards" not in st.session_state:
    st.session_state.flashcards = None

# 📤 Upload section
uploaded_file = st.file_uploader("📄 Upload a .pdf, .txt, .csv, or .json file", type=["pdf", "txt", "csv", "json"])
text_input = st.text_area("📝 Or paste content here", height=300)

col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox("📘 Subject", ["General", "Biology", "History", "CS"])
with col2:
    language = st.selectbox("🌐 Output Language", ["English", "Hindi", "Spanish", "French", "German"])

# 🚀 Generate Flashcards Button
if st.button("🚀 Generate Flashcards"):
    with st.spinner("Processing..."):

        # Extract text content
        text = ""
        if uploaded_file:
            file_type = uploaded_file.name.split(".")[-1].lower()

            if file_type in ["pdf", "txt"]:
                text = extract_text_from_file(uploaded_file)

            elif file_type == "csv":
                df = pd.read_csv(uploaded_file)
                text = df.astype(str).apply(" ".join, axis=1).str.cat(sep=" ")

            elif file_type == "json":
                try:
                    data = json.load(uploaded_file)
                    if isinstance(data, list):
                        text = " ".join(json.dumps(item) for item in data)
                    elif isinstance(data, dict):
                        text = json.dumps(data)
                    else:
                        st.error("Unsupported JSON structure.")
                        st.stop()
                except Exception as e:
                    st.error(f"Failed to parse JSON: {e}")
                    st.stop()

        elif text_input.strip():
            text = text_input.strip()

        else:
            st.error("Please upload a file or paste content.")
            st.stop()

        # Generate & parse flashcards
        raw_output = generate_flashcards(text, subject=subject, language=language)
        flashcards = parse_flashcards(raw_output)

        if not flashcards:
            st.error("No flashcards generated. Please try different input.")
            st.stop()

        st.session_state.flashcards = flashcards

# 📇 Display Flashcards & Downloads
if st.session_state.flashcards:
    st.subheader("📇 Flashcards (Editable)")
    df = pd.DataFrame(st.session_state.flashcards)
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    # Show preview
    for i, row in edited_df.iterrows():
        st.markdown(f"**Q{i+1} ({row.get('difficulty', 'N/A')}, {row.get('section', 'No Section')}):** {row['question']}")
        st.markdown(f"**A{i+1}:** {row['answer']}")

    # 📥 Downloads
    csv = edited_df.to_csv(index=False).encode("utf-8")
    json_data = edited_df.to_json(orient="records", indent=2)
    anki_tsv = edited_df[['question', 'answer']].to_csv(index=False, sep='\t', header=False).encode('utf-8')

    st.download_button("⬇️ Download as CSV", data=csv, file_name="flashcards.csv", mime="text/csv")
    st.download_button("⬇️ Download as JSON", data=json_data, file_name="flashcards.json", mime="application/json")
    st.download_button("🧠 Export for Anki (TSV)", data=anki_tsv, file_name="anki_flashcards.tsv", mime="text/tab-separated-values")
