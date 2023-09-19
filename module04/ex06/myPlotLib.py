import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MyplotLib:
	def __init__(self):
		pass

	def histogram(self, data, features):
		try :
			data[features]

		except KeyError as k:
			print('ERROR:', k)
			return None


		return None

if __name__ == "__main__":
	from fileLoader import FileLoader
	df = FileLoader().load('./athlete_events.csv')
	ploter = MyplotLib()
	print(ploter.histogram(df, ["Year", "Sex"]))
