import os
import shutil
import gradio as gr
from core.embedding_store import EmbeddingStore
from core.llm_interface import ask_llm
from core.document_loader import load_text_from_file

DOCUMENTS_DIR = "documents"
VECTORSTORE_DIR = "vectorstore"
TOP_K = 3

def beschikbare_documenten():
    return [
        os.path.splitext(f)[0]
        for f in os.listdir(DOCUMENTS_DIR)
        if f.lower().endswith(('.pdf', '.txt', '.docx', '.csv', '.md'))
    ]

def beantwoord_vraag(vraag: str, document_naam: str) -> str:
    vectorstore_path = f"{VECTORSTORE_DIR}/{document_naam}.faiss"

    try:
        store = EmbeddingStore.load(vectorstore_path)
    except FileNotFoundError:
        return f"❌ Bestand niet gevonden: {vectorstore_path}"

    context = store.query(vraag, top_k=TOP_K)
    if not context:
        return "⚠️ Geen relevante context gevonden."
    return ask_llm(vraag, context)

def verwerk_upload(file) -> str:
    if file is None:
        return "⚠️ Geen bestand geüpload."

    bestandsnaam = os.path.basename(file.name)
    doelpad = os.path.join(DOCUMENTS_DIR, bestandsnaam)
    shutil.copy(file.name, doelpad)

    tekst = load_text_from_file(doelpad)
    store = EmbeddingStore()
    store.add_text(tekst)

    indexpad = os.path.join(VECTORSTORE_DIR, f"{os.path.splitext(bestandsnaam)[0]}.faiss")
    store.save(indexpad)

    return f"✅ Bestand '{bestandsnaam}' verwerkt en geïndexeerd."

def start_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("# 📄 AI Documentassistent")

        with gr.Row():
            vraag = gr.Textbox(label="Stel je vraag")
            document = gr.Dropdown(choices=beschikbare_documenten(), label="Kies een document")


        antwoord = gr.Textbox(label="Antwoord")

        knop = gr.Button("Beantwoord vraag")
        knop.click(beantwoord_vraag, inputs=[vraag, document], outputs=antwoord)

        gr.Markdown("## 📤 Upload een nieuw document")
        uploader = gr.File(label="Upload een tekstbestand")
        upload_uitvoer = gr.Textbox(label="Status upload")
        uploader.upload(verwerk_upload, inputs=uploader, outputs=upload_uitvoer)

    demo.launch()

if __name__ == "__main__":
    start_gradio()

