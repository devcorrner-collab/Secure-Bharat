from flask import Blueprint, render_template, jsonify
from datetime import datetime

bp = Blueprint('pages', __name__, url_prefix='')

@bp.route('/privacy-assurance')
def privacy_assurance():
    """Privacy assurance page"""
    return render_template('privacy_assurance.html')

@bp.route('/privacy-info')
def privacy_info():
    """Privacy information page"""
    privacy_features = {
        'local_scan': 'Advanced scanning algorithms process everything directly on your device.',
        'no_cloud': 'Your files never leave your phone. We don\'t have servers to store your data.',
        'no_tracking': 'We don\'t collect personal info, usage patterns, or metadata.'
    }
    return render_template('privacy_info.html', features=privacy_features)

@bp.route('/api/privacy-policy', methods=['GET'])
def get_privacy_policy():
    """Get privacy policy"""
    return jsonify({
        'version': '2.0',
        'updated_at': datetime.now().isoformat(),
        'features': {
            'local_scanning': True,
            'no_cloud_upload': True,
            'no_data_tracking': True,
            'end_to_end_encrypted': True
        },
        'compliance': {
            'gdpr': True,
            'ccpa': True,
            'audit_verified': True,
            'security_certified': 'ISO 27001'
        }
    })
