from sklearn.mixture import GaussianMixture

def doGMM(X, n_components=2,max_iter=100, random_state=10):
    model = GaussianMixture(n_components=n_components, random_state=random_state, max_iter=max_iter)
    clust_labels = model.fit_predict(X)
    return clust_labels