# Flask Email Verification

<p align=center>
	<img src="https://github.com/Xenia101/Flask-Email-Authentication/blob/master/img/email_verification.png?raw=true">
</p>

Flask based Email Verification, Used in [WITHME](http://www.withme.xyz/info) 

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
    
  # DB user.activate = True
  # User  = data['username']
```

- example of email

```python
# href in Email
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
  - Python **3.6**

