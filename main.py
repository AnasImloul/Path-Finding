import cv2
import numpy as np
from Graph import Graph
import matplotlib.pyplot as plt


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)


def image_to_grid(img):
    "convert an image to a grid of 0 and 255 and set the intesnity as the max of the 3 channels"
    grid = np.max(img, axis=2)
    # set the intensity to 0 or 255
    grid = cv2.threshold(grid, 192, 255, cv2.THRESH_BINARY)[1]
    return grid


def grid_to_image(grid):
    img = cv2.cvtColor(grid, cv2.COLOR_GRAY2BGR)
    return img


def draw_path(img, path):
    plt.imshow(img, cmap="gray")
    plt.plot([x for x, _ in path], [y for _, y in path], "r-")
    plt.show()


def grid_to_graph(grid):
    return Graph(grid)


def find_depart(img):
    # find the first red pixel
    try:
        y, x = np.argwhere(np.all(img == RED, axis=-1))[0]
        return x, y
    except:
        return None


def find_arrivee(img):
    # find the first green pixel
    try:
        y, x = tuple(np.argwhere(np.all(img == GREEN, axis=-1))[0])
        return x, y
    except:
        return None

def solve(img):
    grid = image_to_grid(img)
    graph = grid_to_graph(grid)

    depart = find_depart(img)
    arrivee = find_arrivee(img)

    path = graph.a_star(depart, arrivee)

    print(graph.cost(path))
    draw_path(img, path)


#get image path from command line

import sys

path = sys.argv[1]

img = cv2.imread(path)
solve(img)
