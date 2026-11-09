from fastapi import FastAPI, HTTPException, status
from models import VehicleCreate, VehicleUpdate
from database import get_connection
import mysql.connector


app = FastAPI()

@app.get("/")

def home():
    return {"message" : "Vehicle API is running"}

@app.get("/vehicles")
def get_vehicles():
    connection = None 
    cursor = None 
    result = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary = True)

        cursor.execute("SELECT * FROM vehicles")

        result = cursor.fetchall()
    
    except mysql.connector.Error:
        raise HTTPException(
            status_code = 500,
            detail = 'Database error'
        )
    
    finally:
        if cursor:
            cursor.close()
        
        if connection and connection.is_connected():
            connection.close()

    return result
    

@app.post("/vehicles", status_code=status.HTTP_201_CREATED)
def add_vehicles(vehicle: VehicleCreate):
    connection = None 
    cursor = None 

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """INSERT INTO vehicles(id, brand, model, year)
        VALUES(%s, %s, %s, %s)"""

        values = (
            vehicle.id, 
            vehicle.brand,
            vehicle.model, 
            vehicle.year
        )

        cursor.execute(query, values)
        connection.commit()
    
    except mysql.connector.Error:
        raise HTTPException(
            status_code = 500, 
            detail = 'Database error'
        )
    
    finally:
        if cursor:
            cursor.close()
        
        if connection and connection.is_connected():
            connection.close()

    return {"message": "Vehicle added successfully"}

@app.put("/vehicles/{vehicle_id}")
def update_vehicle(vehicle_id: int, updated_vehicle: VehicleUpdate):
    connection = None 
    cursor = None 
    updated = None 

    try:

        connection = get_connection()
        cursor = connection.cursor()

        query = """UPDATE vehicles SET brand=%s, model=%s, year=%s
        WHERE id=%s"""

        values = (
            updated_vehicle.brand,
            updated_vehicle.model,
            updated_vehicle.year,
            vehicle_id,
        )

        cursor.execute(query, values)
        connection.commit()

        updated = cursor.rowcount

    except mysql.connector.Error:
        raise HTTPException(
            status_code = 500, 
            detail = 'Database error'
        )
    
    finally:

        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
        
        if updated == 0:
            raise HTTPException(
                status_code = 404,
                detail = 'Vehicle not found'
            )
        
    return {"message": "Vehicle updated successfully"}

@app.delete("/vehicles/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    connection = None 
    cursor = None 
    deleted = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """DELETE FROM vehicles WHERE id = %s"""

        cursor.execute(query, (vehicle_id,))
        connection.commit()

        deleted = cursor.rowcount
    

    except mysql.connector.Error:
        raise HTTPException(
            status_code = 500,
            detail = 'Database error'
        )
    
    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

        if deleted == 0:
            raise HTTPException(
                status_code = 404,
                detail = 'Vehicle not found'
            )
        
    return {"message": "Vehicle deleted successfully"}


    

   

