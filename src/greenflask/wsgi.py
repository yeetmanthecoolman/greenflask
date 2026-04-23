#    The main file of the Greenflask programme.
#    Copyright (C) 2026 Frank J. Barth

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
