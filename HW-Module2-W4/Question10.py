from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

vi_data_df = pd.read_csv(
    r"C:\Users\Lan Dao\Desktop\AIO-exercise\AIO-HW-2024\HW-Module2-W4\vi_text_retrieval.csv")

context = vi_data_df['text']

context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()

context_embedded = tfidf_vectorizer.fit_transform(context)

print(context_embedded.toarray()[7][0])
