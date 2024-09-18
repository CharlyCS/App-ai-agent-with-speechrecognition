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
        for token in doc:
            if token.dep_ in ('dobj', 'iobj', 'obj'):
                return token.text
        '''for entidad in doc.ents:
            print(entidad)
            if entidad.label_ == 'PER':
                print(entidad.label_)
                return entidad.text'''
        return "No se encontró nombre"
        
text = "envia 200 soles a mi causa jose garcia"
#PATH = "sql_ai_agent/database_clients.csv"
extraccion = Extraction(text)
print(extraccion.name_extraction())