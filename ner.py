
from corenlp import CoreNLP

def main():

	with open("database/data.txt", "r") as f:

		sents = f.read().strip().split("\n")

	model = CoreNLP()

	dic = {}

	with open("ner.pl", "w") as f:

		for sent in sents:

			for word, ner in model.ner(sent):

				if ner != "O":

					print(word, ner)

					if not ner in dic:
						dic[ner] = []
					dic[ner].append(word)

		for ner in dic:

			print(ner)

			for word in set(dic[ner]):

				f.write("{}_(\"{}\").\n".format(ner.lower(), word))

if __name__ == "__main__": main()
