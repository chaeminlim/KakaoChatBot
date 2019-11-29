from flask import Flask, jsonify, request

app = Flask(__name__)
"""
@app.route("/<route>", methods=["GET", "POST"])
def foo():
    pass
def test():
    data = jsonify(
    version = 1.0,
    value_list =[
        "abc",
        "def"
    ])
"""
@app.route("/", methods = ["GET"])
def main():
    return "Hello u wanna got response go to /skill"

@app.route("/test", methods=["GET", "POST"])
def test():
    data = jsonify(
    version = 1.0,
    value_list =[
        "abc",
        "def"
    ])
    return data

@app.route("/skill", methods=["POST"])
def skill():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text" : "user key:" + str(request.json['userRequest']['utterance'])
                    }
                }
            ],
            "quickReplies":[
            {
                "label":"quick reply",
                "action" : "message",
                "messageText" : "hello"
            }
            ]
        }
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
