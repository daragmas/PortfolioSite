#  Set up Flask and Bootstrap
# What is being showcased?
# Multi-page: Home, Resume, Portfolio, Contact
# Color Scheme
# Set up on Heroku

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import smtplib
import os

app = Flask(__name__)
ckeditor = CKEditor(app)
Bootstrap(app)
email_password = os.environ.get('EMAIL_PASSWORD')
email_address = os.environ.get('EMAIL_ADDRESS')
email_destination = os.environ.get('DESTINATION_EMAIL')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        with smtplib.SMTP(host="smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=email_address, password=email_password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs=email_destination,
                msg=f"Subject:Message from {request.form['name']}\n\n"
                    f"You got the following message from {request.form['name']}:\n"
                    f"{request.form['message']}\n"
                    f"Contact Info: {request.form['email']} {request.form['phone']}"
            )
    return render_template('contact.html')


if __name__ == "__main__":
     app.run(debug=False)
