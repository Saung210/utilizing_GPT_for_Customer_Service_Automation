# Customer Service Chatbot

**Implementation**
 - APISetup:
   For this implementation, I used Google's Generative AI (Gemini Pro model) to handle the API requests.
   
 - Input Handling:
   The script accepts user inquiries via a text input box and a submit button using *Streamlit*.
   
 - Interacting with GPT model:
   The function “**get_gemini_response**” is responsible for interacting with the GPTmodel to generate a response to the user's inquiry. It sends the user's question to the model using the “**send_message**” method, which streams the response back.
   
 - Formatting:
   Once a response is generated, it is formatted for clear and user-friendly text. If the response is generated from the predefined script, it is directly returned. The response is then appended to the chat history.

**Chatbot**

   ![image](https://github.com/user-attachments/assets/eda2ecbe-e9f9-48d0-8056-2bdc1ff42d6f)
