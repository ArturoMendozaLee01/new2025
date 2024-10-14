import pandas as pd

# Ruta del archivo CSV en Google Drive
RUTA_CSV = '/content/drive/MyDrive/Proyecto_2025/df_proyecto2025.csv'
RUTA_EXPORT = '/content/drive/MyDrive/Proyecto_2025/df_filtrado.csv'

def cargar_dataframe():
    """Carga el DataFrame desde la ruta definida."""
    try:
        df = pd.read_csv(RUTA_CSV)
        print("DataFrame cargado correctamente.")
        return df
    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
        return None

def filtrar_datos(df, metric, sites, bucket):
    """Filtra el DataFrame según los parámetros proporcionados."""
    df_filtrado = df[
        (df['Metric'] == metric) &
        (df['Site'].isin(sites)) &
        (df['Bucket'] == bucket)
    ]
    return df_filtrado

def exportar_csv(df):
    """Exporta el DataFrame filtrado a la ruta definida."""
    if not df.empty:
        df.to_csv(RUTA_EXPORT, index=False)
        print(f"Archivo exportado como {RUTA_EXPORT}.")
    else:
        print("No se puede exportar. El filtro no arrojó resultados.")
