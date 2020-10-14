#!flask/bin/python
from flask import Flask, render_template, url_for
import numpy as np
from model import create_field, init_agents, model

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    url_for('static', filename='style.css')
    return render_template('index.html')


@app.route('/upload_red', methods=['GET'])
def get_red():
    ag, _, _, _ = model(agents, agent_matrix)
    tmp = [{"x": c[0], "y": c[1]} for c in ag]
    return {"data": tmp}


@app.route('/upload_blue', methods=['GET'])
def get_blue():
    global agents, agent_matrix
    _, ag, agents, agent_matrix = model(agents, agent_matrix)
    tmp = [{"x": c[0], "y": c[1]} for c in ag]
    return {"data": tmp}


if __name__ == '__main__':
    # params initialization
    n = 50
    ratio = 0.7
    tot_size = n * n
    sat = 0.4
    empty = 0.4
    emp = int(tot_size * empty)
    a_num = int((tot_size - emp) * ratio)
    b_num = int((tot_size - emp) * (1 - ratio))

    agent_matrix = create_field(n)
    agents = []

    agent_matrix, agent = init_agents(agents, a_num, 0, agent_matrix)
    agent_matrix, agent = init_agents(agents, b_num, 1, agent_matrix)
    app.run(port=80)
