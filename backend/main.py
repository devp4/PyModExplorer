from flask import Flask, request
from Visitor import Visitor, getTreeFromModule, getTreeFromSourceCode

app = Flask(__name__)
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#flask --app main run

@app.route("/parse", methods=['POST'])
@cross_origin()
def parse_module():
    module = request.json["name"]
    content = request.json["content"]

    visitor = Visitor(module)

    tree = getTreeFromSourceCode(content)
    visitor.visit(tree)

    return visitor.data