from flask import Flask, Blueprint, render_template
from greenhaus.main import do_shutdown, change_setting, water, light, camera_capture, create_video

#welcome to hell

app = Flask(__name__)

@app.route("/")
def main_page():
  return render_template("mainpage.html")
