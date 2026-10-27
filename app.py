from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <h1>Secure Web Application</h1>
    <p>Welcome to our Cyber Security project.</p>
    <p>Security testing will be performed in a
    controlled local environment.</p>
    """)

if __name__ == "__main__":
    app.run(debug=False)