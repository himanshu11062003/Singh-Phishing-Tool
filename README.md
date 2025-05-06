# Singh Phishing Tool 🛡️

> ⚠️ DISCLAIMER: This project is for educational and cybersecurity awareness training only. Do NOT use it for unauthorized or malicious purposes.

## 📘 About the Project

Singh Phishing Tool is a simulated phishing website built using Python Flask. It demonstrates how phishing attacks capture credentials by mimicking login pages of popular websites like:

- Instagram
- Facebook
- Twitter
- Gmail

This tool is ideal for:

- Ethical hacking labs
- Cybersecurity awareness training
- Educational demos for phishing simulations

## 📁 Project Structure

Singh-Phishing-Tool/
│
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates for fake login UIs
│   ├── home.html
│   ├── instagram.html
│   ├── facebook.html
│   ├── twitter.html
│   └── gmail.html

## 🚀 How to Run

1. Clone the Repository

git clone https://github.com/himanshu11062003/Singh-Phishing-Tool.git
cd Singh-Phishing-Tool

2. Set Up Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements

pip install -r requirements.txt

4. Run the Application

python app.py

Go to: http://localhost:5001 in your browser.

## 📂 Credentials Storage

Captured credentials are stored (for demo purposes) in the following files under the /tmp/ directory:

- /tmp/instagram_creds.txt
- /tmp/facebook_creds.txt
- /tmp/twitter_creds.txt
- /tmp/gmail_creds.txt

These files are temporary and cleared on server restarts when deployed on platforms like Render.

## 🛑 Disclaimer

This tool is built strictly for ethical learning and cybersecurity awareness. The author is not responsible for any misuse.

