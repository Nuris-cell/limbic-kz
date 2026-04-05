import streamlit as st
import part1, part2, part3  # Импортируем наши базы задач

# Настройка страницы
st.set_page_config(page_title="Limbic.kz | Олимпиадная Генетика", page_icon="🧬", layout="wide")

# --- СТИЛИЗАЦИЯ (DARK PREMIUM) ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stApp { background: linear-gradient(180deg, #0d1117 0%, #161b22 100%); }
    
    /* Приветственный блок */
    .hero-container {
        padding: 60px; border-radius: 30px; background: rgba(255, 255, 255, 0.03);
        border: 1px solid #30363d; text-align: center; margin-bottom: 50px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    .hero-title { font-size: 4rem; font-weight: 800; color: #58a6ff; margin-bottom: 10px; }
    .preface-text { font-size: 1.25rem; line-height: 1.9; color: #e6edf3; text-align: justify; }
    
    /* Карточки задач */
    .task-card {
        background: #1c2128; padding: 30px; border-radius: 20px;
        border-left: 8px solid #58a6ff; margin-bottom: 30px;
        transition: 0.3s;
    }
    .task-card:hover { transform: scale(1.01); border-left-color: #79c0ff; }
    
    /* Навигация */
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- ЛОГИКА НАВИГАЦИИ ---
all_tasks = {**part1.DATA, **part2.DATA, **part3.DATA}

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3067/3067144.png", width=100) # Заглушка лого
    st.title("Limbic.kz")
    st.markdown("---")
    page = st.radio("Куда отправимся?", ["🏠 Главная и Предисловие"] + list(all_tasks.keys()))
    st.markdown("---")
    st.caption("© 2026 Сайлаубек Нурислам. Все права защищены.")

# --- КОНТЕНТ: ГЛАВНАЯ СТРАНИЦА ---
if page == "🏠 Главная и Предисловие":
    # Блок с фото и приветствием
    col1, col2 = st.columns([1, 2])
    with col1:
        # Здесь вставь свое фото. Пока стоит заглушка.
        st.image("https://img.freepik.com/free-photo/dna-representation-abstract-background_23-2149156475.jpg", 
                 caption="Science is the power of progress", use_container_width=True)
    with col2:
        st.markdown("<h1 style='color: #58a6ff;'>Всем привет! 👋</h1>", unsafe_allow_html=True)
        st.write("### Рад видеть тебя в моем цифровом задачнике.")
        st.info("Это не просто сборник задач. Это путь от основ до уровня IBO.")

    st.markdown("""
    <div class="hero-container">
        <div class="preface-text">
            <b>Дорогой коллега и будущий олимпиец!</b> <br><br>
            Этот задачник — плод долгой работы над анализом олимпиадных заданий последних лет. Я создал его, 
            потому что в свое время мне не хватало ресурса, который бы не просто давал "сухой" ответ, а объяснял 
            <b>логику ошибки</b>. <br><br>
            Генетика — это не про зазубривание формул. Это про понимание того, как микроскопические изменения 
            в ДНК превращаются в макроскопические изменения популяций. Здесь мы разберем всё: от классического 
            равновесия Харди-Вайнберга до сложных статистических моделей Байеса и критериев Хи-квадрат. <br><br>
            <b>Как работать с этим приложением?</b> <br>
            1. Выбери главу в левом меню. <br>
            2. Не спеши смотреть ответ! Разверни 'Этап 1' — там я даю подсказку, как подступиться к задаче. <br>
            3. Если запутался в математике — иди в 'Этап 3'. <br><br>
            Помни: <i>каждая ошибка — это катализатор твоего прогресса</i>. Удачи!
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Быстрые кнопки навигации
    st.subheader("🚀 Быстрый старт по разделам:")
    c1, c2, c3 = st.columns(3)
    chapters = list(all_tasks.keys())
    if c1.button("⚖️ Основы (Глава 1)"): st.toast("Переходи в меню слева!")
    if c2.button("🧬 Эволюция (Глава 4)"): st.toast("Раздел доступен в меню!")
    if c3.button("📊 Статистика (Глава 6)"): st.toast("Листай меню вниз!")

# --- КОНТЕНТ: ЗАДАЧИ ---
else:
    st.markdown(f"<h1>{page}</h1>", unsafe_allow_html=True)
    
    for task in all_tasks[page]:
        with st.container():
            st.markdown(f"""
            <div class="task-card">
                <h3 style="color: #79c0ff;">Задача №{task['id']}: {task.get('title', '')}</h3>
                <p style="font-size: 1.15rem;">{task['q']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            steps = st.columns(3)
            with steps[0]:
                with st.expander("🧐 ЭТАП 1: Анализ"):
                    st.write(task['step1'])
            with steps[1]:
                with st.expander("📐 ЭТАП 2: Модель"):
                    st.write(task['step2'])
            with steps[2]:
                with st.expander("🔢 ЭТАП 3: Расчет"):
                    st.write(task['step3'])
            
            if st.button(f"Показать ответ к №{task['id']}", key=f"ans_{task['id']}"):
                st.success(f"**ОТВЕТ:** {task['ans']}")
            st.markdown("---")
