"""
Demo del Sistema de Frameworks
Demuestra cómo el agente selecciona y recomienda frameworks automáticamente.
"""

from intent_classifier import FrameworkSelector
from chat_gpt4_advanced import ChatGPT4Advanced
import os


def print_separator():
    print("\n" + "=" * 80 + "\n")


def demo_selector_basico():
    """Demo: Uso básico del FrameworkSelector"""
    print_separator()
    print("DEMO 1: USO BÁSICO DEL FRAMEWORK SELECTOR")
    print_separator()

    # Inicializar selector
    selector = FrameworkSelector()

    print("📚 Total de frameworks en catálogo:", len(selector.get_all_frameworks()))

    # Frameworks por tema
    print("\n🎯 FRAMEWORKS POR TEMA:\n")

    for tema in ["Estrategia", "Procesos", "Innovación"]:
        frameworks = selector.get_frameworks_by_tema(tema.lower())
        print(f"{tema}:")
        for fw in frameworks:
            print(f"  - {fw['nombre']} ({fw['id']})")
        print()


def demo_recomendacion_por_intencion():
    """Demo: Recomendación de frameworks según intención"""
    print_separator()
    print("DEMO 2: RECOMENDACIÓN SEGÚN INTENCIÓN")
    print_separator()

    selector = FrameworkSelector()

    casos = [
        ("diagnosticar", "estrategia", "Diagnosticar problemas estratégicos"),
        ("elegir_herramienta", "procesos", "Elegir framework para optimizar procesos"),
        ("usar_herramienta", "innovacion", "Aprender a usar framework de innovación"),
        ("analizar_resultado", "estrategia", "Analizar resultado de análisis estratégico"),
    ]

    for intencion, tema, descripcion in casos:
        print(f"📌 {descripcion}")
        print(f"   Intención: {intencion} | Tema: {tema}\n")

        frameworks = selector.recommend_frameworks(tema, intencion, limit=3)

        if frameworks:
            print(f"   Recomendados ({len(frameworks)}):")
            for i, fw in enumerate(frameworks, 1):
                print(f"   {i}. {fw['nombre']} - {fw['descripcion_corta']}")
        else:
            print("   No hay frameworks disponibles")

        print()


def demo_framework_especifico():
    """Demo: Consulta de framework específico"""
    print_separator()
    print("DEMO 3: CONSULTA DE FRAMEWORK ESPECÍFICO")
    print_separator()

    selector = FrameworkSelector()

    frameworks_query = ["SWOT", "BMC", "JOURNEY", "SIPOC"]

    for fw_id in frameworks_query:
        fw = selector.get_framework_by_id(fw_id)
        if fw:
            print(f"🔧 {fw['nombre']} ({fw['id']})")
            print(f"   Tema: {fw['tema']}")
            print(f"   Descripción: {fw['descripcion_corta']}")
            print(f"   Pasos clave: {fw['pasos_clave']}")
            print(f"   Visual: {fw['image_url']}")
            print()


def demo_chat_con_frameworks():
    """Demo: Chat que recomienda frameworks automáticamente"""
    print_separator()
    print("DEMO 4: CHAT CON RECOMENDACIÓN AUTOMÁTICA DE FRAMEWORKS")
    print_separator()

    # Verificar API key
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Esta demo requiere OPENAI_API_KEY configurada")
        print("   Por favor, configura tu .env y vuelve a intentar\n")
        return

    print("Inicializando chat con modo 'rapido'...\n")
    chat = ChatGPT4Advanced(model="gpt-4", modo_clasificacion="rapido")

    ejemplos = [
        {
            "mensaje": "¿Qué framework me recomiendas para analizar mi posición competitiva?",
            "tema_esperado": "estrategia",
            "intencion_esperada": "elegir_herramienta"
        },
        {
            "mensaje": "Necesito optimizar el proceso de atención al cliente",
            "tema_esperado": "procesos",
            "intencion_esperada": "diagnosticar"
        },
        {
            "mensaje": "Enséñame a usar Design Thinking",
            "tema_esperado": "innovacion",
            "intencion_esperada": "usar_herramienta"
        }
    ]

    for i, ejemplo in enumerate(ejemplos, 1):
        print(f"--- Ejemplo {i} ---")
        print(f"👤 Usuario: {ejemplo['mensaje']}\n")

        # No llamar a la API real, solo clasificar
        clasificacion = chat.clasificar_mensaje(ejemplo['mensaje'])

        print(f"📊 Clasificación:")
        print(f"   Intención: {clasificacion['intencion']}")
        print(f"   Tema: {clasificacion['tema']}\n")

        # Obtener frameworks recomendados
        frameworks = chat.framework_selector.recommend_frameworks(
            clasificacion['tema'],
            clasificacion['intencion'],
            limit=3
        )

        if frameworks:
            print(f"🔧 Frameworks recomendados ({len(frameworks)}):")
            for j, fw in enumerate(frameworks, 1):
                print(f"   {j}. {fw['nombre']} - {fw['descripcion_corta']}")
        else:
            print("   No hay frameworks específicos para este caso")

        print()


