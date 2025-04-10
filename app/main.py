import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from routes import content_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(content_bp)

@app.route("/")
def home():
    return "<h1>Bienvenue sur la plateforme de diffusion de contenu</h1>"


if __name__ == "__main__":
    print("la chance n'existe pas")
    app.run(debug=True, host="0.0.0.0", port=5000)

