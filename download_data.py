import os
import urllib.request

# URL of the dataset
URL = "https://storage.googleapis.com/kagglesdsdata/datasets/6988295/11193915/AIML%20Dataset.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20250501%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20250501T095948Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=29a01354af15414784991a69f94b0b633c27b784e0c1129a8d4698942777a99029a1714e800df57883649ac7a63e8a20f1790826afec7d36bca70c521ba338cce8239ec266303395bc5ad787841fa169085bab6642df06d0b3197ebaecac53643b204bbb214483178c87d0002e2c1c0a799a739e52ecd793f23e715e156cc75b5b4bebf77f0e23101d7a7f8eacd5e867421bfa20f8ed662e7db8f5fee3196ded36bc97036047df2d6fa421a7f0d71e42c1e77b094156017ed6c901a0253b8b7f0485bd276b2f46c9f03faef1e5f42e30c3429ba32ba8cba494c63197d5209b3c09cd796252690c8114e76c3e30db1e251b7b58287eca495c75914868a4d281bd"

# Local path where the dataset will be saved
DEST_PATH = "data/AIML_Dataset.csv"

# Ensure the destination directory exists
os.makedirs(os.path.dirname(DEST_PATH), exist_ok=True)

# Download the file
urllib.request.urlretrieve(URL, DEST_PATH)
print(f"Downloaded dataset to {DEST_PATH}")