
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

	with open("input.txt", "r") as f: sent = f.read().strip()

	model = CoreNLP()

	ner_result, pos_tag_result = model.ner(sent), model.pos_tag(sent)

	with open("goal.pl", "w") as f:

		word_list, ner_list, pos_tag_list = [], [], []

		for (word, ner), (_, pos_tag) in zip(ner_result, pos_tag_result):
			if pos_tag[0] == "V" or pos_tag[0] == "N" or ner != "O":
				word_list.append(lemmatize(word))
				ner_list.append(ner)
				pos_tag_list.append(pos_tag)

		for word, ner, pos_tag in zip(word_list, ner_list, pos_tag_list):
			f.write('input("{}", "{}", "{}").\n'.format(word, ner, pos_tag))

		items = set((ner, pos_tag) for ner, pos_tag in zip(ner_list, pos_tag_list))

		ner_list, pos_tag_list = [ner for ner, _ in items], [pos_tag for _, pos_tag in items]

		f.write("goal :-\n")

		f.write("\tsolve(YEAR, {}, {}),\n".format(
			'["{}"]'.format('", "'.join(ner_list)), 
			'["{}"]'.format('", "'.join(pos_tag_list)), 
		))

		f.write("\tprint(YEAR), nl, fail.\n")

if __name__ == "__main__": main()
