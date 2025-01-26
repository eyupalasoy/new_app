import pandas as pd
import scipy.stats
import streamlit as st
import time

# Initialize stateful variables if they don't exist
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

# Application header
st.header('Tossing a Coin')

# Line chart to display the mean over trials
chart = st.line_chart([0.5])

# Function to simulate coin tosses
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# User input for number of trials
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

# Run the experiment when the button is clicked
if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    
    # Update the experiment results DataFrame
    new_result = pd.DataFrame({
        'no': [st.session_state['experiment_no']],
        'iterations': [number_of_trials],
        'mean': [mean]
    })
    
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        new_result
    ], ignore_index=True)

# Display the experiment results
st.write(st.session_state['df_experiment_results'])
