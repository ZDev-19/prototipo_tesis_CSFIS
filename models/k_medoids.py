from sklearn_extra.cluster import KMedoids

def doKMedoids(X, ncluster=2, init='k-medoids++', max_iter=100, random_state=10):
    model = KMedoids(ncluster)
    model.fit(X)
    clust_labels = model.labels_
    return (clust_labels)
