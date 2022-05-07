from criptos import app
import requests
from config import MONEDAS, ENDPOINT, API_KEY
#from errores import APIError
import sqlite3

"""class Gestiona_Cambio():
    def __init__(self, moneda_from, moneda_to):
        self.moneda_from = moneda_from
        self.moneda_to = moneda_to
        self.tasa_cambio = 0.0

    def solicita_operacion(self):
        self.respuesta = requests.get(ENDPOINT.format(self.moneda_from, self.moneda_to,API_KEY))
        if self.respuesta.status_code != 200:
            raise APIError(self.respuesta.json()["error"])
        else:    
            tasa_cambio = self.respuesta.json()["rate"]            
            return tasa_cambio

    #Comprueba si ambas monedas son iguales
    def monedas_iguales(self):
        if self.moneda_from == self.moneda_to:
            condicion1 = False
            return condicion1
        else:
            condicion1 = True
            return condicion1

    #Comprueba si hay saldo en la base de datos
    def divisaFromSaldo(self):
        if self.moneda_from != "EUR":
            pass #Lanza consulta de bbdd para ver si hay saldo -> sum movimientos moneda_to - sum movimientos moneda_from
            #condicion2
            #return condicion2
        else:
            condicion2 = True
            return condicion2

    def ejecutaApi(self):
        if (self.monedas_iguales() and self.divisaFromSaldo()):
            pass
"""        

#Gestión de la base de datos
#     
class Gestiona_Datos():
    def __init__(self, file=":memory:"):
        self.base_datos = file

    def genera_dic(self, cursor):
        filas = cursor.fetchall()

        campos = []
        for item in cursor.description:
            campos.append(item[0])

        resultado = []

        for fila in filas:
            registro = {}

            for clave, valor in zip(campos, fila):
                registro[clave] = valor
            
            resultado.append(registro)
        return resultado

    def resultados(self, cursor, con):
        if cursor.description:
            resultado = self.genera_dic(cursor)
        else:
            resultado = None
            con.commit()
        return resultado

    def realiza_consulta(self, consulta, parametros = []):
        con = sqlite3.connect(self.base_datos)
        cursor = con.cursor()

        cursor.execute(consulta, parametros)
        resultado = self.resultados(cursor, con)

        con.close()

        return resultado

    #Extrae todos los movimientos de la base de datos
    def todos_movimientos(self):
        return self.realiza_consulta("""
                                        SELECT date, time, moneda_from, cantidad_from, moneda_to, cantidad_to
                                        FROM movimientos
                                        ORDER BY date
                                    """
                                    )

    #Consulta saldo para balance y para ver saldo disponible
    def consulta_saldo_from(self, moneda):
        return self.realiza_consulta("""
                                        SELECT SUM(cantidad_from)
                                        FROM movimientos
                                        WHERE moneda_from = ? 
                                    """, [moneda,])
    
    #Consulta saldo para balance
    def consulta_saldo_to(self, moneda):
        return self.realiza_consulta("""
                                        SELECT SUM(cantidad_to)
                                        FROM movimientos
                                        WHERE moneda_to = ? 
                                    """, (moneda,))       



    

   

    


