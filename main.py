# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import smtplib
import streamlit as st
from PIL import Image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.set_page_config(page_title="WE Data mobile inquiry",
                       page_icon=":iphone:")

    image = Image.open('wedata.jpeg')

    st.image(image)
    st.header("WE Data mobile type inquiry :iphone:")

    deviceType = st.radio(
        "Please choose your main mobile device type",
        ('Android Phone', 'iPhone'))

    if deviceType == 'Android Phone':
        st.write('Please enter your Google email address below')
    if deviceType == 'iPhone':
        st.write('Please enter your Apple ID email address below')
    fullName = st.text_input('Full Name')
    email_addr = st.text_input('Email Address')

    if st.button('Send Invitation Link'):
        linkURL = ''
        if deviceType == 'Android Phone':
            linkURL = "http://www.google.com"
        if deviceType == 'iPhone':
            linkURL = "http://www.apple.com"
        port = 587  # For SSL
        smtp_server = "smtp.mailersend.net"
        sender_email = "MS_jvwhcw@arkleap.com"  # Enter your address
        receiver_email = "islam.youssef@arkleap.com"  # Enter receiver address
        password = "HGxB5mHy1AzTX9UK"
        message = f"""\
        Subject: PeopleMate Mobile app invitation link

        Dear {fullName},

            We have received that your mobile device is {deviceType}.
            Please use this link to download the app on your mobile

            {linkURL}

        Best Regards,
        PeopleMate Copilot"""
        # message = f"""\
        #     Subject: test email
        #
        #     This is from people mate"""
        print(receiver_email)
        print(message)
        with st.spinner("Sending Invitation..."):
            smtp = smtplib.SMTP(smtp_server, 587)

            smtp.ehlo()  # send the extended hello to our server
            smtp.starttls()  # tell server we want to communicate with TLS encryption

            smtp.login(sender_email, password)  # login to our email server

            # send our email message 'msg' to our boss
            smtp.sendmail('PeopleMateCP@arkleap.com',
                          email_addr,
                          message)

            smtp.quit()  # finally, don't forget to close the connection

        st.write('Thanks for submitting your info. You can now close this window.')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
