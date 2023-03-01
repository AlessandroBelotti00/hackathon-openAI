import openai

class OpenAIAPI():
    def __init__(self, key):
        openai.api_key = key


    def call_API(
            self,
            message, engine="text-davinci-003",      
            temperature=0.5,
            max_tokens=1024,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0):

        response = openai.Completion.create(
        engine=engine,
        prompt=message,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
        )

        return response['choices'][0]['text']