"""
Chat con Memoria usando OpenAI GPT-4
Este script implementa un chat interactivo que mantiene el historial de conversación
para proporcionar contexto en cada interacción.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class ChatGPT4:
    def __init__(self, model="gpt-4"):
        """
        Inicializa el cliente de OpenAI con memoria de conversación.

        Args:
            model (str): Modelo a utilizar (por defecto gpt-4)
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY no encontrada en variables de entorno")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history = []

        # Mensaje del sistema para configurar el comportamiento del asistente
        system_message = {
            "role": "system",
            "content": "Eres un asistente útil y amigable. Respondes de manera clara y concisa."
        }
        self.conversation_history.append(system_message)

    def chat(self, user_message):
        """
        Envía un mensaje al chat y recibe una respuesta.

        Args:
            user_message (str): Mensaje del usuario

        Returns:
            str: Respuesta del asistente
        """
        # Agregar mensaje del usuario al historial
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        try:
            # Hacer la llamada a la API con todo el historial
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history
            )

            # Extraer la respuesta
            assistant_message = response.choices[0].message.content

            # Agregar la respuesta al historial
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })

            return assistant_message

        except Exception as e:
            return f"Error al comunicarse con OpenAI: {str(e)}"

    def reset_conversation(self):
        """Reinicia el historial de conversación manteniendo solo el mensaje del sistema."""
        system_message = self.conversation_history[0]
        self.conversation_history = [system_message]

    def get_history(self):
        """Retorna el historial de conversación."""
        return self.conversation_history

    def get_history_length(self):
        """Retorna el número de mensajes en el historial (excluyendo el sistema)."""
        return len(self.conversation_history) - 1


def main():
    """Función principal para ejecutar el chat interactivo."""
    print("=" * 60)
    print("Chat con GPT-4 - Conversación con Memoria")
    print("=" * 60)
    print("\nComandos especiales:")
    print("  'salir' o 'exit' - Terminar el chat")
    print("  'reset' - Reiniciar la conversación")
    print("  'historial' - Ver el número de mensajes en memoria")
    print("=" * 60)
    print()

    try:
        # Inicializar el chat
        chat = ChatGPT4(model="gpt-4")
        print("✓ Chat inicializado correctamente\n")

        while True:
            # Obtener input del usuario
            user_input = input("Tú: ").strip()

            if not user_input:
                continue

            # Comandos especiales
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("\n¡Hasta luego!")
                break

            if user_input.lower() == 'reset':
                chat.reset_conversation()
                print("\n✓ Conversación reiniciada\n")
                continue

            if user_input.lower() == 'historial':
                count = chat.get_history_length()
                print(f"\n✓ Mensajes en memoria: {count}\n")
                continue

            # Enviar mensaje y obtener respuesta
            print("\nAsistente: ", end="", flush=True)
            response = chat.chat(user_input)
            print(response)
            print()

    except ValueError as e:
        print(f"\n❌ Error de configuración: {e}")
        print("Por favor, asegúrate de tener tu OPENAI_API_KEY en el archivo .env")
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")


if __name__ == "__main__":
    main()
