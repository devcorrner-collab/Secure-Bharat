from backend.services.folder_watch import FolderWatcher
from backend.services.scanner import scan_file
from backend.database.db_manager import DatabaseManager

# Global Object
db = DatabaseManager()

def process_new_file(filepath):
    print(f"🔍 Scanning: {filepath}...")
    
    result = scan_file(filepath)
    filename = filepath.split(r"\\")[-1] # Windows path fix

    if result.get("success"):
        malicious = result.get('malicious', 0)
        
        if malicious > 0:
            status = "DANGER"
            print(f" THREAT DETECTED: {filename} ({malicious} engines)")
        else:
            status = "SAFE"
            print(f" Safe File: {filename}")
            # Safe file pe user ko disturb mat karo, bas log karo
            
        # DB mein save
        db.save_scan(filename, status, malicious)
    else:
        print(f" Scan Error: {result.get('error')}")

if __name__ == "__main__":
    print("--- SecureBharat Background Service Started ---")
    
    # Watcher start karo
    watcher = FolderWatcher(callback_func=process_new_file)
    watcher.start()

    try:
        # Program ko chalta rakhne ke liye loop
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()
        print("Service Stopped.")