from kmodes.kmodes import KModes

def doKModes(X, ncluster=2, init='Huang',n_init=5, verbose=1):
    model = KModes(ncluster,init=init)
    clust_labels = model.fit_predict(X)
    return clust_labels