import requests
import pytest

@pytest.mark.api
class TestUserCreditRequest:
    def test_user_credit_request(self):
        login_admin_response = requests.post(
            url='http://localhost:4111/api/auth/token/login',
            json={
                "username": "admin",
                "password": "123456"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_admin_response.status_code == 200
        token = login_admin_response.json()["token"]

        create_user_response = requests.post(
            url='http://localhost:4111/api/admin/create',
            json={
                "username": "Max1",
                "password": "Pas!sw0rd",
                "role": "ROLE_CREDIT_SECRET"
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {token}'
            }
        )

        assert create_user_response.status_code == 200
        assert create_user_response.json()["username"] == "Max1"
        assert create_user_response.json()["role"] == "ROLE_CREDIT_SECRET"

        login_user_response = requests.post(
            url='http://localhost:4111/api/auth/token/login',
            json={
                "username": "Max1",
                "password": "Pas!sw0rd"
            },
            headers={
                "Content-Type": "application/json",
                "accept": "application/json"
            }
        )

        assert login_user_response.status_code == 200
        token = login_user_response.json()["token"]

        create_account_response = requests.post(
            url='http://localhost:4111/api/account/create',
            headers={
                "Content-Type": "application/json",
                'Authorization': f'Bearer {token}'
            }
        )

        assert create_account_response.status_code == 201
        assert create_account_response.json()["balance"] == 0
        account_id = create_account_response.json()["id"]

        credit_request_response = requests.post(
            url='http://localhost:4111/api/credit/request',
            json={
                "accountId": account_id,
                "amount": 5000,
                "termMonths": 12
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {token}',
                "accept": "application/json"
            }
        )

        assert credit_request_response.status_code == 201
        assert credit_request_response.json()["amount"] == 5000
        assert credit_request_response.json()["termMonths"] == 12