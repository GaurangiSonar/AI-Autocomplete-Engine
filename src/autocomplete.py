import random

def rank_suggestions(words, df):

    scored = [(word, random.random()) for word in words]

    ranked = sorted(scored, key=lambda x: x[1], reverse=True)

    return [word for word, score in ranked[:5]]