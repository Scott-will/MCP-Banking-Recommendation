from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from plaid_service import plaid_service

app = FastAPI()

@app.get("/get_hello_world", operation_id="get_hello_world")
async def get_hello_world(name: str) -> str:
    return f"Hello, {name}!"

@app.get("/last_month_transactions", operation_id="last_month_transactions")
async def get_last_month_transactions():
    transactions = plaid_service.get_transactions_last_month()
    return transactions

mcp = FastApiMCP(app, name="Hello world", description="Hello world")
mcp.mount()
