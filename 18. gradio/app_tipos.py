import gradio as gr


def processar_dados(texto, numero, imagem, lista_txt, cor, opcoes):
    texto_rev = texto[::-1]
    dobrar_numero = numero * 2
    mensagem_imagem = "Imagem recebida: " if imagem else "Nenhuma imagem recebida."
    
    
    lista_processada = [[item] for item in lista_txt.splitlines()] if lista_txt else [] # Converte a lista de texto em uma lista de listas
    
    return(
        texto_rev,
        dobrar_numero,
        mensagem_imagem,
        lista_processada,
        f"cor: {cor}",
        opcoes
    )
    
    
iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label="Texto"),
        gr.Slider(minimum=0, maximum=100, label="Número", value=0),
        gr.Image(type="pil", label="Imagem"), # type="pil" indica que a imagem será recebida como um objeto PIL, que é 0 tipo de imagem do Python
        gr.Textbox(label="Lista de texto", lines=4, placeholder="Uma linha\nOutra linha\nMais uma linha"),
        gr.ColorPicker(label="Cor"),
        gr.CheckboxGroup(label="Cores", choices=["Vermelho", "Verde", "Azul"]
        )
    ],
    outputs=[
        gr.Textbox(label="Texto invertido"),
        gr.Number(label="Número dobrado"),
        gr.Textbox(label="Imagem"),
        gr.DataFrame(label="Lista de texto processada"),
        gr.Textbox(label="Cor selecionada"),
        gr.Textbox(label="Opções selecionadas")
    ],
    title="Processamento de Dados",
    description="Esta é uma interface para processar diferentes tipos de dados."
)

iface.launch()