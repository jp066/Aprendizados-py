import gradio as gr

def reverter_texto(texto):
    texto_invertido = texto[::-1]
    return texto_invertido, len(texto_invertido) # a logica de inverter uma string
    

iface = gr.Interface(fn=reverter_texto, inputs="text", outputs=["text", "number"], title="reverse text", description="Insira um texto para reverter.")

iface.launch()