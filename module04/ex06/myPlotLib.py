import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class MyplotLib:
	def __init__(self):
		pass

	def histogram(self, data, features):
		try :
			clean_data = data[features].dropna()
			fig, axs = plt.subplots(1, len(features))
			fig.suptitle(f'histogram distribution of {features}')
			for i, feature in enumerate(features):
				if len(features) == 1:
					axs.hist(clean_data[feature])
					break
				axs[i].hist(clean_data[feature])
			plt.subplots_adjust(wspace=0.4)
			plt.show()
			return True
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return False

	def density(self, data, features):
		try :
			clean_data = data[features].dropna()

			for f in features:
				sns.kdeplot(
					clean_data[f],
					label = f
				)
			plt.legend(prop={'size': 16}, title = 'features')
			plt.title('Density Plot for multiple features')
			plt.xlabel('measurement system')
			plt.ylabel('Density')
			plt.show()
			return True
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return False

	def pair_plot(self, data, features):
		try:
			clean_data = data[features].dropna()
			pd.plotting.scatter_matrix(clean_data, figsize=(5, 5), grid=True)
			plt.show()
			return True
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return False

	def box_plot(self, data, features):
		try:
			clean_data = data[features].dropna()
			plt.boxplot([clean_data[f] for f in features], labels=features)
			plt.show()
			return True
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return False



# MAYBE YOU WILL HAVE TO FILL THE NaN VALUES WITH SOME VALUES  ???

if __name__ == "__main__":
	from fileLoader import FileLoader
	df = FileLoader().load('./athlete_events.csv')
	ploter = MyplotLib()

	# HISTOGRAM
	print(ploter.histogram(df, ["Height", "Weight"]))
	# DENSITY
	print(ploter.density(df, ["Height", "Weight"]))
	# PAIR PLOTS
	print(ploter.pair_plot(df, ["Weight", "Height"]))
	# BOX PLOTS
	print(ploter.box_plot(df, ["Weight", "Height"]))
