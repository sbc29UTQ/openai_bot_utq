"""
Ejemplos de Uso del Chat GPT-4 Avanzado
Demuestra cómo el agente detecta intenciones y adapta sus respuestas.
"""

from chat_gpt4_advanced import ChatGPT4Advanced
import os


def ejemplo_diagnosticar():
    """
    Ejemplo: Intención DIAGNOSTICAR
    El usuario quiere analizar un problema.
    """
    print("\n" + "="*70)
    print("EJEMPLO 1: DIAGNOSTICAR")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    mensajes = [
        "Necesito diagnosticar por qué mi equipo no está cumpliendo los objetivos trimestrales",
        "Hemos notado baja productividad y desmotivación",
    ]

    for mensaje in mensajes:
        print(f"\n👤 Usuario: {mensaje}")
        resultado = chat.chat(mensaje)
        print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
        print(f"\n🤖 Asistente: {resultado['respuesta']}")


def ejemplo_elegir_herramienta():
    """
    Ejemplo: Intención ELEGIR_HERRAMIENTA
    El usuario busca recomendación de framework/metodología.
    """
    print("\n" + "="*70)
    print("EJEMPLO 2: ELEGIR HERRAMIENTA")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    mensaje = "¿Qué framework me recomiendas para mejorar nuestros procesos de desarrollo de software?"

    print(f"\n👤 Usuario: {mensaje}")
    resultado = chat.chat(mensaje)
    print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
    print(f"\n🤖 Asistente: {resultado['respuesta']}")


def ejemplo_usar_herramienta():
    """
    Ejemplo: Intención USAR_HERRAMIENTA
    El usuario quiere guía paso a paso.
    """
    print("\n" + "="*70)
    print("EJEMPLO 3: USAR HERRAMIENTA (Guía Paso a Paso)")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    mensaje = "¿Me puedes guiar paso a paso en cómo aplicar Design Thinking para innovar en mi producto?"

    print(f"\n👤 Usuario: {mensaje}")
    resultado = chat.chat(mensaje)
    print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
    print(f"\n🤖 Asistente: {resultado['respuesta']}")


def ejemplo_analizar_resultado():
    """
    Ejemplo: Intención ANALIZAR_RESULTADO
    El usuario presenta resultados y quiere feedback.
    """
    print("\n" + "="*70)
    print("EJEMPLO 4: ANALIZAR RESULTADO")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    mensaje = """Analiza estos resultados de mi análisis FODA:

    Fortalezas: Equipo capacitado, tecnología moderna
    Oportunidades: Mercado en crecimiento
    Debilidades: Procesos lentos, alta rotación
    Amenazas: Competencia agresiva

    ¿Qué opinas?"""

    print(f"\n👤 Usuario: {mensaje}")
    resultado = chat.chat(mensaje)
    print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
    print(f"\n🤖 Asistente: {resultado['respuesta']}")


def ejemplo_recomendaciones():
    """
    Ejemplo: Intención RECOMENDACIONES
    El usuario pide próximos pasos.
    """
    print("\n" + "="*70)
    print("EJEMPLO 5: RECOMENDACIONES")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    mensajes = [
        "Hemos implementado Scrum en nuestro equipo hace 3 meses",
        "¿Cuáles serían los próximos pasos para madurar nuestra práctica ágil?"
    ]

    for mensaje in mensajes:
        print(f"\n👤 Usuario: {mensaje}")
        resultado = chat.chat(mensaje)
        print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
        print(f"\n🤖 Asistente: {resultado['respuesta']}")


def ejemplo_clasificacion_temas():
    """
    Ejemplo: Clasificación por TEMAS
    Demuestra cómo el agente clasifica por Estrategia, Procesos e Innovación.
    """
    print("\n" + "="*70)
    print("EJEMPLO 6: CLASIFICACIÓN POR TEMAS")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    ejemplos_temas = [
        ("¿Cómo definimos nuestra ventaja competitiva en el mercado?", "ESTRATEGIA"),
        ("Necesitamos optimizar nuestro proceso de atención al cliente", "PROCESOS"),
        ("Queremos implementar IA para automatizar tareas repetitivas", "INNOVACIÓN"),
    ]

    for mensaje, tema_esperado in ejemplos_temas:
        print(f"\n👤 Usuario: {mensaje}")
        print(f"   (Tema esperado: {tema_esperado})")
        resultado = chat.chat(mensaje)
        print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
        print(f"\n🤖 Respuesta (primeras 200 caracteres): {resultado['respuesta'][:200]}...")


