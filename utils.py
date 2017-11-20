import numpy as np

def read(row):

def gen_batch(data, batch_size=32):
	batches_per_epoch = data.shape[0] // batch_size

	i = 0
	while (True):
		s = i * batch_size
		e = s + batch_size - 1

		X_batch = np.zeros((batch_size, 64, 64, 2), dtype=np.float32)
		y_batch = np.zeros((batch_size,), dtype=np.float32)

		j = 0

		for index, row in data.loc[s:e].iterrows():
			X_batch[j], y_batch[j] = read(row)
			j += 1

		i += 1
		if i == batches_per_epoch-1:
			i = 0

		yield X_batch, y_batch