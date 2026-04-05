import streamlit as st

# --- CONFIG ---
st.set_page_config(page_title="Limbic.kz | Olimp Prep", page_icon="🧬", layout="wide")

# --- УЛУЧШЕННЫЙ CSS ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    /* Стиль карточек на главной */
    .menu-card {
        background: linear-gradient(145deg, #1c2128, #161b22);
        border: 1px solid #30363d;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        transition: 0.4s;
        cursor: pointer;
        height: 100%;
    }
    .menu-card:hover {
        border-color: #58a6ff;
        transform: translateY(-10px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }
    /* Плашки сложности */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .lvl-easy { background-color: #238636; color: white; }
    .lvl-med { background-color: #9e6a03; color: white; }
    .lvl-hard { background-color: #da3633; color: white; }
    
    /* Красивый скроллбар */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #30363d; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- ИНИЦИАЛИЗАЦИЯ НАВИГАЦИИ ---
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Главная"

def set_page(name):
    st.session_state.page = name

# --- БАЗА ЗАДАЧ ---
data = {
    "⚖️ Харди-Вайнберг": [
        {"id": 1, "lvl": "Область", "class": "lvl-easy", "title": "Кабаны Алаколя", "q": "В популяции 1000 особей. 510 черных (A-), остальные серые (aa). Найдите p и q.", "step1": "Серые (aa) = 1000 - 510 = 490. q² = 0.49.", "step2": "q = √0.49 = 0.7. p = 1 - 0.7 = 0.3.", "ans": "p=0.3, q=0.7"},
        {"id": 2, "lvl": "Область", "class": "lvl-easy", "title": "Гетерозиготность", "q": "Частота рецессивного аллеля q = 0.2. Каков процент гетерозигот?", "step1": "p = 1 - 0.2 = 0.8.", "step2": "2pq = 2 * 0.8 * 0.2 = 0.32.", "ans": "32%"}
    ],
    "💉 Множественные аллели": [
        {"id": 3, "lvl": "Республика", "class": "lvl-med", "title": "Группы крови AB0", "q": "Группа I (ii) = 16%, Группа II (IA-) = 20%. Найдите частоты IA, IB, i.", "step1": "r (i) = √0.16 = 0.4. (p+r)² = 0.16 + 0.20 = 0.36.", "step2": "p+r = 0.6 => p(IA) = 0.2. q(IB) = 1 - 0.4 - 0.2 = 0.4.", "ans": "IA=0.2, IB=0.4, i=0.4"}
    ],
    "🎲 Дрейф и Отбор": [
        {"id": 4, "lvl": "Республика", "class": "lvl-med", "title": "Эффект основателя", "q": "10 основателей, у одного болезнь (aa). Начальная частота q?", "step1": "10 человек = 20 аллелей. У больного 2 аллеля 'a'.", "step2": "q = 2 / 20 = 0.1.", "ans": "q=0.1"},
        {"id": 5, "lvl": "IBO", "class": "lvl-hard", "title": "Мутационное давление", "q": "Скорость мутации A->a (u) = 10⁻⁵. Сколько поколений нужно для заметного сдвига?", "step1": "Используйте формулу Δq = u * p.", "step2": "При малых u изменения крайне медленны без участия отбора.", "ans": "Расчет зависит от конечного q_t."}
    ],
    "📊 Статистика": [
        {"id": 6, "lvl": "Республика", "class": "lvl-med", "title": "Хи-квадрат тест", "q": "Наблюдаемые: 40, 40, 20. Ожидаемые: 36, 48, 16. Вычислите X².", "step1": "Формула: Σ(O-E)²/E.", "step2": "X² = 0.44 + 1.33 + 1.0 = 2.77.", "ans": "X² = 2.77 (p > 0.05)"}
    ]
}

# --- SIDEBAR ---
with st.sidebar:
    st.title("🧬 Limbic.kz")
    st.write("🇰🇿 Поддержка био-олимпийцев")
    st.markdown("---")
    choice = st.radio("Навигация:", ["🏠 Главная"] + list(data.keys()), index=0 if st.session_state.page == "🏠 Главная" else list(data.keys()).index(st.session_state.page)+1)
    if choice != st.session_state.page:
        st.session_state.page = choice
        st.rerun()
    st.divider()
    st.caption("Автор: Нурислам С.")

# --- MAIN PAGE LOGIC ---
if st.session_state.page == "🏠 Главная":
    st.title("Limbic.kz: Интерактивный Задачник")
    st.markdown("#### Выберите модуль для глубокого погружения в популяционную генетику")
    
    # Сетка меню
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""<div class="menu-card"><h2>⚖️ Баланс</h2><p>Фундаментальные законы Харди-Вайнберга и расчеты аллелей.</p></div>""", unsafe_allow_html=True)
        if st.button("Открыть Глава 1", key="g1"): set_page("⚖️ Харди-Вайнберг"); st.rerun()
            
        st.markdown("""<div class="menu-card"><h2>💉 Группы крови</h2><p>Анализ систем AB0, Rh и множественного аллелизма.</p></div>""", unsafe_allow_html=True)
        if st.button("Открыть Глава 2", key="g2"): set_page("💉 Множественные аллели"); st.rerun()

    with col2:
        st.markdown("""<div class="menu-card"><h2>🎲 Эволюция</h2><p>Дрейф генов, отбор, инбридинг и миграция.</p></div>""", unsafe_allow_html=True)
        if st.button("Открыть Глава 3", key="g3"): set_page("🎲 Дрейф и Отбор"); st.rerun()

        st.markdown("""<div class="menu-card"><h2>📊 Статистика</h2><p>Математический анализ: Хи-квадрат и t-тесты.</p></div>""", unsafe_allow_html=True)
        if st.button("Открыть Глава 4", key="g4"): set_page("📊 Статистика"); st.rerun()

else:
    # Страница задач
    st.title(st.session_state.page)
    if st.button("⬅️ Назад в меню"): set_page("🏠 Главная"); st.rerun()
    
    for task in data[st.session_state.page]:
        with st.container():
            st.markdown(f"""
                <div style="background-color: #161b22; padding: 25px; border-radius: 15px; border-left: 5px solid #58a6ff; margin-bottom: 20px;">
                    <span class="badge {task['class']}">{task['lvl']}</span>
                    <h3 style="margin-top: 10px;">Задача №{task['id']}: {task['title']}</h3>
                    <p style="font-size: 18px; color: #e6edf3;">{task['q']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("🔍 Шаг 1: Методология"):
                    st.write(task['step1'])
            with c2:
                with st.expander("🔢 Шаг 2: Вычисления"):
                    st.write(task['step2'])
            
            if st.button(f"Показать финальный ответ №{task['id']}"):
                st.success(f"✅ **Ответ:** {task['ans']}")
            st.markdown("---")
