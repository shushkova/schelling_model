import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from agent import Agent
import time

"""# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')

# Initialize an instance of Tk
root = tk.Tk()

# Initialize matplotlib figure for graphing purposes
fig = plt.figure(1)

# Special type of "canvas" to allow for matplotlib graphing
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

# Add the plot to the tkinter widget
plot_widget.grid(row=0, column=0)"""

def create_field(n):
    agent_matrix = [0] * (n + 2)
    for i in range(n + 2):
        agent_matrix[i] = [0] * (n + 2)
    return agent_matrix


def init_agents(agents, num, type, agent_matrix, n=50):
    for i in range(num):
        ag = Agent(type, n)
        agents.append(ag)
        loc = ag.get_location()
        while (agent_matrix[loc[0]][loc[1]] != 0):
            ag.change_location(n)
            loc = ag.get_location()
        agent_matrix[loc[0]][loc[1]] = ag

    return agent_matrix, agents



def updateGraph(ag0, ag1, title, n, i):
    """Example function triggered by Tkinter GUI to change matplotlib graphs."""
    # global currentGraph
    # plt.clf()
    fig, ax = plt.subplots()
    # Clear all graphs drawn in figure
    #plt.clf()

    x0, y0 = zip(*ag0)
    x1, y1 = zip(*ag1)
    ax.scatter(x0, y0, color='b', marker='s')
    ax.scatter(x1, y1, color='r', marker='s')

    """for agent in agents:
        loc = agent.get_location()
        ax.scatter(loc[0], loc[1], color=agent_colors[agent.ag_type], marker='s')"""

    ax.set_title(f'Satis = {title}', fontsize=10, fontweight='bold')
    ax.set_xlim([0, n])
    ax.set_ylim([0, n])
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.savefig(file_name)
    plt.savefig(f'pictures/plot_{i}.png')
    # plt.show()
    # fig.canvas.draw_idle()
    # plt.plot(x,y)
    # fig.canvas.draw()
    # plt.close()


def plot(ag0, ag1, title, i):
    fig, ax = plt.subplots()
    agent_colors = {1: 'b', 0: 'r'}

    x0, y0 = zip(*ag0)
    x1, y1 = zip(*ag1)
    ax.scatter(x0, y0, color='#A7BD3F', marker='s')
    ax.scatter(x1, y1, color='#000000', marker='s')

    ax.set_title(f'Satisfaction = {title}', fontsize=10, fontweight='bold')
    ax.set_xlim([0, n])
    ax.set_ylim([0, n])
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.savefig(file_name)
    plt.savefig(f'pictures/plot_{i}.png')
    # plt.show()
    # fig.canvas.draw_idle()


def model(agents, agent_matrix, n=50):
    changes = 1
    i = 0
    sat = 0.3
    cnt_sat = 0
    agent_matrix_new = create_field(n)
    agents_new = []
    ag1 = []
    ag0 = []
    for agent in agents:
        loc = agent.get_location()

        if agent.get_type() == 0:
            ag0.append(loc)
        else:
            ag1.append(loc)

        res = 0
        neigbors = [agent_matrix[loc[0] - 1][loc[1] - 1], agent_matrix[loc[0] - 1][loc[1]],
                    agent_matrix[loc[0] - 1][loc[1] + 1], agent_matrix[loc[0]][loc[1] - 1],
                    agent_matrix[loc[0]][loc[1] + 1], agent_matrix[loc[0] + 1][loc[1] - 1],
                    agent_matrix[loc[0] + 1][loc[1]], agent_matrix[loc[0] + 1][loc[1] + 1]]
        for neib in neigbors:
            if neib == 0:
                continue
            res += agent.satisfaction(neib)
        if res / 8. >= sat:
            agent.satisf = 'Yes'
            cnt_sat += 1
            agent_matrix_new[loc[0]][loc[1]] = agent
        else:
            agent.satisf = 'No'
            agent.change_location(n)
            loc = agent.get_location()
            while (agent_matrix_new[loc[0]][loc[1]] != 0):
                agent.change_location(n)
                loc = agent.get_location()
            agent_matrix_new[loc[0]][loc[1]] = agent
            changes = 1

        agents_new.append(agent)

        # sat = cnt_sat /len(agents)
        # x0, y0 = zip(*ag0)
        # x1, y1 = zip(*ag1)
        # print(ag1)

    return ag0, ag1, agents, agent_matrix
    # plot(ag0, ag1, cnt_sat / len(agents), i)


# root.mainloop()