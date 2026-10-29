import pandas as pd

# Seleccionar y subir el archivo CSV
archivos = files.upload()

# Obtener el nombre del archivo subido
spotify = next(iter(archivos))

# Leer el dataset (usando la variable directamente)
df = pd.read_csv(spotify)

# Mostrar las primeras filas
display(df.head())

# Número de filas y columnas
print("Dimensiones del dataset:", df.shape)

# Nombres de las columnas
print("\nColumnas disponibles:")
print(df.columns.tolist())

# Tipos de datos y valores no nulos
print("\nInformación general:")
df.info()

# Valores faltantes por columna
print("\nValores faltantes:")
display(df.isnull().sum().sort_values(ascending=False))

# Registros duplicados
print("\nFilas duplicadas:", df.duplicated().sum())
