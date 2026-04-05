import streamlit as st

# --- CONFIG & THEME ---
st.set_page_config(page_title="Limbic.kz | Bio Platform", page_icon="🧬", layout="wide")

# Кастомный дизайн меню и карточек
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button { 
        background-color: #238636; color: white; border-radius: 8px; 
        border: none; font-weight: 600; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #2ea043; transform: translateY(-2px); }
    .task-card { 
        background-color: #161b22; padding: 20px; border-radius: 12px; 
        border: 1px solid #30363d; margin-bottom: 20px; 
    }
    .stExpander { border: 1px solid #30363d !important; border-radius: 10px !important; background-color: #0d1117 !important; }
    h1, h2 { color: #58a6ff !important; }
    .stBadge { background-color: #1f6feb; color: white; padding: 4px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- DATABASE (Задачи из твоего PDF) ---
# Я структурировал их так, чтобы они подгружались автоматически
data = {
    "⚖️ Харди-Вайнберг": [
        {
            "id": 1, "lvl": "Region", "title": "Кабаны Алаколя",
            "q": "В популяции 1000 особей. 510 черных (A-), остальные серые (aa). Найдите частоты p и q.",
            "step1": "Серые (aa) = 1000 - 510 = 490. Частота q² = 0.49.",
            "step2": "q = √0.49 = 0.7. Следовательно, p = 1 - 0.7 = 0.3.",
            "ans": "p=0.3, q=0.7"
        },
        {
            "id": 2, "lvl": "Region", "title": "Гетерозиготность",
            "q": "Частота рецессивного аллеля q = 0.2. Каков процент гетерозигот?",
            "step1": "p = 1 - 0.2 = 0.8.",
            "step2": "Частота Aa = 2pq = 2 * 0.8 * 0.2 = 0.32.",
            "ans": "32%"
        }
    ],
    "💉 Множественные аллели": [
        {
            "id": 3, "lvl": "Republic", "title": "Группы крови AB0",
            "q": "Группа I (ii) = 16%, Группа II (IA-) = 20%. Найдите IA, IB, i.",
            "step1": "r (i) = √0.16 = 0.4. (p+r)² = 0.16 + 0.20 = 0.36.",
            "step2": "p+r = 0.6 => p(IA) = 0.2. q(IB) = 1 - 0.4 - 0.2 = 0.4.",
            "ans": "IA=0.2, IB=0.4, i=0.4"
        }
    ],
    "🧬 Сцепление с полом": [
        {
            "id": 4, "lvl": "IBO", "title": "Дальтонизм",
            "q": "У мужчин частота дальтонизма 8%. Какова частота среди женщин?",
            "step1": "Для X-сцепленных: мужчины (XaY) = q = 0.08.",
            "step2": "Женщины (XaXa) = q² = 0.08² = 0.0064.",
            "ans": "0.64%"
        }
    ],
    "🎲 Дрейф и Отбор": [
        {
            "id": 5, "lvl": "Republic", "title": "Эффект основателя",
            "q": "10 основателей, у одного болезнь (aa). Начальная частота q?",
            "step1": "10 человек = 20 аллелей. У больного 2 аллеля 'a'.",
            "step2": "q = 2 / 20 = 0.1.",
            "ans": "q=0.1"
        },
        {
            "id": 6, "lvl": "IBO", "title": "Коэффициент отбора (s)",
            "q": "Если выживаемость aa = 0.8, чему равен коэффициент отбора s?",
            "step1": "Выживаемость (w) = 1 - s.",
            "step2": "s = 1 - 0.8 = 0.2.",
            "ans": "s=0.2"
        }
    ],
    "📊 Статистика (X²)": [
        {
            "id": 7, "lvl": "Republic", "title": "Критерий Хи-квадрат",
            "q": "Ожидаемые: 36, 48, 16. Наблюдаемые: 40, 40, 20. Вычислите X².",
            "step1": "Σ(O-E)²/E = (4/36) + (64/48) + (16/16).",
            "step2": "0.44 + 1.33 + 1.0 = 2.77.",
            "ans": "X² = 2.77"
        }
    ]
}

# --- SIDEBAR MENU ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022607.png", width=100)
    st.title("Limbic.kz")
    st.markdown("---")
    
    # Красивый выбор раздела
    st.subheader("Навигация")
    choice = st.radio("Разделы задачника:", list(data.keys()))
    
    st.markdown("---")
    st.info(f"**Автор:** Сайлаубек Н.\n\n**Цель:** KAIST Portfolio Project")

# --- MAIN CONTENT ---
if choice:
    st.title(choice)
    st.write(f"Оцифрованные задачи из раздела '{choice[2:]}' твоего учебника.")
    
    for task in data[choice]:
        # Создаем карточку задачи
        st.markdown(f"""
            <div class="task-card">
                <span class="stBadge">{task['lvl']}</span>
                <h3>Задача №{task['id']}: {task['title']}</h3>
                <p>{task['q']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Интерактивные подсказки внутри карточки
        c1, c2 = st.columns(2)
        with c1:
            with st.expander("💡 Шаг 1: Логика"):
                st.write(task['step1'])
        with c2:
            with st.expander("🔢 Шаг 2: Расчет"):
                st.write(task['step2'])
        
        if st.button(f"Проверить ответ №{task['id']}", key=f"btn_{task['id']}"):
            st.success(f"**Правильный ответ:** {task['ans']}")
        
        st.markdown("<br>", unsafe_allow_html=True)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Limbic.kz | Bio-Systematic Learning")
