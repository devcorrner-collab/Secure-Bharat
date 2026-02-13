import pymongo
from datetime import datetime
from backend.config import Config

class DatabaseManager:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(Config.MONGO_URI)
            self.db = self.client["CyberBodyguardDB"]
            self.collection = self.db["scan_history"]
            print(" Database Connected")
        except Exception as e:
            print(f" DB Connection Error: {e}")
            self.collection = None

    def save_scan(self, filename, status, engines):
        if self.collection is not None:
            record = {
                "filename": filename,
                "status": status,
                "engines": engines,
                "timestamp": datetime.now()
            }
            self.collection.insert_one(record)
            print(f" Saved to History: {filename}")
