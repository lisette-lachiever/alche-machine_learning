#!/usr/bin/env python3
"""Display a stacked bar chart of fruit per person."""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

x = np.arange(3)

plt.bar(x, fruit[0], width=0.5, color='red',
        label='Apples')

plt.bar(x, fruit[1], width=0.5, bottom=fruit[0],
        color='yellow', label='Bananas')

plt.bar(x, fruit[2], width=0.5,
        bottom=fruit[0] + fruit[1],
        color='#ff8000', label='Oranges')

plt.bar(x, fruit[3], width=0.5,
        bottom=fruit[0] + fruit[1] + fruit[2],
        color='#ffe5b4', label='Peaches')

plt.xticks(x, ['Farrah', 'Fred', 'Felicia'])
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()