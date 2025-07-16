from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()

@app.get("/get_hello_world", operation_id="get_hello_world")
async def get_hello_world(name: str) -> str:
    return f"Hello, {name}!"

mcp = FastApiMCP(app, name="Hello world", description="Hello world")
mcp.mount()
