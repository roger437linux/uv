from flask import Flask, jsonify
import app.api as api

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(api.sos())


def main():
    app.run(host="0.0.0.0", port="8080", debug=True)


if __name__ == "__main__":
    main()
