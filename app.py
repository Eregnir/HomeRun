from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import calc

application = Flask(__name__, '/static')
CORS(application)


@application.route('/calculations', methods=['POST'])
@cross_origin()
def time_spent_on_event():
    return calc.done_df


#################### Configure DB: ####################
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:1forall!@rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com/Bambook'
##need to initialize an engine 
##need connection
# db = SQLAlchemy(application)
# engine = create_engine('mysql+pymysql://admin:1forall!@rds-mysql-bambook.cqjurd0qbtdg.eu-central-1.rds.amazonaws.com/Bambook')
#################### DB Models ####################

# class People(db.Model):
#     id = db.column(db.Integer, primary_key=True)
#     name = db.column(db.String(200), nullable=False)
#     email = db.column(db.String(200), nullable=False, unique=True)

#     #create A string
#     def __repr__(self):
#         return '<Name %r>' % self.name

#################### Application Routes ####################
@application.route('/')
def index():
    return render_template('pages/index.html')


@application.route('/login')
def home2():
    return render_template('pages/login.html')
    

@application.route('/test')
def test():
    return render_template('pages/TestPage.html')

@application.route('/o')
def cart():
    return render_template('pages/Overview.html')

@application.route('/a')
def bookshelf():
    return render_template('pages/dashboard.html')

@application.route('/b')
def b():
    return render_template('pages/welcome.html')

@application.route('/c')
def c():
    return render_template('pages/login.html')

@application.route('/pages')
def pages():
    return render_template('cart.html')

@application.route('/reading')
def reading():
    return render_template('reading.html')

@application.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    application.run()

