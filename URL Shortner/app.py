import json
import random

from flask import Flask, flash, jsonify, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'to_be_added_later_in_env'


class URLForm(FlaskForm):
    url = StringField('URL')
    submit = SubmitField('Shorten URL')

with open('urls.json', 'r') as f:
    data = json.load(f)

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        url = form.url.data
        short_code = ''.join(random.choice(letters) for i in range(6))
        while short_code in data:
            short_code = ''.join(random.choice(letters) for i in range(6))
        data[short_code] = url
        with open('urls.json', 'w') as f:
            json.dump(data, f)
        link = f'{request.host_url}{short_code}'
        return render_template('index.html', form=form, link=link)

    return render_template('index.html', form=form)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = data.get(short_code)
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)