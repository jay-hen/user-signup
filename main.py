from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['debug'] = True

@app.route("/", methods=['get'])
def index():
    title = 'Signup'
    return render_template('form.html', title='', username='', name_error='', password='', password_error="", verify='', verify_error='', email='', email_error='')

@app.route('/signup', methods=['post'])
def validate_form():
    title = 'Signup'
    print("got title")

    username = cgi.escape(request.form['username'])
    print("got username")

    password = cgi.escape(request.form['password'])
    print("got password")

    verify = cgi.escape(request.form['verify'])
    print("got verify")

    email = cgi.escape(request.form['email'])
    print("got email")

    name_error = ""
    password_error = ''
    verify_error = ''
    email_error = ''

    if not username:
        print("Please, enter a username.")
        name_error = "Please, enter a username."
    elif len(username) < 3 or len(username) > 20:
        name_error = "Your username must be between 3 and 20 characters."
    else:
        print("testing username")

        for char in username:
            if char.isspace():
                name_error = "Your username cannot contain spaces."

    print("testing password")

    if not password:
        name_error = "Please, enter a password."
    elif len(password) < 3 or len(password) > 20:
        name_error = "Your password must be between 3 and 20 characters."
    else:
        for char in password:
            if char.isspace():
                password_error = "Your password cannot contain spaces."
    print("testing verify")
    
    if password != verify:
        verify_error = "Your passwords need to match."

    if not email:
        email_error = "Please, enter an email."

        at == 0
        period == 0

        for char in email:
            if char == "@":
                at += 1
            else:
                if at != 1:
                    email_error = "You email cannot contain spaces and must include a '.' and a '@'."
            if char == ".":
                period += 1
            else:
                if period != 1:
                    email_error = "You email cannot contain spaces and must include a '.' and a '@'." 
            if char.isspace():
                email_error = "You email cannot contain spaces and must include a '.' and a '@'."
    print("testing email")
    

    if not name_error and not password_error and not verify_error and not email_error:
        print("doing a redirect")
        return redirect('/success?username=' + username)
        
    return render_template('form.html', title=title, username=username, name_error=name_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error) 

@app.route('/success', methods=['get'])
def success():
    title = "Hello!"
    username = request.args.get("username")
    return render_template('success.html', title=title, username=username)
    

if __name__ == '__main__':
    app.run()