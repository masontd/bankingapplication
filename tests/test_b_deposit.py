from app import app

#use nonexistent ID
def test_deposit_api_endpoint_nonexistent_id():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "59483",
            "amount": "50"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#use wrongly-formatted ID
def test_deposit_api_endpoint_wrongly_formatted_id():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "594sd$/n\n8567883",
            "amount": "50"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#use wrongly-formatted amount
def test_deposit_api_endpoint_wrongly_formatted_amount():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "1hshd00"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You must enter an integer for the amount (no dollar sign)'

#use plus before amount
def test_deposit_api_endpoint_plus_before_amount():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "+40"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'Do not enter + or - before the integer.'

#use minus before amount
def test_deposit_api_endpoint_minus_before_amount():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "-40"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'Do not enter + or - before the integer.'


#no id given
def test_deposit_api_no_id():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == { "message": { "id": "You must include an id with this post request." } }
        assert response.status_code == 400

#no amount given
def test_deposit_api_no_amount():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "9306783"
        })
        json_response = response.get_json()
        assert json_response == { "message": { "amount": "You must include an amount with this post request." } }
        assert response.status_code == 400


#valid deposit for Noah Brown
def test_deposit_api_endpoint_correct():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "1075920",
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Deposit of 50 successful! Your balance is now 155.'}
        assert response.status_code == 200

#too high deposit for Noah Brown
def test_deposit_api_endpoint_amount_too_high():
    with app.test_client() as c:
        response = c.post('/api/Deposit', json={
            "id": "7529366",
            "amount": "10001"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot deposit more than $10,000 in a single transaction.'


def test_chain_deposit():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 6096.'}
        assert response.status_code == 200

        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "5000"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Deposit of 5000 successful! Your balance is now 11096.'}
        assert response.status_code == 200

        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 11096.'}
        assert response.status_code == 200

        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "10001"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot deposit more than $10,000 in a single transaction.'

        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 11096.'}
        assert response.status_code == 200
    