# SecureBharat Frontend - Python Flask Application

A modern, secure file scanning application frontend built with Flask and Tailwind CSS.

## Features

- 🛡️ Real-time file scanning interface
- 📊 Dashboard with security statistics
- 📁 Scan history tracking
- 🎨 Modern UI with Tailwind CSS
- ⚡ Fast and responsive design
- 🔒 Privacy-first architecture

## Project Structure

```
FRONTEND 2/
├── app/
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images
│   ├── routes/              # Blueprint routes
│   ├── models/              # Data models
│   ├── utils/               # Utility functions
│   └── __init__.py
├── config.py                # Configuration
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "FRONTEND 2"
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The app will be available at `http://localhost:5000`

## Pages

- `/` - Dashboard
- `/scans/history` - Scan History
- `/scans/active` - Active Scan
- `/scans/complete` - Scan Complete
- `/privacy-assurance` - Privacy Info
- `/scan-complete` - Scan Completion
- `/threat-detected` - Threat Detection Alert
- `/safe-file-confirmation` - Safe File Confirmation

## API Endpoints

### Dashboard
- `GET /api/dashboard-stats` - Get dashboard statistics

### Scans
- `POST /scans/api/start-scan` - Start a file scan
- `GET /scans/api/scan-status/<scan_id>` - Get scan status

### Settings
- `POST /settings/api/update` - Update user settings

## Configuration

Configuration is managed through `config.py`. Environment variables can override defaults:

```bash
export SECRET_KEY="your-secret-key"
export DEBUG=False
export DATABASE_URL="postgresql://user:password@localhost/securebharat"
```

## Security Features

- Secure session management
- Password hashing and verification
- File upload validation
- SQL injection prevention
- CSRF protection

## Development

To run in development mode with auto-reload:

```bash
python run.py
```

## Production Deployment

1. Set `DEBUG=False` in config
2. Use a production WSGI server (Gunicorn/uWSGI)
3. Enable HTTPS
4. Set secure configuration variables

Example with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

## License

All rights reserved - SecureBharat
