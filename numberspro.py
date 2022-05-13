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

# Route to the Documentation page
@app.route('/docs')
def docs_page():
    return render_template('docs.html')

# Route to the Sign Up page
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

# Route to the Pricing page
@app.route('/pricing')
def pricing_page():
    return render_template('pricing.html')

# Route to the Documentation page
@app.route('/docs')
def docs_page():
    return render_template('docs.html')

# Route to the Blog page
@app.route('/blog')
def blog_page():
    return render_template('blog.html')

# Route to the Dashboard page
@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

    
if __name__ == '__main__':
    app.run(debug=True)
