from app import app

#use nonexistent ID
def test_withdraw_api_endpoint_nonexistent_id():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "59483",
            "amount": "50"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#use wrongly-formatted ID
def test_withdraw_api_endpoint_wrongly_formatted_id():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "594sd$/n\n8567883",
            "amount": "50"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#use wrongly-formatted amount
def test_withdraw_api_endpoint_wrongly_formatted_amount():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "1hshd00"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You must enter an integer for the amount (no dollar sign)'

#use plus before amount
def test_withdraw_api_endpoint_plus_before_amount():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "+40"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'Do not enter + or - before the integer.'

#use minus before amount
def test_withdraw_api_endpoint_minus_before_amount():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "-40"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'Do not enter + or - before the integer.'


#no id given
def test_deposit_api_no_id():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == { "message": { "id": "You must include an id with this post request." } }
        assert response.status_code == 400

#no amount given
def test_deposit_api_no_amount():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "9306783"
        })
        json_response = response.get_json()
        assert json_response == { "message": { "amount": "You must include an amount with this post request." } }
        assert response.status_code == 400


#valid withdrawal for Ellen Johnson
def test_withdraw_api_endpoint_correct():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "7529366",
            "amount": "50"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 50 successful. Your balance is now 120305.'}
        assert response.status_code == 200

#over 90% withdrawal for Ellen Johnson
def test_withdraw_api_endpoint_over_90_percent():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "7529366",
            "amount": "108275"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot withdraw more than 90 percent of your account balance in a single transaction.'
        

#under $100 withdrawal for Noah Brown
def test_withdraw_api_endpoint_under_100():
    with app.test_client() as c:
        response = c.post('/api/Withdraw', json={
            "id": "1075920",
            "amount": "56"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot have less than $100 in your account at any point.'

#test chain withdrawal and deposit
def test_chain_withdrawal():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 11096.'}
        assert response.status_code == 200    


        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "400"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 400 successful. Your balance is now 10696.'}
        assert response.status_code == 200


        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 10696.'}
        assert response.status_code == 200


        response = c.post('/api/Deposit', json={
            "id": "9306783",
            "amount": "67"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Deposit of 67 successful! Your balance is now 10763.'}
        assert response.status_code == 200    


        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 10763.'}
        assert response.status_code == 200


        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "4000"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 4000 successful. Your balance is now 6763.'}
        assert response.status_code == 200


        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 6763.'}
        assert response.status_code == 200


        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "6087"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot withdraw more than 90 percent of your account balance in a single transaction.'


        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 6763.'}
        assert response.status_code == 200

        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "3664"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 3664 successful. Your balance is now 3099.'}
        assert response.status_code == 200

        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "2000"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 2000 successful. Your balance is now 1099.'}
        assert response.status_code == 200

        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "500"
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Withdrawal of 500 successful. Your balance is now 599.'}
        assert response.status_code == 200

        response = c.post('/api/Withdraw', json={
            "id": "9306783",
            "amount": "500"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'You cannot have less than $100 in your account at any point.'

        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 599.'}
        assert response.status_code == 200