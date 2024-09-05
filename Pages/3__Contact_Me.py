import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Function to send email
def send_email(name, email, message):
    sender_email = "your_email@gmail.com" 
    receiver_email = "malaktaj2002@gmail.com"  
    password = "Malo19215ka" 
    # Create the email content 
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"New message from {name}"
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, 'plain'))
    # Connect to the server and send the email 
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
st.subheader("Contact Me")
with st.form(key='contact_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label='Send')
if submit_button:
    if send_email(name, email, message):
        st.success(f"Thank you, {name}! Your message has been sent.")
    else:
        st.error("There was an error sending your message. Please try again later.")