def ejemplo_conversacion_completa():
    """
    Ejemplo: Conversación completa con múltiples intenciones
    Demuestra cómo el agente adapta su comportamiento dinámicamente.
    """
    print("\n" + "="*70)
    print("EJEMPLO 7: CONVERSACIÓN COMPLETA CON MÚLTIPLES INTENCIONES")
    print("="*70)

    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    conversacion = [
        "Tenemos problemas de comunicación entre equipos",  # DIAGNOSTICAR
        "¿Qué metodología me recomiendas para mejorar la colaboración?",  # ELEGIR_HERRAMIENTA
        "¿Me explicas cómo implementar Kanban paso a paso?",  # USAR_HERRAMIENTA
        "Ya implementamos el tablero Kanban, ¿qué opinas de esta configuración: To Do, In Progress, Review, Done?",  # ANALIZAR_RESULTADO
        "Perfecto, ¿cuáles serían los próximos pasos?",  # RECOMENDACIONES
    ]

    for i, mensaje in enumerate(conversacion, 1):
        print(f"\n--- Mensaje {i} ---")
        print(f"👤 Usuario: {mensaje}")
        resultado = chat.chat(mensaje)
        print(f"\n📊 Clasificación: {resultado['clasificacion']['intencion']} / {resultado['clasificacion']['tema']}")
        print(f"\n🤖 Asistente: {resultado['respuesta']}")
        print()


def ejemplo_uso_programatico():
    """
    Ejemplo: Uso programático del agente
    Muestra cómo integrar el agente en tus propias aplicaciones.
    """
    print("\n" + "="*70)
    print("EJEMPLO 8: USO PROGRAMÁTICO")
    print("="*70)

    # Inicializar con modo rápido
    chat = ChatGPT4Advanced(mode_clasificacion="rapido")

    # Enviar mensaje
    resultado = chat.chat("¿Qué framework me recomiendas para gestión de proyectos ágiles?")

    # Acceder a la información
    print(f"Respuesta: {resultado['respuesta'][:100]}...")
    print(f"Intención detectada: {resultado['clasificacion']['intencion']}")
    print(f"Tema detectado: {resultado['clasificacion']['tema']}")
    print(f"Confianza: {resultado['clasificacion'].get('confianza', 'N/A')}")

    # Cambiar manualmente la intención
    chat.cambiar_intencion("diagnosticar", "procesos")
    print(f"\nClasificación actual: {chat.get_clasificacion_actual()}")

    # Ver historial
    print(f"\nMensajes en memoria: {chat.get_history_length()}")


def main():
    """Ejecuta todos los ejemplos."""
    print("\n🚀 EJEMPLOS DE USO DEL CHAT GPT-4 AVANZADO")
    print("=" * 70)

    # Verificar API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  ADVERTENCIA: OPENAI_API_KEY no configurada")
        print("Estos ejemplos requieren una API key válida para funcionar.")
        print("Por favor, configura tu .env antes de ejecutar los ejemplos.\n")
        return

    ejemplos = [
        ("1. Diagnosticar", ejemplo_diagnosticar),
        ("2. Elegir Herramienta", ejemplo_elegir_herramienta),
        ("3. Usar Herramienta", ejemplo_usar_herramienta),
        ("4. Analizar Resultado", ejemplo_analizar_resultado),
        ("5. Recomendaciones", ejemplo_recomendaciones),
        ("6. Clasificación por Temas", ejemplo_clasificacion_temas),
        ("7. Conversación Completa", ejemplo_conversacion_completa),
        ("8. Uso Programático", ejemplo_uso_programatico),
    ]

    print("\nEjemplos disponibles:")
    for nombre, _ in ejemplos:
        print(f"  {nombre}")

    print("\nOpciones:")
    print("  • Número (1-8): Ejecutar ejemplo específico")
    print("  • 'todos': Ejecutar todos los ejemplos")
    print("  • Enter: Salir")

    seleccion = input("\nSelecciona opción: ").strip().lower()

    if seleccion == 'todos':
        for nombre, funcion in ejemplos:
            try:
                funcion()
                input("\nPresiona Enter para continuar...")
            except Exception as e:
                print(f"\n❌ Error en {nombre}: {e}")
    elif seleccion.isdigit() and 1 <= int(seleccion) <= len(ejemplos):
        idx = int(seleccion) - 1
        try:
            ejemplos[idx][1]()
        except Exception as e:
            print(f"\n❌ Error: {e}")
    else:
        print("\n¡Hasta luego!")


if __name__ == "__main__":
    main()
