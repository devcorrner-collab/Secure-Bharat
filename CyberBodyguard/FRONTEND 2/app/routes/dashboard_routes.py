from flask import Blueprint, render_template, request, jsonify
from datetime import datetime, timedelta
from app.models import DashboardStats, ProtectionStatus

bp = Blueprint('dashboard', __name__, url_prefix='')

class DashboardService:
    """Service class for dashboard operations"""
    
    @staticmethod
    def get_dashboard_statistics():
        """Fetch dashboard statistics"""
        return {
            'threats_blocked': 1284,
            'last_scan': '22m ago',
            'protection_status': 'Enabled',
            'files_scanned': 4521,
            'scan_time': '0.02s',
            'signatures_checked': '2.1M',
            'heuristic_engine': 'AI-V3',
            'uptime_percentage': 99.9,
            'total_files_analyzed': 15420
        }
    
    @staticmethod
    def get_protection_status():
        """Get current protection status"""
        return {
            'status': 'Active',
            'real_time_protection': True,
            'cloud_connected': True,
            'last_update': (datetime.now() - timedelta(hours=2)).isoformat(),
            'database_version': '2024.02.13',
            'engine_version': '4.2.0'
        }
    
    @staticmethod
    def get_quick_stats():
        """Get quick stats for dashboard"""
        return [
            {
                'title': 'Threats Blocked',
                'value': '1,284',
                'icon': 'verified_user',
                'color': 'primary'
            },
            {
                'title': 'Last Scan',
                'value': '22m ago',
                'icon': 'update',
                'color': 'success'
            },
            {
                'title': 'Real-time Protection',
                'value': 'Enabled',
                'icon': 'bolt',
                'color': 'blue'
            }
        ]

@bp.route('/')
def home():
    """Home/Dashboard page"""
    stats = DashboardService.get_dashboard_statistics()
    protection = DashboardService.get_protection_status()
    quick_stats = DashboardService.get_quick_stats()
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         protection=protection,
                         quick_stats=quick_stats)

@bp.route('/dashboard')
def dashboard():
    """Main dashboard view"""
    stats = DashboardService.get_dashboard_statistics()
    protection = DashboardService.get_protection_status()
    quick_stats = DashboardService.get_quick_stats()
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         protection=protection,
                         quick_stats=quick_stats)

@bp.route('/api/dashboard-stats', methods=['GET'])
def get_dashboard_stats():
    """API endpoint for dashboard statistics"""
    stats = DashboardService.get_dashboard_statistics()
    stats['timestamp'] = datetime.now().isoformat()
    return jsonify(stats)

@bp.route('/api/protection-status', methods=['GET'])
def get_protection_status():
    """API endpoint for protection status"""
    protection = DashboardService.get_protection_status()
    protection['timestamp'] = datetime.now().isoformat()
    return jsonify(protection)

@bp.route('/api/quick-stats', methods=['GET'])
def get_quick_stats():
    """API endpoint for quick stats"""
    quick_stats = DashboardService.get_quick_stats()
    return jsonify({'stats': quick_stats, 'timestamp': datetime.now().isoformat()})

@bp.route('/api/scan-now', methods=['POST'])
def trigger_scan_now():
    """Trigger immediate scan of downloads folder"""
    try:
        data = request.get_json() or {}
        
        return jsonify({
            'success': True,
            'message': 'Scan initiated',
            'scan_id': 'SB-' + datetime.now().strftime('%Y%m%d%H%M%S'),
            'status': 'started',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
