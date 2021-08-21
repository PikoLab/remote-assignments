from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import pymysql.cursors

db = pymysql.connect(host='localhost',
                             user='bella',
                             password='123456',
                             db='assignment',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
         with db.cursor() as cursor:
            sql="SELECT * FROM user WHERE username = %s"
            cursor.execute(sql, username.data)
            check_username = cursor.fetchone()
 
            if check_username:  
                raise ValidationError('The username is taken. Please try another one.')

    def validate_email(self, email):
         with db.cursor() as cursor:
            sql="SELECT * FROM user WHERE email = %s"
            cursor.execute(sql, email.data)
            check_email = cursor.fetchone()
 
            if check_email:  
                raise ValidationError('The email is taken. Please try another one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')