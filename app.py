from flask import Flask
import Db, mysql.connector
app = Flask(__name__)
myDb = Db.connect()

@app.route('/Users')
def get_all_users():
    my_cursor = myDb.cursor()

    my_cursor.execute('SELECT * FROM USER')

    users = my_cursor.fetchall()

    return users

@app.route('/Users/<id>')
def get_user(id):
    my_cursor = myDb.cursor()
    # Search why you bind params in sql
    my_cursor.execute('SELECT * FROM USER WHERE user_id = %s', list(id))

    user = my_cursor.fetchall()
    # investigate  into fetchone why it returns something weird
    return user

@app.route('/vipMembers')
def get_vips():



if __name__ == '__main__':
    app.run()
