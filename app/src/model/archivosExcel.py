import pandas as pd
import os, sys

class ExcelModel():
    
    def __init__ (self, parent=None):
        self.pathToLoad = "../../resources/data/loadData/"
        self.pathToSave = "../../resources/data/saveData/"
        self.data = None
        self.dataGeneral = None
        
    def leerData(self, nombre_archivo):
        datos = None
        try:
            datos = pd.read_csv(nombre_archivo)
        except:
            print("No se pudo leer el archivo de la ruta: %s" % nombre_archivo)
            datos = None
        else:
            if datos is not None:
                print("Datos leidos correctamente")
        finally:
            self.data = datos
            return datos
        
    def guardarData (self, nombre_archivo, data):
        try:
            if os.path.isfile(nombre_archivo):
                # Si el archivo existe, cargar los datos existentes
                df_existente = pd.read_excel(nombre_archivo)
                
                # Agregar los nuevos datos al DataFrame existente
                df_nuevo = pd.concat([df_existente, data], ignore_index=True)
                
                # Guardar el DataFrame actualizado en el archivo Excel
                with pd.ExcelWriter(nombre_archivo, engine='openpyxl', mode='a') as writer:
                    df_nuevo.to_excel(writer, index=False, sheet_name='Hoja1', startrow=len(df_existente)+1)
            else:
                # Si el archivo no existe, crear uno nuevo y guardar los datos
                df_nuevo = pd.DataFrame(data)
                df_nuevo.to_excel(nombre_archivo, index=False, sheet_name='Hoja1')
        
        except Exception as e:
            print(f"Error al guardar los datos en el archivo Excel: {e}")
