from flask import Flask, request, redirect, render_template
import cgi
import os
# import jinja2
import string


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html',username_error = "")


@app.route('/sign-up', methods=['POST'])
def validate_fields():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    e_mail = request.form['email']

    username_error = ""
    password_error = ""
    e_mail_error = ""

    # letter_check = string.ascii_letters
    # punctuation_check = string.punctuation
    # print(letter_check)


    # for letter in username:
    #     if letter not in letter_check or letter not in punctuation_check:
    #         username_error = "You can't put spaces here! How dare you?!?!?"
    #     else:
    #         return render_template('/home.html', password_error = username_error)

    error = False
        
    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "I can't deal with incompetent people like you!"
        username = ""
#        return render_template('/home.html', username_errorhtml = username_error)
        error = True
   
    # for letter in password:
    #     if letter not in letter_check or letter not in punctuation_check:
    #         password_error = "You can't put spaces here! How dare you?!?!?"
    #     else:
    #         return render_template('/home.html', password_error = password_error) 

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "I can't deal with incompetent people like you!"
        password = ""
        error = True

    if verify_password == "" or password != verify_password:
        verification_error = "And just what do you think you're doing?!"
        verify_password = ""
#        return render_template('/home.html', verification_errorhtml = verification_error)
        error = True

    if e_mail == "" or "@" not in e_mail or "." not in e_mail or len(e_mail) < 3 or len(e_mail) > 20:
        e_mail_error = "How dare you?!"
        e_mail = ""
#        return render_template('/home.html', e_mail_errorhtml = e_mail_error)
        error = True

    if error == False:
        return render_template('/welcome.html', the_name = username)

    return render_template('/home.html', username_errorhtml = username_error, password_errorhtml = password_error, verification_errorhtml = verification_error, e_mail_errorhtml = e_mail_error, username = username, email = e_mail)

    #    redirect ('/welcome?username={0}'.format(username))


    # if password == "":
    #     password_error = "You can't just leave this box empty like that!"

    # elif len(password) < 3 or len(password) > 20:
    #     password_error = "That doesn't work."

    # letter_check = string.ascii_letters
    # for letters in password:
    #     if letters not in letter_check:
    #         password_error = "You can't put spaces here! How dare you?!?!?"
    # else:
    #     redirect ('/welcome?username={0}'.format(username))
    
    # if verify_password == "":
    #     verification_error = "You can't just leave this box empty like that!"

    # elif password != verify_password:
    #     verification_error = "Uh oh! Those don't match."

    # else:
    #     redirect ('/welcome?username={0}'.format(username))

    # if e-mail == "":
    #     e-mail_error = "You can't just leave this box empty like that!"


    # elif "@" not in e-mail or "." not in e-mail or len(e-mail) < 3 or len(e-mail) > 20:
    #     e-mail-error = "Uh oh!  That's not an e-mail.  Please try again."

    # else:
    #     redirect ('/welcome?username={0}'.format(username))

# @app.route('/welcome', methods=['POST'])
# def welcome_page():
#     return render_template('welcome.html', the_name=username)

app.run()