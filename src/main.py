from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    json = request.get_json()
    user_tag = set(json["resume"]["tags"])
    result = []
    for vacancie in json["vacancies"]:
        result.append({"id": vacancie["id"], "score": len(set(vacancie["tags"]) & user_tag)})

    return jsonify(result)

if __name__ == '__main__':
    app.run("0.0.0.0", port=5001, debug=True)
