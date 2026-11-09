Vehicle API
A RESTful API for managing vehicle data, built with Python, FastAPI, MySQL and Docker Compose.

Overview
This project provides an API to create, retrieve, update and delete vehicle records stored in a MySQL database.
The application is containerized with Docker Compose, allowing the API and database to run in separate containers.

Technologies
- Python 3.11
- FastAPI
- REST API
- MySQL 8.0
- Docker
- Docker Compose
- Pydantic
- mysql-connector-python

Project Structure

vehicle-api/
│
├── app/
│   ├── create_db.sql
|   ├── database.py
│   ├── main.py
|   ├── models.py
│   
├── requirements.txt
├── dockerfile
├── docker-compose.yml
├── .env
├── .dockerignore
├── .gitignore
└── README.md

Features

- Create new vehicle records
- Retrieve all vehicles
- Update existing vehicle records
- Delete vehicle records
- Validate input data with Pydantic
- Connect to a MySQL database
- Run the application using Docker Compose

Getting Started

Prerequisites
- Docker
- Docker Compose


Configuration

Create a .env file in the project root directory:

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=vehicle_db
MYSQL_PORT=3306

Replace your_password with your own MySQL password.

Run the Application

Build and start the containers:
docker compose up --build -d

The API will be available at:
http://localhost:8000

Interactive API documentation:
http://localhost:8000/docs

Stop the Application
docker compose down

API Endpoints
Method	      Endpoint	        Description
GET	              /	            Check API status
GET	          /vehicles	        Retrieve all vehicles
POST	        /vehicles	        Create a vehicle
PUT	    /vehicles/{vehicle_id}	Update a vehicle
DELETE	/vehicles/{vehicle_id}	Delete a vehicle

Example Vehicle
{
  "id": 1,
  "brand": "Volkswagen",
  "model": "Golf",
  "year": 2023
}

Learning Objectives

This project was developed to gain practical experience with:
- Building REST APIs with FastAPI
- Working with relational databases and SQL
- Connecting Python applications to MySQL
- Containerizing applications with Docker
- Managing multiple services with Docker Compose
