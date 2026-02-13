import hashlib

def calculate_sha256(file_path):
    """File ka SHA256 hash generate karta hai efficiently"""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # 4KB ke tukdon mein padho taaki PC hang na ho
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"❌ Hashing Error: {e}")
        return None