# NumbersPro.py
# Development version 1.0
# Flask route code to HTML files that make up this app

from flask import Flask, render_template
app = Flask(__name__)

# Route to the Home page. Viewer can use either '/' or '/home'
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

# Route to the About page
@app.route('/about')
def about_page():
    return render_template('about.html')

# Route to the Sign-in page
@app.route('/signin')
def signin_page():
    return render_template('signin.html')

# Route to the Purchase page
@app.route('/purchase')
def purchase_page():
    return render_template('purchase.html')

# Route to the Documentation page
@app.route('/docs')
def docs_page():
    return render_template('docs.html')

# Route to the Dashboard page
@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

    
if __name__ == '__main__':
    app.run(debug=True)