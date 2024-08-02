import pandas as pd
import numpy as np
from Question10 import context_embedded
from Question10 import tfidf_vectorizer
from sklearn.metrics.pairwise import cosine_similarity

vi_data_df = pd.read_csv(
    r"C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW_Module2_W4\vi_text_retrieval.csv")


def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = np.corrcoef(query_embedded.toarray()[
                              0], context_embedded.toarray())

    corr_scores = corr_scores[0][1:]
    results = []

    for idx in corr_scores.argsort()[-top_d:][::-1]:

        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }

        results.append(doc)

    return results


question = vi_data_df.iloc[0]['question']

results = corr_search(question, tfidf_vectorizer, top_d=5)

print(results[1]['corr_score'])
