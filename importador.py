import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


'''
Parce el importador funciona muy bien, pero en el momento el man funciona asi:
Sube una columna de ese archivo a la vez entonces para otras columnas toca modificarlo por el nombre de la columna que se quiere importar,
si se modifica ese formato de una revienta, entonces para hacer una importación diferente toca revisar el formato en base de datos, pero pues
casi que en todas es igual
'''

#Conexión a la base de datos PostgreSQL
db_connection_string = 'postgresql+psycopg2://user_sibi_db:s1b1s14t4@localhost:5432/sibi_db'
engine = create_engine(db_connection_string)


# Define la ubicación del archivo Excel y la hoja que quieres leer
excel_path = 'listas.xlsx'
sheet_name = 'LISTA' # Nombre de la hoja


# Lee el archivo Excel usando pandas
data_frame = pd.read_excel(excel_path, sheet_name=sheet_name, engine='openpyxl')


# Selecciona solo la columna "Referencia*" y agrega las demás columnas necesarias
data_frame = data_frame.rename(columns={"existing_name_column": "REFERENCIA*"}) # Reemplaza REFERENCIA* con el nombre de la columna en el Excel

#Estructura de la tabla de la db parce
data_frame['nombre'] = data_frame['REFERENCIA*']
data_frame['descripcion'] = data_frame['nombre'] # Descripcion tiene el mismo valor que nombre
data_frame['created'] = datetime.now() 
data_frame['updated'] = datetime.now()
data_frame['is_active'] = True #True pa que los ponga en formato [v] como activos

#Reordena las columnas
data_frame = data_frame[['nombre', 'descripcion', 'created', 'updated', 'is_active']]


#Este es el nombre de la tabla
table_name = 'sibi_referencia'

#Este es el campo que importa todo y usa append para apilar los datos, osea no reemplaza y el consecutivo de la db continua
data_frame.to_sql(table_name, con=engine, if_exists='append', index=False) 



