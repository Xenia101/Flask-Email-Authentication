from flask import Flask, render_template, request, redirect, url_for, session, escape, flash, jsonify
from datetime import datetime
import random
import time
import os

from config import BaseConfig
from utils import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/signup',methods = ['POST', 'GET'])
def signup():
	if request.method == 'POST':
		email = request.form['email']
                session['email'] = email
		send_confirmation_mail(email, id)

		return redirect(url_for('home'))
	else:
		return render_template("signup.html")

@app.route('/confirm/<token>')
def confirm_email(token):
	try:
		data = confirm_token(token)
	except:
		flash('이메일 인증 토큰이 만료되었습니다!', 'danger')
		return redirect(url_for('home'))

	flash('이메일 인증에 성공했습니다!!', 'primary')
	return redirect(url_for('home'))

@app.route('/resend')
def resend_confirmation():
	send_confirmation_mail(session['email'], session['username'])

if __name__ == "__main__":
	app.run(host='', port=80) 

