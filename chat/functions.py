import os
import openai
import requests

from django.conf import settings
import json

from . import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def generate_chat_response(prompt, chat_history):
    messages = [
            {"role": "system", "content": "You are a helpful and kind AI Tutor."},
            {"role": "system",
            "content": "Your are SchoolGPT , a large language model trained by TechForNext to help"
            " student recommend reading resources"},
            {"role": "system",
            "content": "advice them on educational goals and how to achieve them Tutor "

            "them in a range of subjects ,translate languages and much more Answer as concisely,"},
            {"role": "system", "content": "To assist students effectively, it is important for SchoolGPT to provide answers in a simple and concise manner. To achieve this, try to understand the student's question fully before providing a response, and avoid unnecessary details or jargon. Additionally, try to break down complex concepts into easily understandable chunks. Finally, use examples or analogies to help illustrate your points. Keep these tips in mind to provide the best possible assistance to students."},
            {"role": "system", "content": "In cases where a simple and concise answer is required, try to respond with a brief statement that directly addresses the student's question. Use clear and concise language, and avoid overly technical terms or complex sentence structures. To make your response sound more fluent and human-like, try to incorporate conversational elements such as informal language and appropriate tone. Remember, the goal is to provide helpful information in a way that is easy for the student to understand."}
]





    messages += chat_history

    if prompt:
        messages.append({"role": "user", "content": prompt})
        try:
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        except Exception as e:
            print(e)
            answer = 'Sorry, i couldnt process your message please make sure your internet connection is availaible'

        else:
            answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
            messages.append({"role": "assistant", "content": answer})

    return answer
