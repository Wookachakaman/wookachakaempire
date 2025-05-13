from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'super_secret_key_here'  # This MUST be set to use sessions

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == 'wookachakahp':
            session['authenticated'] = True
            return redirect(url_for('home'))
        else:
            return '''
                <p style="color:red;">Incorrect password</p>
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
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template('website.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
