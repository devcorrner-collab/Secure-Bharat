from flask import Blueprint, render_template, request, jsonify
from datetime import datetime, timedelta
import uuid
import os

bp = Blueprint('scans', __name__, url_prefix='/scans')

class ScanService:
    """Service class for scan operations"""
    
    # In-memory storage for active scans (in production, use database)
    active_scans = {}
    scan_history = [
        {
            'id': 'scan-001',
            'filename': 'report_q4.pdf',
            'status': 'safe',
            'scan_date': (datetime.now() - timedelta(hours=2)).isoformat(),
            'size': '1.24 MB',
            'threats': 0,
            'scan_time': '0.02s'
        },
        {
            'id': 'scan-002',
            'filename': 'setup.exe',
            'status': 'threat',
            'scan_date': (datetime.now() - timedelta(hours=5)).isoformat(),
            'size': '45.2 MB',
            'threats': 1,
            'threat_type': 'Malware / Trojan.Generic',
            'scan_time': '0.15s'
        },
        {
            'id': 'scan-003',
            'filename': 'marketing_plan.docx',
            'status': 'safe',
            'scan_date': (datetime.now() - timedelta(days=1)).isoformat(),
            'size': '2.1 MB',
            'threats': 0,
            'scan_time': '0.05s'
        }
    ]
    
    @staticmethod
    def get_scan_history(limit=10):
        """Get scan history"""
        return ScanService.scan_history[:limit]
    
    @staticmethod
    def get_scan_details(scan_id):
        """Get detailed scan information"""
        for scan in ScanService.scan_history:
            if scan['id'] == scan_id:
                return scan
        return None
    
    @staticmethod
    def create_active_scan(filename, file_size):
        """Create a new active scan"""
        scan_id = f"scan-{uuid.uuid4().hex[:8]}"
        
        scan = {
            'scan_id': scan_id,
            'filename': filename,
            'file_size': file_size,
            'status': 'in_progress',
            'progress': 0,
            'started_at': datetime.now().isoformat(),
            'current_step': 'Heuristic Analysis',
            'threats_found': 0,
            'signatures_checked': 0
        }
        
        ScanService.active_scans[scan_id] = scan
        return scan
    
    @staticmethod
    def get_active_scan_status(scan_id):
        """Get status of active scan"""
        if scan_id in ScanService.active_scans:
            scan = ScanService.active_scans[scan_id]
            # Simulate progress
            if scan['progress'] < 100:
                scan['progress'] += 15
                if scan['progress'] >= 100:
                    scan['status'] = 'completed'
                    scan['current_step'] = 'Complete'
            return scan
        return None
    
    @staticmethod
    def complete_scan(scan_id, is_safe=True):
        """Complete a scan"""
        if scan_id in ScanService.active_scans:
            scan = ScanService.active_scans[scan_id]
            scan['status'] = 'completed'
            scan['progress'] = 100
            scan['completed_at'] = datetime.now().isoformat()
            
            # Add to history
            history_entry = {
                'id': scan_id,
                'filename': scan['filename'],
                'status': 'safe' if is_safe else 'threat',
                'scan_date': scan['started_at'],
                'size': scan['file_size'],
                'threats': 0 if is_safe else 1,
                'scan_time': '0.02s'
            }
            ScanService.scan_history.insert(0, history_entry)
            
            return scan
        return None

@bp.route('/history')
def scan_history():
    """Scan history page"""
    scans = ScanService.get_scan_history()
    return render_template('scan_history.html', scans=scans)

@bp.route('/active')
def active_scan():
    """Active scan in progress"""
    current_file = {
        'name': 'invoice_02.pdf',
        'size': '4.2 MB',
        'type': 'PDF Document',
        'encrypted': True,
        'current_step': 'Heuristic Analysis',
        'signatures_checked': 1200000
    }
    return render_template('active_scan.html', current_file=current_file)

@bp.route('/threat-detected')
def threat_detected():
    """Threat detected alert page"""
    threat = {
        'filename': 'invoice_9921.exe',
        'detection_time': '2 minutes ago',
        'threat_type': 'Malware / Trojan.Generic',
        'detected_at': datetime.now().isoformat(),
        'severity': 'high',
        'action': 'quarantined'
    }
    return render_template('threat_detected.html', threat=threat)

@bp.route('/safe-file')
def safe_file_confirmation():
    """Safe file confirmation page"""
    safe_file = {
        'filename': 'report_2023_final.pdf',
        'size': '2.4 MB',
        'status': 'Verified Safe',
        'scan_id': 'SB-99283-PDF',
        'threats_found': 0
    }
    return render_template('safe_file_confirmation.html', safe_file=safe_file)

@bp.route('/api/history', methods=['GET'])
def api_scan_history():
    """API endpoint for scan history"""
    limit = request.args.get('limit', 10, type=int)
    scans = ScanService.get_scan_history(limit)
    return jsonify({
        'scans': scans,
        'total': len(scans),
        'timestamp': datetime.now().isoformat()
    })

@bp.route('/api/scan-details/<scan_id>', methods=['GET'])
def api_scan_details(scan_id):
    """Get detailed scan information"""
    scan = ScanService.get_scan_details(scan_id)
    if scan:
        return jsonify(scan)
    return jsonify({'error': 'Scan not found'}), 404

@bp.route('/api/start-scan', methods=['POST'])
def start_scan():
    """API endpoint to start a file scan"""
    try:
        data = request.get_json() or {}
        filename = data.get('filename', 'unknown.pdf')
        file_size = data.get('file_size', '0 MB')
        
        scan = ScanService.create_active_scan(filename, file_size)
        
        return jsonify({
            'success': True,
            'scan': scan,
            'timestamp': datetime.now().isoformat()
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/api/scan-status/<scan_id>', methods=['GET'])
def scan_status(scan_id):
    """Get current scan status"""
    scan = ScanService.get_active_scan_status(scan_id)
    if scan:
        return jsonify({
            'scan_id': scan_id,
            'status': scan['status'],
            'progress': scan['progress'],
            'current_step': scan['current_step'],
            'filename': scan['filename'],
            'threats_found': scan['threats_found'],
            'timestamp': datetime.now().isoformat()
        })
    return jsonify({'error': 'Scan not found'}), 404

@bp.route('/api/complete-scan/<scan_id>', methods=['POST'])
def complete_scan_api(scan_id):
    """Complete a scan"""
    try:
        data = request.get_json() or {}
        is_safe = data.get('is_safe', True)
        
        scan = ScanService.complete_scan(scan_id, is_safe)
        if scan:
            return jsonify({
                'success': True,
                'scan': scan,
                'timestamp': datetime.now().isoformat()
            })
        return jsonify({'error': 'Scan not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/api/threat-details/<threat_id>', methods=['GET'])
def api_threat_details(threat_id):
    """Get threat detection details"""
    threat = {
        'threat_id': threat_id,
        'filename': 'invoice_9921.exe',
        'threat_type': 'Malware / Trojan.Generic',
        'severity': 'high',
        'quarantine_path': '/quarantine/threat_12345',
        'action_taken': 'quarantined',
        'detected_at': datetime.now().isoformat()
    }
    return jsonify(threat)

@bp.route('/api/verify-safe-file/<file_id>', methods=['GET'])
def api_verify_safe_file(file_id):
    """Verify safe file details"""
    file_info = {
        'file_id': file_id,
        'filename': 'report_2023_final.pdf',
        'size': '2.4 MB',
        'status': 'safe',
        'scan_id': 'SB-99283-PDF',
        'threats_found': 0,
        'verified_at': datetime.now().isoformat()
    }
    return jsonify(file_info)
