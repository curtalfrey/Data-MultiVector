# web_ui.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render index.html template with instructions and user variables
    return render_template('index.html', instructions=INSTRUCTIONS, user_variables=USER_VARIABLES)

@app.route('/documentation')
def documentation():
    # Render documentation.html template with documentation text
    return render_template('documentation.html', documentation_text=DOCUMENTATION_TEXT)
