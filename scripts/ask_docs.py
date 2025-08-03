import sys
import os
from core.document_loader import load_text_from_file
from core.embedding_store import EmbeddingStore
from core.llm_interface import ask_llm

VECTORSTORE_DIR = "vectorstore"
TOP_K = 3

def main():
    if len(sys.argv) < 2:
        print("Gebruik: python ask_docs.py \"Wat is je vraag?\" [optioneel: bestandsnaam zonder extensie]")
        sys.exit(1)

    vraag = sys.argv[1]
    target_doc = sys.argv[2] if len(sys.argv) > 2 else None

    if target_doc:
        vectorstore_path = os.path.join(VECTORSTORE_DIR, f"{target_doc}.faiss")
        print(f"📦 Laden van vectorstore voor '{target_doc}'...")
        if not os.path.exists(vectorstore_path):
            print(f"❌ Bestand niet gevonden: {vectorstore_path}")
            sys.exit(1)
        store = EmbeddingStore.load(vectorstore_path)
    else:
        print("❌ Geef voor deze versie een documentnaam mee als tweede argument.")
        sys.exit(1)

    print("🔍 Relevante tekst ophalen...")
    chunks = store.query(vraag, top_k=TOP_K)

    print("\n📚 🔎 Contextfragmenten:")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- Fragment {i} ---\n{chunk}\n")

    print("🤖 Antwoord genereren via LLM...")
    context = "\n\n".join(chunks)
    antwoord = ask_llm(vraag, context)

    print("\n✅ Antwoord:")
    print(antwoord)

if __name__ == "__main__":
    main()

