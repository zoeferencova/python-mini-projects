import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(f'{page_name}.html')


def write_to_file(data):
    with open('database.txt', encoding='utf-8', mode='a') as database:
        database.write(f'\n{ data["text"] }')


def write_to_csv(data):
    with open('database.csv', encoding='utf-8', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['text']])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou')
    else:
        return 'something went wrong'
