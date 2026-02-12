import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import plotly.express as px

# Configuration
DATA_FILE = "data/regimen_data.json"
PAGE_TITLE = "White Matter Regimen Tracker"
PAGE_ICON = "🧠"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- Data Handling ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- UI Components ---
def main():
    st.title(f"{PAGE_ICON} {PAGE_TITLE}")
    
    # Tabs for different monitoring areas
    tab1, tab2, tab3 = st.tabs(["🧠 Regimen Tracker", "🩸 Medical Labs", "ℹ️ About"])

    with tab1:
        st.markdown("""
        ### White Matter Enhancement Metrics
        Track your 3 Pillars of Brain Health.
        """)
        
        # Sidebar/Input Layout for Tab 1
        col_input, col_view = st.columns([1, 2])
        
        with col_input:
            st.subheader("Daily Log")
            with st.form("daily_entry_form"):
                date = st.date_input("Date", datetime.now())
                
                st.markdown("#### 1. The Fuel (BDNF) 🏃‍♀️")
                fuel_activity = st.selectbox("Activity", ["Walk", "Swim", "Recumbent Cycle", "HIIT", "Other"])
                fuel_minutes = st.number_input("Minutes (Goal: 30+)", min_value=0, step=5)
                
                st.markdown("#### 2. The Wiring (Myelination) 🎹")
                wiring_activity = st.selectbox("Activity", [
                    "Piano / Instrument", 
                    "Table Tennis (Ping Pong)", 
                    "Dancing / Choreography", 
                    "New Language", 
                    "Bilateral Hand Skill",
                    "Strategy Game (Chess/Go)"
                ])
                wiring_notes = st.text_input("Notes (e.g., 'Practiced Bach for 15m')")
                frustration_level = st.slider("Frustration Signal (1-10)", 1, 10, help="Higher effort = Better Myelination")
                
                st.markdown("#### 3. Protection 🛡️")
                systolic_bp = st.number_input("Systolic BP (<120)", min_value=0, value=120)
                diastolic_bp = st.number_input("Diastolic BP (<80)", min_value=0, value=80)
                
                submitted = st.form_submit_button("Log Regimen")

                if submitted:
                    new_entry = {
                        "date": str(date),
                        "type": "regimen",
                        "fuel_activity": fuel_activity,
                        "fuel_minutes": fuel_minutes,
                        "wiring_activity": wiring_activity,
                        "wiring_notes": wiring_notes,
                        "frustration_level": frustration_level,
                        "systolic_bp": systolic_bp,
                        "diastolic_bp": diastolic_bp
                    }
                    current_data = load_data()
                    current_data.append(new_entry)
                    save_data(current_data)
                    st.success("Saved!")

        with col_view:
            data = load_data()
            regimen_data = [d for d in data if d.get('type') == 'regimen' or 'fuel_minutes' in d] # Backwards compatibility
            
            if regimen_data:
                df = pd.DataFrame(regimen_data)
                df['date'] = pd.to_datetime(df['date'])
                df = df.sort_values('date')
                
                # KPIs
                latest = df.iloc[-1]
                kpi1, kpi2, kpi3 = st.columns(3)
                kpi1.metric("Latest Frustration", f"{latest.get('frustration_level', 0)}/10")
                kpi2.metric("Latest BP", f"{latest.get('systolic_bp')}/{latest.get('diastolic_bp')}")
                
                weekly_fuel = df[df['date'] > (datetime.now() - pd.Timedelta(days=7))]['fuel_minutes'].sum()
                kpi3.metric("Weekly Fuel", f"{weekly_fuel} min", "Goal: 120+")

                # Charts
                st.plotly_chart(px.bar(df, x='date', y='fuel_minutes', color='fuel_activity', title="Aerobic Fuel (BDNF Boost)"), use_container_width=True)
                st.plotly_chart(px.line(df, x='date', y='frustration_level', title="Cognitive Intensity (Wiring)"), use_container_width=True)

    with tab2:
        st.markdown("### Medical Lab Tracking")
        st.info("Based on 'Medical Data Visualization Project', monitoring for **Introduction of Volatilities**.")
        
        with st.form("lab_entry_form"):
            lab_date = st.date_input("Lab Date", datetime.now())
            
            l1, l2, l3 = st.columns(3)
            with l1:
                a1c = st.number_input("HbA1c (%)", min_value=0.0, step=0.1, help="Goal: <7.5% for age bracket")
                glucose = st.number_input("Random Glucose (mg/dL)", min_value=0, step=1)
            with l2:
                b12 = st.number_input("Vitamin B12 (pg/mL)", min_value=0, step=10, help="Warning: >1000 can be toxic")
                vit_d = st.number_input("Vitamin D (ng/mL)", min_value=0, step=1, help="Warning: >100 is toxic range")
            with l3:
                egfr = st.number_input("eGFR (mL/min)", min_value=0, step=1)
                
            lab_submit = st.form_submit_button("Log Lab Results")
            
            if lab_submit:
                lab_entry = {
                    "date": str(lab_date),
                    "type": "lab",
                    "a1c": a1c,
                    "glucose": glucose,
                    "b12": b12,
                    "vit_d": vit_d,
                    "egfr": egfr
                }
                current_data = load_data()
                current_data.append(lab_entry)
                save_data(current_data)
                st.success("Lab Data Saved")

        # Lab Visualization
        data = load_data()
        lab_data_list = [d for d in data if d.get('type') == 'lab']
        if lab_data_list:
            ldf = pd.DataFrame(lab_data_list)
            ldf['date'] = pd.to_datetime(ldf['date'])
            ldf = ldf.sort_values('date')
            
            lc1, lc2 = st.columns(2)
            
            with lc1:
                st.subheader("Metabolic Control")
                fig_met = px.line(ldf, x='date', y=['a1c'], markers=True, title="HbA1c Trend")
                # Add reference line
                fig_met.add_hline(y=7.5, line_dash="dot", annotation_text="Target Limit (7.5%)", annotation_position="top right")
                st.plotly_chart(fig_met, use_container_width=True)
                
            with lc2:
                st.subheader("Micronutrients (Toxicity Watch)")
                fig_micro = px.line(ldf, x='date', y=['b12', 'vit_d'], markers=True, title="B12 & Vit D Levels")
                fig_micro.add_hline(y=1000, line_dash="dash", line_color="red", annotation_text="B12 Toxicity Risk")
                fig_micro.add_hline(y=100, line_dash="dash", line_color="orange", annotation_text="Vit D Toxicity Risk")
                st.plotly_chart(fig_micro, use_container_width=True)

    with tab3:
        st.markdown("""
        ### About the Framework
        
        **The 3 Pillars of White Matter Health:**
        1.  **Fuel (Aerobics):** Increases BDNF. *Key Activities: Walking, Swimming, Ping Pong.*
        2.  **Wiring (Challenge):** The "Frustration Signal" builds myelin. *Key Activities: Music, Logic Games, New Skills.*
        3.  **Protection (Vascular):** Managing BP and Glucose prevents damage.
        
        **Medical Watchlist:**
        -   **Vitamin B12:** Monitor for levels >1,500 pg/mL (Supplement overuse).
        -   **Vitamin D:** Monitor for >100 ng/mL.
        -   **Diabetes:** Watch for volatility in A1c and Glucose spikes.
        """)
        
        # Export Data Button
        data = load_data()
        if data:
            df = pd.DataFrame(data)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download All Data (CSV)", csv, "medical_regimen_log.csv", "text/csv")

if __name__ == "__main__":
    main()
