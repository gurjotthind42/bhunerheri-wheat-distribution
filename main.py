from fastapi import FastAPI
from scheduler import start_scheduler
from scraper import get_all_fps_data
from database import get_wheat_data
from fastapi.middleware.cors import CORSMiddleware
from scraper import refresh_fps_data

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/api/wheat")
def fetch_data():
     return get_all_fps_data()
    
@app.get("/api/refresh")
def refresh_data():
    refresh_fps_data()
    return {"status": "Data refreshed"}
    
