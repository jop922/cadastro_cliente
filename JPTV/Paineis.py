import streamlit as st

def Paineis():
    st.markdown('''
    ## Acesso aos paineis''')
    colunas = st.columns((2,2,2))
    campos = ['Servidor','Usuario','Senha']
    for col, campo_nome in zip(colunas,campos):
          col.write(campo_nome)

    col1, col2,col3 = st.columns(3)
    
    with col1:
        st.link_button('Warez','https://wplay.vip/')
        st.write('userficticio')
        st.write('Senha123')
    
    with col2:
        st.link_button('Live','https://cms.connectvps.com/login.php')
        st.write('userficticio')
        st.write('Senha123')

        
    with col3:
        st.link_button('Elite','https://cms.offx.me/login')
        st.write('userficticio')       
        st.write('Senha123')
