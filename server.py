from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')                             # This function goes to the home page of http://127.0.0.1:5000
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')           # This function replaces all of the individual functions (below)
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankYou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong.  Try again!'

# Function for writing to database text file used by Flask server for the email form data
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# Function for writing to database csv file used by Flask server for the email form data
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# @app.route('/works.html')
# def work():
#     print(url_for('static', filename='middle_finger.ico'))
#     return render_template('works.html')
#
# @app.route('/about.html')
# def about():
#     print(url_for('static', filename='middle_finger.ico'))
#     return render_template('about.html')
#
# @app.route('/contact.html')
# def contact():
#     print(url_for('static', filename='middle_finger.ico'))
#     return render_template('contact.html')
#
# @app.route('/components.html')
# def components():
#     print(url_for('static', filename='middle_finger.ico'))
#     return render_template('components.html')

