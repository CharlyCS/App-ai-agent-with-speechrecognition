import spacy
import re
import es_core_news_sm
import en_core_web_sm
#nlp = spacy.load('en_core_news_sm')
nlp = es_core_news_sm.load() # https://spacy.io/models/es

class Extraction:
    def __init__(self, text):
        self.text = text

    def send_extraction(self):
        doc = nlp(self.text.lower())
        clave = ['envia', 'mandar', 'pasar', 'transferir', 'remitir', 'despachar']
        
        for token in doc:
            if token.lemma_ in clave:
                return token.lemma_
        return "No se encuentra envío"

    def mount_extraction(self):
        patron = r'\b\d+'
        #patron = r'\b\d+\s*soles\b'
        #number = patron.split()[1]
        result = re.search(patron, self.text.lower())
        return result.group() if result else "No se encontró monto"

    def name_extraction(self):
        doc = nlp(self.text)
        for entidad in doc.ents:
            if entidad.label_ == 'PER':
                return entidad.text
        return "No se encontró nombre"
        
text = "envia 400 soles a mi causa juan"

extraccion = Extraction(text)

print(extraccion.send_extraction()) 
print(extraccion.mount_extraction()) 
print(extraccion.name_extraction()) 