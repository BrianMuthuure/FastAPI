import time
from typing import Optional, List
import psycopg2
from fastapi import FastAPI, Response, status, HTTPException, Depends
from psycopg2.extras import RealDictCursor
import models
from database import engine
from routers import posts, users, auth

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='Brian6894',
            cursor_factory=RealDictCursor  # gives you the column names
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print(" Connecting to database failed")
        print("Error", error)
        time.sleep(2)


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)