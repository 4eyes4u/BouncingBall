from matplotlib import pyplot as plt


def singleton_plot(ball, idx):
    f = plt.figure(num='Singleton')
    # xy plot
    ax_xy = f.add_subplot(2, 2, 1)
    plt.xlabel('t [s]')
    plt.ylabel('x, y [m]')
    plt.title('r / t')
    ball.plot_xy(ax_xy, idx)
    plt.legend()
    # E plot
    ax_E = f.add_subplot(2, 2, 2)
    plt.xlabel('x [m]')
    plt.ylabel('E [J]')
    plt.title('E / x')
    ball.plot_E(ax_E, idx)
    plt.legend()
    # r plot
    ax_r = f.add_subplot(2, 1, 2)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title('r (x, y)')
    ball.plot_r(ax_r, idx)
    plt.legend()


def comparison_plot(ball):
    f = plt.figure(num='Comparison')
    ax = f.add_subplot(1, 1, 1)
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title('r (x, y)')
    ball.plot_r(ax)
    plt.legend()


def simulation(ball, indices):
    '''
    #REQ: 'Indices' is a list.
    '''

    ball.simulation(indices)
