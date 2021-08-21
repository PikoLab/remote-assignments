from flask import Flask, render_template, redirect, url_for, flash, session
from forms import RegistrationForm, LoginForm
import pymysql.cursors
from flask_bcrypt import Bcrypt

db = pymysql.connect(host='localhost',
                             user='bella',
                             password='123456',
                             db='assignment',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app=Flask(__name__)
app.config['SECRET_KEY'] = '5k91629bb0b13caa0c676dfde280ba876'
bcrypt=Bcrypt(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        try:
            with db.cursor() as cursor:
                sql="INSERT INTO user (username, email, password) VALUES (%s,%s,%s)"
                cursor.execute(sql, (username,email,hashed_password))
                db.commit()
        finally:
            flash(f'Hi, {form.username.data}. Your account is created!', 'success')
            session['username'] = username
            session['email'] = email
            return redirect(url_for('member'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        with db.cursor() as cursor:
            sql="SELECT * FROM user WHERE email = %s"
            cursor.execute(sql, email)
            user = cursor.fetchone()
            if user and  bcrypt.check_password_hash(user["password"], password): 
                flash(f'You have been logged in.', 'success')
                session['username'] = user["username"]
                session['email'] = user["email"]
                return redirect(url_for('member'))
            else: 
                flash(f'Fail to login! Please check your email address and password.', 'danger')
    return render_template("login.html", form=form)


@app.route('/member')
def member():
    return render_template("member.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='localhost')