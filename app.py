from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Temporary storage for user details (replace with a database in a real application)
user_details = {}


@app.route('/')
def registration_page():
    return render_template('registration.html')


@app.route('/process_details', methods=['POST'])
def process_details():
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    # Store user details
    user_details[username] = {
        'password': password,
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }

    return redirect(url_for('display_info', username=username))


@app.route('/display_info/<username>')
def display_info(username):
    user_info = user_details.get(username, {})
    return render_template('display_info.html', user_info=user_info)


@app.route('/retrieve_info', methods=['GET', 'POST'])
def retrieve_info():
    if request.method == 'POST':
        entered_username = request.form['username']
        entered_password = request.form['password']

        # Check if username and password match
        if entered_username in user_details and user_details[entered_username]['password'] == entered_password:
            user_info = user_details[entered_username]
            return render_template('display_info.html', user_info=user_info)

    return render_template('retrieve_info.html')


if _name_ == '_main_':
    app.run(debug=True)
