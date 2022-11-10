import pymysql
import time

class DataBase:
    def __init__(self):
        pass

    def tiempo_sincronizacion(self, puerto):
        contador = 0
        for x in range(10):
            st = time.process_time()
            self.connection = pymysql.connect(
                host='localhost',
                port=puerto,
                user='root',
                password='',
            )

            self.cursor = self.connection.cursor()
            print('Conexión establecida con éxito')
            et = time.process_time()
            tiempo_ejecucion = et - st
            contador += tiempo_ejecucion
            print('Tiempo de ejecución tardado:{0:.20g}'.format(tiempo_ejecucion))
            self.connection.close()
            print('')

        promedio= contador /10
        print('Promedio de tiempo de sincronización:{0:.20g}'.format(promedio))
        print('')
        print('')
        print('')

    def tiempo_consulta(self,puerto, db, tabla):
      contador = 0
      for x in range(10):
        st = time.process_time()
        self.connection = pymysql.connect(
            host='localhost',
            port=puerto,
            user='root',
            password='',
        )

        self.cursor = self.connection.cursor()
        try:
          query = 'USE '+db+';'
          self.cursor.execute(query)
          query = 'SELECT * FROM '+tabla+';'          
          self.cursor.execute(query)
          cosulta = self.cursor.fetchall()
          print(cosulta)
          pass
        except Exception as e:
          raise
        et = time.process_time()
        tiempo_ejecucion = et - st
        contador += tiempo_ejecucion
        print(x)
        print('Tiempo de ejecución tardado:{0:.20g}'.format(tiempo_ejecucion))
        self.connection.close()
        print('')

      promedio= contador /10
      print('Promedio de tiempo de sincronización:{0:.20g}'.format(promedio))
      print('')
      print('')
      print('')

    def tiempo_latencia(self,puerto):
        contador = 0
        for x in range(10):
            st = time.process_time()
            self.connection = pymysql.connect(
                host='localhost',
                port=puerto,
                user='root',
                password='',
            )

            self.cursor = self.connection.cursor()
            try:
                query = 'CREATE DATABASE prueba_latencia;'
                self.cursor.execute(query)
                query = 'USE prueba_latencia;'          
                self.cursor.execute(query)
                query = 'CREATE TABLE tabla_prueba (nombre VARCHAR(30) NOT NULL PRIMARY KEY, valor INT) engine=ndb;'
                self.cursor.execute(query)
                for i in range(5):
                    query = 'INSERT INTO tabla_prueba VALUES ("'+str(i)+'", '+str(i)+');'
                    self.cursor.execute(query)
                    cosulta = self.cursor.fetchall()
                    print(cosulta)
                    pass
            except Exception as e:
                raise
            et = time.process_time()
            tiempo_ejecucion = et - st
            contador += tiempo_ejecucion
            print(x)
            print('Tiempo de ejecución tardado:{0:.20g}'.format(tiempo_ejecucion))
            query = 'DROP DATABASE prueba_latencia;'
            self.cursor.execute(query)
            self.connection.close()
            print('')

        promedio= contador /10
        print('Promedio de tiempo de sincronización:{0:.20g}'.format(promedio))
        print('')
        print('')
        print('')

db = DataBase()
db.tiempo_sincronizacion(3306)
db.tiempo_consulta(3306, 'ndbinfo', 'logspaces')
db.tiempo_latencia(3306)