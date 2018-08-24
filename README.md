# python_k-means
Simple k-means clustering algorithm python implementation for educational purposes.

## About

dataGenerator.py and normalized.py are utils classes that return random scatter points based on provided parameters and normalize data (if desired), respectively.

kMeans.py contains a class implementing the algorithm aswell as aditional visualization(plotting) methods.

example.py contains an executable example for the algorithm, as explained below. To run, type `python example.py` while at the project folder.

## Usage

You can initialize data on your own, or use the dataGenerator.py provided class. Data must be an array where each entrance is a cartesian point in the format [a,b]. A data array of 3 values would be [[25,40], [12,28], [76,90]].
If you choose to use the provided class:
```python
from dataGenerator import dataGenerator

dGen = dataGenerator()
data = dGen.generateCartesianPoints([0,10000], 500)
```
will generate 500 cartesian points with values ranging from 0 to 10000.
Normalization is not required, but a common practice in Data Mining algorithms, if you choose to use it:
```python
from normalizer import normalizer

norm = normalizer()
normalized_data = norm.normalize_data(data, 0, 100)
```

Now, in order to clusterize your data:
```python
from kMeans import k_means

kMeans = k_means()
clusters = kMeans.clusterize(normalized_data, 5)
```
This will cluster your data in 5 clusters (you can decide how many clusters you want by simply informing a different value on the second parameter). If you choose not to normalize the data, simply pass the original unnormalized array as the first parameter.

If you wish to visualize the clustered data:

```python
kMeans.plotCluster(clusters, data)
```

Any doubts/suggestions, feel free to contact me.
