from flask import Flask, render_template
from datetime import datetime
# from sys_config import run_neofetch_ext

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wiki')
def wiki():
    return render_template('wiki.html')

@app.route('/robots')
def robots():
    return render_template('robots.html', robot=None)

@app.route('/robots/dcr1')
def DCR1():
    # result = run_neofetch_ext()
    sys_info = {
        "OS": "Ubuntu20.04",
        "CPU": "Intel",
        "GPU": "Nvidia",
        "Memory": "8GB",
        "Storage": "956GB",
        "Lidar IP": "192.168.1.10"
    }

    sys_status = {
        "Comm": "Connected",
        "Power": "On",
        "Lidar": "Connected",
        "RGB1": "Connected",
        "RGB2": "Disconnected",
        "Thermal": "Connected",
        "INS": "Connected",
        "Memory": "14% used",
        "Storage": "4.5% used"
    }

    robot_app_status = {
        "AD": "On",
        "Mission": "Off",
        "Postion (lon, lat)": "128.3, 46.5",
        "Velocity (mph)": "0",
        "lidar_grabber": "On 10Hz",
        "rgb_grabber1": "On 9.6Hz",
        "localization": "Off",
        "object_detector": "Off"
    }

    robot_coord = { 
        "lat": 39.049363, 
        "lng": -84.654340 
    }
    
    time_checked = datetime.now().strftime("%B %dth, %Y %I:%M%p")

    return render_template('robots.html', time_checked=time_checked, robot="DCR1", sys_info=sys_info, sys_status=sys_status, robot_app_status=robot_app_status, robot_coord=robot_coord)

@app.route('/robots/dcr2')
def DCR2():
    # result = run_neofetch_ext()
    sys_info = {
        "OS": "Ubuntu20.04",
        "CPU": "AMD",
        "GPU": "Nvidia",
        "Lidar IP": "192.168.1.20"
    }

    sys_status = {
        "Comm": "Disconnected",
        "Power": "On",
        "Lidar": "Connected",
        "RGB1": "Connected",
        "RGB2": "Disconnected",
        "Thermal": "Connected",
        "INS": "Connected",
        "Memory": "14% used",
        "Storage": "4.5% used"
    }

    robot_app_status = {
        "AD": "On",
        "Mission": "On",
        "Postion (lon, lat)": "128.3, 46.5",
        "Velocity (mph)": "3",
        "lidar_grabber": "On 10Hz",
        "rgb_grabber1": "On 9.6Hz",
        "localization": "Off",
        "object_detector": "Off"
    }

    robot_coord = { 
        "lat": 39.05386673013814, 
        "lng": -84.65436215509604 
    }
    
    time_checked = datetime.now().strftime("%B %dth, %Y %I:%M%p")

    return render_template('robots.html', time_checked=time_checked, robot="DCR2", sys_info=sys_info, sys_status=sys_status, robot_app_status=robot_app_status, robot_coord=robot_coord)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)
