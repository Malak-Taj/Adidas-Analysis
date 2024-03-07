import streamlit as st
st.header(":mailbox: Let's Contact !")
contactform ="""
<form action="https://formsubmit.co/malaktaj2002@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" required placeholder = "Your Name">
     <input type="email" name="email" required placeholder = "Your Email">
      <textarea name="message" placeholder="Details of your message"></textarea>
     <button type="submit" class=button >Send</button>
</form>
"""

st.markdown(contactform , unsafe_allow_html=True)

def read_css(file_name):
   with open(file_name) as f:
       st.markdown(f"<style> {f.read()} </style>" , unsafe_allow_html=True)
read_css(r'C:\Users\ooo\Downloads\MidProjectStreamlit\Pages\main.css')
