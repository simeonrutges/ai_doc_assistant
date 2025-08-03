# AI Document Assistant

**AI Document Assistant** is een lokaal Python-project waarin ik werk aan een lokale AI-documentassistent.  
Het is opgezet als persoonlijk oefenproject om ervaring op te doen met AI-technieken zoals document parsing, chunking, embeddings en Retrieval-Augmented Generation (RAG) met lokaal draaiende Large Language Models via [Ollama](https://ollama.com).

Het project draait volledig lokaal waarbij rekening is gehouden met privacy, modulariteit en uitbreidbaarheid. De huidige versie werkt via de command line, maar is voorbereid op uitbreiding met een API of webinterface.

---

## Huidige functionaliteit

- **Ondersteuning voor meerdere bestandsformaten**  
  Inlezen van `.pdf`, `.txt`, `.docx`, `.csv` en `.md` bestanden.

- **Chunking & vectorstore**  
  Documenttekst wordt opgesplitst in beheersbare stukken (chunks), voorzien van embeddings, en opgeslagen in een FAISS-vectorstore.

- **RAG-gebaseerde vraagbeantwoording**  
  Je kunt vragen stellen over documenten via de CLI. De assistent zoekt relevante context en laat een lokaal LLM een antwoord genereren.

- **Automatische document-samenvattingen**  
  Alle documenten in de `documents/`-map kunnen automatisch worden samengevat. De resultaten worden opgeslagen in `summaries/`.

- **Modulaire opzet met professioneel versiebeheer**  
  Duidelijke structuur (`core/`, `scripts/`, enz.), dependency management met Poetry, en werken met feature branches in Git.

---

## Mogelijke vervolgstappen

- REST API bouwen met FastAPI  
- Webinterface via Gradio of Streamlit  
- Vragen stellen over meerdere documenten tegelijk  
- Contextuele of hoofdstukgerichte samenvattingen  
- Feedback-logging en evaluatie van gegenereerde antwoorden

