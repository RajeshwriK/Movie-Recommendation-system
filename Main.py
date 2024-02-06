
def movie_recommender_engine(movie_name, matrix, cf_model, n_recs):
    # Fit model on matrix
    cf_knn_model.fit(matrix)
    
    # Extract input movie ID
    movie_id = process.extractOne(movie_name, movie_names['title'])[2]
    
    # Calculate neighbour distances
    distances, indices = cf_model.kneighbors(matrix[movie_id], n_neighbors=n_recs)
    movie_rec_ids = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
    
    # List to store recommendations
    cf_recs = []
    for i in movie_rec_ids:
        cf_recs.append({'Title':movie_names['title'][i[0]],'Distance':i[1]})
    
    # Select top number of recommendations needed
    df = pd.DataFrame(cf_recs, index = range(1,n_recs))
     
    return df
