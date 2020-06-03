"""
Python module for creating bar plots
"""

import numpy as np
from matplotlib import pyplot as plt

def plot_survivors_per_category(categories, survivors, title, xlabel):

	# set up plot
	fig, ax = plt.subplots()
	ax.set_title(title)
	ax.set_xlabel(xlabel)
	ax.set_ylabel("Survivors (%)")

	# plot barplot
	ax.bar(categories,survivors)
	# annotate barplot
	for i, data in enumerate(survivors):
		ax.annotate(data, (i, data-10), ha="center")


def plot_model_accuracies(names, results, stdev):

    # set up plot
    fig, ax = plt.subplots()
    _ = ax.set_title("Accuracies of ML models")
    _ = ax.set_xlabel("Classifiers")
    _ = ax.set_ylabel("Accuracy (%)")
    _ = ax.set_ylim(0, 1)

    # plot barplot
    _ = ax.bar(names, results, yerr=stdev)
    # annotate barplot
    for i, data in enumerate(results):
        _ = ax.annotate(round(data, 2), (i, data-0.1), ha="center")


def plot_feature_importance(clf, feat, ylabel, importances):

    # set variables
    x = np.arange(len(feat[:-1]))  # the label locations
    width = 0.35  # the width of the bars

    # set up plot
    fig, ax = plt.subplots()
    _ = ax.set_title("Feature importances")
    _ = ax.set_xticks(x)
    _ = ax.set_xticklabels(feat[:-1])
    _ = ax.set_xlabel("Features")
    _ = ax.set_ylabel(ylabel)
    _ = ax.set_ylim(0, max(max(importances)) + max(max(importances))*0.1)

    # plot barplot
    for i,j,k in zip(importances, [-1, 1], clf):
        _ = ax.bar(x + width/2*j, i, width, label=f'{k}')
        # annotate barplot
        for l, data in enumerate(i):
            _ = ax.annotate(s=round(data, 2), xy=(l+width/2*j, data+0.01), ha='center')
    _ = ax.legend()