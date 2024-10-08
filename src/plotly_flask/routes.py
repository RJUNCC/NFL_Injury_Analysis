from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Landing page"""
    return render_template(
        "index.jinja2",
        title="NFL Injury Analysis Home Page",
        description="NFL injury main metrics",
        template="home-template",
        body="NFL Injury Analysis",
    )