import jsonpickle
import sqlite3

from Tienda_Mascotas_Package.Dominio.comprador import Comprador


class PersistenciaComprador:
    def connect(self):
        self.con = sqlite3.connect('la_tienda_del_yeye_comprador.sqlite')
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE COMPRADOR(nombre text, apellido text, id text primary key) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_comprador(self, comprador: Comprador):
        cursor = self.con.cursor()
        query = "insert into COMPRADOR( nombre, apellido, id) values(?,?,?)"
        cursor.execute(query, (
            str(comprador.id), comprador.nombre, comprador.apellido))
        self.con.commit()

    @classmethod
    def save_json(cls, comprador):
        text_open = open("files/" + str(comprador.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(comprador)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        comprador = jsonpickle.decode(json_gui)
        text_open.close()
        return comprador
