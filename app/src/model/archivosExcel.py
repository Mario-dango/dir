# -*- coding: utf-8 -*-
##### LIBRERIAS Y DEPENDENCIAS NECESARIAS PARA LA CLASE #####
import pandas as pd
import os, sys
################################################################

class ExcelModel():
    
    def __init__ (self, parent=None):
        self.pathToLoad = "../../resources/data/loadData/"
        self.pathToSave = "../../resources/data/saveData/"
        self.path = None
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
                # print("Datos leidos correctamente")
                pass
        finally:
            self.data = datos
            return datos
        
    def guardarData (self, nombre_archivo, data):
        try:
            if os.path.isfile(nombre_archivo):
                # Si el archivo existe, cargar los datos existentes
                self.data_existente = pd.read_excel(nombre_archivo)
                
                # Agregar los nuevos datos al DataFrame existente
                self.data_nuevo = pd.concat([self.data_existente, data], ignore_index=True)
                
                # Guardar el DataFrame actualizado en el archivo Excel
                with pd.ExcelWriter(nombre_archivo, engine='openpyxl', mode='a') as writer:
                    self.data_nuevo.to_excel(writer, index=False, sheet_name='Hoja1', startrow=len(self.data_existente)+1)
            else:
                # Si el archivo no existe, crear uno nuevo y guardar los datos
                self.data_nuevo = pd.DataFrame(data)
                self.data_nuevo.to_excel(nombre_archivo, index=False, sheet_name='Hoja1')
        
        except Exception as e:
            print(f"Error al guardar los datos en el archivo Excel: {e}")


## CLASE DEFINIDA DEL MODELO DE PLANILLA ##
class PlanillaModel():
    def __init__(self, parent=None):        
        self.pathToLoad = "../../resources/data/loadData/"
        self.pathToSave = "../../resources/data/saveData/"
        self.path = None
        self.data = None
        self.dataLongitudinal = pd.DataFrame()
        self.dataTransversal = []
        self.dataGeneral = None
        
        
        
    def leerFilaDesde(self, nombreFila):
        # Busca la fila que comienza con "PROGRESIVAS"
        filaTarget = None
        for index, row in self.data.iterrows():
            if nombreFila in row.values:
                filaTarget = row
                break

        # Si se encontró la fila "PROGRESIVAS", filtra los valores no nulos desde esa posición
        if filaTarget is not None:
            filaValor = filaTarget[filaTarget.notna()].tolist()
            filaValor.pop(0)
            return filaValor[1:]
        else:
            print(f"La etiqueta '{filaTarget}' no se encontró en la hoja especificada.")
            return None

        
    def leerData(self, nombre_archivo, sheet_name=None):
        try:
            self.data = pd.read_excel(nombre_archivo, sheet_name=sheet_name)
        except:
            print("No se pudo leer el archivo de la ruta: %s" % nombre_archivo)
            self.data = None
        else:
            if self.data is not None:
                # print("Datos leidos correctamente")
                progresivaLista = self.leerFilaDesde("PROGRESIVA")
                cotaTerrenoLista = self.leerFilaDesde("COTA DE TERRENO")
                cotaProyectoLista = self.leerFilaDesde("COTA DE PROYECTO")
                diferenciaCotasLista = self.leerFilaDesde("DIFERENCIA DE COTA")
                pendienteLista = self.leerFilaDesde("PENDIENTE")
                dataLong = {
                    "Progresivas": progresivaLista, 
                    "Cota de Terreno": cotaTerrenoLista,
                    "Cota de Proyecto": cotaProyectoLista,
                    "Diferencia de Cotas": diferenciaCotasLista,
                    "Pendiente": pendienteLista
                    }
                ## Muestro las longitudes de los valores del diccionario dataLong
                for clave, valor in dataLong.items():
                    if isinstance(valor, (list, str)):  # Verifica si el valor es una lista o una cadena
                        longitud_elemento = len(valor)
                        # print(f"Longitud del elemento en la clave '{clave}': {longitud_elemento}")
                ## Muestro las longitudes de los valores del diccionario dataLong
                long = 0
                for clave, valor in dataLong.items():
                    if isinstance(valor, (list, str)):  # Verifica si el valor es una lista o una cadena
                        longitud_elemento = len(valor)
                        if clave == "Progresivas":
                            long = longitud_elemento
                        elif longitud_elemento != long:
                            for i in range(longitud_elemento, long):
                                dataLong[clave].append(0)
                ## Muestro las longitudes de los valores del diccionario dataLong
                for clave, valor in dataLong.items():
                    if isinstance(valor, (list, str)):  # Verifica si el valor es una lista o una cadena
                        longitud_elemento = len(valor)
                        # print(f"Longitud del elemento en la clave '{clave}': {longitud_elemento}")
                ## Muestro las longitudes de los valores del diccionario dataLong
                ## Seteo el atributo dataLongitudinal con la nueva estructura de DataFrame desde el diccionario formateado
                self.dataLongitudinal = pd.DataFrame(dataLong)
                
                # Variables para realizar un seguimiento del índice de la columna actual y de las dos filas siguientes
                indice_columna_actual = None
                perfilesTransversales = "PERFIL TRANSV."
                cont = 0
                for index, row in self.data.iterrows():
                    if perfilesTransversales in str(row.values):
                        # Obtén la lista de valores no nulos desde la columna siguiente
                        dicTransver = {
                            str(self.data.iloc[index + 0, 1:].tolist()[0]): self.data.iloc[index + 0, 2:].tolist(),
                            str(self.data.iloc[index + 1, 1:].tolist()[0]): self.data.iloc[index + 1, 2:].tolist(),
                            str(self.data.iloc[index + 2, 1:].tolist()[0]): self.data.iloc[index + 2, 2:].tolist(),
                        }
                        self.dataTransversal.append(pd.DataFrame(dicTransver))
                        cont += cont          
        finally:
            print("Fin de lectura")
        
        
    def guardarData (self, nombre_archivo, data):
        try:
            if os.path.isfile(nombre_archivo):
                # Si el archivo existe, cargar los datos existentes
                self.data_existente = pd.read_excel(nombre_archivo)
                
                # Agregar los nuevos datos al DataFrame existente
                self.data_nuevo = pd.concat([self.data_existente, data], ignore_index=True)
                
                # Guardar el DataFrame actualizado en el archivo Excel
                with pd.ExcelWriter(nombre_archivo, engine='openpyxl', mode='a') as writer:
                    self.data_nuevo.to_excel(writer, index=False, sheet_name='Hoja1', startrow=len(self.data_existente)+1)
            else:
                # Si el archivo no existe, crear uno nuevo y guardar los datos
                self.data_nuevo = pd.DataFrame(data)
                self.data_nuevo.to_excel(nombre_archivo, index=False, sheet_name='Hoja1')
        
        except Exception as e:
            print(f"Error al guardar los datos en el archivo Excel: {e}")
