import os
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from config import Config

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config.from_object(Config)

# Database initialization (if needed)
# from models import db
# db.init_app(app)

# Import routes
from app.routes import auth_routes, dashboard_routes, scan_routes, settings_routes, pages_routes

# Register blueprints
app.register_blueprint(dashboard_routes.bp)
app.register_blueprint(scan_routes.bp)
app.register_blueprint(auth_routes.bp)
app.register_blueprint(settings_routes.bp)
app.register_blueprint(pages_routes.bp)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Context processors
@app.context_processor
def inject_config():
    return {
        'app_name': 'SecureBharat',
        'version': '2.4.0'
    }

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
