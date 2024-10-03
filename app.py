from flask import Flask, render_template
from models import Student, session

app=Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    Students = session.query(Student).all()
    return render_template('index.html', x=Students)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

if __name__=="__main__":
    app.run(debug=True,port=5001)  