from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
# Route for password entry (login page)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "wookachakahp":
            session['authenticated'] = True 
            return redirect('/home')  
        else:
            return '''
                <p style="color:red;">Access Denied. Try again.</p>
                <form method="POST">
                    <input type="password" name="password" placeholder="Enter password" required>
                    <button type="submit">Submit</button>
                </form>
            '''
    return '''
        <form method="POST">
            <input type="password" name="password" placeholder="Enter password" required>
            <button type="submit">Submit</button>
        </form>
    '''

@app.route('/home')
def home():
    # Check if the user is authenticated
    if 'authenticated' not in session or not session['authenticated']:
        return redirect(url_for('login'))  
    
    return render_template('website.html')  

# Optional: Route to log out and clear the session
@app.route('/logout')
def logout():
    session.pop('authenticated', None)  
    return redirect(url_for('login'))  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

        </form>
    '''

@app.route('/home')
def home():
    return render_template('website.html')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
