# Question 5:

def diff_nth_root_error(y, y_hat, n, p):

    y_root = y**(1/n)

    y_hat_root = (y_hat)**(1/n)

    nth_root_error = (y_root - y_hat_root)**p

    print(
        f"The different nth root error value with y = {y}, y_hat = {y_hat}, n = {n}, p = {p} is: {nth_root_error}")
