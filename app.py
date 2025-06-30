from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_time_and_ip():
    ist_timezone = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(ist_timezone)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %z")
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    return jsonify({
        "timestamp": formatted_time,
        "ip": visitor_ip
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)