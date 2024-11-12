from flask import Flask, render_template

app = Flask(__name__)

# Home route (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# User Registration route (register.html)
@app.route('/register')
def register():
    return render_template('register.html')

# Login route (login.html)
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard route (dashboard.html)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Transaction page route (transaction.html)
@app.route('/transaction')
def transaction():
    return render_template('transaction.html')

# Account creation page route (account_creation.html)
@app.route('/account_creation')
def account_creation():
    return render_template('account_creation.html')

# Check balance page route (balance.html)
@app.route('/balance')
def balance():
    return render_template('balance.html')

# Deposit page route (deposit.html)
@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

# Services page route (services.html)
@app.route('/services')
def services():
    return render_template('services.html')

# Contact page route (contact.html)
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Confirm action page route (confirm.html)
@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

# Account statement page route (statement.html)
@app.route('/statement')
def statement():
    return render_template('statement.html')


if __name__ == '__main__':
    app.run(debug=True)