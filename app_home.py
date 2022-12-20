import streamlit as st


def run_home_app() :
    st.text('안녕하세요.')
    img_url = 'https://blog.kakaocdn.net/dn/MIwEC/btqZ3gi5r2C/m9QnC7TlkSc9rLL1NuMcEK/img.png'
    st.image(img_url)

    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다. 데이터 분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해줍니다.')
    

    
    