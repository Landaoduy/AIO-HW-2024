import pandas as pd
from Question10 import context_embedded
from Question10 import tfidf_vectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Question 11:
vi_data_df = pd.read_csv(
    r"C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W4\vi_text_retrieval.csv")


def tfidf_search(question, tfidf_vectorizer, top_d=5):

    # lower casing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(
        context_embedded, query_embedded).reshape((-1,))

    results = []

    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc)

    return results


question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print(results[0]['cosine_score'])
