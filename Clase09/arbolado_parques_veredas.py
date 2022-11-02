# arbolado_parques_veredas.py
"""
Queremos hacer un boxplot del diámetro a la altura del pecho para las Tipas 
(su nombre científico es tipuana tipu), que crecen en ambos tipos de ambiente.
"""
import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Abrí ambos datasets a los que llamaremos df_parques y df_veredas.
def obtener_ruta_csv(nombre_archivo:str) -> str:
    """
    Devuelve el nombre del archivo con la ruta a la carpeta Data.
    """
    return os.path.join('..', 'Data', nombre_archivo + '.csv')

def agregar_col_ambiente(df:pd.DataFrame, value:str) -> pd.DataFrame:
    """
    Agrega la columna ambiente con valor = value para todas las observaciones del df
    """
    df['ambiente'] = [value] * len(df)
    return df

def obtener_dfs_tipas(df_parques:pd.DataFrame, df_veredas:pd.DataFrame) -> list:
    """
    A partir de los datasets enteros de parques y veredas,
    genera los df de altura y diametro para las Tipuanas Tipu aka Tipas
    """
    parques_renamer = {'altura_tot': 'altura'}
    df_tipas_parques = df_parques[df_parques.nombre_cie == 'Tipuana Tipu'][['altura_tot', 'diametro']].rename(columns = parques_renamer)
    df_tipas_parques = agregar_col_ambiente(df_tipas_parques, 'Parque')
    
    veredas_renamer = {'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'}
    df_tipas_veredas = df_veredas[df_veredas.nombre_cientifico == 'Tipuana tipu'][['altura_arbol', 'diametro_altura_pecho']].rename(columns = veredas_renamer)
    df_tipas_veredas = agregar_col_ambiente(df_tipas_veredas, 'Vereda')
    
    return [df_tipas_parques, df_tipas_veredas]


def plot_metricas_tipas() -> None:
    """
    Función principal del módulo. Levanta los archivos y grafica las métricas
    de comparación de alturas y diámetros de Tipuanas Tipus en parques y veredas
    """
    df_parques = pd.read_csv(obtener_ruta_csv('arbolado-en-espacios-verdes'))
    df_veredas = pd.read_csv(obtener_ruta_csv('arbolado-publico-lineal-2017-2018'))
    
    df_tipas = pd.concat(obtener_dfs_tipas(df_parques, df_veredas))
    
    sns.boxplot(
        data = df_tipas,
        x = 'diametro',
        y = 'ambiente'
        ).set(
            title='Diametros de Tipuanas Tipus según el ambiente',
            xlabel='Diámetro [cm]',
            ylabel='Ambiente de CABA'
            )
    plt.show()
    
    sns.boxplot(
        data = df_tipas,
        x = 'altura',
        y = 'ambiente'
        ).set(
            title='Alturas de Tipuanas Tipus según el ambiente',
            xlabel='Alturas [m]',
            ylabel='Ambiente de CABA'
            )
    plt.show()

plot_metricas_tipas()
