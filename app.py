from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)


import os
import json

def load_shows():
    shows = []

    for filename in os.listdir("shows"):
        if filename.endswith(".json"):
            with open(f"shows/{filename}", "r") as file:
                shows.append(json.load(file))

    return shows

@app.route("/", methods=["GET", "POST"])
def home():
    shows = load_shows()
    selected_show = None
    selected_episode = None

    if request.method == "POST":
        show_name = request.form.get("show")

        for show in shows:
            if show["show"] == show_name:
                selected_show = show_name
                selected_episode = random.choice(show["episodes"])
                break

    return render_template(
        "index.html",
        shows=shows,
        selected_show=selected_show,
        selected_episode=selected_episode,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)