from app import app  # Could cause circular dependancy issues

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
