# Flask Email Verification

Flask based Email Verification, Used in [WITHME](http://www.withme.xyz) 

## EXAMPLE

- import modules ```config.py``` ```utils.py```
```python
from config import BaseConfig
from utils import *
```

- mail server (SMTP:587)

```python
MAIL_SERVER = 'smtp.gmail.com:587'
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

- example of email

```python
http://www.example.com/confirm/eyJlbWFpbCI6ImxvbW15MTAxQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoicXdlcXdlIn0.XkA0IQ.3izTIkyiiMuTHvEi2BVmbW7QJYo

token = "eyJlbWFpbCI6ImxvbW15MTAxQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoicXdlcXdlIn0.XkA0IQ.3izTIkyiiMuTHvEi2BVmbW7QJYo"
```

- resend a verify email

```python
@app.route('/resend')
def resend_confirmation():
	send_confirmation_mail(session['email'], session['username'])
```

## Execution / Test Environment
  - Ubuntu Linux
  - Python3.x

