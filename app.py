from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'janissql',
    'database': 'page_counter'
}

@app.route("/increment/<page_name>", methods=["GET"])
def increment_counter(page_name):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        user_ip = request.remote_addr
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert a new view log with timestamp and IP
        cursor.execute("""
            INSERT INTO counter (page_name, view_time, ip_address)
            VALUES (%s, %s, %s)
        """, (page_name, now, user_ip))
        conn.commit()

        # Total views for that page
        cursor.execute("SELECT COUNT(*) FROM counter WHERE page_name = %s", (page_name,))
        total_views = cursor.fetchone()[0]

        # Unique visitors for that page
        cursor.execute("SELECT COUNT(DISTINCT ip_address) FROM counter WHERE page_name = %s", (page_name,))
        unique_visitors = cursor.fetchone()[0]

        return jsonify({
            'page': page_name,
            'total_views': total_views,
            'unique_visitors': unique_visitors,
            'last_ip': user_ip,
            'timestamp': now
        })

    except Error as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/dashboard", methods=["GET"])
def view_dashboard():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Show recent 100 page views sorted by time
        cursor.execute("""
            SELECT page_name, view_time, ip_address
            FROM counter
            ORDER BY view_time DESC
            LIMIT 100
        """)
        rows = cursor.fetchall()
        return jsonify(rows)

    except Error as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)
