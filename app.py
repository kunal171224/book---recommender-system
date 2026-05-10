import streamlit as st
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

st.title("Book Recommender System")

selected_book = st.selectbox(
    "Type or select a book",
    pt.index.values
)

if st.button('Recommend'):

    index = np.where(pt.index == selected_book)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    for i in similar_items:

        temp_df = books[books['Book-Title'] == pt.index[i[0]]]

        title = temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0]
        author = temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0]
        image = temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0]

        st.text(title)
        st.text(author)
        st.image(image)