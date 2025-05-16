import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8383))
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(host="0.0.0.0", port=port)
