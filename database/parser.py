
import nltk
import numpy as np
import pandas as pd

def main(dataset, parsing):

	with open(parsing, "w") as f:

		for df in pd.read_csv(dataset, header = None, chunksize = 1):

			items = df.values.reshape((-1, ))

			text = str(items[0]).strip()
			text = text[len('{"sentence":"'):-len('"}')]

			sents = nltk.sent_tokenize(text)

			f.write("{}\n".format("\n".join(sents)))

if __name__ == "__main__": 

	dataset = "final_project/fin_pairs.csv"

	parsing = "data.txt"

	main(dataset, parsing)
