import streamlit as st
from data_part1 import CHAPTERS_1_3
from data_part2 import CHAPTERS_4_6

# Объединяем все базы данных
FULL_DB = {**CHAPTERS_1_3, **CHAPTERS_4_6}

st.set_page_config(page_title="Limbic.kz | Pro Prep", page_icon="🧬", layout="wide")

# --- СТИЛИЗАЦИЯ ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stApp { background-image: radial-gradient(circle at 2px 2px, #21262d 1px, transparent 0); background-size: 40px 40px; }
    
    /* Карточки задач */
    .task-card {
        background-color: #161b22;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #30363d;
        border-left: 6px solid #58a6ff;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Главное меню */
    .hero-section {
        background: linear-gradient(90deg, #0d1117 0%, #161b22 100%);
        padding: 50px;
        border-radius: 20px;
        border: 1px solid #30363d;
        text-align: center;
        margin-bottom: 40px;
    }
    
    .chapter-box {
        background-color: #1c2128;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        transition: 0.3s;
        cursor: pointer;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .chapter-box:hover { border-color: #58a6ff; transform: translateY(-5px); }
    
    h1, h2, h3 { color: #58a6ff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА НАВИГАЦИИ ---
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Главная"

def go_to(page_name):
    st.session_state.page = page_name

# --- SIDEBAR ---
with st.sidebar:
    st.title("🧬 Limbic.kz")
    st.markdown("### Олимпиадный задачник")
    st.divider()
    if st.button("🏠 Вернуться на главную"): go_to("🏠 Главная")
    st.divider()
    st.subheader("Разделы:")
    for ch in FULL_DB.keys():
        if st.button(ch, key=f"side_{ch}"): go_to(ch)

# --- КОНТЕНТ ---
if st.session_state.page == "🏠 Главная":
    st.markdown("""
        <div class="hero-section">
            <h1 style='font-size: 3.5rem;'>Всем привет! 👋</h1>
            <p style='font-size: 1.5rem; color: #8b949e;'>Добро пожаловать в цифровое издание интерактивного задачника <b>Limbic.kz</b></p>
            <p style='max-width: 800px; margin: 0 auto; line-height: 1.6;'>
                Этот проект создан для того, чтобы превратить сложную математическую логику популяционной генетики 
                в понятный и увлекательный процесс. Здесь собраны все задачи из 1-го издания, разбитые по уровням сложности и темам.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗺 Выбери траекторию обучения:")
    
    # Сетка меню
    cols = st.columns(2)
    for i, chapter in enumerate(FULL_DB.keys()):
        with cols[i % 2]:
            st.markdown(f"""<div class="chapter-box"><h3>{chapter}</h3><p>Нажмите кнопку ниже, чтобы открыть список задач.</p></div>""", unsafe_allow_html=True)
            if st.button(f"Открыть {chapter[:15]}...", key=f"main_{chapter}"):
                go_to(chapter)
                st.rerun()
            st.write("")

else:
    # Страница конкретной главы
    st.title(st.session_state.page)
    if st.button("⬅️ Назад в меню"): go_to("🏠 Главная"); st.rerun()
    
    st.divider()
    
    for task in FULL_DB[st.session_state.page]:
        st.markdown(f"""
            <div class="task-card">
                <span style="color: #8b949e; font-weight: bold;">ЗАДАЧА №{task['id']}</span>
                <h2 style="margin-top: 5px;">{task.get('title', 'Без названия')}</h2>
                <p style="font-size: 1.2rem; line-height: 1.6;">{task['q']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Socratic Stepper (3 этапа)
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.expander("📝 ЭТАП 1: Анализ"):
                st.info(task['step1'])
        with c2:
            with st.expander("📐 ЭТАП 2: Стратегия"):
                st.warning(task['step2'])
        with c3:
            with st.expander("🔢 ЭТАП 3: Расчет"):
                st.success(task['step3'])
        
        if st.button(f"✨ Показать финальный ответ №{task['id']}", key=f"ans_{task['id']}"):
            st.balloons()
            st.markdown(f"""<div style="background-color: #238636; color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 1.5rem; font-weight: bold;">
                Ответ: {task['ans']}
            </div>""", unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
