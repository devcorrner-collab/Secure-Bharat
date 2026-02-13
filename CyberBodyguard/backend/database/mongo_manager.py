import pymongo
from datetime import datetime
from ..config import Config

import pymongo
from datetime import datetime
from backend.config import Config

class MongoManager:
    def __init__(self):
        try:
            # Connection banao
            self.client = pymongo.MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
            self.db = self.client["CyberBodyguardDB"]
            self.collection = self.db["scan_history"]
            
            # Check connection (Ping karo)
            self.client.server_info()
            print("✅ Database Connected: MongoDB Action mein hai!")
        except Exception as e:
            print(f"❌ Database Connection Failed: {e}")
            self.collection = None

    def save_scan(self, filename, file_hash, malicious_count, scan_url):
        """Scan result ko database mein save karta hai"""
        if self.collection is None:
            return # Agar DB fail hai to skip karo

        record = {
            "filename": filename,
            "hash": file_hash,
            "status": "DANGER" if malicious_count > 0 else "SAFE",
            "malicious_engines": malicious_count,
            "vt_link": scan_url,
            "timestamp": datetime.now()
        }
        
        try:
            self.collection.insert_one(record)
            print(f"💾 Saved to DB: {filename}")
        except Exception as e:
            print(f"⚠️ Save Error: {e}")

    def get_history(self, limit=10):
        """Last 10 scans nikal ke deta hai UI ke liye"""
        if self.collection is None:
            return []
        return list(self.collection.find().sort("timestamp", -1).limit(limit))
class MongoManager:
    def __init__(self):
        try:
            # Connection banao
            self.client = pymongo.MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
            self.db = self.client["CyberBodyguardDB"]
            self.collection = self.db["scan_history"]
            
            # Check connection (Ping karo)
            self.client.server_info()
            print(" Database Connected: MongoDB Action mein hai!")
        except Exception as e:
            print(f" Database Connection Failed: {e}")
            self.collection = None

    def save_scan(self, filename, file_hash, malicious_count, scan_url):
        """Scan result ko database mein save karta hai"""
        if self.collection is None:
            return # Agar DB fail hai to skip karo

        record = {
            "filename": filename,
            "hash": file_hash,
            "status": "DANGER" if malicious_count > 0 else "SAFE",
            "malicious_engines": malicious_count,
            "vt_link": scan_url,
            "timestamp": datetime.now()
        }
        
        try:
            self.collection.insert_one(record)
            print(f" Saved to DB: {filename}")
        except Exception as e:
            print(f" Save Error: {e}")

    def get_history(self, limit=10):
        """Last 10 scans nikal ke deta hai UI ke liye"""
        if self.collection is None:
            return []
        return [doc for doc in self.collection.find().sort("timestamp", -1).limit(limit)]