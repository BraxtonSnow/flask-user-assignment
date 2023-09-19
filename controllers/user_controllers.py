from flask import jsonify, request
import json
from uuid import uuid4



def database_read():
    try:
        with open("database.json", "r") as openfile:

            return json.load(openfile)

    except:

        return []


def database_write(records):
    with open("database.json", "w") as outfile:
        json.dump(records, outfile)



def user_add():
    post_data = request.form if request.form else request.json

    user = {
        "user_id": str(uuid4()),
        "first_name": post_data["first_name"],
        "last_name": post_data["last_name"],
        "email": post_data["email"],
        "phone_number": post_data["phone_number"],
        "active": True
    }

    user_records = database_read()
    user_records.append(user)

    database_write(user_records)

    return jsonify(f"User {user['first_name']} {user['last_name']} has been added"), 201




def users_get_all():
    user_records = database_read()

    if len(user_records) == 0:

        return jsonify(f"No user records were found"), 404
    
    return jsonify(user_records), 200



def user_get_by_id(user_id):
    user_records = database_read()

    if len(user_records) == 0:

        return jsonify(f"No user records were found"), 404
    
    for user in user_records:
        if user["user_id"] == user_id:

            return jsonify(user), 200

        return jsonify(f"User with id: {user_id} not found"), 404 



def user_activity(user_id):
    user_records = database_read()

    if len(user_records) == 0:

        return jsonify(f"No user records were found"), 404
    
    for user in user_records:
        if user["user_id"] == user_id:
            user["active"] = not user["active"]

            database_write(user_records)

            if user["active"]:

                return jsonify(f"User has been activated"), 200
            
            else:

                return jsonify(f"User has been dactivated"), 200
            
    return jsonify(f"User with id: {user_id} not foune"), 404



def user_delete_by_id(user_id):
    user_records = database_read()

    if len(user_records) == 0:

        return jsonify(f"No user records were found"), 404
    
    for index, user in enumerate(user_records):
        if user["user_id"] == user_id:
            user_records.pop(index)

            database_write(user_records)

            return jsonify(f"User with user_id: {user_id} has been deleted"), 200
        
    return jsonify(f"User with user_id: {user_id} has not been found"), 404



def user_update_by_id(user_id):
    user_records = database_read()
    post_data = request.form if request.form else request.json

    if len(user_records) == 0:

        return jsonify(f"No user records were found"), 404
    
    for user in user_records:
        if user["user_id"] == user_id:

            for key in list(user.keys()):
                try:
                    user[key] = post_data[key]

                except:
                    pass

            database_write(user_records)

            return jsonify(f"User updated successfully"), 200
        
    return jsonify(f"No user records were found"), 404



