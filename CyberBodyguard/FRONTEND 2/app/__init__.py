# Flask app initialization
from flask import Flask

def create_app(config_name='development'):
    """Application factory"""
    from config import DevelopmentConfig, ProductionConfig, TestingConfig
    
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')
    
    # Load configuration
    if config_name == 'production':
        app.config.from_object(ProductionConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)
    
    return app
