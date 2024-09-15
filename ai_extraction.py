import spacy
import re
import es_core_news_sm
import en_core_web_sm
#nlp = spacy.load('en_core_news_sm')
nlp = es_core_news_sm.load() # https://spacy.io/models/es

class extraction(text):
    def __init__(self):
        self.send_extraction = send_extraction(text)
        self.mount_extraction = mount_extraction(text)
        self.name_extraction = name_extraction(text)
        

    def send_extraction(texto):
        doc = nlp(texto.lower())
        clave = ['envia', 'mandar', 'pasar', 'transferir', 'remitir', 'despachar']

        '''for token in doc:
            print(f"Palabra: {token.text}, Lemmatizado: {token.lemma_}")'''
        for token in doc:
            if token.lemma_ in clave:
                return token.lemma_
        return "No se encuentra envio", 400

    def mount_extraction(texto):
        patron = r'\b\d+\s*soles\b'
        result = re.search(patron, texto.lower())
        return result.group() if result else None

    def name_extraction(texto):
        doc = nlp(texto)
        for entidad in doc.ents:
            if entidad.label_ == 'PER':
                return entidad.text
            else:
                return "No se encontro nombre", 400
        
text = "envia 400 soles a mi causa juan"
