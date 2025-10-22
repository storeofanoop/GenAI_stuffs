################################## Preparation Stage #############################

# Install OpenAI in the container itself
pip3 install openAI

# Import openai library
import openai

#openai.api_key="dsadsadsadsadsad"
openai.api_key=

################################## Testing with small questions ##################

#Open Questions to chatGPT

messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of Netherlands?"}
    ]

chat_response=openai.chat.completions.create(
    model="gpt-4.1-mini",
    max_tokens=100,
    messages=messages
)

print(chat_response.choices[0].message.content)