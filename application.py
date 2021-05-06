from flask import Flask
import pymysql
import mysql.connector

# conn = pymysql.connect(
#         host= 'rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com', 
#         port = 3306,
#         user = 'admin', 
#         password = '1forall!',
#         db = 'rds-mysql-bambook'    
#         )

# db = mysql.connector.connect(
#     host= 'rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com', 
#     port = 3306,
#     user = 'admin', 
#     passwd = '1forall!',
#     db = 'rds-mysql-bambook'
# )

# mycursor = db.cursor()

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM users")
    details = cur.fetchall()
    return details