from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('settings', __name__, url_prefix='/settings')

@bp.route('/')
def settings():
    """Settings page"""
    user_settings = {
        'real_time_protection': True,
        'auto_scan': True,
        'notifications': True,
        'scan_on_download': True
    }
    return render_template('settings.html', settings=user_settings)

@bp.route('/api/update', methods=['POST'])
def update_settings():
    """Update user settings"""
    data = request.get_json()
    # Save settings to database
    return jsonify({
        'success': True,
        'message': 'Settings updated successfully'
    })
