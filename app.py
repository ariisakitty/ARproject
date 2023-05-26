from flask import Flask, render_template
from sys_config import run_neofetch_ext

app = Flask(__name__)

@app.route('/system')
def index():
    result = run_neofetch_ext()
    #{"OS": "Ubuntu 20.04.6 LTS x86_64", "Host": "20QES4T601 ThinkPad X1 Carbon 7th", "Kernel": "5.15.0-72-generic", "Shell": "bash 5.0.17", "CPU": "Intel i7-8665U (8) @ 4.800GHz", "GPU": "Intel UHD Graphics 620", "MEM (Used/Total)": "15.28GB / 16.69% used", "SSD (Used/Total)": "467.89GB / 8.65% used"}
    print(type(result))
    return render_template('system.html', result=result)

if __name__ == '__main__':
    app.run()
