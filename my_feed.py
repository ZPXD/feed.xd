from flask import Flask, render_template, url_for, redirect

from pyfacebook import GraphAPI
from pyfacebook.api.facebook.client import FacebookApi

from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/xddd.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = ':)'

db = SQLAlchemy(app)



key_file = 'keys/facebook_key'

my_name = 'Łukasz Pintal'
use_real_name = True


@app.route('/')
def index():
	posts = Post.query.all() # recode
	return render_template("index.html", posts=posts)

@app.route('/get_new_posts')
def get_my_new_posts():
	read_own_wall()
	return redirect(url_for('index'))




def read_keys():
	key = open(key_file).read()
	return key

def read_own_wall():
	key = read_keys()
	api = GraphAPI(access_token=key)
	MY_data = api.get_connection("me", "posts")
	post_ids = [post.id for post in Post.query.all()]
	for i, post in enumerate(MY_data['data']):

		if str(post['id']) not in post_ids:

			msg = post.get('message', '')
			post_id = str(post.get('id', None))
			created_at = post.get('created_time', 'None')
			
			post = Post(msg=msg, post_id=post_id, created_at=created_at, author=my_name)
			db.session.add(post)
			db.session.commit()





class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(120))
	msg = db.Column(db.String(120))
	post_id  = db.Column(db.String(120))
	created_at = db.Column(db.String(120))


@app.before_first_request
def create_all():
    db.create_all()


if __name__=="__main__":
	app.run(debug=True)