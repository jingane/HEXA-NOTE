import streamlit as st

# 데이터 저장소
data_store = {}

def save_data(x, y, value):
    data_store[(x, y)] = value

def load_data():
    return data_store

def login(username, password):
    return username == 'admin' and password == '2212'

st.title('Hexagon Text Boxes')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.header('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if login(username, password):
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.error('Invalid username or password')
else:
    st.sidebar.button('Logout', on_click=lambda: st.session_state.update(logged_in=False))
    
    st.write("## Hexagon Container")

    size = 100
    spacingX = size * 1.2
    spacingY = size * (3**0.5) * 0.5

    container = st.container()
    data = load_data()

    for i in range(20):
        for j in range(20):
            x = spacingX * i
            y = spacingY * j
            if j % 2 == 1:
                x += spacingX / 2
            key = (x, y)
            value = data.get(key, "")
            with container:
                col1, col2, col3 = st.columns([1, 4, 1])
                with col2:
                    hexagon_value = st.text_input(f'Hexagon ({i},{j})', value, key=f'input_{i}_{j}')
                    if hexagon_value:
                        save_data(x, y, hexagon_value)
