# the file where we will code the streamlit app

import streamlit as st
import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


data = pd.read_csv(r"E:\DS Projects\Project\dataset.csv", sep=",", encoding='cp1252')


# Split the dataset into features (X) and labels (y)
y = data['Personality']
X = data[['Seeing other people cry can easily make you feel like you want to cry too',
       'You usually stay calm, even under a lot of pressure',
       'At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know',
       'You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.',
       'You enjoy participating in group activities.',
       'You like books and movies that make you come up with your own interpretation of the ending.',
       'Your happiness comes more from helping others accomplish things than your own accomplishments.',
       'You are interested in so many things that you find it difficult to choose what to try next.',
       'You are prone to worrying that things will take a turn for the worse.',
       'Your mood can change very quickly.',
       'You often end up doing things at the last possible moment.',
       'You find it easy to empathize with a person whose experiences are very different from yours.',
       'You rarely second-guess the choices that you have made.',
       'After a long and exhausting week, a lively social event is just what you need.',
       'You enjoy going to art museums.',
       'You often have a hard time understanding other people’s feelings.',
       'You avoid making phone calls.',
       'You are still bothered by mistakes that you made a long time ago.',
       'You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.',
       'You struggle with deadlines.']]

# Create and train a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X, y)
 
# Define the list of features
features = ['Seeing other people cry can easily make you feel like you want to cry too',
       'You usually stay calm, even under a lot of pressure',
       'At social events, you rarely try to introduce yourself to new people and mostly talk to the ones you already know',
       'You usually prefer just doing what you feel like at any given moment instead of planning a particular daily routine.',
       'You enjoy participating in group activities.',
       'You like books and movies that make you come up with your own interpretation of the ending.',
       'Your happiness comes more from helping others accomplish things than your own accomplishments.',
       'You are interested in so many things that you find it difficult to choose what to try next.',
       'You are prone to worrying that things will take a turn for the worse.',
       'Your mood can change very quickly.',
       'You often end up doing things at the last possible moment.',
       'You find it easy to empathize with a person whose experiences are very different from yours.',
       'You rarely second-guess the choices that you have made.',
       'After a long and exhausting week, a lively social event is just what you need.',
       'You enjoy going to art museums.',
       'You often have a hard time understanding other people’s feelings.',
       'You avoid making phone calls.',
       'You are still bothered by mistakes that you made a long time ago.',
       'You feel more drawn to places with busy, bustling atmospheres than quiet, intimate places.',
       'You struggle with deadlines.']



# Create a dictionary to map agreement levels to numeric values
agreement_levels = {
    'Fully Agree': 3,
    'Partially Agree': 2,
    'Slightly Agree': 1,
    'Neutral': 0,
    'Slightly Disagree': -1,
    'Partially Disagree': -2,
    'Fully Disagree': -3,
}

# Create a dictionary to store user responses
user_responses = {}

# Create a dictionary to map agreement levels to numeric values
agreement_levels = {
    'Fully Agree': 3,
    'Partially Agree': 2,
    'Slightly Agree': 1,
    'Neutral': 0,
    'Slightly Disagree': -1,
    'Partially Disagree': -2,
    'Fully Disagree': -3,
}

# Create a Streamlit app
st.title("Personality Assessment")

# Collect user responses for each feature
for index, feature in enumerate(features):
    st.write(feature)
    agreement = st.radio(f"Select your agreement level for Feature {index + 1}:", list(agreement_levels.keys()), key=f"feature_{index}")
    user_responses[feature] = agreement_levels[agreement]






# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_classifier= joblib.load('RandomForest.joblib')

