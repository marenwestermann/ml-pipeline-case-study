"""
Python module for creating bar plots
"""

from matplotlib import pyplot as plt

def plot_barplot(categories, survivors, title, xlabel):

	# set up plot
	fig, ax = plt.subplots()
	ax.set_title(title)
	ax.set_xlabel(xlabel)
	ax.set_ylabel("Survivors (%)")

	# plot barplot
	ax.bar(categories,survivors)
	# annotate barplot
	for i, data in enumerate(survivors):
		ax.annotate(data, (i-0.07, data-10))
