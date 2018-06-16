import os
import jinja2    # jinja.pocoo.org
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
				autoescape = True )
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

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):	
	self.render("signup.html", username="", password="", verify="", email="",
		    user_err="", pass_err="", ver_err="", email_err="")

    def post(self):

	username = self.request.get("username")
	v_user = valid_username(username) is not None
	user_err = "That's not a valid username."
	if username:
	    if v_user:
		user_err = ""
		
		
	password = self.request.get("password")
	v_pass = valid_password(password) is not None
        pass_err = "That wasn't a valid password."
	if password:
	    if (v_pass):
		pass_err = ""
		
	verify = self.request.get("verify")
	v_verify = valid_password(verify) is not None
	ver_err = ""
	if verify:
	    if not (v_verify):
		ver_err = "That wasn't a valid password."

	check = False
	if (v_pass):
	    check = password == verify
	    if not check:
	        ver_err = "Your passawords didn't match."
	    
	email = self.request.get("email")
	email_err = ""
	if email:
	    v_email = valid_email(email) is not None
	    if not (v_email):
		email_err = "That's not a valid email"
	else:
	    v_email = True
	    email_err = ""
		
	if (v_user & v_pass & v_verify & v_email & check):
	   self.render("welcome.html", username = username)
	else:
	    self.render("signup.html", username = username, user_err = user_err,
		        password = "", pass_err = pass_err,
			verify = "", ver_err = ver_err,
			email = email, email_err = email_err)

app = webapp2.WSGIApplication([('/', MainPage),
			      ],
			     debug=True)
