from flask import Flask
import psycopg2

# creates an application that is named after the name of the file
app = Flask(__name__)


@app.route('/')
def index():
    conn = psycopg2.connect("postgresql://postgres:root@localhost:5432/postgres")
    cur = conn.cursor()
    # Execute a query
    cur.execute("SELECT * FROM my_data")
    # Retrieve query results
    records = cur.fetchall()
    return records


# if running this module as a standalone program (cf. command in the Python Dockerfile)
if __name__ == "__main__":
    app.run(debug=True)
