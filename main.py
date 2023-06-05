import openai

KEY = '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'

openai.api_key = KEY


def generate_response(text):
    response = openai.Completion.create(
        promt=text,  ## параметры
        engine='text-davinci-003',  ## можно использовать другие модели
        max_tokens=100,  ## число знаков при ответе
        temperature=0.7,  ## отвечает за креативность
        n=1,  ## количество ответов
        stop=None,  ## список слов на которые должен заканчиваться текст
        timeout=15  ## время для ответа, в секундах
    )

    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None


res = generate_response('Привет, как у тебя дела? Какая погода в Москве?')
print(res)
