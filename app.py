from flask import Flask, render_template
from sys_config import run_neofetch_ext

app = Flask(__name__)

@app.route('/system')
def index():
    result = run_neofetch_ext()
    print(type(result))
    return render_template('system.html', result=result)

if __name__ == '__main__':
    app.run()
