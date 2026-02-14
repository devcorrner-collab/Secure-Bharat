# Models package
from datetime import datetime

class DashboardStats:
    """Dashboard statistics model"""
    def __init__(self):
        self.threats_blocked = 1284
        self.last_scan = '22m ago'
        self.protection_status = 'Enabled'
        self.files_scanned = 4521
        self.uptime_percentage = 99.9
        
    def to_dict(self):
        return {
            'threats_blocked': self.threats_blocked,
            'last_scan': self.last_scan,
            'protection_status': self.protection_status,
            'files_scanned': self.files_scanned,
            'uptime_percentage': self.uptime_percentage
        }

class ProtectionStatus:
    """Protection status model"""
    def __init__(self):
        self.status = 'Active'
        self.real_time_protection = True
        self.cloud_connected = True
        self.database_version = '2024.02.13'
        self.engine_version = '4.2.0'
        self.last_update = datetime.now()
        
    def to_dict(self):
        return {
            'status': self.status,
            'real_time_protection': self.real_time_protection,
            'cloud_connected': self.cloud_connected,
            'database_version': self.database_version,
            'engine_version': self.engine_version,
            'last_update': self.last_update.isoformat()
        }

class Scan:
    """Scan model"""
    def __init__(self, filename, status, size, threats=0):
        self.id = None
        self.filename = filename
        self.status = status
        self.size = size
        self.threats = threats
        self.scan_date = datetime.now()
        self.scan_location = 'Mumbai, India'
        self.hash_sha256 = None
        self.scan_time = '0.02s'
        self.scan_id = None
        
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'status': self.status,
            'size': self.size,
            'threats': self.threats,
            'scan_date': self.scan_date.isoformat(),
            'scan_location': self.scan_location,
            'scan_time': self.scan_time,
            'scan_id': self.scan_id
        }

class User:
    """User model"""
    def __init__(self, username, email):
        self.id = None
        self.username = username
        self.email = email
        self.created_at = datetime.now()
        self.real_time_protection = True
        self.auto_scan = True
        
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class ThreatDetection:
    """Threat detection model"""
    def __init__(self, filename, threat_type):
        self.id = None
        self.filename = filename
        self.threat_type = threat_type
        self.detected_at = datetime.now()
        self.severity = 'high'
        self.action_taken = 'quarantined'
        
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'threat_type': self.threat_type,
            'detected_at': self.detected_at.isoformat(),
            'severity': self.severity,
            'action_taken': self.action_taken
        }

class ActiveScan:
    """Active scan model"""
    def __init__(self, scan_id, filename, file_size):
        self.scan_id = scan_id
        self.filename = filename
        self.file_size = file_size
        self.status = 'in_progress'
        self.progress = 0
        self.started_at = datetime.now()
        self.current_step = 'Initialization'
        self.threats_found = 0
        self.signatures_checked = 0
        self.estimated_time_remaining = '2m'
        
    def to_dict(self):
        return {
            'scan_id': self.scan_id,
            'filename': self.filename,
            'file_size': self.file_size,
            'status': self.status,
            'progress': self.progress,
            'started_at': self.started_at.isoformat(),
            'current_step': self.current_step,
            'threats_found': self.threats_found,
            'signatures_checked': self.signatures_checked
        }

