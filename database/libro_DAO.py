from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def read_libri(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        result=[]
        query= """SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca from LIBRO
                WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
                AND genere = COALESCE(%s, genere)"""
        if cnx is not None:
            cursor = cnx.cursor()
            cursor.execute(query, (id_biblioteca, genere))

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
            return result
        else:
            print("Could Not Connect")
            return None