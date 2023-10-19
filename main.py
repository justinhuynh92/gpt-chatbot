import openai

openai.api_key = "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"

# create function that you'll call every time there's a new completion
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": "prompt"
            }]
    )

    # return the user
    # remove any trailing white space
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        # print response with each input
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
