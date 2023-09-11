import sys
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from csvreader import CsvReader
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def check_pos(vec1, vec2):
    if isinstance(vec1, np.ndarray) and isinstance(vec2, np.ndarray):
        if vec1[0] == vec2[0] and vec1[1] == vec2[1] and vec1[2] == vec2[2]:
            return True
    return False

def check_no_same(citizens_dict, current):
    planets = [ "venus", "belt", "earth", "mars"]
    check_other_planet = 0
    while check_other_planet < len(planets):
        if check_other_planet != current and check_pos(citizens_dict[planets[check_other_planet]], citizens_dict[planets[current]]):
            return False
        check_other_planet += 1
    return True


def checker(citizens_dict):
    if citizens_dict["mars"][0] > citizens_dict["earth"][0] and citizens_dict["venus"][1] < citizens_dict["earth"][1] and citizens_dict["belt"][0] > citizens_dict["earth"][0] and citizens_dict["belt"][0] > citizens_dict["mars"][0] and citizens_dict["belt"][0] > citizens_dict["venus"][0]:
        return True
    return False

def deduce_species(citizens_dict, centroids, i):
        planets = [ "venus", "belt", "earth", "mars"]
        if i == len(centroids):
            return checker(citizens_dict)
        else:
            for idx in range(len(planets)):
                citizens_dict[planets[i]] = centroids[idx]
                if check_no_same(citizens_dict, i):
                    if deduce_species(citizens_dict, centroids, i + 1) == 0:
                        continue
                    else:
                        return True
            citizens_dict[planets[i]] = None
            return False

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        if ncentroid < 1 or max_iter < 1:
            print('centroid and max_iter must be a valid positive integer')
            sys.exit()
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

        test = rd.choices(range(len(X)), k=self.ncentroid)
        self.centroids.append(X[test])
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
        if len(self.centroids) != 0:
            kept_centroids = self.centroids[-1]
            for datapoint in X:
                distances = [self.compute_distance(datapoint, centroid) for centroid in kept_centroids]
                closer = [idx for idx in range(len(distances)) if min(distances) == distances[idx]]
                yield closer[0]

    def associated_centroid_lst(self, X):
        kept_centroids = self.centroids[-1]
        distances = 0
        cluster = []
        for datapoint in X:
            distances = [self.compute_distance(datapoint, centroid) for centroid in kept_centroids]
            closer = [idx + 1 for idx in range(len(distances)) if min(distances) == distances[idx]]
            cluster.append(closer[0])
        return cluster


if __name__ == "__main__":
    
    path=0
    ncentroid=0
    m_iter=0

    count_arg=0
    for args in sys.argv:
        if 'filepath=' in args:
            path = args[len('filepath='):]
            count_arg += 1
        if 'ncentroid=' in args:
            ncentroid = args[len('ncentroid='):]
            count_arg += 1
        if 'max_iter=' in args:
            m_iter = args[len('max_iter='):]
            count_arg += 1

    if count_arg != 3:
        print('ERROR args must be like:\n>> python Kmeans.py filepath=\'../ressources/solar_system_census.csv\' ncentroid=4 max_iter=30')
    kmeans = KmeansClustering(max_iter=int(m_iter), ncentroid=int(ncentroid))
    nps = 0
    with CsvReader(filename = path, header=True) as solar_system_census:
        nps = np.array(solar_system_census.getdata())[::, 1::].astype(np.float64)
    
    centroids = kmeans.fit(nps)

    pop = [0 for i in range(len(centroids))]
    for cluster in kmeans.predict(nps):
        pop[cluster] += 1

    if kmeans.ncentroid == 4:
        print('\nCASE [4 CENTROIDS] DEDUCTION:\n')
        system = {
            "venus":0,
            "belt": 0,
            "earth":0,
            "mars": 0
        }
        print('ret = ', deduce_species(system, centroids, 0))
        for key, value in system.items():
            pop_size = 0
            for pop_idx, pop_s in enumerate(pop):
                if check_pos(centroids[pop_idx], value):
                    pop_size = pop_s
            print(f'{key} origin: size: {value[0]}, weigth: {value[1]}, bone density: {value[2]}, population size: {pop_size}')
        
        # Generate some example 3D data
        x = nps[::, 0]
        y = nps[::, 1]
        z = nps[::, 2]

        # Create a 3D scatter plot
        fig = plt.figure(figsize=(12, 4))

        # XY Plane
        colormap = plt.cm.get_cmap('tab10', 4)
        ax1 = fig.add_subplot(131, projection='3d')
        sc1 = ax1.scatter(x, y, z, c=kmeans.associated_centroid_lst(nps), cmap=colormap)
        ax1.scatter(x, y, z)
        ax1.set_xlabel('taille')
        ax1.set_ylabel('poid')
        ax1.set_zlabel('densite osseuse')
        ax1.set_title('taille / poid')
        # fig.colorbar(sc1, ax=ax1, label='Cluster')

        # XZ Plane
        ax2 = fig.add_subplot(132, projection='3d')
        ax2.scatter(x, y, z, c=kmeans.associated_centroid_lst(nps), cmap=colormap)
        ax2.scatter(x, z, y)
        ax2.set_xlabel('taille')
        ax2.set_ylabel('densite osseuse')
        ax2.set_zlabel('poid')
        ax2.set_title('taille / densite osseuse')
        
        ax3 = fig.add_subplot(133, projection='3d')
        ax3.scatter(x, y, z, c=kmeans.associated_centroid_lst(nps), cmap=colormap)
        ax3.scatter(y, z, x)
        ax3.set_xlabel('poid')
        ax3.set_ylabel('densite osseuse')
        ax3.set_zlabel('taille')
        ax3.set_title('poid / densite osseuse')


        plt.tight_layout()
        plt.show()

    else:
        print('\nRANDOM CLUSTER OUTPUT\n')
        for i in range(kmeans.ncentroid):
            print(f'cluster n{i + 1}: size: {centroids[i][0]}, weigth: {centroids[i][1]}, bone density: {centroids[i][2]}, population size: {pop[i]}')

    


    
        
    
