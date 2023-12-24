from app import app

def test_post_api_endpoint_correct():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "1075920",
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Deposit of 50 successful! Your balance is now 155.'}
        assert response.status_code == 200


def test_post_api_endpoint_wrong_id():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "59483",
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'id not found.'}
        assert response.status_code == 200

def test_post_api_endpoint_amount_too_high():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "7529366",
            "amount": "10001"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'You cannot deposit more than $10,000 in a single transaction.'}
        assert response.status_code == 200



#include ID
#include amount
#send wrongly formatted data
        
        