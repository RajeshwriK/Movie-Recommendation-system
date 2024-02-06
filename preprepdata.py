user_item_matrix = ratings_data.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0)
user_item_matrix
# Define a KNN model on cosine similarity
cf_knn_model= NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)


# Fitting the model on our matrix
cf_knn_model.fit(user_item_matrix)
