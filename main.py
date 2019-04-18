from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['debug'] = True

@app.route("/")
def index():
    return render_template('form.html')

#def is_legal():
    #if char in text is "/^\w+$/":
        #return True
    #else:
        #return name_error

@app.route('/', methods=['post'])
def display_signup():
    return render_template('form.html', username='', password='', name_error='', password_error="")

@app.route('/signup', methods=['get'])
def validate_form():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])

    name_error = ""
    password_error = ''

    if not username:
        name_error = "Please, enter a username."
        username = ''
    if not password:
        password_error = "Please, enter a password."
        password=''
    elif len(password) < 3:
        password_error = "Please, enter a password that's between 3 and 20 characters."
        password=''
    elif len(password) > 20:
        password_error = "Please, enter a password that's between 3 and 20 characters."
        password=''

    if not name_error and not password_error:
        return "awyus"
    else:
        return render_template('form.html', name_error=name_error, password_error=password_error, username=username, password=password) 
    #if password != password2:
        #password2_error = "Your passwords muust match."





    #if not is_legal(username):
        #name_error = "Please, enter a username between 3 and 20 characters with no whitespaces."
        #username = ''

if __name__ == '__main__':
    app.run()