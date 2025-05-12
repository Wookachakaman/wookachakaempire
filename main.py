from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "wookachakahp":
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
    return render_template('website.html')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
