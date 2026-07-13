import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Генератор Нейросказок", page_icon="🧚♀️")

# Стили
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); min-height: 100vh; }
    h1 { font-family: 'Comic Sans MS', sans-serif; color: #4a4a4a; text-align: center; }
    .story-box { 
        background-color: rgba(255, 255, 255, 0.95); 
        padding: 30px; 
        border-radius: 20px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        margin-top: 20px; 
        font-size: 18px; 
        line-height: 1.6; 
        color: #2c3e50;
        white-space: pre-wrap; /* Сохраняет абзацы */
    }
    div.stButton > button { 
        background-color: #2ecc71; color: white; font-size: 20px; 
        padding: 15px 30px; border-radius: 50px; border: none; width: 100%; 
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧚♀️ Генератор Нейросказок")
st.write("Нажми кнопку, и я придумаю для тебя уникальную историю!")

# Данные
heroes = ["Ленивый дракон", "Забывчивый волшебник", "Кот в сапогах", "Принцесса-хакер", "Говорящее дерево"]
items = ["невидимые очки", "сапоги-скороходы", "волшебная сосиска", "бесконечный кофе", "золотой ключик"]
problems = ["потерял ключи от замка", "забыл важное заклинание", "решил испечь пирог", "превратился в лягушку"]
endings = [
    "И с тех пор они жили дружно и пекли пироги.",
    "Оказывается, главное волшебство — это доброта!",
    "Так герой понял, что быть собой — лучше всего.",
    "И даже драконы иногда нуждаются в друзьях."
]

def generate_full_story():
    hero = random.choice(heroes)
    item = random.choice(items)
    problem = random.choice(problems)
    ending = random.choice(endings)
    
    # Используем нейтральные формулировки, чтобы подходило всем родам
    story = f"""
Жил-был удивительный персонаж по имени {hero}. Он был необычным, потому что любил приключения больше всего на свете.

Однажды утром {hero} проснулся и обнаружил, что у него есть {item}. 
"Ура!" — подумал наш герой. — "Теперь я смогу совершить великий подвиг!"

Но тут случилась беда: оказалось, что {hero} {problem}. 
Персонаж расстроился и чуть не заплакал. Но потом вспомнил про {item} и решил не сдаваться.

{hero} использовал {item}, чтобы решить проблему. Это было непросто, но справился!

{ending}
    """
    # .strip() убирает лишние пробелы и невидимые символы в начале и конце
    return story.strip()

# Кнопка и вывод
if st.button("✨ Придумать новую сказку"):
    full_story = generate_full_story()
    # Используем конкатенацию (+) вместо f-строки для надежности
    st.markdown(
        '<div class="story-box">' + full_story + '</div>', 
        unsafe_allow_html=True
    )
