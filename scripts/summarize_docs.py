import os
import sys
from core.document_loader import load_text_from_file
from core.llm_interface import ask_llm

SUMMARY_DIR = "summaries"

def main():
    if len(sys.argv) < 2:
        print("Gebruik: python summarize_docs.py documents/bestand.pdf")
        sys.exit(1)

    filepath = sys.argv[1]
    filename = os.path.splitext(os.path.basename(filepath))[0]
    os.makedirs(SUMMARY_DIR, exist_ok=True)
    output_path = os.path.join(SUMMARY_DIR, f"{filename}.summary.txt")

    print(f"📄 Document laden: {filepath}")
    text = load_text_from_file(filepath)

    print("🧠 Samenvatting genereren...")
    prompt = f"""Vat het volgende document samen in duidelijke bullet points. Benoem hoofdlijnen, intentie en eventuele conclusies:

{text}

Samenvatting:"""

    summary = ask_llm("Vat samen:", text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary.strip())

    print(f"✅ Samenvatting opgeslagen in: {output_path}")

if __name__ == "__main__":
    main()
