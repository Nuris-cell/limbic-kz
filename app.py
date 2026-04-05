import streamlit as st

st.set_page_config(page_title="Limbic.kz", page_icon="🧬")

# Боковое меню
st.sidebar.title("Навигация")
topic = st.sidebar.selectbox("Выберите раздел:", ["Главная", "Генетика", "Цитология", "Биоинформатика"])

if topic == "Главная":
    st.title("🧬 Limbic.kz")
    st.write("Добро пожаловать на платформу для олимпийцев Казахстана.")
    st.write("Выбирай раздел в меню слева и начинай прокачку.")

elif topic == "Генетика":
    st.title("🧬 Раздел: Генетика")
    
    # Твоя задача про кабанов
    with st.container():
        st.subheader("Задача №1. Популяция кабанов Алаколя")
        st.info("В популяции 1000 особей. 510 черных кабанов... (условие)")
        
        with st.expander("Шаг №1: Анализ"):
            st.write("Начинаем с рецессивных особей...")
            
        with st.expander("Шаг №2: Расчет"):
            st.latex(r"q = \sqrt{0.49} = 0.7")
            
        if st.button("Показать ответ"):
            st.success("Ответ: p=0.3, q=0.7")

elif topic == "Цитология":
    st.title("🔬 Раздел: Цитология")
    st.write("Тут скоро появятся задачи на циклы и метаболизм.")
