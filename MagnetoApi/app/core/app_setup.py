from ..api import api  # noqa
from ..main import app


@app.route("/")
def hello():
    # This could also be returning an index.html
    return """Magneto api endpoint GET: <a href="/mutant/">/mutant/</a>"""
