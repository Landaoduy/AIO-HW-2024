def find_max_sliding_window(num_list, k):

  if k > 1:
    n = len(num_list)
    result = []

    for i in range(n-k+1):
      window = num_list[i:i+k] ## Trượt cửa sổ để tìm số lớn nhất trong khoảng [i:i+k]

      window_max = max(window) ## Tìm max

      result.append(window_max)

    print(result)

  elif k == 1:
    print(num_list)

  else:
    print('Invalid Input or k is smaller than 1')

