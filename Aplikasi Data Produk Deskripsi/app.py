from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "asdfghjkl12345fdsa_fdsakld8rweodfds"

# mysql config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'perusahaan'
mysql = MySQL(app)


@app.route('/')
def produk():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM produk''')
    produk = cursor.fetchall()
    cursor.close()

    return render_template('produk.html', produk=produk)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
