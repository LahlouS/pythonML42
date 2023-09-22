import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from math import sqrt

class Komparator:
	def __init__(self, df):
		if isinstance(df, pd.DataFrame):
			self.df = df

	def compare_box_plots(self, categorical_var, numerical_var):
		df = self.df.dropna(subset=[numerical_var])
		subPop = df[categorical_var].unique()
		l_en = 0
		test = [df[df[categorical_var] == group][numerical_var] for group in subPop]
		index = -1
		for idx, sets in enumerate(test):
			if len(sets) > l_en:
				l_en = len(sets)
				index = idx
		test2 = []
		for idx, sets in enumerate(test):
			if len(sets) < l_en:
				test2.append(np.pad(sets, (0, l_en - len(sets)), constant_values=sets.mean() + (sqrt(sets.var()) * random.choice([-1, 1]))))
			else:
				test2.append(sets)
		plt.boxplot(test2, labels=[group + ' - ' + numerical_var for group in subPop])
		plt.show()

	def density(self, categorical_var, numerical_var):
		try :
			df = self.df.dropna(subset=[numerical_var])
			subPop = df[categorical_var].unique()

			for group in subPop:
				sns.kdeplot(
					df[df[categorical_var] == group][numerical_var],
					label = group + ' - ' + numerical_var
				)
			plt.legend(prop={'size': 16}, title = 'features')
			plt.title('Density Plot for subpop')
			plt.xlabel('measurement system')
			plt.ylabel('Density')
			plt.show()
			return True
		except (KeyError, ValueError) as k:
			print('ERROR:', k)
			return False

	def compare_histograms(self, categorical_var, numerical_var):
		df = self.df.dropna(subset=[numerical_var])
		subPop = df[categorical_var].unique()

		fig, axs = plt.subplots(1, len(subPop))
		fig.suptitle(f'histogram distribution of {subPop} {numerical_var}')
		for i, group in enumerate(subPop):
			if len(subPop) == 1:
				axs.hist(df[numerical_var])
				break
			axs[i].hist(df[df[categorical_var] == group][numerical_var])
		plt.subplots_adjust(wspace=0.4)
		plt.show()


if __name__ == "__main__":
	from fileLoader import FileLoader

	df = FileLoader().load('./athlete_events.csv')
	komp = Komparator(df)
	komp.compare_box_plots("Sex", "Height")
	komp.density("Sex", "Height")
	komp.compare_histograms("Sex", "Height")
