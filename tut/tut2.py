from bottle import template, static_file, request, response, abort, redirect, run
from bottle import route, get, post

PORT = 8081


@route("/")  # The route decorator serves as a hook for linking / to home()
def home():
    return '<html><body> Hello! </body></html>'


@route("/home/<name>")  # Dynamic route, matches /home/Alice, /home/Bob, etc.
def home2(name):
    return f"<html><body> Hello {name}! </body></html>"


@route("/greeting")
@route("/home2/<name>")
# Multiple routes can be mapped to the same callback function
def greeting(name="Stranger"):
    return f"<html><body> Hello {name}! </body></html>"


@route("/static/<filename:re:.*\\.html>")  # regex to match any .html file
def static(filename):
    # Read file from the static/ subdirectory
    return static_file(filename, root='static')


@get("/login")  # This is equivalent to @route("/login")
def login():
    return static_file('login.html', root='static')


@post("/login")
def process_login():
    # Process the form data
    username = request.forms.get('username')
    password = request.forms.get('password')
    # Echo back the username and password
    return f"<html><body> Hello {username}! PW:{password} </body></html>"


@route("/restricted")
def restricted():
    abort(401, "You are not allowed to access this page.")


@route("/wrong")
def wrong():
    redirect("/")  # Go back to home page


@route("/cookie")
def hello_cookie():
    if request.get_cookie("visited"):
        return f"Welcome back! Nice to see you again (cookies = {request.get_cookie("visited")})"
    else:
        response.set_cookie("visited", "yes")
        return "Hello! Nice to meet you!"


@route("/template")
def template_demo():
    # You can pass variables as keyword arguments
    tpl = template("Hello {{name}}", name="World")
    # You can also unpack a dictionary into keyword arguments
    dict = {"dept": "ECE", "code": "ECE326"}
    tpl2 = template("Department {{dept}} Course Code:{{code}}", **dict)
    return tpl + '</br>' + tpl2


@route("/template2")
def template_demo2():
    basket_list = ["A", "B", "C"]
    # You can also specify the template file directly
    return template("tpl.html", basket=basket_list)


run(host='localhost', port=PORT, reloader=True)
