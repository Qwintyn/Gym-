from flask import Flask, request, render_template
import Db, mysql.connector

app = Flask(__name__, static_folder="static")
myDb = Db.connect()

@app.route('/Users')
def get_all_users():
    my_cursor = myDb.cursor()
    my_cursor.execute('SELECT firstName, user_id FROM USER')
    users = my_cursor.fetchall()
    return users

@app.route('/')
def r():
    return render_template('Index.html')
@app.route('/User/<id>', methods=['GET'])
def get_user(id):
    my_cursor = myDb.cursor()
    # Search why you bind params in sql
    # to pass values into a query without placing the value itself in the sql statement
    sql1 ='SELECT * FROM USER WHERE user_id = %s'
    my_cursor.execute(sql1, list(id))
    user = my_cursor.fetchall()
    return user
    # investigate  into fetchone why it returns something weird
    # fetchall = will return all rows
    # fetchone = will return one row at a time


@app.route('/vipMembers/<id>')
def get_vips(id):
    my_cursor = myDb.cursor()
    sql2 = 'SELECT * FROM VIP_member WHERE user_id = %s'
    my_cursor.execute(sql2, list(id))
    vip = my_cursor.fetchone()
    return {'Vip member': vip}
# second make sure the primary key (id) is foreign key of userid

@app.route('/User/<id>', methods = ['DELETE'] )
def delete_user(id):
    my_cursor = myDb.cursor()
    sql3 = 'DELETE FROM USER where user_id = %s '
    my_cursor.execute(sql3, list(id))
    myDb.commit()
    return {'Message': 'User deleted'}




if __name__ == '__main__':
    app.run()
