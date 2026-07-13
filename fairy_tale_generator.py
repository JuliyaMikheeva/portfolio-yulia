import streamlit as st
import random

# Настройка страницы и кастомные стили (фон, шрифты)
st.set_page_config(page_title="Генератор Нейросказок", page_icon="🧚♀️")

st.markdown("""
    <style>
    /* Красивый градиентный фон */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        min-height: 100vh;
    }

    /* Стиль заголовка */
    h1 {
        font-family: 'Comic Sans MS', 'Arial', sans-serif;
        color: #4a4a4a;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    /* Стиль текста сказки */
    .story-text {
        font-size: 28px;
        font-weight: bold;
        color: #2c3e50;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 20px;
        line-height: 1.5;
    }

    /* Большая зеленая кнопка */
    div.stButton > button {
        background-color: #2ecc71;
        color: white;
        font-size: 24px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 50px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }

    div.stButton > button:hover {
        background-color: #27ae60;
        transform: scale(1.02);
        box-shadow: 0 6px 8px rgba(0,0,0,0.25);
    }
    </style>
""", unsafe_allow_html=True)


    # Вывод результата крупным шрифтом в красивом блоке
    story = f"Однажды {hero} нашел {item}, но вдруг {problem}!"
    st.markdown(f'<div class="story-text">{story}</div>', unsafe_allow_html=True)
