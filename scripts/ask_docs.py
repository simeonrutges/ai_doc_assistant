import sys
from core.embedding_store import EmbeddingStore
from core.llm_interface import ask_llm

VECTORSTORE_DIR = "vectorstore"

def main():
    if len(sys.argv) < 2:
        print("Gebruik: python ask_docs.py \"Wat is dit document?\"")
        sys.exit(1)

    vraag = sys.argv[1]
    print(f"❓ Vraag: {vraag}")

    print("📦 Laden van vectorstore...")
    store = EmbeddingStore()
    store.load(VECTORSTORE_DIR)

    print("🔍 Relevante tekst ophalen...")
    context_chunks = store.query(vraag, top_k=3)
    context = "\n\n".join(context_chunks)

    print("🤖 Antwoord genereren via LLM...")
    antwoord = ask_llm(vraag, context)

    print("\n🧠 Antwoord:")
    print(antwoord)

if __name__ == "__main__":
    main()
