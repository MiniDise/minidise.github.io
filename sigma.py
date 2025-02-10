from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from datetime import datetime
import csv
import json

app = Flask(__name__)
CORS(app)

@app.route("/balls", methods=['POST','GET'])
def balls():

    if request.method == 'GET':

        with open('sigma.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            lst = []
            for row in reader:
                lst.append({"name": row["name"], "msg": row["msg"], "date":row["date"]})

            return jsonify(lst)


    elif request.method == 'POST': 
        print(request.get_json())
        with open("sigma.csv", "a", newline="") as file:
            data = request.get_json()
            fieldnames = ["name", "msg", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            writer.writerow(data)
        return redirect("file:///C:/Users/minir/Desktop/sigma/sigma.html")



if __name__ == "__main__":
    app.run(debug=True)