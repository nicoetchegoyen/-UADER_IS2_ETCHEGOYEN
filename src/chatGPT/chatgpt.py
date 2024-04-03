import sys
import openai


API_KEY = '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'  #clave de la API
openai.api_key = API_KEY
historial = []  #lista que almacena el historial de consultas

def interactuar_chatgpt(consulta):  #funcion para poder interactuar con openAI
    try:
        if not consulta.strip():  #verifica que la consulta no esta vacia
            print("ingrese una consulta válida.")
            return

        respuesta = openai.chat.completions.create(  #invoca el modelo de openai(esqueleto)
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "contexto"},
                {"role": "user", "content": "usertask"},
                {"role": "user", "content": consulta}
            ],
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        #obtener el contenido de la respuesta de chatgpt
        respuesta_chatgpt = respuesta.choices[0].message.content
        historial.append(respuesta_chatgpt) #agregar la respuesta al historial de consultas

        print("You:", consulta)
        print("chatGPT:", respuesta_chatgpt)  #imprime la respuesta de chatgpt
    except Exception as e:
        print("error al interactuar con chatGPT:", e) #si un error ocurre, está la excepcion

def ingreso(convers):    #función para manejar la entrada del usuario y la interacción con ChatGPT
    historial
    while True:
        # verificar si la conversacion esta activada y si hay un historial de consultas
        if convers and historial:
            consulta = historial[-1]
        else:
            #solicita una consulta, y da la opcion de salir del programa
            consulta = input("ingrese una consulta (o presione ENTER para salir): ")

            if not consulta:
                print("hasta la proxima.")  #se despide si presionas enter con la terminal vacia
                break

        interactuar_chatgpt(consulta)  #interactua con openai usando la ultima consulta

def main():
    if "--convers" in sys.argv: #verifica si se paso el argumento "--convers"
        ingreso(convers=True)  #activa el modo de conversación
    else:
        ingreso(convers=False) #una consulta única

if __name__ == "__main__":  # ejecuta la funcion principal
    main()
