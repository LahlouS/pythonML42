import sys
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from csvreader import CsvReader

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids


    def compute_distance(self, P1, P2):
        return np.sqrt(((P1 - P2) ** 2).sum())
    
    def mean(self, X):
        return (X.sum() / len(X))

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.centroids.append(X[rd.choices(range(len(X)), k=self.ncentroid)])

        for i in range(self.max_iter):
            clusters = []
            for rows in X:
                distances = [self.compute_distance(rows, centroids) for centroids in self.centroids[i]]
                closer = [idx for idx in range(len(distances)) if min(distances) == distances[idx]]
                clusters.append(closer[0])
            self.centroids.append(np.zeros(self.centroids[i].shape, dtype=np.float64))
            for cluster_idx in range(self.ncentroid):
                current_cluster_group = (np.array(clusters) == cluster_idx)
                self.centroids[i + 1][cluster_idx] = X[current_cluster_group].sum(axis = 0) / (X[current_cluster_group].shape[0])
        return self.centroids[-1]
        #  NOW YOU RE-COMPUTE THE CENTROID FOR EACH CLUSTERS BY CALCULATING THE MEAN DATAPOINT OF EVERY CLUSTER AND YOU RELAUNCH THE ALGO 

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """

if __name__ == "__main__":
    
    kmeans = KmeansClustering(max_iter=42, ncentroid=4)
    nps = 0
    with CsvReader(filename = 'solar_system_census.csv', header=True) as solar_system_census:
        nps = np.array(solar_system_census.getdata())[::, 1::].astype(np.float64)
    
    
    centroids = kmeans.fit(nps)
    print(centroids)
    citizens = {
        "The_flying_cities_of_Venus" : 0,
        "United_Nations_of_Earth" : 0,
        "Mars_Republic" : 0,
        "Asteroids_Belt_colonies" : 0
    }

    belt_idx = 0
    for idx in range(len(centroids)):
        if centroids[idx, 0] == max(centroids[::, 0]) and min(centroids[::, 2]) == centroids[idx, 2]:
            citizens["Asteroids_Belt_colonies"] = centroids[idx]
            belt_idx = idx
            break
        
    
        
    
