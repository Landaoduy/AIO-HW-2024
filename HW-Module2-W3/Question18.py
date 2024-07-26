# Question 18:

import numpy as np
from Dataset import create_train_data
from Question16 import get_index_from_value
from Conditional_Prob import compute_conditional_probability

train_data = create_train_data()

conditional_probability, list_x_name = compute_conditional_probability(
    train_data)

x1 = get_index_from_value('Sunny', list_x_name[0])

print('P(Outlook = Sunny | Play tennis = No) = ',
      np.round(conditional_probability[0][0, x1], 2))
