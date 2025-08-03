import os
from core.document_loader import load_text_from_file
from core.llm_interface import ask_llm

DOCUMENTS_DIR = "documents"
SUMMARY_DIR = "summaries"

def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)

    files = [
        f for f in os.listdir(DOCUMENTS_DIR)
        if f.lower().endswith(('.pdf', '.txt', '.docx'))
    ]

    if not files:
        print("⚠️ Geen documenten gevonden in de 'documents/' map.")
        return

    for filename in files:
        path = os.path.join(DOCUMENTS_DIR, filename)
        name = os.path.splitext(filename)[0]
        output_path = os.path.join(SUMMARY_DIR, f"{name}.summary.txt")

        print(f"\n📄 Samenvatten: {filename}")
        text = load_text_from_file(path)

        prompt = f"""Vat het volgende document samen in duidelijke bullet points. Benoem hoofdlijnen, intentie en eventuele conclusies:

{text}

Samenvatting:"""

        summary = ask_llm("Vat samen:", text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(summary.strip())

        print(f"✅ Opgeslagen in: {output_path}")

    print("\n📚 Alle documenten zijn samengevat.")

if __name__ == "__main__":
    main()

