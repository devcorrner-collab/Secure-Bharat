"""
SecureBharat Application - Main Entry Point
"""
import os
import sys
from app import create_app
from config import DevelopmentConfig, ProductionConfig

# Determine environment
env = os.environ.get('FLASK_ENV', 'development')
config_name = 'production' if env == 'production' else 'development'

# Create Flask app
app = create_app(config_name)

# Import and register blueprints
with app.app_context():
    from app.routes import dashboard_routes, scan_routes, auth_routes, settings_routes, pages_routes
    
    app.register_blueprint(dashboard_routes.bp)
    app.register_blueprint(scan_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(settings_routes.bp)
    app.register_blueprint(pages_routes.bp)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>404 Not Found</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for doesn't exist.</p>
    </body>
    </html>
    ''', 404

@app.errorhandler(500)
def internal_error(error):
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>500 Server Error</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; }
            h1 { color: #c33; }
        </style>
    </head>
    <body>
        <h1>500 - Internal Server Error</h1>
        <p>Something went wrong on our end.</p>
    </body>
    </html>
    ''', 500

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs(app.config.get('UPLOAD_FOLDER', 'app/uploads'), exist_ok=True)
    
    # Run the application
    app.run(
        debug=app.config['DEBUG'],
        host=app.config.get('HOST', '127.0.0.1'),
        port=app.config.get('PORT', 5000)
    )
