#Importing required libraries
import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI API key
genai.configure(api_key='your_gemini_api_token')


# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        return [f"Error: {str(e)}"]

# Customer service script with 35 common questions
def customer_service_script(question):
    script = {
        "greeting": "Hello! How can I assist you today?",
        "hi": "Hello! How can I assist you today?",
        "hello": "Hello! How can I assist you today?",
        "hey there": "Hello! How can I assist you today?",
        "farewell": "Thank you for reaching out. Have a great day!",
        "thanks": "Thank you for reaching out. Have a great day!",
        "ok": "Thank you for reaching out. Have a great day!",
        "bye": "Thank you for reaching out. Have a great day!",
        "quite": "Thank you for reaching out. Have a great day!",
        "refund": "To process a refund, please provide your order number and the reason for the refund request.",
        "shipping": "Shipping typically takes 5-7 business days. You can track your order using the tracking number provided in your confirmation email.",
        "support": "For technical support, please describe the issue you are experiencing, and we will assist you as soon as possible.",
        "create an account": "To create a new account, please visit our sign-up page, fill in your details, and follow the instructions. If you need further assistance, please let us know!",
        "reset password": "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions.",
        "update account details": "To update your account details, log in to your account and navigate to the 'Account Settings' section.",
        "cancel order": "To cancel an order, please provide your order number and the reason for cancellation.",
        "track order": "You can track your order using the tracking number provided in your confirmation email.",
        "payment methods": "We accept various payment methods including credit/debit cards, PayPal, and bank transfers.",
        "apply discount code": "To apply a discount code, enter the code at checkout in the 'Discount Code' field.",
        "check balance": "To check your account balance, log in to your account and go to the 'Balance' section.",
        "contact support": "You can contact support via email or call us directly.",
        "human agent": "I am informing to the customer service team. You can contact support via email or call us directly.",
        "customer service team": "I am informing to the customer service team. You can contact support via email or call us directly.",
        "business hours": "Our business hours are Monday to Friday, 9 AM to 6 PM.",
        "return policy": "Our return policy allows returns within 30 days of purchase. The item must be in original condition.",
        "exchange item": "To exchange an item, please provide your order number and the item you wish to exchange.",
        "subscription plan": "To change your subscription plan, log in to your account and go to the 'Subscription' section.",
        "delivery options": "We offer standard and express delivery options. Choose your preferred option at checkout.",
        "gift cards": "You can purchase gift cards on our website. They can be redeemed during checkout.",
        "product availability": "To check product availability, visit the product page on our website.",
        "order confirmation": "You will receive an order confirmation email after placing your order.",
        "loyalty program": "Join our loyalty program to earn points and enjoy exclusive benefits.",
        "billing issue": "For billing issues, please contact our billing department at billing@example.com.",
        "report a problem": "To report a problem, please describe the issue in detail and provide any relevant information.",
        "error": "Apologize for any convience. Please contact support via email or call us directly."
    }
    
    for key in script:
        if key in question.lower():
            return script[key]
    
    # If no predefined response, use the AI model
    return get_gemini_response(question)

# Initialize the Streamlit app
st.set_page_config(page_title="Customer Service Chatbot")

st.header("Customer Service Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input section
input = st.text_input("Ask your question:", key="input")
submit = st.button("Submit")

# Handle the submission of the user's question
if submit and input:
    response = customer_service_script(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response:")
    if isinstance(response, list):
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
    else:
        st.write(response)
        st.session_state['chat_history'].append(("Bot", response))

# Display the chat history
st.subheader("Chat History:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
    
