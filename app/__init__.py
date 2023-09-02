from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__,
            static_folder="static",
            static_url_path="/static",
            )

bootstrap = Bootstrap5(app)
