import streamlit as st

# --- CONFIG & THEME ---
st.set_page_config(page_title="Limbic.kz | Bio Platform", page_icon="🧬", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button { 
        background-color: #238636; color: white; border-radius: 8px; 
        border: none; font-weight: 600; transition: 0.3s; width: 100%;
    }
    .stButton>button:hover { background-color: #2ea043; transform: translateY(-2px); }
    .task-card { 
        background-color: #161b22; padding: 20px; border-radius: 12px; 
        border: 1px solid #30363d; margin-bottom: 20px; 
    }
    .chapter-card {
        background-color: #1c2128; padding: 25px; border-radius: 15px;
        border: 1px solid #388bfd; text-align: center; height: 250px;
    }
    h1, h2 { color: #58a6ff !important; }
    .stBadge { background-color: #1f6feb; color: white; padding: 4px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE ---
data = {
    "⚖️ Харди-Вайнберг": [
        {"id": 1, "lvl": "Область", "title": "Кабаны Алаколя", "q": "В популяции 1000 особей. 510 черных (A-), остальные серые (aa). Найдите p и q.", "step1": "Серые (aa) = 1000 - 510 = 490. q² = 0.49.", "step2": "q = √0.49 = 0.7. p = 1 - 0.7 = 0.3.", "ans": "p=0.3, q=0.7"},
        {"id": 2, "lvl": "Область", "title": "Гетерозиготность", "q": "Частота рецессивного аллеля q = 0.2. Каков процент гетерозигот?", "step1": "p = 1 - 0.2 = 0.8.", "step2": "2pq = 2 * 0.8 * 0.2 = 0.32.", "ans": "32%"}
    ],
    "💉 Множественные аллели": [
        {"id": 3, "lvl": "Республика", "title": "Группы крови AB0", "q": "Группа I (ii) = 16%, Группа II (IA-) = 20%. Найдите частоты IA, IB, i.", "step1": "r (i) = √0.16 = 0.4. (p+r)² = 0.16 + 0.20 = 0.36.", "step2": "p+r = 0.6 => p(IA) = 0.2. q(IB) = 1 - 0.4 - 0.2 = 0.4.", "ans": "IA=0.2, IB=0.4, i=0.4"}
    ],
    "🧬 Сцепление с полом": [
        {"id": 4, "lvl": "IBO", "title": "Дальтонизм", "q": "У мужчин частота дальтонизма 8%. Какова частота среди женщин?", "step1": "Для X-сцепленных: мужчины (XaY) = q = 0.08.", "step2": "Женщины (XaXa) = q² = 0.08² = 0.0064.", "ans": "0.64%"}
    ],
    "🎲 Дрейф и Отбор": [
        {"id": 5, "lvl": "Республика", "title": "Эффект основателя", "q": "10 основателей, у одного болезнь (aa). Начальная частота q?", "step1": "10 человек = 20 аллелей. У больного 2 аллеля 'a'.", "step2": "q = 2 / 20 = 0.1.", "ans": "q=0.1"}
    ],
    "📊 Статистика (X²)": [
        {"id": 6, "lvl": "Республика", "title": "Критерий Хи-квадрат", "q": "Ожидаемые: 36, 48, 16. Наблюдаемые: 40, 40, 20. Вычислите X².", "step1": "Σ(O-E)²/E = (4/36) + (64/48) + (16/16).", "step2": "0.44 + 1.33 + 1.0 = 2.77.", "ans": "X² = 2.77"}
    ]
}

# --- SIDEBAR ---
with st.sidebar:
    st.title("🧬 Limbic.kz")
    st.write("Поддержка олимпийского резерва Казахстана 🇰🇿")
    st.divider()
    
    # Добавляем "Главную" в список выбора
    menu_options = ["🏠 Главная"] + list(data.keys())
    choice = st.radio("Переход по разделам:", menu_options)
    
    st.divider()
    st.caption("Автор задачника: Сайлаубек Нурислам")

# --- MAIN LOGIC ---

if choice == "🏠 Главная":
    st.title("Добро пожаловать в Limbic.kz")
    st.markdown("#### Интерактивная платформа для подготовки к олимпиадам по биологии")
    st.write("Выберите раздел, чтобы приступить к решению задач из обновленного задачника:")
    
    # Сетка разделов (Главное меню)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="chapter-card"><h3>⚖️ Баланс</h3><p>Закон Харди-Вайнберга и основы популяционной генетики.</p></div>', unsafe_allow_html=True)
        if st.button("Открыть Генетику"): st.session_state.choice = "⚖️ Харди-Вайнберг"
            
    with col2:
        st.markdown('<div class="chapter-card"><h3>💉 Группы крови</h3><p>Множественный аллелизм и система AB0 в популяциях.</p></div>', unsafe_allow_html=True)
        if st.button("Открыть Аллели"): st.session_state.choice = "💉 Множественные аллели"

    with col3:
        st.markdown('<div class="chapter-card"><h3>🎲 Эволюция</h3><p>Дрейф генов, эффект основателя и коэффициенты отбора.</p></div>', unsafe_allow_html=True)
        if st.button("Открыть Факторы"): st.session_state.choice = "🎲 Дрейф и Отбор"
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown('<div class="chapter-card"><h3>🧬 Сцепление</h3><p>Наследование признаков, сцепленных с полом (X/Y).</p></div>', unsafe_allow_html=True)
        if st.button("Открыть Сцепление"): st.session_state.choice = "🧬 Сцепление с полом"
    with col5:
        st.markdown('<div class="chapter-card"><h3>📊 Статистика</h3><p>Критерий Хи-квадрат и анализ достоверности данных.</p></div>', unsafe_allow_html=True)
        if st.button("Открыть Статистику"): st.session_state.choice = "📊 Статистика (X²)"
    with col6:
        st.markdown('<div class="chapter-card"><h3>🇰🇿 О проекте</h3><p>Миссия Limbic.kz — развитие биологического комьюнити в Казахстане.</p></div>', unsafe_allow_html=True)

else:
    # Отрисовка задач выбранного раздела
    st.title(choice)
    st.button("⬅️ Вернуться на главную", on_click=lambda: st.write("Нажми на Главную в меню"))
    
    for task in data[choice]:
        st.markdown(f"""
            <div class="task-card">
                <span class="stBadge">{task['lvl']}</span>
                <h3>Задача №{task['id']}: {task['title']}</h3>
                <p>{task['q']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            with st.expander("💡 Шаг 1: Логика"): st.write(task['step1'])
        with c2:
            with st.expander("🔢 Шаг 2: Расчет"): st.write(task['step2'])
        
        if st.button(f"Проверить ответ №{task['id']}", key=f"btn_{task['id']}"):
            st.success(f"**Правильный ответ:** {task['ans']}")
        st.markdown("<br>", unsafe_allow_html=True)
