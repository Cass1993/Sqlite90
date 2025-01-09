from flask import Flask, render_template
import psycopg2
import os
from urllib.parse import urlparse

app = Flask(__name__)

def get_db_connection():
    # Parse the DATABASE_URL environment variable
    result = urlparse(os.getenv('DATABASE_URL'))
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=result.path[1:],  # Remove the leading '/' from the path
        user=result.username,
        password=result.password,
        host=result.hostname,
        port=result.port
    )
    return conn

@app.route('/')
def home():
    # Example of using the database connection
    conn = get_db_connection()
    # You can execute queries here using the connection
    # For example: cur = conn.cursor()
    # Don't forget to close the connection after use
    conn.close()
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the app binds to 0.0.0.0 and the correct port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)