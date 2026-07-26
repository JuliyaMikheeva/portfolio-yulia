import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Нейромастерская НЮансов", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Пути к фото
yulia_photo = "yulia.jpg"
natalia_photo = "natalia.jpg"

st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #fff9f0 0%, #fff 50%, #f3e5f5 100%);
        color: #333333;
    }
    h1, h2, h3 { 
        color: #6A1B9A; 
        font-family: 'Georgia', serif; 
    }
    
    .hero {
        text-align: center; 
        padding: 60px 30px;
        background: linear-gradient(135deg, #8E24AA 0%, #AB47BC 50%, #FDD835 100%);
        border-radius: 25px; 
        margin-bottom: 50px;
        box-shadow: 0 10px 40px rgba(142, 36, 170, 0.3);
    }
    .hero h1 { 
        font-size: 3em; 
        margin-bottom: 20px; 
        color: #ffffff;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    .hero p { 
        font-size: 1.4em; 
        color: #fffde7;
        margin-bottom: 40px;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    
    .big-link-container {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 30px;
    }
    .big-link {
        font-size: 1.6em;
        font-weight: bold;
        text-decoration: none;
        padding: 18px 35px;
        border-radius: 50px;
        transition: all 0.3s;
        display: inline-block;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }
    .big-link:hover { 
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    .link-yellow {
        color: #1a1a2e;
        background: linear-gradient(135deg, #FDD835, #FBC02D);
        border: 3px solid #F9A825;
    }
    .link-purple {
        color: #ffffff;
        background: linear-gradient(135deg, #8E24AA, #6A1B9A);
        border: 3px solid #AB47BC;
    }
    
    .card {
        background: white;
        padding: 35px; 
        border-radius: 20px;
        box-shadow: 0 6px 25px rgba(142, 36, 170, 0.12);
        margin-bottom: 25px;
        border-left: 6px solid #FDD835;
        color: #424242;
    }
    .card-purple { 
        border-left: 6px solid #8E24AA; 
    }
    .expert-card { 
        text-align: center; 
        padding: 30px; 
    }
    
    .btn-contact {
        display: block; 
        width: 100%; 
        padding: 18px; 
        margin-top: 20px;
        background: linear-gradient(135deg, #8E24AA, #6A1B9A);
        color: white !important;
        border-radius: 15px; 
        text-decoration: none;
        font-size: 1.2em; 
        font-weight: bold; 
        text-align: center;
        box-sizing: border-box;
        box-shadow: 0 6px 20px rgba(142, 36, 170, 0.4);
        transition: all 0.3s;
    }
    .btn-contact:hover { 
        background: linear-gradient(135deg, #AB47BC, #8E24AA);
        box-shadow: 0 8px 25px rgba(142, 36, 170, 0.6);
        transform: translateY(-2px);
    }

    @keyframes pulse-purple {
        0% { box-shadow: 0 0 0 0 rgba(142, 36, 170, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(142, 36, 170, 0); }
        100% { box-shadow: 0 0 0 0 rgba(142, 36, 170, 0); }
    }
    @keyframes pulse-yellow {
        0% { box-shadow: 0 0 0 0 rgba(253, 216, 53, 0.7); }
        70% { box-shadow: 0 0 0 20px rgba(253, 216, 53, 0); }
        100% { box-shadow: 0 0 0 0 rgba(253, 216, 53, 0); }
    }
    
    .btn-main {
        padding: 18px 35px; 
        border-radius: 50px; 
        text-decoration: none;
        font-weight: bold; 
        font-size: 1.2em; 
        display: inline-block;
        margin: 15px; 
        transition: all 0.3s; 
        border: none;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }
    .btn-purple {
        background: linear-gradient(135deg, #8E24AA, #6A1B9A);
        color: white !important;
        animation: pulse-purple 2s infinite;
    }
    .btn-yellow {
        background: linear-gradient(135deg, #FDD835, #FBC02D);
        color: #1a1a2e !important;
        animation: pulse-yellow 2s infinite;
    }
    .btn-main:hover { 
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }

    .comparison-card {
        background: white;
        padding: 30px; 
        border-radius: 20px;
        box-shadow: 0 6px 25px rgba(142, 36, 170, 0.12);
        margin-bottom: 25px;
        text-align: center;
        border: 2px solid rgba(142, 36, 170, 0.1);
        transition: all 0.3s;
    }
    .comparison-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 35px rgba(142, 36, 170, 0.2);
    }
    .comparison-card h3 {
        margin-bottom: 25px; 
        padding: 18px; 
        border-radius: 15px; 
        color: white;
        font-size: 1.4em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    .free-title { 
        background: linear-gradient(135deg, #66BB6A, #43A047); 
    }
    .club-title { 
        background: linear-gradient(135deg, #8E24AA, #6A1B9A); 
    }
    .comparison-card ul { 
        list-style: none; 
        padding: 0; 
        line-height: 2.2; 
        text-align: left;
        color: #424242;
        font-size: 1.05em;
    }
    .comparison-card li:before { 
        content: "✓ "; 
        color: #66BB6A; 
        font-weight: bold; 
        font-size: 1.2em;
        margin-right: 8px; 
    }
    
    .highlight { 
        background: linear-gradient(135deg, #FDD835, #FBC02D);
        color: #1a1a2e;
        padding: 5px 12px; 
        border-radius: 8px; 
        font-weight: bold;
        box-shadow: 0 3px 10px rgba(253, 216, 53, 0.3);
    }
    
    .buttons-row {
        display: flex;
        justify-content: center;
        gap: 25px;
        flex-wrap: wrap;
        margin-top: 25px;
    }
    
    footer {
        background: linear-gradient(135deg, #f3e5f5, #fff9f0);
        padding: 30px;
        border-radius: 15px;
        margin-top: 40px;
        border-top: 3px solid #8E24AA;
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

# 3. КАРТОЧКИ ЭКСПЕРТОВ С ФОТО (используем st.image)
col1, col2 = st.columns(2)

with col1:
    # Показываем фото Юлии
    try:
        st.image(yulia_photo, caption="Юлия Михеева", width=220)
    except:
        st.info("📸 Фото Юлии")
    
    st.markdown("""
        <div class="card expert-card">
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
    # Показываем фото Натальи
    try:
        st.image(natalia_photo, caption="Наталья Урванцева", width=220)
    except:
        st.info("📸 Фото Натальи")
    
    st.markdown("""
        <div class="card expert-card card-purple">
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
            <a href="https://t.me/praktikumdlynahinajuchih" class="btn-main btn-yellow" style="font-size: 1em; padding: 12px 25px;" target="_blank">Подписаться бесплатно</a>
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
            <a href="https://t.me/+e4CJuDcXMro3ODcy" class="btn-main btn-purple" style="font-size: 1em; padding: 12px 25px;" target="_blank">Вступить в клуб</a>
        </div>
    """, unsafe_allow_html=True)

# 5. УСЛОВИЯ
st.markdown("## 💰 Условия участия в клубе")
st.markdown("""
    <div class="card card-purple" style="text-align: center; border: 3px solid #8E24AA;">
        <h2 style="color: #6A1B9A; margin-bottom: 15px; font-size: 2.2em;">2 000 ₽ / месяц</h2>
        <ul style="text-align: left; display: inline-block; font-size: 1.1em; line-height: 1.8;">
            <li>Оплата раз в месяц (перевод на карту)</li>
            <li><b>Работаем официально</b> (самозанятость, налоги)</li>
            <li>Отмена в любой момент</li>
        </ul>
        <div class="buttons-row">
            <a href="https://t.me/a_yulija19790111" class="btn-main btn-purple" target="_blank">📩 Написать Юлии</a>
            <a href="https://t.me/Natalia_U" class="btn-main btn-purple" target="_blank">💫 Написать Наталье</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# 6. ПОДВАЛ
st.markdown("---")
st.markdown("""
    <footer>
        <div style="text-align: center; color: #6A1B9A; padding: 20px;">
            <p style="font-size: 1.1em;">Простой ИИ без стресса и сложных терминов.</p>
            <p style="font-size: 1.2em; margin: 15px 0;"><b>Юлия и Наталья</b> 💫</p>
            <p><a href="https://t.me/praktikumdlynahinajuchih" style="color: #FDD835; text-decoration: none; background: #6A1B9A; padding: 8px 20px; border-radius: 20px; display: inline-block; font-weight: bold;">Перейти в наш бесплатный Telegram-канал</a></p>
        </div>
    </footer>
""", unsafe_allow_html=True)
