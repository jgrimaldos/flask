from flask import Flask, request, render_template, session
app = Flask(__name__)
app.secret_key = 'u\x91\xa1r#\x9e\xea\xd1\xb2D\x88pG\x98\x17\xe0'

@app.route('/')
@app.route('/oauth2/callback')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['POST'])
def authorized():
	session['auth_id'] = request.form['auth']
	return render_template('auth.html')

if __name__ == '__main__':
    app.run(debug=True)