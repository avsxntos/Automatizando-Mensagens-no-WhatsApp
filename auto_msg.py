import time
import pywhatkit as kit
import plyer
import socket


IP_CASA = "endereço de IP"  
CONTATO = "+551100000000"  
MENSAGEM = "Isto é um teste, caso tenha recebido isso o código está funcionando corretamente, considere isso uma mensagem pronta, não responder"


def verificar_rede_casa():
    try:
        hostname = socket.gethostname()
        ip_atual = socket.gethostbyname_ex(hostname)[-1][-1]  
        print(f"IP detectado: {ip_atual}")  

        return ip_atual == IP_CASA
    except Exception as e:
        print("Erro ao verificar IP:", e)
        return False


def confirmar_envio():
    plyer.notification.notify(
        title="Chegou em casa?",
        message="Deseja enviar uma mensagem para sua namorada?",
        timeout=10
    )

    resposta = input("Enviar mensagem? (s/n): ")
    return resposta.lower() == "s"


while True:
    print("Verificando rede...")  
    if verificar_rede_casa():
        print("Você está na rede de casa!")  
        if confirmar_envio():
            try:
                kit.sendwhatmsg_instantly(CONTATO, MENSAGEM)
                print("Mensagem enviada!")
            except Exception as e:
                print("Erro ao enviar mensagem:", e)
        else:
            print("Envio cancelado.")
    else:
        print("Fora de casa, aguardando...")  

    time.sleep(60)  
