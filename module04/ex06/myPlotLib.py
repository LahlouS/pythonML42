import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MyplotLib:
	def __init__(self):
		pass

	def histogram(self, data, features):
		try :
			print(len(features))
			fig, axs = plt.subplots(1, len(features))
			fig.suptitle(f'histogram distribution of {features}')
			for i, feature in enumerate(features):
				if len(features) == 1:
					axs.hist(data[feature])
					break
				axs[i].hist(data[feature])
			plt.subplots_adjust(wspace=0.4)
			plt.show()
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return None


		return None

if __name__ == "__main__":
	from fileLoader import FileLoader
	df = FileLoader().load('./athlete_events.csv')
	ploter = MyplotLib()
	print(ploter.histogram(df, ["Height", "Weight"])) #
