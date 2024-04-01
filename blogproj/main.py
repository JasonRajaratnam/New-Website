import asyncio
import subprocess
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    # Run the Django development server as a subprocess
    asyncio.create_task(run_django_server())


async def run_django_server():
    # Adjust the path to your Django project's manage.py file
    manage_py_path = "path/to/your/manage.py"

    # Run the Django development server using subprocess
    process = await asyncio.create_subprocess_exec(
        "python", manage_py_path, "runserver", "127.0.0.1:8000",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    # Wait for the process to finish
    await process.communicate()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
