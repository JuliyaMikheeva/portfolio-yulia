import streamlit as st
from pathlib import Path
import os

st.set_page_config(
    page_title="Нейромастерская НЮансов", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Путь к фото
photo_path = "team-photo.jpg"

st.markdown("""
    <style>
    .stApp { background-color: #fdfbf7; color: #333333; }
    h1, h2, h3 { color: #4a148c; font-family: 'Georgia', serif; }
    .hero {
        text-align: center; padding: 50px 20px;
        background: linear-gradient(135deg, #f3e5f5 0%, #fff9c4 100%);
        border-radius: 20px; margin-bottom: 40px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .hero h1 { font-size: 2.8em; margin-bottom: 15px; color: #311b92; }
    .hero p { font-size: 1.3em; color: #555; margin-bottom: 30px; }
    .card {
        background: white; padding: 30px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px;
        border-left: 5px solid #fbc02d;
    }
    .card-purple { border-left: 5px solid #7b1fa2; }
    .expert-card {
        text-align: center; padding: 20px;
    }
    .btn-primary {
        background-color: #7b1fa2; color: white !important;
        padding: 15px 30px; border-radius: 30px; text-decoration: none;
        font-weight: bold; font-size: 1.1em; display: inline-block;
        margin: 10px; transition: transform 0.2s;
    }
    .btn-secondary {
        background-color: #fbc02d; color: #333 !important;
        padding: 15px 30px; border-radius: 30px; text-decoration: none;
        font-weight: bold; font-size: 1.1em; display: inline-block;
        margin: 10px; transition: transform 0.2s;
    }
    .btn-primary:hover, .btn-secondary:hover { transform: scale(1.05); }
    .comparison-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    .comparison-card h3 {
        text-align: center; margin-bottom: 20px; padding: 15px;
        border-radius: 10px; color: white;
    }
    .free-title { background: linear-gradient(135deg, #66bb6a, #43a047); }
    .club-title { background: linear-gradient(135deg, #7b1fa2, #5e35b1); }
    .comparison-card ul {
        list-style: none; padding: 0; line-height: 2;
    }
    .comparison-card li:before {
        content: "✓ "; color: #43a047; font-weight: bold;
        margin-right: 8px;
    }
    .review-box {
        background: #f3e5f5; padding: 20px; border-radius: 15px;
        border-left: 5px solid #7b1fa2; margin: 15px 0; font-style: italic;
    }
    .highlight { background-color: #fff9c4; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    .telegram-link {
        display: inline-block; margin: 5px; padding: 8px 15px;
        background: #0088cc; color: white; border-radius: 20px;
        text-decoration: none; font-size: 0.9em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <h1>Нейросети — понятный помощник, а не головная боль</h1>
        <p>Бесплатный практикум для первых шагов + закрытый клуб «Нейромастерская НЮансов» для глубокого погружения.</p>
        <br>
        <a href="https://t.me/praktikumdlynahinajuchih" class="btn-secondary" target="_blank">🎁 Начать с бесплатного практикума</a>
        <a href="https://t.me/+e4CJuDcXMro3ODcy" class="btn-primary" target="_blank">💫 Посмотреть, что внутри клуба</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 👩💻 Эксперты Юлия и Наталья")
st.markdown("""
    <div class="card">
        <p>Наша задача простая: помочь внедрить ИИ в повседневные дела и довести каждую идею до результата — «рука об руку».</p>
        <p>Мы — действующие эксперты по нейросетям и кураторы крупной онлайн-школы. За нашими плечами более <span class="highlight">1000 учеников</span>, которым мы уже помогли сделать первые шаги.</p>
    </div>
""", unsafe_allow_html=True)

# Показываем фото команды
try:
    st.image(photo_path, caption="Юлия и Наталья — основатели Нейромастерской", use_container_width=True)
except:
    st.info("📸 Фото команды (загрузите файл team-photo.jpg в репозиторий)")

col1, col2 = st.columns(2)

with col1:
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
            <a href="https://t.me/a_yulija19790111" class="telegram-link" target="_blank">Написать Юлии в Telegram</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
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
            <a href="https://t.me/Natalia_U" class="telegram-link" target="_blank" style="background: #0088cc;">Написать Наталье в Telegram</a>
        </div>
    """, unsafe_allow_html=True)

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
        </div>
    """, unsafe_allow_html=True)

st.markdown("## 💰 Условия участия в клубе")
st.markdown("""
    <div class="card card-purple" style="text-align: center; border: 2px solid #7b1fa2;">
        <h2 style="color: #7b1fa2; margin-bottom: 10px;">2 000 ₽ / месяц</h2>
        <ul style="text-align: left; display: inline-block; font-size: 1.05em; line-height: 1.6;">
            <li>Оплата раз в месяц (перевод на карту)</li>
            <li><b>Работаем официально</b> (самозанятость, налоги)</li>
            <li>Отмена в любой момент</li>
        </ul>
        <br><br>
        <a href="https://t.me/a_yulija19790111" class="btn-primary" target="_blank">💫 Написать Юлии: "Хочу в клуб"</a>
    </div>
""", unsafe_allow_html=True)
