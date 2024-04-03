import streamlit as st

# Load secrets from Streamlit Secrets
secrets = st.secrets

# Authenticate user based on provided credentials
def authenticate(username, password):
    if username == secrets["authentication"]["username"] and password == secrets["authentication"]["password"]:
        return True
    else:
        return False

# Main Streamlit app
def main():
    st.title('Secure Chatbot App')

    # Authentication form
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    # Check if login button is clicked
    if st.button('Log in'):
        # Authenticate user
        if authenticate(username, password):
            st.success('Logged in successfully!')
            st.markdown(
                '<iframe src="https://udify.app/chatbot/0HbD5FcGtV6xgtww" style="width: 100%; height: 100%; min-height: 700px" frameborder="0" allow="microphone"></iframe>',
                unsafe_allow_html=True
            )
        else:
            st.error('Invalid username or password. Please try again.')

if __name__ == '__main__':
    main()
