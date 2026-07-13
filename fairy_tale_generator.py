import streamlit as st
import random

st.set_page_config(page_title="Генератор Нейросказок", page_icon="🧚♀️")

# Списки данных
heroes = ["Ленивый дракон", "Забывчивый волшебник", "Кот в сапогах", "Храбрый пирожок", "Грустный тролль"]
items = ["невидимые очки", "сапоги-скороходы", "волшебная сосиска", "золотая вилка", "шапка-невидимка"]
problems = ["потерял ключи от замка", "забыл заклинание", "хочет стать пекарем", "случайно превратился в лягушку", "испугался собственной тени"]

# Стилизация (CSS)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton > button {
        width: 100%;
        height: 80px;
        font-size: 24px;
        background-color: #28a745;
        color: white;
        border-radius: 15px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #218838;
        transform: scale(1.02);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .result-box {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 28px;
        color: #333;
        margin-top: 30px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Заголовок
st.title("Генератор Нейросказок 🧚♀️")

# Кнопка
if st.button("🎲 Придумать новую сказку"):
    hero = random.choice(heroes)
    item = random.choice(items)
    problem = random.choice(problems)
    
    story = f"Однажды {hero} нашел {item}, но вдруг {problem}!"
    
    # Вывод результата
    st.markdown(f'<div class="result-box">{story}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="result-box">Нажми на кнопку, чтобы создать чудо! ✨</div>', unsafe_allow_html=True)
