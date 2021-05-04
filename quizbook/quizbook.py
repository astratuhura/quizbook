import time
import streamlit as st
import numpy as np
import pandas as pd
import plotly as px

from end_code_block import end_code_block as __

st.title('The Quizbook for MBA509')

st.header("Hi, this is our book of quizzes on algorithms and artificial intelligence")

st.header("Title")
st.subheader("But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness")

user_input = st.text_input("Enter your student email address", 'studentid@kaplanstuden.edu.au')

# definitions learning outcomes
st.header("Find the correct definition for each of the questions")
st.write("What is artificial intelligence?")
algo = st.radio(
"Select the correct definition",
('Artificial Intelligence, or AI, is the name for algorithmic machines that that do not have human-like intelligence', 'Artificial Intelligence, or AI, is the name for algorithmic machines that cannot think, reason and act with human-like intelligence', 'Artificial Intelligence, or AI, is the name for algorithmic machines that can think, reason and act with human-like intelligence'))

st.write("What are the three phases of artificial intelligence?")
machines_learn = st.multiselect(
'Which of the following do not belong to the three phases of artificial intelligence?',
['Phase 1: Artificial Narrow Intelligence', 'Phase 2: Artificial General Intelligence', 'Phase 3: Artificial Superintelligence', 'Phase 4: Artificial Singularity'],
['Phase 2: Artificial General Intelligence', 'Phase 4: Artificial Singularity'])

st.write('You selected:', machines_learn)

st.markdown('----')
st.write("What is an algorithm?")
ai = st.radio(
"Select the correct definition",
('An algorithm is a infinite sequence of computable instructions', 'An algorithm is a infinite sequence of well-defined computable instructions', 'An algorithm is a finite sequence of well-defined computable instructions'))

st.markdown('----')
st.write("What is Narrow AI")
ai = st.radio(
"Select the correct definition",
('designed with predefined instructions to perform and simulates human behaviour', 'machines posses the ability to perform independent reasoning and decision making, at the level of human intelligence', 'AI singularity more capable than human intelligence'))

st.markdown('----')
st.write("What is Machine Learning or ML?")
ai = st.radio(
"Select the correct definition",
('ML is wide learning', 'ML is general ai', 'ML is narrow intelligence'))

st.markdown('----')
st.header("What is the difference between forecasting and predictions?")
st.write("Forecasting is?")
ai = st.radio(
"Select the correct definition",
('estimate future trends', 'predicts the future', 'estimates future trends with  time series data'))

st.markdown('----')
st.header("What is an artificial neural network?")
st.write("Select that which is most correct")
ai = st.radio(
"Select the correct definition",
('simulates the behaviour of the human brain, and this simulation allows ANNs to recognise patterns in data and solve business problems', 'simulates the behaviour of the human brain, to recognise patterns in data and predict the future', 'simulates the behaviour of the human brain, makes forecasts'))


st.markdown('----')
st.header("What is Reinforcement ML?")
st.write("Select that which is most correct")
reinforce_learn = st.multiselect(
'Which of the following is not Reinforcement Learning?',
['The agent is provided with a set of rules, actions, parameters and goals (end values)', 'The agent receives a reward for reaching the goals', 'Agent learns by trial and error', 'Artificial Neural Networks (ANNs)','Random Forest Algorithms'],
['Artificial Neural Networks (ANNs)', 'Agent learns by trial and error','Random Forest Algorithms'])
st.markdown('----')