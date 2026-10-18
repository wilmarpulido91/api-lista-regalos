# Funcion para formatear la respuesta en JSON #
def toJSON(fields, data):
    column_list = []
    jsonData_list = []

    for i in fields:
        column_list.append(i[0])

    for row in data:
        data_dict = {}
        for i in range(len(column_list)):
            data_dict[column_list[i]] = row[i]
        jsonData_list.append(data_dict)
    
    return jsonData_list