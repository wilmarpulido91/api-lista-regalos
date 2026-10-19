from flask import jsonify, request
from app import api
from app import mysql
from app.functions import functions

# Obtener todos los usuarios #
@api.route("/gifts", methods=["GET"])
def get_gifts():
    conection = mysql.connect()
    cursor = conection.cursor()

    try:
        sql = "SELECT * FROM regalos"
        cursor.execute(sql)

        if cursor.execute(sql) > 0 :
            conection.commit()
            data = cursor.fetchall()
            fields = cursor.description
            return jsonify({"code": 200, "gifts": functions.toJSON(fields, data)}), 200
        else :
            return jsonify({"code": 201, "message": "No hay regalos en la base de datos"}), 201
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally:
        cursor.close()
        conection.close()

# Actualizar un usuario por su ID #
@api.route("/gift/<int:id_gift>", methods=["PUT"])
def edit_gift(id_gift):
    conection = mysql.connect()
    cursor = conection.cursor()

    block = 1

    try :
        sql = "UPDATE regalos SET bloqueado = %s WHERE idRegalo = %s"
        cursor.execute(sql, (block, id_gift))
        conection.commit()

        return jsonify({"code": 200, "message": "Regalo actualizado con exito"}), 200
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally :
        cursor.close()
        conection.close()