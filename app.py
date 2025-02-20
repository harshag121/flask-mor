from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getlogin()
    
    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    # Format the response
    response = f"""
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> Harsha Vardhan G</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
