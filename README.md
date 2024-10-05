# Django-Redis-Inventory-API-with-JWT-Logging-and-Tests
__________________________________________________________

This project is a RESTful API built with Django Rest Framework for managing inventory items. It uses PostgreSQL for data storage, Redis for caching, and JWT for secure authentication. The API includes logging for monitoring and debugging, along with unit tests to ensure reliable functionality.

## Features
__________________________________________________________

- User registration and authentication
- JWT-based access and refresh tokens
- CRUD operations for inventory items
- Redis caching for improved performance
- Logging for debugging and monitoring

## Technologies Used
__________________________________________________________

- Django
- Django REST Framework
- PostgreSQL
- Redis
- JWT (JSON Web Tokens)

## Installation
___________________________________________________________

### Prerequisites
___________________________________________________________
- Python 3.x
- Django
- Django REST Framework
- Redis
- PostgreSQL

### Steps to Install
___________________________________________________________

 1. Clone the repository:

   ```bash
   git clone [https://github.com/adhulyamaya/Django-Redis-Inventory-API.git](https://github.com/adhulyamaya/Django-Redis-Inventory-API.git)
  ```

2.Navigate to the project directory:
```bash
   cd Django-Redis-Inventory-API
  ```
3.Create a virtual environment 
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
4.Install the required packages:
  ```
 pip install -r requirements.txt
  ```
5.Set up the PostgreSQL database:
  ```
   Create a database for your application.
   Update the DATABASES setting in settings.py with your database credentials.
  ```
6.Run migrations to create the necessary database tables:
  ```
   python manage.py migrate
  ```
7.Start the Redis server
8.Run the Django server:
  ```
    python manage.py runserver
  ```

### API Documentation
_______________________________________________________________
1)User Registration : /api/register/
 
   ```
Method: POST
 Request Body:{
    "username": "your_username",
    "password": "your_password"
}
  ```
2) User Login: /api/login/
  ```
 Method: POST
 Request Body:{
    "username": "your_username",
    "password": "your_password"
}
  ```

3) Inventory Items
  Get All Items: /api/items/
  
  ```
  Method: GET
  ```

4) Create an Item
  Endpoint: /api/items/

```
  Method: POST
  Request Body:{
  "name": "item name ",
  "description":"hi",
  "quantity": 10,
  "unit_price": 20.5,
  "category": "hai",
  "supplier": "hai"
}
  ```
5)Get Item Details: /api/items/<item_id>/

  ```
    Method: GET
  ```
6)Update an Item
Endpoint: /api/items/<item_id>/

  ```
Method: PUT
Request Body:{
 "name": "item name updation",
 "description":"hi",
 "quantity": 10,
 "unit_price": 20.5,
 "category": "hai",
 "supplier": "hai"
}
  ```

7)Delete an Item : /api/items/<item_id>/

  ```
Method: DELETE
Response: Success message
  ```
 



















