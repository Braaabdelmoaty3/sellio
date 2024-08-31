from flask_wtf import flaskform
from wtforms import stringform, PasswordField
from wtforms.validators import data_required, email, EqualTo, length


class regestration():
    def regestraion():
        username = stringform('username',
                              validators= [data_required(),length(max(30), min(2))])
        email = email('email',
                      validators=[data_required(), email()])
        password = PasswordField('password',
                                 validators=[data_required()])
        confirm_password = PasswordField('comferm password',
                                 validators=[data_required(),EqualTo('password', message='Passwords must match')])


class login():
    def login():
        email = email('email',
                      validators=[data_required(), email()])
        password = PasswordField('password',
                                 validators=[data_required()])








# log in form 
# regestration form 


