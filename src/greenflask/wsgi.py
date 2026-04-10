from flask import Flask
from greenhaus.main import do_shutdown, change_setting, water, light, camera_capture, create_video

#welcome to hell

app = Flask(__name__)

@app.route("/")
def stuck_in_the_ninties():
  return "<p>We're stuck in the ninties.<p>"
