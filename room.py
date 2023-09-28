import sqlite3
from flask import Flask
from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_room(room_id):
    conn = get_db_connection()
    room = conn.execute('SELECT * FROM rooms WHERE id = ?',
                        (room_id,)).fetchone()
    conn.close()
    if room is None:
        abort(404)
    return room

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg= ''
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        conn=sqlite3.connect("database.db")
        cur=conn.cursor() 
        cur.execute("SELECT * FROM admin WHERE username = (?) and password = (?)",(username, password))
        r = cur.fetchall()
        for i in r:
            
            if(username == i[1] and password == i[2]):
                session["logedin"] = True
                session["username"]=username
                return redirect(url_for('room_list_admin'))
            else:
                flash('invlaid username or password')
        conn.commit()
        conn.close    
    return render_template('login.html',msg=msg)

@app.route('/user', methods=['GET', 'POST'])
def user():
    msg= ''
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        conn=sqlite3.connect("database.db")
        cur=conn.cursor() 
        cur.execute("SELECT * FROM user WHERE username = (?) and password = (?)",(username, password)) 
        r = cur.fetchall()
        for i in r:
            
            if(username == i[1] and password == i[2]):
                session["logedin"] = True
                session["username"]=username
                return redirect(url_for('room_list'))
            else:
                flash('invlaid username or password')

        conn.commit()
        conn.close    
    return render_template('user.html',msg=msg)

@app.route('/user/room_list')
def room_list():
    conn=get_db_connection()
    rooms=conn.execute("SELECT * FROM rooms").fetchall()
    conn.close
    return render_template('room_list.html',rooms=rooms)

@app.route('/user/room_list/<int:room_id>')
def room(room_id):
    room = get_room(room_id)
    return render_template('room.html',room=room)

@app.route('/admin/room_list_admin')
def room_list_admin():
    conn=get_db_connection()
    rooms=conn.execute("SELECT * FROM rooms").fetchall()
    conn.close
    return render_template('room_list_admin.html',rooms=rooms)

@app.route('/admin/room_list_admin/<int:id>/edit',methods=('GET','POST'))
def edit(id):
    room = get_room(id)

    if request.method == 'POST':
        title = request.form['title']
        capacity = request.form['capacity']
        location = request.form['location']

        if not title:
            flash('Hall name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE rooms SET title = ?, capacity = ?, location = ? WHERE id = ?',
                         (title, capacity, location, id))
            conn.commit()
            conn.close()
            return redirect(url_for('room_list_admin'))

    return render_template('edit.html', room=room)

@app.route('/admin/room_list_admin/<int:room_id>')
def room_admin(room_id):
    room = get_room(room_id)
    return render_template('room_admin.html',room=room)

@app.route('/admin/room_list_admin/<int:id>/delete', methods=('GET','POST',))
def delete(id):
    room = get_room(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM rooms WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(room['title']))
    return redirect(url_for('room_list_admin'))

@app.route('/admin/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        capacity = request.form['capacity']
        location = request.form['location']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO rooms (title, capacity, location) VALUES(?, ?, ?)',
                         (title, capacity,location))
            conn.commit()
            conn.close()
            return redirect(url_for('room_list_admin'))

    return render_template('create.html')