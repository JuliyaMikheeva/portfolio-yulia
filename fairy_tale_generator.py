import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Генератор Нейросказок", page_icon="🧚♀️")

# Стили (как раньше, чтобы было красиво)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); min-height: 100vh; }
    h1 { font-family: 'Comic Sans MS', sans-serif; color: #4a4a4a; text-align: center; }
    .story-box { 
        background-color: rgba(255, 255, 255, 0.9); 
        padding: 30px; 
        border-radius: 20px; 
        box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
        margin-top: 20px; 
        font-size: 18px; 
        line-height: 1.6; 
        color: #2c3e50;
    }
    div.stButton > button { 
        background-color: #2ecc71; color: white; font-size: 20px; 
        padding: 15px 30px; border-radius: 50px; border: none; width: 100%; 
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧚♀️ Генератор Нейросказок")
st.write("Нажми кнопку, и я придумаю для тебя уникальную историю!")

# Данные для генерации
heroes = ["Ленивый дракон", "Забывчивый волшебник", "Кот в сапогах", "Принцесса-хакер", "Говорящее дерево"]
items = ["невидимые очки", "сапоги-скороходы", "волшебная сосиска", "бесконечный кофе", "золотой ключик"]
problems = ["потерял ключи от замка", "забыл заклинание", "хочет стать пекарем", "случайно превратился в лягушку"]
endings = [
    "И с тех пор они жили дружно и пекли пироги.",
    "Оказывается, главное волшебство — это доброта!",
    "Так он понял, что быть собой — лучше всего.",
    "И даже драконы иногда нуждаются в друзьях."
]

# Логика генерации полной сказки
def generate_full_story():
    hero = random.choice(heroes)
    item = random.choice(items)
    problem = random.choice(problems)
    ending = random.choice(endings)
    
    story = f"""
    Жил-был {hero}. Он был очень необычным, потому что любил приключения больше всего на свете.
    
    Однажды утром {hero} проснулся и обнаружил, что у него есть {item}. 
    "Ура!" — подумал он. — "Теперь я смогу совершить великий подвиг!"
    
    Но тут случилась беда: {hero} {problem}. 
    Он расстроился и чуть не заплакал. Но потом вспомнил про {item} и решил не сдаваться.
    
    {hero} использовал {item}, чтобы решить проблему. Это было непросто, но он справился!
    
    {ending}
    """
    return story

# Кнопка и вывод
if st.button("✨ Придумать новую сказку"):
    full_story = generate_full_story()
st.markdown(f'<div class="story-box">{full_story}</div>', unsafe_allow_html=True)
