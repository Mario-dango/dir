from app.src.model.archivosExcel import PlanillaModel as pm
import pandas as pd

manager = pm()
path = "C:/Users/mprob/Documents/Proyectos/Sistema de Estimacion de Rutas/SER/app/resources/data/examples/planillaTest.xlsx"
hoja = "Datos"
# datos_excel = manager.leerData(path, hoja)
# Muestra los datos

# # Usando iterrows() para recorrer los valores
# for indice, fila in datos_excel.iterrows():
#     # 'indice' es el índice de la fila
#     # 'fila' es una Serie que contiene los valores de la fila actual
#     for columna, valor in fila.items():
#         # 'columna' es el nombre de la columna
#         # 'valor' es el valor en la posición fila-columna
#         print(f"Valor en la fila {indice}, columna '{columna}': {valor}")


# # Accediendo a los valores por posición
# for i in range(len(datos_excel)):  # Iterando sobre las filas
#     for j in range(len(datos_excel.columns)):  # Iterando sobre las columnas
#         valor = datos_excel.iloc[i, j]  # Accediendo al valor en la posición i, j
#         print(f"Valor en la fila {i}, columna {j}: {valor}")
        

# # Accediendo a los valores por nombre de columna
# for columna in datos_excel.columns:
#     for valor in datos_excel[columna]:
#         print(f"Valor en la columna '{columna}': {valor}")

# print(datos_excel)


            
def leer_fila_desde_progresivas(archivo_excel, nombre_hoja):
    # Lee el archivo Excel en un DataFrame de Pandas
    df = pd.read_excel(archivo_excel, sheet_name=nombre_hoja, header=None)
    # Variables para realizar un seguimiento del índice de la columna actual y de las dos filas siguientes
    indice_columna_actual = None
    perfilesTransversas = []
    perfilesTransversales = "PERFIL TRANSV."
    cont = 0
    for index, row in df.iterrows():
        if perfilesTransversales in str(row.values):
            # Obtén la lista de valores no nulos desde la columna siguiente
            indices_no_nulos = row.notna()
            # Encuentra el índice de la columna actual
            indice_columna_actual = indices_no_nulos[indices_no_nulos].index[0]
            print(indice_columna_actual)
            print(type(indice_columna_actual))

            dicTransver = {
                str(df.iloc[index + 0, indice_columna_actual + 1:].tolist()[0]): df.iloc[index + 0, indice_columna_actual + 2:].tolist(),
                str(df.iloc[index + 1, indice_columna_actual + 1:].tolist()[0]): df.iloc[index + 1, indice_columna_actual + 2:].tolist(),
                str(df.iloc[index + 2, indice_columna_actual + 1:].tolist()[0]): df.iloc[index + 2, indice_columna_actual + 2:].tolist(),
            }
            perfilesTransversas.append(pd.DataFrame(dicTransver))
            cont += cont
            # Haz algo con las filas obtenidas, por ejemplo, imprímelas
            # for i in range(len(filas_siguientes)):
            #     print("Fila siguiente 1:", str(filas_siguientes[i].tolist()[0]))
    # print(f"filas:\n {a}\n{b}\n{c}\n")
    for i in range(len(perfilesTransversas)):
        print(perfilesTransversas[i])
    print(len(perfilesTransversas))
    
    # Busca la fila que comienza con "PROGRESIVAS"
    progresivas_row = None
    for index, row in df.iterrows():
        if "PROGRESIVA" in row.values:
            progresivas_row = row
            break

    # Si se encontró la fila "PROGRESIVAS", filtra los valores no nulos desde esa posición
    if progresivas_row is not None:
        progresivas_values = progresivas_row[progresivas_row.notna()].tolist()
        return progresivas_values
    else:
        print("La etiqueta 'PROGRESIVAS' no se encontró en la hoja especificada.")
        return None

# Uso del método
# archivo_excel = 'ruta/a/tu/archivo.xlsx'
# nombre_hoja = 'nombre_de_tu_hoja'

valores_progresivas = leer_fila_desde_progresivas(path, hoja)

if valores_progresivas:
    print(f"Valores encontrados: {valores_progresivas} y de tipo {type(valores_progresivas)}")
        
