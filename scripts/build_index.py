import os
from core.document_loader import load_text_from_file
from core.embedding_store import EmbeddingStore

DOCUMENT_PATH = "documents/sample.pdf"         # Of verander dit naar een ander bestand
VECTORSTORE_DIR = "vectorstore"

def main():
    print(f"📄 Laden van document: {DOCUMENT_PATH}")
    text = load_text_from_file(DOCUMENT_PATH)

    print("🔪 Tekst opdelen in chunks...")
    store = EmbeddingStore()
    chunks = store.chunk_text(text)

    print(f"🧠 Embeddings genereren voor {len(chunks)} chunks...")
    store.build_index(chunks)

    print(f"💾 Opslaan in vectorstore map: {VECTORSTORE_DIR}")
    store.save(VECTORSTORE_DIR)

    print("✅ Index succesvol opgebouwd en opgeslagen.")

if __name__ == "__main__":
    main()
