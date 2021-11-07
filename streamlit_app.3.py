import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestore-key.json")

# This time, we're creating a NEW post reference for Apple
doc_ref = db.collection("posts").document("Apple")

# And then uploading some data to that reference
doc_ref.set({
	"title": "Apple",
	"url": "www.apple.com"
})

# Now let's make a reference to ALL of the posts
posts_ref = db.collection("posts")

# For a reference to a collection, we use .stream() instead of .get()
for doc in posts_ref.stream():
	st.write("The id is: ", doc.id)
	st.write("The contents are: ", doc.to_dict())
