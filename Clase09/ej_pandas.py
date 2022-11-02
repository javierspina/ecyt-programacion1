# ej_pandas.py
import os
import pandas as pd
import seaborn as sns

# Seleccion flexible del archivo
dir_archivo = 'Data'
nombre_archivo = 'arbolado-publico-lineal-2017-2018.csv'
archivo_arbolado = os.path.join('..', dir_archivo, nombre_archivo)

# Seleccionar solo unas columnas del dataset
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = pd.read_csv(archivo_arbolado, usecols = cols_sel)

# Seleccionar un subconjunto de especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# boxplot de los diámetros de los árboles agrupados por especie.
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

# boxplot de las alturas de los árboles agrupados por especie.
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
