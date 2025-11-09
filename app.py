import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Healthcare Operations Optimizer", layout="wide")

st.title("🏥 Smart Healthcare Operations Optimizer")
st.markdown("### Real-Time Healthcare Systems Engineering Simulator + Advanced Analytics")

tab1, tab2 = st.tabs(["📊 Dashboard", "🧮 Advanced Analytics"])

# ==========================================================
# TAB 1 – MAIN DASHBOARD
# ==========================================================
with tab1:
    st.sidebar.header("⚙️ Input Parameters")
    num_doctors = st.sidebar.slider("Number of Doctors", 1, 20, 5)
    num_patients_per_hour = st.sidebar.slider("Patients per Hour", 10, 100, 30)
    consult_time = st.sidebar.slider("Average Consultation Time (mins)", 5, 30, 10)
    num_beds = st.sidebar.slider("Available Beds", 5, 100, 20)
    staff_shifts = st.sidebar.slider("Staff Shifts", 1, 5, 3)

    # --- Core Calculations ---
    patients_per_doctor = num_patients_per_hour / num_doctors
    doctor_utilization = min(100, (patients_per_doctor * consult_time / 60) * 100)
    waiting_time = max(0, (patients_per_doctor * consult_time) - 60)
    bed_utilization = min(100, (num_patients_per_hour / num_beds) * 100)
    throughput = num_patients_per_hour * staff_shifts

    # --- Recommendations ---
    if doctor_utilization > 90:
        doctor_msg = "⚠️ Doctors are overutilized. Consider hiring more doctors or reducing consultation time."
    else:
        doctor_msg = "✅ Doctor utilization is optimal."

    if bed_utilization > 85:
        bed_msg = "⚠️ High bed occupancy. Risk of patient overflow!"
    else:
        bed_msg = "✅ Bed availability is healthy."

    # --- Display KPIs ---
    st.subheader("📈 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Doctor Utilization", f"{doctor_utilization:.1f} %")
    col2.metric("Avg Waiting Time", f"{waiting_time:.1f} mins")
    col3.metric("Bed Utilization", f"{bed_utilization:.1f} %")
    st.metric("Throughput (patients/shift)", f"{throughput}")

    st.write("---")

    # --- Visualization ---
    fig = go.Figure()
    fig.add_trace(go.Bar(x=["Doctors", "Beds"], y=[doctor_utilization, bed_utilization],
                         marker_color=["#2E86AB", "#76B041"]))
    fig.update_layout(title="Resource Utilization (%)", yaxis=dict(range=[0, 120]))
    st.plotly_chart(fig, use_container_width=True)

    # --- Real-Time Simulation ---
    st.subheader("🩺 Real-Time Patient Flow Simulation")
    progress_text = "Simulating patient inflow..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=f"Simulating {percent_complete+1}%")
    time.sleep(0.5)
    st.success("✅ Simulation Complete")

    # --- Insights ---
    st.subheader("💡 Insights & Optimization Suggestions")
    st.write(f"- {doctor_msg}")
    st.write(f"- {bed_msg}")
    st.write("- Improve scheduling efficiency using rotation between shifts.")
    st.write("- Apply Lean or Six Sigma principles to reduce waiting time.")
    st.write("- Evaluate ROI before capacity expansion.")

# ==========================================================
# TAB 2 – ADVANCED ANALYTICS
# ==========================================================
with tab2:
    st.header("🧮 Advanced Healthcare Analytics")
    st.markdown("#### Quantitative Decision Support for Healthcare Systems")

    st.subheader("💰 ROI (Return on Investment) Calculator")
    colA, colB, colC = st.columns(3)
    investment = colA.number_input("Total Investment (₹)", 10000, 10000000, 500000)
    annual_savings = colB.number_input("Expected Annual Savings (₹)", 1000, 5000000, 100000)
    years = colC.slider("Time Period (years)", 1, 10, 3)

    roi = ((annual_savings * years - investment) / investment) * 100
    st.metric("ROI over Time Period", f"{roi:.2f} %")

    if roi > 50:
        st.success("✅ Excellent ROI — expansion or new process design is financially viable.")
    elif roi > 0:
        st.warning("⚠️ Moderate ROI — consider fine-tuning your process.")
    else:
        st.error("❌ Negative ROI — not financially feasible.")

    st.write("---")

    st.subheader("📈 Six Sigma Performance Estimator")
    defects = st.number_input("Defects Observed per 1,000 Patients", 0, 1000, 50)
    opportunities = 1000 * 10  # assume 10 opportunities per patient
    dpmo = (defects / opportunities) * 1_000_000
    sigma_level = 6 - (np.log10(dpmo/3.4) if dpmo > 0 else 0)

    st.metric("Defects per Million Opportunities (DPMO)", f"{dpmo:.0f}")
    st.metric("Estimated Sigma Level", f"{sigma_level:.2f} σ")

    if sigma_level >= 5:
        st.success("✅ Excellent process quality (World-Class).")
    elif sigma_level >= 4:
        st.info("🟢 Good process, scope for improvement.")
    elif sigma_level >= 3:
        st.warning("🟠 Moderate quality — consider Six Sigma interventions.")
    else:
        st.error("🔴 Poor quality — urgent process redesign required.")

    st.write("---")

    st.subheader("📋 Strategic Recommendations")
    st.markdown("""
    - **Implement continuous improvement programs (Kaizen, Lean Six Sigma).**
    - **Conduct workload balancing across shifts to improve throughput.**
    - **Automate repetitive tasks to improve ROI and reduce human errors.**
    - **Apply Value Stream Mapping to identify process bottlenecks.**
    - **Use ERP systems for integrated healthcare resource management.**
    """)

    st.caption("Analytics based purely on engineering and management principles — No datasets or ML used.")
