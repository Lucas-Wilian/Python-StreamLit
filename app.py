from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Python Site", page_icon=':ghost:', layout='wide')

def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

# def local_css(file_name):
#   with open(file_name) as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# local_css('stle/style.css')

lottie_coding =  load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_project  = Image.open('images/img_thumb.png')

with st.container():
  st.subheader('Olá me chamo Lucas, sou um dev backend  :wave:')
  st.title('Sou um amante da programação e suas tecnologias')
  st.write('Eu gosto de estar por dentro de tudo que a de novo no mundo da informatica, e da programação')
  st.write('[Meu GitHub >] (https://github.com/Lucas-Wilian)')

with st.container():
  st.write('-------')
  left_column, right_column = st.columns(2)

  with left_column:
    st.header('Sobre mim')
    st.write('##')
    st.write("""
      Tenho um canal no Yotube com tutoriais das seguintes linguagens:
      - Python
      - Typescript
      - JavaScript
      Se increva e ative as notificações para assim que sair um video novo vc ser o primeiro a saber.
      """)
    st.write('[Meu Canal >] (https://www.youtube.com/channel/UCU2FA7I_Y9IeC6GJT6oavMg)')

  with  right_column:
    st_lottie(lottie_coding, height=300, key='coding' )

  with st.container():
    st.write('---')
    st.header('Meus Projetos')
    st.write('##')
    img_column, text_column = st.columns((1,2))
    with img_column:
      st.image(img_project)

    with text_column:
      st.subheader('Todo Python')
      st.write("""
        Eae pessoal nesse video vamos estar fazendo uma TODO List com Python de uma maneira simples,
        mais que vai estar clareando muito sobre os conceitos da linguagem.
      """)
      st.markdown("[Assista ao video >](https://www.youtube.com/watch?v=Xjt0MbjlGDU)")