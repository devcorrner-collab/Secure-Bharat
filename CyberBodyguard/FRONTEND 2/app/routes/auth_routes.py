from flask import Blueprint, render_template, jsonify

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    """Login page (if needed)"""
    return render_template('login.html')

@bp.route('/logout', methods=['POST'])
def logout():
    """Logout endpoint"""
    return jsonify({'message': 'Logged out successfully'})
