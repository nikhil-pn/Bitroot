from openai_requests import get_chat_response


text = input("Enter your message: ")
response = get_chat_response(text)

print(response)