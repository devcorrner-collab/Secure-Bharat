import os
import hashlib
from werkzeug.utils import secure_filename

class FileScanner:
    """File scanning utility class"""
    
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'zip', 'exe'}
    MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
    
    @staticmethod
    def allowed_file(filename):
        """Check if file extension is allowed"""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FileScanner.ALLOWED_EXTENSIONS
    
    @staticmethod
    def calculate_hash(filepath):
        """Calculate SHA-256 hash of file"""
        sha256_hash = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b''):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    @staticmethod
    def scan_file(filepath):
        """Simulate file scanning"""
        # In production, this would integrate with actual antivirus engines
        return {
            'scan_id': 'SB-12345',
            'filename': os.path.basename(filepath),
            'status': 'safe',
            'threats_found': 0,
            'scan_time': '0.02s',
            'hash': FileScanner.calculate_hash(filepath)
        }
    
    @staticmethod
    def get_file_size(filepath):
        """Get file size in MB"""
        return round(os.path.getsize(filepath) / (1024 * 1024), 2)

class ValidationUtil:
    """Validation utilities"""
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_filename(filename):
        """Validate filename"""
        return secure_filename(filename) == filename

class EncryptionUtil:
    """Encryption utilities"""
    
    @staticmethod
    def hash_password(password):
        """Hash password for storage"""
        import hashlib
        salt = os.urandom(32)
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return salt.hex() + pwd_hash.hex()
    
    @staticmethod
    def verify_password(password, hash_value):
        """Verify password against hash"""
        import hashlib
        salt = bytes.fromhex(hash_value[:64])
        stored_hash = bytes.fromhex(hash_value[64:])
        pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return pwd_hash == stored_hash
