from flask import Flask, Blueprint, render_template
from greenhaus.main import do_shutdown, change_setting, water, light, camera_capture, create_video

#welcome to hell

app = Flask(__name__)

@app.route("/")
def main_page():
	return render_template("mainpage.html")

@app.route("/settings")
def change_setting_step1():
	return render_template("change_setting/step1.html")
  
@app.route("/photography")
def photogaphy_cameracontrol():
	return render_template("photography/cameracontrol.html")

@app.route("/water")
def water_beds():
	return render_template("water/beds.html")

@app.route("/water")
def light_lights():
	return render_template("light/lights.html")
