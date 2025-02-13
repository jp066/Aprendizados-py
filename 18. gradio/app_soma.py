import gradio as gr


def somar(a, b):
    return a + b


iface = gr.Interface(
                fn=somar, # função, parametro do proprio gr.Interface
                inputs=["number", "number"], 
                outputs="number", 
                title="Soma de dois números",
                description="Insira dois números para somá-los.",
                theme="huggingface"
            ) 
# passo a passo:
# 1. crio a interface: iface = gr.Interface
# 2. passo a função: fn=somar
# 3. passo os inputs: inputs=["number", "number"]
# 4. passo o output: outputs="number"

iface.launch()