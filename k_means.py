#making necesarry imports
import numpy as np
import pandas as pd

#no of clusters to be formed
k = 3

#below are the eight 2-dimensional data points to be clustered
data_points = np.array([[1,1],
              [1,2],
              [2,1],
              [2,3],
              [3,3],
              [4,5],
              [5,4],
              [6,5]])

#taking initial centroids(means) 
initial_centroids = ([[2,3],[3,3],[5,4]])              

#calculating Euclidean distance between two arrays
def dist(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

#assigning clusters based on the nearest centroids
def assign_cluster(centroid):
    cluster = [0]*len(data_points)
    for i in range(len(data_points)):
        dist_arr = []
        for j in range(k):
            dist_arr.append(dist(data_points[i], centroid[j]))
        arr = np.argmin(dist_arr)
        cluster[i] = arr
    return np.asarray(cluster)

#finding unique values in the cluster 
def unique(cluster):
    return np.unique(cluster)

#function to print data points based on the clusters formed 
def printing_clusters(cluster, unique):
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for i in range(len(cluster)):
        for j in range(len(unique)):
            if cluster[i] == unique[j]:
                if unique[j] == 0:
                    cluster1.append(data_points[i].tolist())
                elif unique[j] == 1:
                    cluster2.append(data_points[i].tolist())
                else :
                    cluster3.append(data_points[i].tolist())
    return cluster1, cluster2, cluster3

#calculating centroids based on the mean of the clusters
def compute_centroids(cluster):
    centroid = []
    for i in range(k):
        arr = []
        for j in range(len(data_points)):
            if cluster[j]==i:
                arr.append(data_points[j])
        centroid.append(np.mean(arr, axis=0))
    return np.asarray(centroid)

#findinhg the sum of the squared means
def sum_of_squared_errors(cluster, centroid, unique):
    euc_dis = [] 
    for i in range(len(data_points)):
        for j in range(len(unique)):
            if cluster[i] == unique[j]: 
                #print(data_points[i], centroid[j])
                distance = dist(data_points[i], centroid[j]) 
                euc_dis.append(distance)
            else:
                continue
    return sum(euc_dis)               

#main function to find the k-means clustering
def k_means():
    current_centroid = initial_centroids
    cluster = [0]*len(data_points)
    a = 0
    while a < 5:
        cluster = assign_cluster(current_centroid)
        unique_values = unique(cluster)
        cluster_1 = printing_clusters(cluster, unique_values)
        new_centroid = compute_centroids(cluster)
        sum_of_squarederrors = sum_of_squared_errors(cluster, new_centroid, unique_values)
        print ('Iteration {0}:'.format(a+1))
        print("cluster 1: ",cluster_1[0])
        print("cluster 2: ",cluster_1[1])
        print("cluster 3: ",cluster_1[2])
        print("New mean: ",new_centroid.tolist())
        #print("centroid: ",current_centroid)
        print("Sum of Squared Error: ",sum_of_squarederrors)
        print("\n")
        current_centroid = new_centroid
        a = a+1    

k_means()        