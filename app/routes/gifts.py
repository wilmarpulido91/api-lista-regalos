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
            return jsonify({"code": 200, "users": functions.toJSON(fields, data)}), 200
        else :
            return jsonify({"code": 201, "message": "No hay usuarios en la base de datos"}), 201
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally:
        cursor.close()
        conection.close()