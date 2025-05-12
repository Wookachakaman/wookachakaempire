from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == "wookachakahp":
            return render_template('website.html')
        return "Access denied"
    
    return '''
        <form method="POST">
            <input type="password" name="password" placeholder="Enter password">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
