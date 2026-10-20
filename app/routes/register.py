from flask import jsonify, request
from app import api
from app import mysql
from app.functions import functions

# Crear un nuevo registro #
@api.route("/register", methods=["POST"])
def create_register():
    conection = mysql.connect()
    cursor = conection.cursor()

    data = request.json
    guest = data.get('idGuest')
    gift = data.get('idGift')

    try :
        sql = "INSERT INTO registro (idRegistro, IdAsistente, idRegalo) VALUES (NULL, %s, %s)"
        cursor.execute(sql, (guest, gift))
        conection.commit()

        return jsonify({"code": 200, "message": "Registro creado con exito"}), 200
    except conection.Error as error :
        return jsonify({"code": 500, "error": str(error)}), 500
    finally :
        cursor.close()
        conection.close()