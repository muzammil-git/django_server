import google.generativeai as paml
from django.conf import settings

paml.configure(api_key=settings.PAML_API_KEY)


def get_response(prompt):
    response = paml.chat(messages=prompt)
    print(response.last)
    return response.last