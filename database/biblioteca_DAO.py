from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def read_biblioteca(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = "SELECT id, nome, indirizzo from BIBLIOTECA"
            cursor.execute(query)
            result= []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            return result
        else:
            print("Could Not Connect")
            return None