
from nltk.stem import WordNetLemmatizer
from corenlp import CoreNLP

wordnet_lemmatizer = WordNetLemmatizer()

def lemmatize(token):
	# ADJ (a), ADJ_SAT (s), ADV (r), NOUN (n) or VERB (v)
	for p in ['v', 'n', 'a', 'r', 's']:
		l = wordnet_lemmatizer.lemmatize(token, pos=p)
		if l != token:
			return l
	return token

def main():

	with open("database/data.txt", "r") as f:

		sents = f.read().strip().split("\n")

	model = CoreNLP()

	with open("word.pl", "w") as f:

		words = []

		for i, sent in enumerate(sents, 1):

			ner_result, pos_tag_result = model.ner(sent), model.pos_tag(sent)

			for (word, ner), (_, pos_tag) in zip(ner_result, pos_tag_result):

				words.append('word({}, "{}", "{}", "{}").'.\
					format(i, lemmatize(word), ner, pos_tag))

		f.write("{}\n".format("\n".join(words)))

if __name__ == "__main__": main()
