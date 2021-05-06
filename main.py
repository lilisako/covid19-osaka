import streamlit as st
import numpy as np
import pandas as pd

st.title("🦠OSAKA COVID19 DATA API")
st.write("This is a realtime data visualization of COVID19 in Osaka. Data source is https://github.com/codeforosaka/covid19")

#load sever bed usage
json = pd.read_json("https://raw.githubusercontent.com/codeforosaka/covid19/master/data/severe-bed-usage.json")
bed_rate = pd.json_normalize(json['data'])
bed_rate['date'] = pd.to_datetime(bed_rate['date'], format='%Y-%m-%d')
st.subheader("- Occupancy rate of hospital beds for severe symptom patients / 重症病床使用率")
st.line_chart(bed_rate[['date', 'rate']].rename(columns={'date':'index'}).set_index('index'))

#load new case
json = pd.read_json("https://raw.githubusercontent.com/codeforosaka/covid19/master/data/number-of-new-positives-per-100_000-population.json")
cases = pd.json_normalize(json['data'])
cases['date'] = pd.to_datetime(cases['date'], format='%Y-%m-%d')
st.subheader("- Number of new positive results per 100,000 persons during the previous week / 直近1週間の人口10万人あたり新規陽性者数")
st.line_chart(cases[['date', 'value']].rename(columns={'date':'index'}).set_index('index'))
