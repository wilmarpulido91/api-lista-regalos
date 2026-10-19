from flask import jsonify, request
from app import api
from app import mysql
from app.functions import functions

# Obtener todos los invitados #
@api.route("/guests", methods=["GET"])
def get_guests():
    conection = mysql.connect()
    cursor = conection.cursor()

    try:
        sql = "SELECT * FROM asistentes"
        cursor.execute(sql)

        if cursor.execute(sql) > 0 :
            conection.commit()
            data = cursor.fetchall()
            fields = cursor.description
            return jsonify({"code": 200, "guests": functions.toJSON(fields, data)}), 200
        else :
            return jsonify({"code": 201, "message": "No hay invitados en la base de datos"}), 201
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally:
        cursor.close()
        conection.close()

# Actualizar un invitado por su ID #
@api.route("/guest/<int:id_guest>", methods=["PUT"])
def edit_guest(id_guest):
    conection = mysql.connect()
    cursor = conection.cursor()

    block = 1

    try :
        sql = "UPDATE asistentes SET bloqueado = %s WHERE idAsistente = %s"
        cursor.execute(sql, (block, id_guest))
        conection.commit()

        return jsonify({"code": 200, "message": "Invitado actualizado con exito"}), 200
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally :
        cursor.close()
        conection.close()