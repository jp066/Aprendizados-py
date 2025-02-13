import gradio as gr 
import math as m
# diferença de from e as:
# o from import é para importar uma função especifica
# o as é para renomear a função importada, ex:
# from math import factorial as fatorial
#


def factorial_view(number):
    if number < 0:
        return "Número inválido"
    return m.factorial(number)

iface = gr.Interface(fn=factorial_view, inputs="number", outputs="number", title="Fatorial", description="Insira um número para calcular o fatorial.")


iface.launch() # eu estou marcando meu amigo iface e ele faz a publicação do meu app. uma analogia.