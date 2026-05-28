from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'devops'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASS', 'secret')
    )
    return conn

@app.route('/')
def home():
    return '<h1>Flask + PostgreSQL ishlayapti!</h1>'

@app.route('/db')
def check_db():
    try:
        conn = get_db()
        conn.close()
        return '<h1>Database ulanish: OK!</h1>'
    except Exception as e:
        return f'<h1>Xato: {str(e)}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
