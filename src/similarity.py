from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(words):

    vectorizer = TfidfVectorizer(
        analyzer="char"
    )

    vectors = vectorizer.fit_transform(words)

    similarity_matrix = cosine_similarity(vectors)

    return similarity_matrix