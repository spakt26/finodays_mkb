import streamlit as st    
import pandas as pd 

def main():
    
    # '''___________________ SIDEBAR ___________________'''
    st.sidebar.image('app/logo.png')
    st.sidebar.title('Клиентский путь | МКБ')

    
    # '''___________________  MAIN  ___________________'''
    st.title('Клиентский путь | МКБ')
    st.write('Привет! Это команда MegaQuant. Специально для МКБ мы разработали сервис для работы с клиентским путем:')
    

    file = st.file_uploader('Загрузите csv файл с данными о клиентским путем',type=['csv'])
    if file is not None: 
        st.write('На графике показана совместимость продуктов банка с каналами продвижения. Он показывает, какие продукты привлекательны в конкретном канале. Здесь не используются  исторические данные по маркетинговым кампаниям.')

    else:
        st.info(
            f"""
                👆 Попробуйте загрузить [data.csv](https://raw.githubusercontent.com/m3gaq/finodays_mkb/main/data.csv)
                """
        )
if __name__ == '__main__':
    main()