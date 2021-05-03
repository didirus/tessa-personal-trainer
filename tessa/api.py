from flask import Flask, Response, request, make_response

from tessa.main import main

app = Flask(__name__)


@app.route('/')
def health():
    return 'ok'


@app.route("/start", methods=["POST"])
def start_day():
    main()
