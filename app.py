from flask import Flask, render_template, request
import json
import os
import random

app = Flask(__name__)


def load_shows():
    shows = []

    for filename in os.listdir("shows"):
        if filename.endswith(".json"):
            path = os.path.join("shows", filename)
            with open(path, "r") as file:
                shows.append(json.load(file))

    return shows


@app.route("/", methods=["GET", "POST"])
def home():
    shows = load_shows()
    selected_show = None
    selected_episode = None
    selected_color = "#2563eb"

    if request.method == "POST":
        show_name = request.form.get("show")

        for show in shows:
            if show["show"] == show_name:
                selected_show = show_name
                selected_episode = random.choice(show["episodes"])
                selected_color = show.get("color", "#2563eb")
                break

    return render_template(
        "index.html",
        shows=shows,
        selected_show=selected_show,
        selected_episode=selected_episode,
        selected_color=selected_color,
    )