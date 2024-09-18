import pandas as pd
from ai_extraction import Extraction
text = "envia 200 soles a mi causa jose garcia"
PATH = "sql_ai_agent/database_clients.csv"
extraccion = Extraction(text)
df = pd.read_csv(PATH)
print(extraccion.send_extraction().lower())
print(extraccion.name_extraction().lower())
if extraccion.send_extraction().lower() in ["envia", "mandar"]:
    name = extraccion.name_extraction().strip()[0].lower()
    last_name = extraccion.name_extraction().strip()[1].lower()
    #print(name + last_name)
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

