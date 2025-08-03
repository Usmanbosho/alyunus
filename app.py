from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    flash("Thank you for reaching out! We'll get back to you soon.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
