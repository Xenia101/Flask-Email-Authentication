# Flask Email Verification

Flask based Email Verification

## EXAMPLE

- import modules ```config.py``` ```utils.py```
```python
from config import BaseConfig
from utils import *
```

- sign up page for send confirmation mail

```python
@app.route('/signup',methods = ['POST', 'GET'])
def signup():
  if request.method == 'POST':
    session['email'] = email
    send_confirmation_mail(email, id)
    return redirect(url_for('home'))
```

- confirm token by email

```python
@app.route('/confirm/<token>')
def confirm_email(token):
  try:
    data = confirm_token(token)
  except:
    return redirect(url_for('home'))
```

- resend a verify email

```python
@app.route('/resend')
def resend_confirmation():
	send_confirmation_mail(session['email'], session['username'])
```
