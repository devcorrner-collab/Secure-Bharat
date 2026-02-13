import requests
from backend.config import Config
from backend.services.file_hasher import calculate_sha256

def scan_file(filepath):
    # 1. Hash Nikalo
    file_hash = calculate_sha256(filepath)
    if not file_hash:
        return {"success": False, "error": "File read error"}

    # 2. API Call
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": Config.VT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        
        # --- DEBUGGING START (Ye nayi lines hain) ---
        print(f" VirusTotal Status Code: {response.status_code}") 
        # ------------------------------------------

        if response.status_code == 200:
            data = response.json()
            stats = data['data']['attributes']['last_analysis_stats']
            return {
                "success": True,
                "malicious": stats['malicious'],
                "clean": stats['harmless']
            }
        elif response.status_code == 404:
            return {
                "success": True, 
                "malicious": 0, 
                "clean": 0, 
                "message": "Unknown File (Safe/Private)"
            }
        elif response.status_code == 401:
            return {"success": False, "error": " API Key Galat hai (.env check kar)"}
        elif response.status_code == 429:
            return {"success": False, "error": " Quota Khatam (Thodi der ruk)"}
        else:
            return {"success": False, "error": f"Scan Failed: Code {response.status_code}"}
            
    except Exception as e:
        return {"success": False, "error": f"Offline/Error: {e}"}