def levenshtein_distance(s, t):

    m = len(s)
    n = len(t)
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    for c in range(m + 1):
        matrix[c][0] = c
    for r in range(n + 1):
        matrix[0][r] = r

    for c in range(1, m + 1):
        for r in range(1, n + 1):
            if s[c - 1] == t[r - 1]:
                matrix[c][r] = matrix[c - 1][r - 1]
            else:
                matrix[c][r] = min(matrix[c - 1][r] + 1,
                                   matrix[c][r - 1] + 1,
                                   matrix[c - 1][r - 1] + 1)

    return matrix[m][n]


s = "kitten"
t = "sitting"
print(f"Levenshtein Distance: {levenshtein_distance(s, t)}")
