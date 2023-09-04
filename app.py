from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo
import pyotp
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated user database (replace with a proper database)
users_db = {}

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        totp_secret = pyotp.random_base32()

        # Simulate user data storage (replace with proper database logic)
        users_db[username] = {
            'password': hashlib.sha256(password.encode()).hexdigest(),
            'totp_secret': totp_secret,
        }

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
