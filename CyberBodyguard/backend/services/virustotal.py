import requests
import time
from backend.config import Config

class VirusTotalScanner:
    BASE_URL = "https://www.virustotal.com/api/v3/files"
    
    def __init__(self):
        self.headers = {
            "x-apikey": Config.VT_API_KEY
        }

    def scan_file_hash(self, file_hash):
        """Sirf Hash check karta hai (Fastest Method)"""
        url = f"{self.BASE_URL}/{file_hash}"
        
        try:
            response = requests.get(url, headers=self.headers)
            
            if response.status_code == 200:
                data = response.json()
                stats = data['data']['attributes']['last_analysis_stats']
                return {
                    "success": True,
                    "malicious": stats['malicious'],
                    "total": sum(stats.values()),
                    "link": data['data']['links']['self']
                }
            elif response.status_code == 404:
                return {"success": False, "error": "File Unknown (Upload Required)"}
            elif response.status_code == 429:
                return {"success": False, "error": "Quota Exceeded (Ruk ja bhai!)"}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
