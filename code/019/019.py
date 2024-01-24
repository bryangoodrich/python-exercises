import numpy as np
import faiss

num_vectors, dim = (10, 64)
data = np.random.random((num_vectors, dim)).astype('float32')
index = faiss.IndexFlatL2(dim)  # L2 distance is used
index.add(data)
faiss.write_index(index, "data/index.faiss")

index = faiss.read_index("data/index.faiss")
query_vector = np.random.random((1, dim)).astype('float32')
distances, indices = index.search(query_vector, 3)
nearest_3 = zip(distances[0], indices[0])

for i, document in enumerate(nearest_3):
    print(f"Document {i}: ({document[1]}, {document[0]})")
# Document 0: (3, 8.181063652038574)
# Document 1: (9, 8.26373291015625)
# Document 2: (8, 9.569644927978516)