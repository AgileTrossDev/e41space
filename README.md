#E41

Evolving microblog powered by a Python and Flask.


##INSTALL

```
python -m venv venv
pip-compile requirements.in
pip-compile requirements-dev.in
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

##Execution
`bin/launch`


##Database
`bin/db_update`


##REFERENCE:

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world


##Development Tricks

**Open Flask Shell**
```
export FLASK_APP=e41.py
flask shell
```

**Emulated email server**

`python -m smtpd -n -c DebuggingServer localhost:8025`
