import argparse
import logging
import pygame
import threading
import numpy as np
from BouncingBall import BouncingBall
from utils import *
from matplotlib import pyplot as plt

'''
Solution for the problem 'Bouncing ball with air resistance (7.4.1)'
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', default=0.2, type=float, help='Mass of the ball')
    parser.add_argument('-R', default=0.1, type=float, help='Radius of the ball')
    parser.add_argument('-h0', default=2.0, type=float, help='Initial height')
    parser.add_argument('-v0', default=10.0, type=float, help='Initial speed')
    parser.add_argument('-t', default=20.0, type=float, help='How many seconds will ball bounce')
    parser.add_argument('-dt', default=0.001, type=float, help='Step for Euler-Cromer method')
    parser.add_argument('-v_term', default=10.0, type=float, help='Terminating speed of the ball')
    parser.add_argument('-k', default=1000.0, type=float, help='Coefficient of the string')
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)23s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)
    ball = BouncingBall(logger, args.m, args.R, args.h0, args.v0,
                        args.t, args.dt, args.v_term, args.k)

    singleton_plot(ball, 3)
    comparison_plot(ball)
    thread = threading.Thread(target=simulation, args=(ball, [0, 1, 2, 3, 4]))
    thread.daemon = True
    thread.start()
    plt.show()
