from flask import Flask
from ZoteRulesGiver import get_rule_by_id, get_random_rule
app = Flask(__name__)

@app.route("/")
def random_rule():
    return get_random_rule()

@app.route("/<int:id>")
def rule_by_id(id):
    return get_rule_by_id(id)

if __name__ == "__main__":
    app.run()
