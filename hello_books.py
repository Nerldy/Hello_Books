from flask import Flask, render_template

app = Flask(__name__)


# user sign up
@app.route('/user/signup')
def user_sign_up():
	return render_template('user-sign-up.html', title='Sign Up')


# user sign in
@app.route("/user/signin")
def user_sign_in():
	return render_template('user-sign-in.html', title='Sign In')


# user home
@app.route('/user/home')
def user_home():
	return render_template('user-home.html', title='My Library')


# admin dashboard
@app.route('/admin/home')
def admin_home():
	return render_template('admin-dashboard.html', title='Admin Home')


if __name__ == '__main__':
	app.run(debug=1)
