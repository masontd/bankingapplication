from app import app

#use nonexistent ID
def test_getBalance_api_endpoint_nonexistent_id():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "59483"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#use wrongly-formatted ID
def test_getBalance_api_endpoint_wrongly_formatted_id():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "594sd$/n\n8567883"
        })
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'id not found'

#get balance for Noah Brown
def test_getBalance_api_endpoint_NoahBrown_id():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "1075920",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Noah Brown! Your balance is 105.'}
        assert response.status_code == 200

#get balance for Brent Henry
def test_getBalance_api_endpoint_BrentHenry_id():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "9306783",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Brent Henry! Your balance is 6096.'}
        assert response.status_code == 200

#get balance for Ellen Johnson
def test_getBalance_api_endpoint_EllenJohnson_id():
    with app.test_client() as c:
        response = c.get('/api/getBalance', json={
            "id": "7529366",
        })
        json_response = response.get_json()
        assert json_response == {'message': 'Hello, Ellen Johnson! Your balance is 120355.'}
        assert response.status_code == 200