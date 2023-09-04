import numpy as np
import pickle
import streamlit as st

# loading the saved model.
loaded_model=pickle.load(open('IMDBMovieReviews.sav','rb'))

# creating function

def movie_review(input_data):
    if(input_data==['']):
        return 'Please tell about the movie'
    else:
        prediction=loaded_model.predict(input_data)
        if(prediction=='positive'):
            return 'Positive review for the movie'
        elif(prediction=='negative'):
            return 'Negative review for the movie'
def main():
    # giving the title
    st.title('Movie Critic')

    # input data
    review=st.text_input('Write your review about the film')

    # code for prediction
    Movie_prediction=" "

    # creating a button for prediction
    
    if(st.button('Movie Critic Result')):
        Movie_prediction=movie_review([review])
        
    st.success(Movie_prediction)

if __name__=='__main__':
    main()


