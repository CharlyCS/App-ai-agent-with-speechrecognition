# App with an AI agent (Beta Version)

This project is designed to extract and process specific information from text inputs using Natural Language Processing (NLP) and voice transcription. The solution includes custom classes for entity extraction, name and action recognition, and now voice-to-text transcription. The project is focused on text processing in Spanish and is integrated with an AI agent to assist with extracting and acting on specific data points, such as names, amounts, and actions.

## **Features**

- **NLP Text Extraction**: 
  - Uses SpaCy to extract key actions (e.g., `envia`, `mandar`) and entities (e.g., names, amounts) from input text.
  - Supports lemmatization to standardize words for better matching (e.g., "envia" to "enviar").
  
- **Handling Accented Characters**: 
  - Automatic normalization of characters to remove tildes (e.g., "José García" becomes "Jose Garcia").

- **Voice Transcription**:
  - Speech recognition using speech_recognition and pyaudio.
  - Allows users to input text by voice.

- **Data Handling (Beta)**: 
  - The current version uses `pandas` to read data from a CSV file (`database_clients.csv`) for client data manipulation.
  - SQL integration is planned for future releases.

## **Installation**

1. Clone the repository:
    ```bash
    git clone https://github.com/CharlyCS/App-sql-ai-agent.git
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Download the SpaCy Spanish language model:
    ```bash
    python -m spacy download es_core_news_md
    ```
