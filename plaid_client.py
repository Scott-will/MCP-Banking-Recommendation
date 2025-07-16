import os
import plaid
from dotenv import load_dotenv
from plaid.api import plaid_api

load_dotenv()

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': os.getenv("PLAID_CLIENT_ID"),
        'secret': os.getenv("PLAID_SECRET"),
    }
)
api_client = plaid.ApiClient(configuration)
api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = 'CERT_NONE'
client = plaid_api.PlaidApi(api_client)
