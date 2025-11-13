"""
Chat Avanzado con Detección de Intenciones y Clasificación de Temas
Implementa un agente inteligente que adapta su comportamiento según la intención
del usuario y el tema de conversación.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv
from intent_classifier import IntentClassifier, PromptBuilder, FrameworkSelector
from typing import Dict, Optional, List

# Cargar variables de entorno
load_dotenv()


class ChatGPT4Advanced:
    """
    Chat GPT-4 con capacidades avanzadas de clasificación de intenciones y temas.
    """

    def __init__(self, model="gpt-4", modo_clasificacion="auto"):
        """
        Inicializa el cliente de OpenAI con detección inteligente de intenciones.

        Args:
            model (str): Modelo a utilizar (por defecto gpt-4)
            modo_clasificacion (str): 'auto' (GPT-4), 'rapido' (keywords), 'manual' (sin clasificar)
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY no encontrada en variables de entorno")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.modo_clasificacion = modo_clasificacion

        # Inicializar selector de frameworks
        self.framework_selector = FrameworkSelector()

        # Historial de conversación
        self.conversation_history = []

        # Clasificación actual
        self.clasificacion_actual = {
            "intencion": "conversacion_general",
            "tema": "general",
            "confianza": 1.0
        }

        # Frameworks recomendados actuales
        self.frameworks_recomendados = []

        # Prompt del sistema por defecto
        self._actualizar_prompt_sistema()

    def _actualizar_prompt_sistema(self):
        """Actualiza el prompt del sistema según la clasificación actual e incluye frameworks."""
        prompt_sistema = PromptBuilder.construir_prompt_sistema(
            self.clasificacion_actual["intencion"],
            self.clasificacion_actual["tema"]
        )

        # Agregar contexto de frameworks si el tema no es general
        if self.clasificacion_actual["tema"] != "general":
            # Obtener frameworks recomendados
            self.frameworks_recomendados = self.framework_selector.recommend_frameworks(
                self.clasificacion_actual["tema"],
                self.clasificacion_actual["intencion"],
                limit=5
            )

            # Agregar contexto de frameworks al prompt
            frameworks_context = self.framework_selector.get_frameworks_context(
                self.clasificacion_actual["tema"],
                self.clasificacion_actual["intencion"]
            )
            prompt_sistema += frameworks_context

        # Si ya hay historial, actualizar el primer mensaje
        if self.conversation_history:
            self.conversation_history[0] = {
                "role": "system",
                "content": prompt_sistema
            }
        else:
            # Si no hay historial, agregar el mensaje del sistema
            self.conversation_history.append({
                "role": "system",
                "content": prompt_sistema
            })

    def clasificar_mensaje(self, mensaje: str) -> Dict:
        """
        Clasifica el mensaje del usuario para detectar intención y tema.

        Args:
            mensaje: Mensaje del usuario

        Returns:
            Diccionario con la clasificación (intencion, tema, confianza)
        """
        if self.modo_clasificacion == "manual":
            return {
                "intencion": "conversacion_general",
                "tema": "general",
                "confianza": 1.0,
                "metodo": "manual"
            }

        elif self.modo_clasificacion == "rapido":
            return IntentClassifier.clasificar_rapido(mensaje)

        else:  # modo_clasificacion == "auto"
            # Usar GPT-4 para clasificar
            prompt_clasificacion = IntentClassifier.crear_prompt_clasificacion()

            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Usar modelo más barato para clasificación
                    messages=[
                        {"role": "system", "content": prompt_clasificacion},
                        {"role": "user", "content": mensaje}
                    ],
                    temperature=0.3  # Baja temperatura para clasificación consistente
                )

                respuesta = response.choices[0].message.content
                clasificacion = IntentClassifier.extraer_clasificacion(respuesta)

                return {
                    "intencion": clasificacion.get("intencion", "conversacion_general"),
                    "tema": clasificacion.get("tema", "general"),
                    "confianza": clasificacion.get("confianza", 0.8),
                    "razon": clasificacion.get("razon", ""),
                    "metodo": "gpt"
                }

            except Exception as e:
                # Si falla la clasificación con GPT, usar keywords como fallback
                print(f"⚠️  Clasificación GPT falló, usando keywords: {e}")
                return IntentClassifier.clasificar_rapido(mensaje)

    def chat(self, user_message: str, clasificar: bool = True) -> Dict:
        """
        Envía un mensaje al chat y recibe una respuesta.

        Args:
            user_message (str): Mensaje del usuario
            clasificar (bool): Si debe clasificar el mensaje antes de responder

        Returns:
            Dict con 'respuesta', 'clasificacion' y 'metadata'
        """
        # Clasificar el mensaje si está habilitado
        if clasificar and self.modo_clasificacion != "manual":
            nueva_clasificacion = self.clasificar_mensaje(user_message)

            # Actualizar clasificación si cambió significativamente
            if (nueva_clasificacion["intencion"] != self.clasificacion_actual["intencion"] or
                nueva_clasificacion["tema"] != self.clasificacion_actual["tema"]):

                self.clasificacion_actual = nueva_clasificacion
                self._actualizar_prompt_sistema()

        else:
            nueva_clasificacion = self.clasificacion_actual

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

            return {
                "respuesta": assistant_message,
                "clasificacion": nueva_clasificacion,
                "frameworks_recomendados": self.frameworks_recomendados,
                "metadata": {
                    "tokens_usados": response.usage.total_tokens if hasattr(response, 'usage') else None,
                    "modelo": self.model
                }
            }

        except Exception as e:
            error_msg = f"Error al comunicarse con OpenAI: {str(e)}"
            return {
                "respuesta": error_msg,
                "clasificacion": nueva_clasificacion,
                "metadata": {"error": True}
            }

    def cambiar_intencion(self, intencion: str, tema: Optional[str] = None):
        """
        Cambia manualmente la intención y/o tema del agente.

        Args:
            intencion: Nueva intención
            tema: Nuevo tema (opcional)
        """
        self.clasificacion_actual["intencion"] = intencion
        if tema:
            self.clasificacion_actual["tema"] = tema

        self._actualizar_prompt_sistema()

    def reset_conversation(self):
        """Reinicia el historial de conversación manteniendo solo el mensaje del sistema."""
        system_message = self.conversation_history[0]
        self.conversation_history = [system_message]

        # Resetear clasificación a valores por defecto
        self.clasificacion_actual = {
            "intencion": "conversacion_general",
            "tema": "general",
            "confianza": 1.0
        }
        self._actualizar_prompt_sistema()

    def get_history(self):
        """Retorna el historial de conversación."""
        return self.conversation_history

    def get_history_length(self):
        """Retorna el número de mensajes en el historial (excluyendo el sistema)."""
        return len(self.conversation_history) - 1

    def get_clasificacion_actual(self):
        """Retorna la clasificación actual del agente."""
        return self.clasificacion_actual

    def get_frameworks_recomendados(self) -> List[Dict]:
        """Retorna los frameworks recomendados para el contexto actual."""
        return self.frameworks_recomendados

    def get_framework_info(self, framework_id: str) -> Optional[Dict]:
        """
        Obtiene información detallada de un framework específico.

        Args:
            framework_id: ID del framework

        Returns:
            Dict con información del framework o None
        """
        return self.framework_selector.get_framework_by_id(framework_id)


