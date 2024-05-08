from flask import Flask, render_template, redirect, url_for, request

app  = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods = ['POST'])
def message():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_mail = request.form['user_mail']
        user_message = request.form['user_massage']
        return render_template('message.html', user_name=user_name, user_mail=user_mail, user_message=user_message)
    else:
        return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)