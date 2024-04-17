from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'students'

mysql = MySQL(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        major = request.form['major']
        year = request.form['year']

        # Insert data into MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students(name, email, phone, major, year) VALUES(%s, %s, %s, %s, %s)",
                    (name, email, phone, major, year))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
