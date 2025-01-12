import urllib.parse
import psycopg2
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from flask import Flask, render_template

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    # Parse the DATABASE_URL environment variable
    result = urlparse(os.getenv('DATABASE_URL'))
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=result.path[1:],  # Remove the leading '/' from the path
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route('/')
def home():
    # Example of using the database connection
    conn = get_db_connection()
    # You can execute queries here using the connection
    # For example: cur = conn.cursor()
    # Don't forget to close the connection after use
    if conn is not None:
        conn.close()
    return render_template('index.html')

@app.route('/cartoons')
def cartoons():
    # Establish a database connection
    conn = get_db_connection()
    if conn is None:
        return "Error connecting to database", 500

    # Execute a query to retrieve a list of cartoons
    cur = conn.cursor()
    cur.execute("SELECT * FROM cartoons")
    cartoons = cur.fetchall()

    # Retrieve the video URLs or embed codes for each cartoon
    for i, cartoon in enumerate(cartoons):
        # Assuming the video URL or embed code is stored in a separate column in the database
        # Replace 'video_url' with the actual column name
        video_url = retrieve_video_url(cartoon[0])
        cartoons[i] = (cartoon[0], cartoon[1], cartoon[2], video_url)

    # Close the database connection
    conn.close()

    # Pass the list of cartoons to the template
    return render_template('cartoons.html', cartoons=cartoons)

def retrieve_video_url(cartoon_id):
    # Retrieve the video URL or embed code from the database or a third-party service
    # For example:
    video_url = "https://example.com/videos/{}.mp4".format(cartoon_id)
    return video_url

if __name__ == '__main__':
    # Ensure the app binds to 0.0.0.0 and the correct port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)