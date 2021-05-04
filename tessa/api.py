from flask import Flask, Response, request, make_response

from tessa.main import main

app = Flask(__name__)


@app.route('/')
def health():
    return 'ok'


@app.route("/start", methods=["POST"])
def start_day():
    main()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