def demo_contexto_prompt():
    """Demo: Cómo se agrega el contexto de frameworks al prompt"""
    print_separator()
    print("DEMO 5: CONTEXTO DE FRAMEWORKS EN EL PROMPT")
    print_separator()

    selector = FrameworkSelector()

    print("Ejemplo de cómo se genera el contexto para el prompt del sistema:\n")

    tema = "estrategia"
    intencion = "elegir_herramienta"

    contexto = selector.get_frameworks_context(tema, intencion)

    print(f"Tema: {tema} | Intención: {intencion}\n")
    print("Contexto generado:")
    print("-" * 80)
    print(contexto)
    print("-" * 80)


def demo_casos_uso_reales():
    """Demo: Casos de uso reales con frameworks"""
    print_separator()
    print("DEMO 6: CASOS DE USO REALES")
    print_separator()

    selector = FrameworkSelector()

    casos = [
        {
            "titulo": "Startup necesita definir modelo de negocio",
            "tema": "estrategia",
            "intencion": "usar_herramienta",
            "frameworks_esperados": ["LEAN_CANVAS", "BMC", "VPC"]
        },
        {
            "titulo": "Empresa quiere analizar eficiencia operativa",
            "tema": "procesos",
            "intencion": "diagnosticar",
            "frameworks_esperados": ["SIPOC", "DIAGRAMA_FLUJO"]
        },
        {
            "titulo": "Equipo necesita mejorar experiencia del cliente",
            "tema": "innovacion",
            "intencion": "usar_herramienta",
            "frameworks_esperados": ["JOURNEY", "PAIN_GAIN"]
        },
        {
            "titulo": "Líder quiere priorizar iniciativas estratégicas",
            "tema": "estrategia",
            "intencion": "recomendaciones",
            "frameworks_esperados": ["SWOT"]
        }
    ]

    for i, caso in enumerate(casos, 1):
        print(f"{i}. {caso['titulo']}")
        print(f"   Contexto: {caso['tema']} / {caso['intencion']}\n")

        frameworks = selector.recommend_frameworks(
            caso['tema'],
            caso['intencion'],
            limit=3
        )

        print(f"   Frameworks recomendados:")
        for fw in frameworks:
            es_esperado = "✓" if fw['id'] in caso['frameworks_esperados'] else " "
            print(f"   {es_esperado} {fw['nombre']} ({fw['id']})")
            print(f"     {fw['descripcion_corta']}")

        print()


def menu_principal():
    """Menú principal de demos"""
    print("\n" + "=" * 80)
    print("SISTEMA DE FRAMEWORKS - DEMOS INTERACTIVAS")
    print("=" * 80)
    print("\nDemos disponibles:")
    print("  1. Uso básico del FrameworkSelector")
    print("  2. Recomendación según intención")
    print("  3. Consulta de framework específico")
    print("  4. Chat con recomendación automática")
    print("  5. Contexto de frameworks en el prompt")
    print("  6. Casos de uso reales")
    print("  7. Ejecutar todas las demos")
    print("  0. Salir")

    return input("\nSelecciona demo (0-7): ").strip()


def main():
    """Función principal"""
    demos = {
        "1": demo_selector_basico,
        "2": demo_recomendacion_por_intencion,
        "3": demo_framework_especifico,
        "4": demo_chat_con_frameworks,
        "5": demo_contexto_prompt,
        "6": demo_casos_uso_reales,
    }

    while True:
        opcion = menu_principal()

        if opcion == "0":
            print("\n¡Hasta luego!\n")
            break

        if opcion == "7":
            # Ejecutar todas las demos
            for demo in demos.values():
                try:
                    demo()
                    input("\nPresiona Enter para continuar...")
                except Exception as e:
                    print(f"\n❌ Error en demo: {e}\n")
            continue

        if opcion in demos:
            try:
                demos[opcion]()
                input("\nPresiona Enter para volver al menú...")
            except Exception as e:
                print(f"\n❌ Error: {e}\n")
                input("Presiona Enter para continuar...")
        else:
            print("\n⚠️  Opción no válida\n")


if __name__ == "__main__":
    main()