def main():
    """Función principal para ejecutar el chat interactivo avanzado."""
    print("=" * 70)
    print("Chat GPT-4 Avanzado - Con Detección de Intenciones y Temas")
    print("=" * 70)
    print("\nModos de clasificación:")
    print("  1. Auto (GPT-4) - Clasificación precisa usando IA")
    print("  2. Rápido - Clasificación basada en palabras clave")
    print("  3. Manual - Sin clasificación automática")
    print()

    modo = input("Selecciona modo (1/2/3) [1]: ").strip() or "1"
    modo_map = {"1": "auto", "2": "rapido", "3": "manual"}
    modo_clasificacion = modo_map.get(modo, "auto")

    print(f"\n✓ Modo seleccionado: {modo_clasificacion}")
    print("\nComandos especiales:")
    print("  'salir' - Terminar el chat")
    print("  'reset' - Reiniciar la conversación")
    print("  'historial' - Ver el número de mensajes en memoria")
    print("  'clasificacion' - Ver intención y tema actual")
    print("  'frameworks' - Ver frameworks recomendados")
    print("  'cambiar [intencion] [tema]' - Cambiar manualmente la clasificación")
    print("=" * 70)
    print()

    try:
        # Inicializar el chat
        chat = ChatGPT4Advanced(model="gpt-4", modo_clasificacion=modo_clasificacion)
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

            if user_input.lower() == 'clasificacion':
                clasificacion = chat.get_clasificacion_actual()
                print(f"\n📊 Clasificación actual:")
                print(f"   Intención: {clasificacion['intencion']}")
                print(f"   Tema: {clasificacion['tema']}")
                print(f"   Confianza: {clasificacion.get('confianza', 'N/A')}\n")
                continue

            if user_input.lower() == 'frameworks':
                frameworks = chat.get_frameworks_recomendados()
                if frameworks:
                    print(f"\n🔧 Frameworks recomendados ({len(frameworks)}):\n")
                    for i, fw in enumerate(frameworks, 1):
                        print(f"{i}. {fw['nombre']} ({fw['id']})")
                        print(f"   {fw['descripcion_corta']}")
                        print(f"   📖 Pasos: {fw['pasos_clave']}")
                        if fw.get('image_url'):
                            print(f"   🔗 Visual: {fw['image_url']}")
                        print()
                else:
                    print("\n⚠️  No hay frameworks recomendados para el contexto actual\n")
                continue

            if user_input.lower().startswith('cambiar '):
                parts = user_input.split()
                if len(parts) >= 2:
                    intencion = parts[1]
                    tema = parts[2] if len(parts) >= 3 else None
                    chat.cambiar_intencion(intencion, tema)
                    print(f"\n✓ Clasificación cambiada a: {intencion}" +
                          (f" / {tema}" if tema else "") + "\n")
                else:
                    print("\n⚠️  Uso: cambiar [intencion] [tema]\n")
                continue

            # Enviar mensaje y obtener respuesta
            print()
            resultado = chat.chat(user_input)

            # Mostrar clasificación si es relevante
            clasificacion = resultado["clasificacion"]
            if modo_clasificacion != "manual" and clasificacion.get("metodo") != "manual":
                frameworks_count = len(resultado.get('frameworks_recomendados', []))
                frameworks_info = f" | {frameworks_count} frameworks" if frameworks_count > 0 else ""
                print(f"📊 [Intención: {clasificacion['intencion']} | Tema: {clasificacion['tema']}{frameworks_info}]")

            print(f"\nAsistente: {resultado['respuesta']}")

            # Mostrar hint sobre frameworks si hay disponibles y es relevante
            if resultado.get('frameworks_recomendados') and clasificacion.get('intencion') in ['elegir_herramienta', 'usar_herramienta']:
                print(f"\n💡 Tip: Escribe 'frameworks' para ver {len(resultado['frameworks_recomendados'])} frameworks recomendados")

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
