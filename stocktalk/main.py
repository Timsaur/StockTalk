import os
import psycopg2

from app import app

if __name__ == '__main__':
    app.debug = True
    app.run()

    conn = psycopg2.connect(database="maindb", user = "timothyli", password = "pass123", host = "127.0.0.1", port = "5432")
