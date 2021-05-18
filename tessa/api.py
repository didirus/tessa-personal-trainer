from flask import Flask, Response, request, make_response
import os

from tessa.utils import logger
from tessa.main import main

app = Flask(__name__)


@app.route('/')
def health():
    return 'ok'


@app.route("/start", methods=["POST"])
def start_day():
    logger.debug("Starting personal trainer...")

    config = request.files["cfg"].read().decode('utf-8')
    main(config)
    return Response("")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
