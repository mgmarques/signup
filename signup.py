# -*- coding: utf-8 -*-
"""
Regular Expressions

A regular expression is a handy tool for matching text to a pattern. 
The regular expressions that we're using to validate you input are as follows:
"""

import re

# Username: "^[a-zA-Z0-9_-]{3,20}$"
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
  
def valid_username(username):
  return USER_RE.match(username)

# Password: "^.{3,20}$"
Password_RE = re.compile(r"^.{3,20}$")
  
def valid_password(password):
  return Password_RE.match(password)

# Email: "^[\S]+@[\S]+.[\S]+$"
Email_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
  
def valid_email(email):
  return Email_RE.match(email)

user = "xxx"
v_user = valid_username(user) is not None
if user:
    if (v_user):
        print("valid")
    else:
        print("That's not a valid username.")
        
password = "xxx"
v_pass = valid_password(password) is not None
if password:
    if (v_pass):
        print("valid")
    else:
        print("That wasn't a valid password.")
        
verify = "xxx"
v_verify = valid_password(verify) is not None
if verify:
    if (v_verify):
        print("valid")
    else:
        print("That wasn't a valid password.")

check = password == verify
if not check:
    print("Your passawords didn't match.")
    
email = ""
if email:
    v_email = valid_email(email) is not None
    if (v_email):
        print("valid")
    else:
        print("That's not a valid email")
else:
    v_email = True
        
if (v_user & v_pass & v_verify & v_email & check):
    print("Welcome, %(user)s" % {"user": user})