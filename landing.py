import streamlit as st

st.set_page_config(
    page_title="Нейромастерская НЮансов", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* ТЁМНАЯ ТЕМА */
    .stApp { 
        background: linear-gradient(135deg, #1a1a2e 0%, #2d2d44 100%);
        color: #ffffff;
    }
    h1, h2, h3 { 
        color: #e0e0e0; 
        font-family: 'Georgia', serif; 
    }
    
    /* Главный экран */
    .hero {
        text-align: center; 
        padding: 50px 20px;
        background: linear-gradient(135deg, #6A1B9A 0%, #8E24AA 50%, #FDD835 100%);
        border-radius: 20px; 
        margin-bottom: 40px;
        box-shadow: 0 8px 25px rgba(106, 27, 154, 0.4);
    }
    .hero h1 { 
        font-size: 2.8em; 
        margin-bottom: 15px; 
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .hero p { 
        font-size: 1.3em; 
        color: #fff9c4;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Крупные цветные надписи-ссылки */
    .big-link-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    .big-link {
        font-size: 1.5em;
        font-weight: bold;
        text-decoration: none;
        padding: 15px 30px;
        border-radius: 50px;
        transition: all 0.3s;
        display: inline-block;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(10px);
    }
    .big-link:hover { 
        transform: scale(1.05);
        background: rgba(255,255,255,0.25);
    }
    .link-yellow {
        color: #1a1a2e;
        background: #FDD835;
        border: 2px solid #FDD835;
    }
    .link-purple {
        color: #ffffff;
        background: #6A1B9A;
        border: 2px solid #8E24AA;
    }
    
    /* Карточки */
    .card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        padding: 30px; 
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        border-left: 5px solid #FDD835;
        color: #e0e0e0;
    }
    .card-purple { 
        border-left: 5px solid #8E24AA; 
    }
    .expert-card { 
        text-align: center; 
        padding: 20px; 
    }
    
    /* Фото экспертов */
    .expert-photo {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 20px;
        display: block;
        border: 4px solid #FDD835;
        box-shadow: 0 4px 20px rgba(253, 216, 53, 0.4);
    }
    .expert-photo-natalia {
        border-color: #8E24AA;
        box-shadow: 0 4px 20px rgba(142, 36, 170, 0.4);
    }
    
    /* Кнопки контактов */
    .btn-contact {
        display: block; 
        width: 100%; 
        padding: 15px; 
        margin-top: 15px;
        background: linear-gradient(135deg, #6A1B9A, #8E24AA);
        color: white !important;
        border-radius: 12px; 
        text-decoration: none;
        font-size: 1.1em; 
        font-weight: bold; 
        text-align: center;
        box-sizing: border-box;
        box-shadow: 0 4px 15px rgba(106, 27, 154, 0.4);
    }
    .btn-contact:hover { 
        background: linear-gradient(135deg, #8E24AA, #6A1B9A);
        box-shadow: 0 6px 20px rgba(106, 27, 154, 0.6);
    }

    /* Пульсирующие кнопки */
    @keyframes pulse-purple {
        0% { box-shadow: 0 0 0 0 rgba(142, 36, 170, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(142, 36, 170, 0); }
        100% { box-shadow: 0 0 0 0 rgba(142, 36, 170, 0); }
    }
    @keyframes pulse-yellow {
        0% { box-shadow: 0 0 0 0 rgba(253, 216, 53, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(253, 216, 53, 0); }
        100% { box-shadow: 0 0 0 0 rgba(253, 216, 53, 0); }
    }
    
    .btn-main {
        padding: 15px 30px; 
        border-radius: 50px; 
        text-decoration: none;
        font-weight: bold; 
        font-size: 1.1em; 
        display: inline-block;
        margin: 10px; 
        transition: all 0.3s; 
        border: none;
    }
    .btn-purple {
        background: linear-gradient(135deg, #6A1B9A, #8E24AA);
        color: white !important;
        animation: pulse-purple 2s infinite;
    }
    .btn-yellow {
        background: linear-gradient(135deg, #FDD835, #FBC02D);
        color: #1a1a2e !important;
        animation: pulse-yellow 2s infinite;
    }
    .btn-main:hover { 
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(142, 36, 170, 0.5);
    }

    /* Карточки сравнения */
    .comparison-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(10px);
        padding: 25px; 
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .comparison-card h3 {
        margin-bottom: 20px; 
        padding: 15px; 
        border-radius: 10px; 
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .free-title { 
        background: linear-gradient(135deg, #43A047, #66BB6A); 
    }
    .club-title { 
        background: linear-gradient(135deg, #6A1B9A, #8E24AA); 
    }
    .comparison-card ul { 
        list-style: none; 
        padding: 0; 
        line-height: 2; 
        text-align: left;
        color: #e0e0e0;
    }
    .comparison-card li:before { 
        content: "✓ "; 
        color: #66BB6A; 
        font-weight: bold; 
        margin-right: 8px; 
    }
    
    .highlight { 
        background: linear-gradient(135deg, #FDD835, #FBC02D);
        color: #1a1a2e;
        padding: 3px 8px; 
        border-radius: 6px; 
        font-weight: bold;
        box-shadow: 0 2px 8px rgba(253, 216, 53, 0.3);
    }
    
    .buttons-row {
        display: flex;
        justify-content: center;
        gap: 20px;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    
    /* Подвал */
    footer {
        background: rgba(0,0,0,0.3);
        padding: 20px;
        border-radius: 10px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. ГЛАВНЫЙ ЭКРАН
st.markdown("""
    <div class="hero">
        <h1>Нейросети — понятный помощник, а не головная боль</h1>
        <p>Бесплатный практикум для первых шагов + закрытый клуб «Нейромастерская НЮансов» для глубокого погружения.</p>
        <div class="big-link-container">
            <a href="https://t.me/praktikumdlynahinajuchih" class="big-link link-yellow" target="_blank">🎁 Начать с бесплатного практикума</a>
            <a href="https://t.me/+e4CJuDcXMro3ODcy" class="big-link link-purple" target="_blank">💫 Посмотреть, что внутри клуба</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 2. О НАС
st.markdown("## 👩‍💻 Эксперты Юлия и Наталья")
st.markdown("""
    <div class="card">
        <p>Наша задача простая: помочь внедрить ИИ в повседневные дела и довести каждую идею до результата — «рука об руку».</p>
        <p>Мы — действующие эксперты по нейросетям и кураторы крупной онлайн-школы. За нашими плечами более <span class="highlight">1000 учеников</span>, которым мы уже помогли сделать первые шаги.</p>
    </div>
""", unsafe_allow_html=True)

# 3. КАРТОЧКИ ЭКСПЕРТОВ С ФОТО
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card expert-card">
            <img src="yulia.jpg" alt="Юлия Михеева" class="expert-photo">
            <h3>🛠 Юлия Михеева</h3>
            <p><b>Куратор-практик по нейросетям и цифровым инструментам</b></p>
            <ul style="text-align: left; line-height: 1.8;">
                <li><b>Техническая экспертиза:</b> Создает чат-ботов, ИИ-агентов, пишет код.</li>
                <li><b>Опыт в поддержке:</b> 10+ лет в Ozon, Мегамаркет, Роснефть.</li>
                <li><b>Автор 5 детских книг на Литрес</b> (созданы с помощью ИИ).</li>
                <li><b>Финансист и специалист по госзакупкам.</b></li>
                <li><b>Подход:</b> «Рука об руку» — рядом, пока не получится.</li>
            </ul>
            <a href="https://t.me/a_yulija19790111" class="btn-contact" target="_blank">Написать Юлии</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card expert-card card-purple">
            <img src="natalia.jpg" alt="Наталья Урванцева" class="expert-photo expert-photo-natalia">
            <h3>🎨 Наталья Урванцева</h3>
            <p><b>Наставник по практическому применению ИИ</b></p>
            <ul style="text-align: left; line-height: 1.8;">
                <li><b>Высшее юридическое образование</b> — системное мышление.</li>
                <li><b>Сооснователь «Нейромастерской»</b> и автор «Пиксельных сказок».</li>
                <li><b>Широкий спектр компетенций:</b> AI-видео, инфографика, иллюстрации.</li>
                <li><b>Практик, а не теоретик:</b> метод работы строится на реальной задаче.</li>
                <li><b>Философия:</b> «Не учу кнопкам — учу думать осознанно».</li>
            </ul>
            <a href="https://t.me/Natalia_U" class="btn-contact" target="_blank">Написать Наталье</a>
        </div>
    """, unsafe_allow_html=True)

# 4. СРАВНЕНИЕ
st.markdown("## ⚖️ Бесплатный практикум vs Платный клуб")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="comparison-card">
            <h3 class="free-title">🎁 Бесплатный практикум</h3>
            <ul>
                <li>Мини-гайды и первые шаги в ИИ</li>
                <li>Обзоры нейросетей для визуала и текста</li>
                <li>Самостоятельное изучение</li>
                <li>Общая информация и база</li>
            </ul>
            <br>
            <a href="https://t.me/praktikumdlynahinajuchih" class="btn-main btn-yellow" style="font-size: 1em; padding: 10px 20px;" target="_blank">Подписаться бесплатно</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="comparison-card">
            <h3 class="club-title">💫 Клуб «Нейромастерская НЮансов»</h3>
            <ul>
                <li>Глубокое погружение и рабочие связки</li>
                <li>Библиотека записей уроков и промптов</li>
                <li><b>Живые эфиры</b> с разборами</li>
                <li><b>Персональная обратная связь</b></li>
                <li><b>Новые темы:</b> соцсети, ИИ-агенты</li>
            </ul>
            <br>
            <a href="https://t.me/+e4CJuDcXMro3ODcy" class="btn-main btn-purple" style="font-size: 1em; padding: 10px 20px;" target="_blank">Вступить в клуб</a>
        </div>
    """, unsafe_allow_html=True)

# 5. УСЛОВИЯ
st.markdown("## 💰 Условия участия в клубе")
st.markdown("""
    <div class="card card-purple" style="text-align: center; border: 2px solid #8E24AA;">
        <h2 style="color: #FDD835; margin-bottom: 10px;">2 000 ₽ / месяц</h2>
        <ul style="text-align: left; display: inline-block; font-size: 1.05em; line-height: 1.6;">
            <li>Оплата раз в месяц (перевод на карту)</li>
            <li><b>Работаем официально</b> (самозанятость, налоги)</li>
            <li>Отмена в любой момент</li>
        </ul>
        <div class="buttons-row">
            <a href="https://t.me/a_yulija19790111" class="btn-main btn-purple" target="_blank"> Написать Юлии</a>
            <a href="https://t.me/Natalia_U" class="btn-main btn-purple" target="_blank">💫 Написать Наталье</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. ПОДВАЛ
st.markdown("---")
st.markdown("""
    <footer>
        <div style="text-align: center; color: #e0e0e0; padding: 20px;">
            <p>Простой ИИ без стресса и сложных терминов.</p>
            <p><b>Юлия и Наталья</b> </p>
            <p><a href="https://t.me/praktikumdlynahinajuchih" style="color: #FDD835; text-decoration: none;">Перейти в наш бесплатный Telegram-канал</a></p>
        </div>
    </footer>
""", unsafe_allow_html=True)
