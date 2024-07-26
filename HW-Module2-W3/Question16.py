# Question 16:

from Dataset import create_train_data
import numpy as np
from Conditional_Prob import compute_conditional_probability


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]
    # Function is used to return the index of the feature name


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value('Overcast', outlook)
i2 = get_index_from_value('Rain', outlook)
i3 = get_index_from_value('Sunny', outlook)

print('i1 = ', i1)
print('i2 = ', i2)
print('i3 = ', i3)
