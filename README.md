This Python Flask API simulates transactions of open bank accounts, and includes tests of these functionalities using PyTest.

There are restrictions to these transactions:
- A user can deposit and withdraw money from account
- An account cannot have less than $100 at any time in an account
- A user cannot withdraw more than 90% of their total balance from an account in a
single transaction.
- A user cannot deposit more than $10,000 in a single transaction.

Three open accounts are specified using in-memory data structures in app.py, where the endpoints and server-side logic of the application are defined. To properly interact with this application, you will have to specify these accounts in your API requests.

To run this application and its tests, proceed as follows -

Steps:
Run Docker Desktop
Clone this repository onto your machine and navigate to its directory.
Run the command "docker-compose up"

Two things will then happen:
1. The PyTest tests will execute in alphabetical order by file in the tests directory. Each file corresponds to a unique endpoint (specified in app.py). Within each file, you can read the comments above each test for information about what each test does. The output will be displayed in the command line as dots next to each of the test files (a dot represents successful test execution).
2. The server will begin running on port 5000 of your machine, which you can then interact with using applications like Postman. Here are the endpoints and their expected payloads:

http://localhost:5000/api/getBalance

{
    "id": ""
}


http://localhost:5000/api/Deposit

{
    "id": "", "amount": ""
}


http://localhost:5000/api/Withdraw

{
    "id": "", "amount": ""
}

Where id is a unique user ID specified in the data dictionary in app.py, and amount is a raw integer corresponding to a monetary value.

When you are finished, make sure to ctrl/command-c your way out of the application and then type "docker-compose down".

