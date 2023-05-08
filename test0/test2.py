import numpy as np
import pandas as pd


def c_to_p(c):
    ev = c

    prob = c

    n = int(np.ceil(1 / c))

    cum_prod = 1

    for x in range(2, n):
        cum_prod *= 1 - (x - 1) * c
        prob_x = cum_prod * (x * c)
        prob += prob_x
        ev += x * prob_x

    prob_x = 1 - prob
    ev += n * prob_x

    return 1 / ev


# read the tabulated figure from the source and compare it with p computed by the formula

df = pd.read_html('https://dota2.gamepedia.com/Random_distribution')[0]
df['Self computed p'] = df['C'].apply(c_to_p)