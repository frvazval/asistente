import pyttsx3
import speech_recognition as sr
import datetime

id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

def audio_a_texto():
    
    # Objeto para reconocer el audio
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as source:

        # tiempo de espera hasta que activa el micro
        r.pause_threshold = 0.8

        # Mensaje para el usuario para que sepa que ya puede hablar
        print("Ya puedes hablar")

        # variable paraguardar el audio
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es")

            # mostrar en pantalla el texto
            print("Voz reconocida:", texto)

            return texto

        except sr.UnknownValueError:
            print("El micro no funciona")
            return "Error"

        except sr.RequestError:
            print("Falla la transcripción del texto")
            return "Error"

        except:
            print("Error no identificado")
            return "Error"

# audio_a_texto()

def respuesta_maquina(texto):

    # Iniciar el motor de pyttsx3
    engine = pyttsx3.init()

    # Ajustes
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)

    volumen = engine.getProperty("volume")
    engine.setProperty("volume", 1)

    engine.setProperty("voice", id1) 

    engine.say(texto)

    engine.runAndWait()

# respuesta_maquina("Hola ¿cómo estás?")
def decir_dia_semana():

    # Obtener el día actual 
    dia_actual =datetime.date.today()
    # print(dia)

    dia_semana = dia_actual.weekday()
    # print(dia_semana)

    # nombres de los días
    dias_esp = ("lunes", "martes", "miércoles", "jueves", "viernes", "sabado", "domingo")

    respuesta_maquina(f"Hoy es {dias_esp[dia_semana]}")

# decir_dia_semana()

def decir_la_hora():

    # guardar la hora
    hora_actual = datetime.datetime.now()
    # print(hora_actual)
    hora = f"En este momento son las {hora_actual.hour} horas, {hora_actual.minute} minutos y {hora_actual.second} segundos"

    respuesta_maquina(hora)

# decir_la_hora()

def saludo_inicial():

    hora_actual = datetime.datetime.now().hour
    # print(hora_actual)
    
    # momento del día
    if 6 < hora_actual < 14:
        momento = "Buenos días"
    elif 14 <= hora_actual < 20:
        momento = "Buenas tardes"
    else:
        momento = "Buenas noches"

    saludo = f"{momento}, soy Axela, tu asistente personal"
    respuesta_maquina(saludo)
    respuesta_maquina("¿En qué te puedo ayudar?")


# saludo_inicial()

# Función que lanza las demás
def funcion_principal():

    # que empiece saludando
    saludo_inicial()

    # bucle infinito para que escuche 
    # lo que le vamos a pedir

    activo = True
    while activo:

        peticion = audio_a_texto().lower()
        print(peticion)

        if peticion == "silencio":
            activo = False


funcion_principal()