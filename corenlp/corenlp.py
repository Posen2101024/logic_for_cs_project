
from stanfordcorenlp import StanfordCoreNLP

import os
import gdown
import zipfile

root = os.path.dirname(__file__)
root = root if root else "."

class CoreNLP():

	def __init__(self, model_lang = "en",
		model_name = "stanford-corenlp-4.0.0",
		model_id   = "1g8bXilHf5ZUdB6zLzvHfI9x5ZxyXdcJh"):

		model_dir = "{}/{}".format(root, model_name)

		if not os.path.isdir(model_dir):

			url = "https://drive.google.com/uc?export=download&id={}".format(model_id)

			out = "{}.zip".format(model_dir)

			gdown.download(url, out, quiet = False)

			with zipfile.ZipFile(out, "r") as data:

				data.extractall(root)

			os.remove(out)

		self.model = StanfordCoreNLP(model_dir, lang = model_lang)

	def word_tokenize(self, sent):

		return self.model.word_tokenize(sent)
	
	def pos_tag(self, sent):

		return self.model.pos_tag(sent)

	def ner(self, sent):

		return self.model.ner(sent)

	def parse(self, sent):

		return self.model.parse(sent)

	def dependency_parse(self, sent):

		return self.model.dependency_parse(sent)

	def __del__(self):

		self.model.close()
