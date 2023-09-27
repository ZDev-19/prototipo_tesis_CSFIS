from prince import MCA

def reducirMCA(X,n_components=2):
    mca = MCA(n_components=n_components,n_iter=10)
    X_transformed = mca.fit_transform(X) 

    return X_transformed