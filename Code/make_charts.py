import matplotlib.pyplot as plt
from shapely.geometry import LineString
import numpy as np

def cluster():
	xs = [2,4,8,16,32,64]
	cluster = [53.3515,
	49.2901,
	34.0447,
	28.2745,
	24.9491,
	34.0447
	]
	plt.rcParams["figure.figsize"] = [7.50, 3.50]
	plt.rcParams["figure.autolayout"] = True

	fig, ax  = plt.subplots(1, 1)
	ax.plot(xs, cluster)
	ax.set_xlabel('Number of Threads')
	ax.set_ylabel('Time (seconds)')

	seq_line = LineString(np.column_stack((xs, cluster)))
	ax.legend()
	plt.savefig("cluster.png")
	plt.show()

def teams():
	xs = [20000, 25000, 30000, 45000, 50000]
	impSeq = [5.411925, 6.032743, 7.588712, 18.525552, 20.554327]
	t2 = [6.040235, 7.165107, 8.71174, 15.910451, 19.351132]
	t4 = [5.734174, 6.253542, 7.415538, 12.610695, 14.885857]
	t8 = [5.30323, 6.222421, 7.344133, 12.695659, 15.135402]

	plt.rcParams["figure.figsize"] = [7.50, 3.50]
	plt.rcParams["figure.autolayout"] = True

	# fig = plt.figure(figsize=(4, 4))
	fig, ax  = plt.subplots(1, 1)
	# ax.set_xscale("log")
	ax.plot(xs, impSeq, label="sequencial")
	ax.plot(xs, t2, label="2 Threads")
	ax.plot(xs, t4, label="4 Threads")
	ax.plot(xs, t8, label="8 Threads")
	ax.set_xlabel('Number of teams')
	ax.set_ylabel('Time (seconds)')

	seq_line = LineString(np.column_stack((xs, impSeq)))
	t2_line = LineString(np.column_stack((xs, t2)))
	t4_line = LineString(np.column_stack((xs, t4)))
	t8_line = LineString(np.column_stack((xs, t8)))
	intersection = seq_line.intersection(t2_line)
	ax.plot(*intersection.xy, 'o')

	intersection = seq_line.intersection(t4_line)
	ax.plot(*intersection.xy, 'o')
	print(*intersection.xy)

	intersection = seq_line.intersection(t8_line)
	# for multiple intersections
	ax.plot(*LineString(intersection).xy, 'o')

	# ax.set_xticks(range(1, len(xs)))
	# ax.set_xticklabels(xs)
	ax.legend()
	plt.savefig("chart1.png")
	plt.show()

def teamsXfocal():
	xs = [10000, 250000, 640000, 1000000, 10000000 ]
	impSeq = [1.737427, 1.695187, 1.723713, 1.835826, 5.511364]
	t2 = [1.744368, 1.624315, 1.654085, 1.721149, 3.955861]
	t4 = [1.784506, 1.698878, 1.731241, 1.783247, 3.405557]
	t8 = [1.780357, 1.663076, 1.6684, 1.735846, 3.325923]

	fig, ax  = plt.subplots(1, 1)
	ax.set_xscale("log")
	ax.plot(xs, impSeq, label="sequencial")
	ax.plot(xs, t2, label="2 Threads")
	ax.plot(xs, t4, label="4 Threads")
	ax.plot(xs, t8, label="8 Threads")
	ax.set_xlabel('Number of teams * Number of Focal points')
	ax.set_ylabel('Time (seconds)')

	seq_line = LineString(np.column_stack((xs, impSeq)))
	t2_line = LineString(np.column_stack((xs, t2)))
	t4_line = LineString(np.column_stack((xs, t4)))
	t8_line = LineString(np.column_stack((xs, t8)))
	intersection = seq_line.intersection(t2_line)
	ax.plot(*intersection.xy, 'o')

	intersection = seq_line.intersection(t4_line)
	ax.plot(*intersection.xy, 'o')
	print(*intersection.xy)

	intersection = seq_line.intersection(t8_line)
	ax.plot(*intersection.xy, 'o')

	ax.legend()
	plt.savefig("chart2.png")
	plt.show()

teamsXfocal()
teams()
cluster()