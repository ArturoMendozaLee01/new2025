import script1 as s1
import ipywidgets as widgets
from IPython.display import display

# Cargar el DataFrame
df = s1.cargar_dataframe()

# Crear widgets
metric_widget = widgets.Dropdown(
    options=['VaR', 'CS01', 'EAD', 'NetShort', 'FX'],
    description='Métrica:',
)

site_widget = widgets.SelectMultiple(
    options=['MX', 'BR', 'CL', 'AR', 'UY', 'LAM'],
    description='Sitios:',
    value=('MX',)
)

bucket_widget = widgets.Dropdown(
    options=['1D', '1M', '3M', '6M', '1Y', '5Y', '10Y', '30Y'],
    description='Bucket:',
)

export_button = widgets.Button(
    description='Exportar CSV',
    button_style='success',
)

output = widgets.Output()

def mostrar_resultado(_):
    """Mostrar el DataFrame filtrado en el output."""
    with output:
        output.clear_output()
        df_filtrado = s1.filtrar_datos(df, metric_widget.value, list(site_widget.value), bucket_widget.value)
        if not df_filtrado.empty:
            display(df_filtrado)
        else:
            print("No se encontraron resultados.")

def exportar_datos(_):
    """Exportar los datos filtrados a CSV."""
    df_filtrado = s1.filtrar_datos(df, metric_widget.value, list(site_widget.value), bucket_widget.value)
    s1.exportar_csv(df_filtrado)

def iniciar_widgets():
    """Función para iniciar y mostrar los widgets."""
    metric_widget.observe(mostrar_resultado, names='value')
    site_widget.observe(mostrar_resultado, names='value')
    bucket_widget.observe(mostrar_resultado, names='value')
    export_button.on_click(exportar_datos)

    # Mostrar los widgets al usuario
    if df is not None:
        display(metric_widget, site_widget, bucket_widget, export_button, output)
    else:
        print("Error al cargar el DataFrame.")
