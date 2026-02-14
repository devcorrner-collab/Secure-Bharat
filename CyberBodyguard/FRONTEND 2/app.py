from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# Routes
@app.route('/')
def home():
    return render_template('safe_file_confirmation.html')

@app.route('/safe-file')
def safe_file():
    return render_template('safe_file_confirmation.html')

@app.route('/threat-detected')
def threat_detected():
    return render_template('threat_detected.html')

@app.route('/privacy-assurance')
def privacy_assurance():
    return render_template('privacy_assurance.html')

@app.route('/scan-history')
def scan_history():
    return render_template('scan_history.html')

@app.route('/privacy-info')
def privacy_info():
    return render_template('privacy_info.html')

@app.route('/scan-complete')
def scan_complete():
    return render_template('scan_complete.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/active-scan')
def active_scan():
    return render_template('active_scan.html')

if __name__ == '__main__':
    app.run(debug=True)
