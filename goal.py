
from corenlp import CoreNLP

text = "Founded by brothers Robbie and James Ferguson in July 2018, Immutable reportedly expects to grow Gods Unchained from the current 13,000 to 1 million players with the new investment, James stated in an interview with AFR."

def main():

	keeps = ["COUNTRY", "ORGANIZATION", "PERSON", "MONEY"]

	model = CoreNLP()

	# print(model.word_tokenize(text))

	# print(model.dependency_parse(text))

	items = model.ner(text)

	with open("goal.pl", "w") as f:

		f.write("goal :-\n")

		for keep in keeps:

			words = []

			for name, ner in items:

				if ner == keep:

					words.append("\ttime_(X, \"{}\", \"{}\"),".format(name, ner))

			if len(words) > 0:

				f.write("{}\n".format("\n".join(words)))

		f.write("\tprint(X), nl, fail.\n")

if __name__ == "__main__": main()
