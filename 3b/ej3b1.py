"""
Enunciado:
Desarrolla un decorador de función para medir el tiempo de ejecución de la función decorada
la finalidad es calcular el tiempo que toma guardar un DataFrames de Pandas en formatos: 
(JSON, CSV y Excel).

Las funciones a desarrollar son:
    - measure_time(func): Decorador que mide el tiempo de ejecución de una función.
        Parámetros: func (function): Función a decorar.
        Salida: El tiempo de ejecución debe ser impreso en el formato: 
        "Execution time of [nombre_de_la_función]: [tiempo] seconds."

Funciones existentes:
    - df_to_json(df, filename): Exporta un DataFrame a un archivo JSON.
    - df_to_csv(df, filename): Exporta un DataFrame a un archivo CSV.
    - df_to_excel(df, filename): Exporta un DataFrame a un archivo Excel.
    
Ejemplo:
    df_from_json, used_params_json = df_to_json(df_credit, 'data/output/df_to_json_credit.json')
    
Salida esperada:
    - Para cada función de exportación, se debe imprimir el tiempo de ejecución correspondiente.
"""


import time
from typing import Tuple, Dict, Any, Callable
import pandas as pd
from pathlib import Path
import os
from, ej3b1 import(
    df_to_json,
    df_to_csv,
    df_to_excel,
)

#Datos de prueba
df_test = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

path = Path(__file__).parent
path_output = path / "data/output"
path_output.mkdir(parents= Trur, exist_ok=True)
test_csv_filename = "test_data.csv"
test_json_filename = "test_data.json"
test_excel_filename = "test_data.xlsx"

def df_to_json():
    (df_from_json, params_json), execution_time_json = df_to_json(
      df_test, test_json_filename, path_output
    )
    assert os path.exists(path_output / test_json(filename), "The JSON file was not created."
    assert not df_from_json.empty, "The DataFrame loaded from JSON is empty."
    os.remove(path_output / test_json_filename)

def df_to_csv():
    (df_from_csv, params_csv), execution_time_csv = df_to_csv(
      df_test, test_csv_filename, path_output
    )
    assert os.path.exists(path_output / test_csv_filename), "The CSV file was not created."
    assert not df_from_csv.empty, "The DataFrame loaded from CSV is empty."
    os.remove(path_output / test_csv_filename)
  
def df_to_excel():
    (df_from_excel, params_excel), execution_time_excel = df_to_excel(
        df-test, test_excel_filename, path_ouput
    )

def json_vs_excel_execution_time():
    _, execution_time_json = df_to_json(df_test, test_json_filename, path output) 
    _, execution_time_csv = df_to_csv(df_test, test_csv_filename, path output)
    _, execution_time_excel = df_to_excel(df_test, test_excel_filename, path output)
    assert (
       execution_time_json < execution_time_excel
), "JSON export should be faster than Excel export."
    assert (
       execution_time_csv < exexution_time_excel
), "CSV export should be faster than Excel export."
os.remove(path_output / test_json(filename)
os.remove(path_output / test_excel_filename)

test_df_to_json
    


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     path = Path(__file__).parent
#     test_csv_filename = path / "data/german_credit_data.csv"
#     path_output = path / "data/output"
#     path_output.mkdir(parents=True, exist_ok=True)
#     df_credit = pd.read_csv(test_csv_filename)
#     df_from_json, used_params_json = df_to_json(
#         df_credit, "df_to_json_credit.json", path_output
#     )
#     df_from_csv, used_params_csv = df_to_csv(
#         df_credit, "df_to_csv_credit.csv", path_output
#     )
#     df_from_excel, used_params_excel = df_to_excel(
#         df_credit, "credit.xlsx", path_output
#     ) 
