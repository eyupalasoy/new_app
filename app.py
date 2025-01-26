import pandas as pd
import scipy.stats
import streamlit as st
import time


st.header('Tossing a Coin')
st.write('It is not a functional application yet. Under construction.')
# Initialize stateful variables if they don't exist
import pandas as pd
import scipy.stats
import streamlit as st
import time

# Stateful değişkenleri başlat (eğer yoksa)
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

# Uygulama başlığı
st.header('Tossing a Coin')

# Line chart'ı bir DataFrame ile başlat
chart = st.line_chart(pd.DataFrame({'mean': [0.5]}))

# Yazı tura atma fonksiyonu
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
        chart.add_rows(pd.DataFrame({'mean': [mean]}))  # Chart'ı güncelle
        time.sleep(0.05)  # Görsel efekt için bekle

    return mean

# Kullanıcı girişi: Deneme sayısı
number_of_trials = st.slider('Number of trials?', 1, 1000, 10)
start_button = st.button('Run')

# "Run" butonuna basıldığında denemeyi başlat
if start_button:
    st.write(f'Running the experiment of {number_of_trials} trials.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    
    # Deneme sonuçlarını güncelle
    new_result = pd.DataFrame({
        'no': [st.session_state['experiment_no']],
        'iterations': [number_of_trials],
        'mean': [mean]
    })
    
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        new_result
    ], ignore_index=True)

# Deneme sonuçlarını göster
st.write(st.session_state['df_experiment_results'])
