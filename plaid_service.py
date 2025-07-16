from datetime import date

from dateutil.relativedelta import relativedelta
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.transactions_get_request import TransactionsGetRequest

from plaid_client import client


class PlaidService:
    def __init__(self):
        public_token = ""
        try:
            print("getting public token")
            sandbox_request = SandboxPublicTokenCreateRequest(
                institution_id="ins_43",
                initial_products=[Products("transactions")]
            )
            sandbox_response = client.sandbox_public_token_create(sandbox_request)
            public_token = sandbox_response.public_token
        except Exception as e:
            print(e)
        try:
            print("getting access token")
            exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
            exchange_response = client.item_public_token_exchange(exchange_request)
            self.access_token = exchange_response.access_token
        except Exception as e:
            print(e)

    def get_transactions_last_month(self):
        today = date.today()

        start_date = today - relativedelta(months=1)
        end_date = today

        req = TransactionsGetRequest(
            access_token=self.access_token,
            start_date=start_date,
            end_date=end_date,
            options={"count": 30, "offset": 0}
        )
        response = client.transactions_get(transactions_get_request=req)
        return [t.to_dict() for t in response.transactions]


plaid_service = PlaidService()
