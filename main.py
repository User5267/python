from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return 'login'
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


@app.route('/iam')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    # if key doesn't exist, returns a 400, bad request error
    framework = request.args['framework']
    # if key doesn't exist, returns None
    website = request.args.get('website')
    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
if __name__ == '__main__':
   app.run()