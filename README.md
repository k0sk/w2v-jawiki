# w2v-jawiki
Scripts to train Word2Vec on Japanese Wikipedia with gensim

## Dependencies
Code is written in Python. To use this you will need:

- Python 3.5
- gensim
- MeCab
- mecab-python3

## Getting Started
Firstly, you will need to download the dump file of the Japanese Wikipedia. You can get the file by running

```sh
wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
```

Then, you will need extract the articles from the dump file using tools such as [WikiExtractor](https://github.com/attardi/wikiextractor).

Once you extracted the articles, you can run ```setup_data.py``` to do morphological analysis on the corpus. After that, you can finally train the Word2Vec model by running ```train_w2v.py```.
