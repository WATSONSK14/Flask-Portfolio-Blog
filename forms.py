from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class AdminLoginForm(FlaskForm):
    email = StringField(label="@@@", validators=[DataRequired()])
    password = StringField(label="@@@", validators=[DataRequired()])
    submit = SubmitField("@@@")

class RegisterForm(FlaskForm):
    email= StringField(label="E-Posta", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Email(message="Lütfen geçerli bir e-posta adresi girin.")
    ])

    password = PasswordField(label="Password", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Length(min=6, message="Şifre en az 6 karakter olmalı.")
    ])
    two_password = PasswordField(label="Password Confirm", validators=[
        DataRequired(message="Bu alan boş bırakılamaz."),
        Length(min=6, message="Şifre en az 6 karakter olmalı."),
        EqualTo('password', message="Şifreler Eşleşmiyor")
    ])

    submit = SubmitField(label="Register")

class Login_Form(FlaskForm):
    email = StringField(label="E-Posta",validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Email(message="Lütfen Gerçek Mail Giriniz")
    ])
    password = PasswordField(label="Password",validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz")
    ])
    submit = SubmitField(label="Login")


class ContantForm(FlaskForm):
    name = StringField(label="Name", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Length(min=3,max=20, message="Bu Alana Minimum 3 Maximum 20 Karakter Girebilirsiniz")
    ])

    surname = StringField(label="Surname", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Length(min=3,max=20, message="Bu Alana Minimum 3 Maximum 20 Karakter Girebilirsiniz")
    ])

    email= StringField(label="Email address", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Email(message="Lütfen Gerçek Mail Giriniz"),
        Length(max=30, message="Bu Alana Maximum 40 Karakter Girebilirsiniz")
    ],render_kw={"readonly": True})

    subject= StringField(label="Subject", validators=[
        DataRequired(message="Bu Alan Boş Bırakılamaz"),
        Length(max=30, message="Bu Alana Maximum 30 Karakter Girebilirsiniz")
    ])

    message = TextAreaField(label="Message", validators=[
        DataRequired(message="Bu Alanı Boş Bırakamazsınız"),
        Length(min=20,max=800,message="Bu Alana Minimum 20 Maximum 800 Karakter Girebilirsiniz")
    ])
    submit = SubmitField(label="Send Message")