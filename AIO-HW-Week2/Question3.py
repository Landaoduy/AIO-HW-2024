def read_file(file_name):
    word_count = {}

    try:
        with open(file_name, 'r') as file:

            for line in file:
                words = line.split()
                for word in words:

                    if word not in word_count:
                        word_count[word] = 1

                    else:
                        word_count[word] += 1

        print(word_count)

    except FileNotFoundError:
        print(f"File {file_name} does not found")
