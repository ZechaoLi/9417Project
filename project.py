import KNN
import arff
import numpy as np

for fname in ['autos.arff', "ionosphere.arff"]:
    #read data from arff file into dataset
    dataset = arff.load(open(fname), 'r')
    data = np.array(dataset['data'])


    X = np.array(data)[:, :-1]
    Y = np.array(data)[:, -1]

    print(X, Y)
