import pymongo
import certifi
from datetime import datetime
from backend.config import Config

class DatabaseManager:
    def __init__(self):
        try:
            # SSL Error fix karne ke liye 'tlsCAFile' add kiya hai
            self.client = pymongo.MongoClient(
                Config.MONGO_URI,
                serverSelectionTimeoutMS=5000,
                tlsCAFile=certifi.where()
            )
            self.db = self.client["CyberBodyguardDB"]
            self.collection = self.db["scan_history"]
            
            # Connection Check
            self.client.admin.command('ping')
            print("✅ Database Connected Successfully")
        except Exception as e:
            print(f"❌ DB Connection Error: {e}")
            self.collection = None

    def save_scan(self, filename, status, engines):
        if self.collection is not None:
            record = {
                "filename": filename,
                "status": status,
                "engines": engines,
                "timestamp": datetime.now()
            }
            try:
                self.collection.insert_one(record)
                print(f"💾 Saved to History: {filename}")
            except Exception as e:
                print(f"⚠️ Save Error: {e}")