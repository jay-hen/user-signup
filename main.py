from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['debug'] = True

title = 'Signup'

@app.route("/", methods=['get'])
def index():
    return render_template('form.html', username='', password='', name_error='', password_error="")

@app.route('/signup', methods=['post'])
def validate_form():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])

    name_error = ""
    password_error = ''

    for char in username:
        if char.isspace():
            name_error = "Your username cannot contain spaces."
            username = ""
        elif not username:
            name_error = "Please, enter a username."
            username = ''
        else:
            if (len(username) < 3) or (len(username) > 20):
                name_error = "Please, enter a username that's between 3 and 20 characters."
                username=''

    for char in password:
        if char.isspace():
            password_error = "Your password cannot contain spaces."
            password = ""
        elif not password:
            password_error = "Please, enter a password."
            password = ''
        else:
            if (len(password) < 3) or (len(password) > 20):
                password_error = "Please, enter a password that's between 3 and 20 characters."
                password=''

    if not name_error and not password_error:
        return redirect('/success?username={0}'.format(username))
    
    return render_template('form.html', name_error=name_error, password_error=password_error, username=username, password=password) 
    #if password != password2:
        #password2_error = "Your passwords muust match."

@app.rute('/success')
def success():
    title = "Hello!"
    username = request.form['username']
    return render_template('success.html', title=title, usersname=username)

if __name__ == '__main__':
    app.run()