from database.create_table import create_table
from fastapi import FastAPI
from features.auth.routes import router as authetication_router
app= FastAPI()
create_table()
app.include_router(authetication_router)