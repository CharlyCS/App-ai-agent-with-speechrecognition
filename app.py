import pandas as pd
from ai_extraction import Extraction
from speechai import transcription
#text = "envío 400 soles a mí causa José García" --TEXTO DE PRUEBA
text = transcription()
PATH = "sql_ai_agent/database_clients.csv"
extraccion = Extraction(text)
df = pd.read_csv(PATH)


if extraccion.send_extraction().lower() in ["enviar", "mandar", 'envío', 'envio', 'envía']:
    
    full_name = extraccion.name_extraction().strip().split()
    name = full_name[0].capitalize()
    last_name = full_name[1].capitalize()
    for index, row in df.iterrows():
        if row['nombre'] == name and row['apellido'] == last_name:
            amount_init = float(row['Monto'])
            amount_send = float(extraccion.mount_extraction())
            if amount_init >= amount_send:
                new = amount_init - amount_send
                df.at[index, 'Monto'] = new
                print(f"Transacción exitosa. Nuevo saldo de {name} {last_name}: {new}")
            else:
                print("Saldo insuficiente")
                break

df.to_csv(PATH, index =False)
print(df)
