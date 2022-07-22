import re
from flask import Flask, render_template, request
import script

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/submit/", methods=["POST"])
def submit_page():
    text = request.form["id"]
    script.script()

    # On récupère l'ID de la vod twitch
    id = script.getId(text)
    vod_twitch_link = f"https://twitch.tv/videos/{id}"

    vod_stream = "https://dgeft87wbj63p.cloudfront.net/784b27637229235cde51_sheisoutv_39642508424_1658264233/chunked/index-dvr.m3u8"

    return render_template("submit.html", ID=id, VOD_TWITCH_LINK=vod_twitch_link, VOD_STREAM=vod_stream)


if __name__ == "__main__":
    app.run(debug=True)
