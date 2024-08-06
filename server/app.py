from flask import Flask, request, make_response
from model import rf, crawl
import re
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/fade', methods=["GET"])
def api():
    username = request.args.get('username')
    pattern = re.compile(r'[^a-z\d._]')
    if len(username) > 30 or pattern.search(username):
        return make_response("hacker...", 400)
    result = rf.predict(crawl.get_user_info(username))
    result = "true" if result == 0 else "false"
    return make_response(result, 200)

if __name__ == "__main__":
    app.run("0.0.0.0",80)