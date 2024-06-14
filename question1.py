def classification_model(tp, fp, fn):

    if not isinstance(tp, int):
        print("tp must be integer")
        return

    if not isinstance(fp, int):
        print("fp must be integer")
        return

    if not isinstance(fn, int):
        print("fn must be integer")
        return

    if tp > 0 and fp > 0 and fn > 0:

        precision = tp / (tp + fp)
        print(f"The precision is: {precision}")

        recall = tp / (tp + fn)
        print(f"The recall is: {recall}")

        f1_score = 2 * (precision * recall) / (precision + recall)
        print(f"The F1 score is: {f1_score}")

    else:
        print("tp and fp and fn must be greater than zero")
