from gensim.models import word2vec
import logging

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s",
                        level=logging.INFO)

    corpus = word2vec.Text8Corpus("corpus-jawiki-normalized.txt")

    # Train the 100d Word2Vec model
    # Ignore all words with total frequency lower than 20
    # Other parameters are set by default. For more details, see
    # https://github.com/RaRe-Technologies/gensim/blob/develop/gensim/models/word2vec.py.
    model = word2vec.Word2Vec(corpus, size=100, min_count=20)
    model.save("jawiki.model")
