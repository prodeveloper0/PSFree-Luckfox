import os
import logging

import click

from pathlib import Path

from flask import Flask, send_from_directory, jsonify


app = Flask(__name__)

current_files_dir = Path(os.getcwd())
static_files_dir = current_files_dir / "PSFree"
exclude_path = ["", "index.html", "favicon.ico"]


@app.route("/api/<path:path>", methods=["GET"])
def read_api_routes(path: str):
    return jsonify({"path": path})


@app.route("/<path:path>", methods=["GET"])
@app.route("/", methods=["GET"])
def catch_all_routes(path: str = ""):
    if path == "":
        path = "index.html"
    file_path = (current_files_dir if path in exclude_path else static_files_dir) / path
    return send_from_directory(file_path.parent, file_path.name)


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to run the server on")
@click.option("--port", default=9191, help="Port to run the server on")
@click.option("--debug", is_flag=True, help="Enable debug mode")
def main(host: str, port: int, debug: bool):
    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    main()
