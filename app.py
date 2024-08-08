import re
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True  # Enable TLS
app.config['MAIL_USE_SSL'] = False  # Disable SSL
app.config['MAIL_USERNAME'] = 'academynexusgasc@gmail.com'
app.config['MAIL_PASSWORD'] = 'adrt arwc frtn sklk'
app.config['MAIL_DEFAULT_SENDER'] = 'AcademyNexusGASC <academynexusgasc@gmail.com>'
app.config['SECRET_KEY'] = 'your_secret_key'

mail = Mail(app)

# Email format validation function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

@app.route('/404')
def error_404():
    return render_template('404.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        number = request.form['Number']

        if not is_valid_email(email):
            flash('Invalid email format. Please enter a valid email address.', 'danger')
            return redirect('/contact')
        
        if not number.isdigit() or len(number) != 10:
            flash('Invalid number format. Please enter a valid 10-digit number.', 'danger')
            return redirect('/contact')
            
        msg = Message(subject=subject,
                      recipients=['udhayaboopathi2003@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nNumber: {number}\nMessage:\n{message} "

        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'danger')

        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000 )


