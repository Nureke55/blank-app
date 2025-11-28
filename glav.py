import streamlit as st
import psutil
import time
import matplotlib.pyplot as plt


st.set_page_config(page_title="Компьютер мониторингі", layout="wide")
st.title("🖥 Компьютер күйін бақылау тақтасы")


st.sidebar.header("Бақылау параметрлері")
refresh_rate = st.sidebar.slider("Жаңарту уақыты (сек)", 1, 5, 1)


# Метрикалар алу функциясы
def get_system_stats():
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disk = psutil.disk_usage('/')
return cpu, ram, disk


# Графиктер үшін деректер
cpu_history = []


placeholder = st.empty()


while True:
with placeholder.container():
cpu, ram, disk = get_system_stats()


col1, col2, col3 = st.columns(3)
col1.metric("CPU %", f"{cpu}%")
col2.metric("RAM %", f"{ram.percent}%")
col3.metric("Disk %", f"{disk.percent}%")


cpu_history.append(cpu)
if len(cpu_history) > 20:
cpu_history.pop(0)


fig, ax = plt.subplots()
ax.plot(cpu_history)
ax.set_title("CPU жүктемесінің өзгерісі")
ax.set_ylabel("%")
ax.set_xlabel("Уақыт")


st.pyplot(fig)
time.sleep(refresh_rate)