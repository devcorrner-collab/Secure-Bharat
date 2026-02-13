import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VT_API_KEY = os.getenv("VT_API_KEY")
    MONGO_URI = os.getenv("MONGO_URI")
    
    # Agar key nahi mili to error
    if not VT_API_KEY:
        print(" Warning: VirusTotal API Key missing!")
    if not MONGO_URI:
        print(" Warning: MongoDB URI missing!")