# Add a submit button
if st.button("Submit"):
 

    # Prepare the user input for prediction
    user_input_list = [list(user_responses.values())]


    # Make predictions using the trained model
    predicted_personality = rf_classifier.predict(user_input_list)

    # Display the predicted personality
    st.write(f"Predicted Personality Type: {predicted_personality[0]}")
    if predicted_personality[0]=='ESFP':
        st.write("(Extraverted, Sensing, Feeling, Perceiving):")
        st.write("ESFPs are often outgoing, spontaneous, and enjoy the present moment. They are people-oriented and value excitement and variety in their lives.")
    elif  predicted_personality[0]=='INFJ':
        st.write("(Introverted, Intuitive, Feeling, Judging):")
        st.write("INFJs are compassionate, insightful, and future-focused. They tend to be reserved and are known for their deep understanding of others.")
    elif  predicted_personality[0]=='ENFP':
        st.write("(Extraverted, Intuitive, Feeling, Perceiving):")
        st.write("ENFPs are enthusiastic, creative, and open-minded. They value possibilities, exploration, and are often seen as energetic and optimistic.")
    elif  predicted_personality[0]=='ENTP':
        st.write("(Extraverted, Intuitive, Thinking, Perceiving):")
        st.write("ENTPs are curious, logical, and enjoy intellectual challenges. They are often seen as witty and innovative.")
    elif  predicted_personality[0]=='ESTJ':
        st.write("(Extraverted, Sensing, Thinking, Judging):")
        st.write("INFJs are compassionate, insightful, and future-focused. They tend to be reserved and are known for their deep understanding of others.")
    elif  predicted_personality[0]=='ISTJ':
        st.write("(Introverted, Sensing, Thinking, Judging):")
        st.write(" ISTJs are dependable, detail-oriented, and methodical. They are often seen as responsible and loyal.")
    elif  predicted_personality[0]=='ISTP':
        st.write("(Introverted, Sensing, Thinking, Perceiving):")
        st.write("ISTPs are hands-on, adaptable, and enjoy problem-solving. They often have a love for mechanics and practical skills.")
    elif  predicted_personality[0]=='ESTP':
        st.write("(Extraverted, Sensing, Thinking, Perceiving):")
        st.write("ESTPs are action-oriented, daring, and enjoy taking risks. They thrive in dynamic environments.")
    elif  predicted_personality[0]=='ISFP':
        st.write("(Introverted, Sensing, Feeling, Perceiving):")
        st.write("ISFPs are artistic, sensitive, and value individuality. They often have a strong appreciation for aesthetics and the arts.")
    elif  predicted_personality[0]=='ESFJ':
        st.write("(Extraverted, Sensing, Feeling, Judging):")
        st.write("ESFJs are sociable, caring, and dependable. They place a strong emphasis on maintaining harmony in relationships.")
    elif  predicted_personality[0]=='ENFJ':
        st.write("(Extraverted, Intuitive, Feeling, Judging):")
        st.write("ENFJs are charismatic, empathetic, and nurturing. They often take on leadership roles and are driven by a desire to help others.")
    elif  predicted_personality[0]=='INTJ':
        st.write("(Introverted, Intuitive, Thinking, Judging):")
        st.write("INTJs are strategic, analytical, and independent thinkers. They excel in long-term planning and problem-solving.")
    elif  predicted_personality[0]=='ESFJ':
        st.write("(Extraverted, Sensing, Feeling, Judging):")
        st.write("ESFJs are sociable, caring, and dependable. They place a strong emphasis on maintaining harmony in relationships.") 
    elif  predicted_personality[0]=='INTP':
        st.write("(Introverted, Intuitive, Thinking, Perceiving):")
        st.write("INTPs are logical, curious, and enjoy exploring complex ideas. They are often seen as intellectuals and inventors.") 
    elif  predicted_personality[0]=='ISFJ':
        st.write("(Introverted, Sensing, Feeling, Judging):")
        st.write("ISFJs are reliable, caring, and detail-oriented. They are often seen as the nurturers and value tradition and stability.") 
    elif  predicted_personality[0]=='ENTJ':
        st.write("(Extraverted, Intuitive, Thinking, Judging):")
        st.write("ENTJs are assertive, strategic, and natural leaders. They are often driven to achieve their goals and are confident decision-makers.") 
    elif  predicted_personality[0]=='INFP':
        st.write("(Introverted, Intuitive, Feeling, Perceiving):")
        st.write("INFPs are idealistic, creative, and value authenticity. They are often introspective and deeply in tune with their emotions.")                         
    #st.image('images.jpg.crdownload')

    # Now, you can pass the user responses to your model for further processing
    # Replace this part with your model integration code
    # model_result = your_model_function(user_responses)

    # Display the model result
    # st.write(f"Model Result: {model_result}")