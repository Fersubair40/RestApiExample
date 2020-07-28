from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(postedData, functionName):
    if (functionName == "add" or functionName == 'subtract' or functionName == 'multiply'):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200


# class Index(Resource):
#     def get(self):
#         return 'REST API'


class Add(Resource):
    def post(self):

        postedData = request.get_json()

        status_code = check_posted_data(postedData, "add")

        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code ": status_code
            }

            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x + y

        retMap = {"Message": ret, "Status Code": 200}
        return jsonify(retMap)


class Subtract(Resource):
     def post(self):

        postedData = request.get_json()

        status_code = check_posted_data(postedData, "subtract")

        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code ": status_code
            }

            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x - y

        retMap = {"Message": ret, "Status Code": 200}
        return jsonify(retMap)


class Multiply(Resource):
     def post(self):

        postedData = request.get_json()

        status_code = check_posted_data(postedData, "multiply")

        if (status_code != 200):
            retJson = {
                "Message": "An error occured",
                "Status Code ": status_code
            }

            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        ret = x * y

        retMap = {"Message": ret, "Status Code": 200}
        return jsonify(retMap)


class Divide(Resource):
    pass

# api.add_resource(Index, "/")
api.add_resource(Add, "/add")

 
@app.route("/")
def hello_world():
    return "Hello from docker World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
