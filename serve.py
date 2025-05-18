import os
import click
import uvicorn

from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()
virtual_root_path = "PSFree"
exclude_path = ["", "index.html", "favicon.ico"]


virtual_static_files_dir = Path(os.getcwd()) / virtual_root_path
current_static_files_dir = Path(os.getcwd())


@app.post("/api/{path:path}")
def post_api_root(path: str):
    return "Hello, world"


@app.get("/api/{path:path}")
def get_api_root(path: str):
    return "Hello, world"


@app.get("/{path:path}")
def get_root(path: str):
    path = "index.html" if not path else path

    file_path = (current_static_files_dir / path) if path in exclude_path else (virtual_static_files_dir / path)
    
    if file_path.exists() and file_path.is_file():
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}, 404


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to run the server on.")
@click.option("--port", default=9191, help="Port to run the server on.")
def main(host: str, port: int):
    uvicorn.run(app, host=host, port=port, loop="uvloop")


if __name__ == "__main__":
    main()
