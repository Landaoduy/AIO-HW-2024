from Dataset import create_train_data
from Conditional_Prob import compute_conditional_probability

train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
print('x1 =  ', list_x_name[0])
print('x2 =  ', list_x_name[1])
print('x3 =  ', list_x_name[2])
print('x4 =  ', list_x_name[3])