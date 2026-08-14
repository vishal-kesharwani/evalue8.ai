import os

import pandas as pd
import requests
import streamlit as st

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="LLM Router — Trace Dashboard", layout="wide")
st.title("LLM Router — Trace Dashboard")

try:
    analytics = requests.get(f"{BACKEND_URL}/api/v1/analytics", timeout=5).json()
except requests.RequestException as exc:
    st.error(f"Could not reach the backend at {BACKEND_URL}: {exc}")
    st.stop()

st.metric("Total requests", analytics["total_requests"])

if analytics["total_requests"] == 0:
    st.info("No routing traces yet. Call POST /api/v1/route on the backend to generate some.")
    st.stop()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Requests by model")
    df = pd.DataFrame(analytics["requests_by_model"])
    st.bar_chart(df.set_index("model")["count"])

with col2:
    st.subheader("Cost by model")
    df = pd.DataFrame(analytics["cost_by_model"])
    st.bar_chart(df.set_index("model")["total_cost"])

with col3:
    st.subheader("Cost by domain")
    df = pd.DataFrame(analytics["cost_by_domain"])
    st.bar_chart(df.set_index("domain")["total_cost"])

st.subheader("Historical decisions")

filter_col1, filter_col2, filter_col3 = st.columns(3)
model_filter = filter_col1.text_input("Filter by model")
domain_filter = filter_col2.text_input("Filter by domain")
outcome_filter = filter_col3.text_input("Filter by outcome")

params = {"limit": 200}
if model_filter:
    params["model"] = model_filter
if domain_filter:
    params["domain"] = domain_filter
if outcome_filter:
    params["outcome"] = outcome_filter

traces = requests.get(f"{BACKEND_URL}/api/v1/traces", params=params, timeout=5).json()
st.dataframe(pd.DataFrame(traces), use_container_width=True)
