# Question 19:

from Train_Naive_Bayes import train_naive_bayes
from Dataset import create_train_data
from Train_Naive_Bayes import prediction_play_tennis

X = ['Sunny', 'Cool', 'High', 'Strong']

data = create_train_data()

prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)

pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print('Ad should go!')

else:
    print('Ad should not go')
