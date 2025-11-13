"""
Módulo de Clasificación de Intenciones y Temas
Detecta automáticamente la intención del usuario y clasifica el mensaje por tema.
"""

from enum import Enum
from typing import Dict, Optional
import json


class Intencion(Enum):
    """Intenciones posibles del usuario."""
    DIAGNOSTICAR = "diagnosticar"
    ELEGIR_HERRAMIENTA = "elegir_herramienta"
    USAR_HERRAMIENTA = "usar_herramienta"
    ANALIZAR_RESULTADO = "analizar_resultado"
    RECOMENDACIONES = "recomendaciones"
    CONVERSACION_GENERAL = "conversacion_general"


class Tema(Enum):
    """Temas principales de clasificación."""
    ESTRATEGIA = "estrategia"
    PROCESOS = "procesos"
    INNOVACION = "innovacion"
    GENERAL = "general"


class IntentClassifier:
    """
    Clasificador de intenciones y temas usando GPT-4.
    """

    # Palabras clave para detección rápida de intenciones
    KEYWORDS_INTENCION = {
        Intencion.DIAGNOSTICAR: [
            "diagnosticar", "analizar problema", "identificar", "evaluar situación",
            "qué está pasando", "cuál es el problema", "revisar", "examinar"
        ],
        Intencion.ELEGIR_HERRAMIENTA: [
            "qué herramienta", "qué framework", "qué metodología", "recomienda usar",
            "cuál aplicar", "qué usar", "mejor opción", "que framework"
        ],
        Intencion.USAR_HERRAMIENTA: [
            "cómo usar", "guía", "paso a paso", "ayúdame con", "cómo aplico",
            "instrucciones", "tutorial", "enséñame", "muéstrame cómo"
        ],
        Intencion.ANALIZAR_RESULTADO: [
            "qué opinas", "analiza esto", "feedback", "retroalimentación",
            "revisa esto", "que te parece", "mira esto", "observa", "evalúa"
        ],
        Intencion.RECOMENDACIONES: [
            "próximos pasos", "qué sigue", "recomendaciones", "sugerencias",
            "qué más", "conclusiones", "herramientas extras", "siguiente"
        ]
    }

    # Palabras clave para detección rápida de temas
    KEYWORDS_TEMA = {
        Tema.ESTRATEGIA: [
            "estrategia", "visión", "misión", "objetivos", "metas", "planificación",
            "strategic", "roadmap", "dirección", "futuro", "competencia", "mercado",
            "posicionamiento", "ventaja competitiva", "análisis FODA", "SWOT"
        ],
        Tema.PROCESOS: [
            "proceso", "procedimiento", "workflow", "flujo", "operación", "metodología",
            "implementación", "ejecución", "optimización", "eficiencia", "productividad",
            "automatización", "mejora continua", "kaizen", "lean", "six sigma"
        ],
        Tema.INNOVACION: [
            "innovación", "innovar", "creatividad", "nuevo", "transformación",
            "disrupción", "tecnología", "digital", "IA", "inteligencia artificial",
            "automatización", "blockchain", "cloud", "agile", "scrum", "design thinking"
        ]
    }

    @staticmethod
    def _detectar_por_keywords(texto: str, keywords_dict: Dict) -> Optional[Enum]:
        """
        Detecta coincidencias usando palabras clave.

        Args:
            texto: Texto a analizar
            keywords_dict: Diccionario con palabras clave por categoría

        Returns:
            Categoría detectada o None
        """
        texto_lower = texto.lower()

        # Contador de coincidencias por categoría
        coincidencias = {}

        for categoria, keywords in keywords_dict.items():
            count = sum(1 for keyword in keywords if keyword in texto_lower)
            if count > 0:
                coincidencias[categoria] = count

        # Retornar la categoría con más coincidencias
        if coincidencias:
            return max(coincidencias, key=coincidencias.get)

        return None

    @staticmethod
    def crear_prompt_clasificacion() -> str:
        """
        Crea el prompt para que GPT-4 clasifique intención y tema.
        """
        return """Analiza el mensaje del usuario y clasifícalo en:

1. INTENCIÓN (selecciona UNA):
   - diagnosticar: Usuario quiere identificar/analizar un problema o situación
   - elegir_herramienta: Usuario busca recomendación de herramienta/framework/metodología
   - usar_herramienta: Usuario quiere guía paso a paso para aplicar algo
   - analizar_resultado: Usuario presenta un resultado (texto/imagen) y quiere feedback
   - recomendaciones: Usuario pide próximos pasos, conclusiones o sugerencias
   - conversacion_general: Conversación normal sin intención específica

2. TEMA (selecciona UNO):
   - estrategia: Relacionado con visión, objetivos, planificación, competencia
   - procesos: Relacionado con metodologías, workflows, operaciones, eficiencia
   - innovacion: Relacionado con nuevas tecnologías, transformación, creatividad
   - general: No encaja claramente en los anteriores

Responde SOLO en formato JSON:
{
    "intencion": "nombre_intencion",
    "tema": "nombre_tema",
    "confianza": 0.0-1.0,
    "razon": "breve explicación"
}"""

    @staticmethod
    def extraer_clasificacion(respuesta_gpt: str) -> Dict:
        """
        Extrae la clasificación de la respuesta de GPT-4.

        Args:
            respuesta_gpt: Respuesta en formato JSON de GPT-4

        Returns:
            Diccionario con la clasificación
        """
        try:
            # Intentar parsear JSON directamente
            return json.loads(respuesta_gpt)
        except json.JSONDecodeError:
            # Si falla, buscar JSON en el texto
            start = respuesta_gpt.find('{')
            end = respuesta_gpt.rfind('}') + 1
            if start != -1 and end > start:
                json_str = respuesta_gpt[start:end]
                return json.loads(json_str)

            # Si no se puede parsear, retornar valores por defecto
            return {
                "intencion": "conversacion_general",
                "tema": "general",
                "confianza": 0.5,
                "razon": "No se pudo clasificar automáticamente"
            }

    @staticmethod
    def clasificar_rapido(mensaje: str) -> Dict:
        """
        Clasificación rápida basada en palabras clave (sin usar API).

        Args:
            mensaje: Mensaje del usuario

        Returns:
            Diccionario con clasificación preliminar
        """
        intencion = IntentClassifier._detectar_por_keywords(
            mensaje,
            IntentClassifier.KEYWORDS_INTENCION
        )

        tema = IntentClassifier._detectar_por_keywords(
            mensaje,
            IntentClassifier.KEYWORDS_TEMA
        )

        return {
            "intencion": intencion.value if intencion else "conversacion_general",
            "tema": tema.value if tema else "general",
            "confianza": 0.7 if (intencion or tema) else 0.3,
            "metodo": "keywords"
        }


class PromptBuilder:
    """
    Constructor de prompts especializados según intención y tema.
    """

    # Prompts base por intención
    PROMPTS_INTENCION = {
        Intencion.DIAGNOSTICAR: """Eres un consultor experto en diagnóstico organizacional.
Tu objetivo es ayudar a identificar y analizar problemas de manera estructurada.

Cuando el usuario te presente una situación:
1. Haz preguntas clarificadoras si necesitas más información
2. Identifica los síntomas y posibles causas raíz
3. Proporciona un análisis estructurado
4. Sugiere áreas que requieren atención

Mantén un enfoque analítico y profesional.""",

        Intencion.ELEGIR_HERRAMIENTA: """Eres un consultor experto en metodologías y frameworks.
Tu objetivo es recomendar la mejor herramienta/framework según el contexto.

Cuando el usuario busque una recomendación:
1. Entiende el contexto y objetivos
2. Presenta 2-3 opciones con pros y contras
3. Recomienda la más adecuada según su situación
4. Explica por qué es la mejor opción

Sé específico y práctico en tus recomendaciones.""",

        Intencion.USAR_HERRAMIENTA: """Eres un instructor experto en implementación de metodologías.
Tu objetivo es guiar paso a paso en la aplicación de herramientas/frameworks.

Cuando el usuario pida guía:
1. Confirma qué herramienta/framework quiere usar
2. Proporciona instrucciones paso a paso claras
3. Da ejemplos prácticos
4. Anticipa dudas comunes
5. Ofrece plantillas o formatos si aplica

Sé didáctico y asegúrate de que pueda seguir los pasos fácilmente.""",

        Intencion.ANALIZAR_RESULTADO: """Eres un evaluador experto que proporciona feedback constructivo.
Tu objetivo es analizar resultados y dar retroalimentación valiosa.

Cuando el usuario presente un resultado:
1. Reconoce lo que está bien hecho
2. Identifica áreas de mejora específicas
3. Proporciona sugerencias concretas y accionables
4. Explica el razonamiento detrás de tu feedback

Sé constructivo, específico y orientado a la mejora.""",

        Intencion.RECOMENDACIONES: """Eres un asesor estratégico que ayuda a definir próximos pasos.
Tu objetivo es proporcionar recomendaciones accionables.

Cuando el usuario pida próximos pasos:
1. Resume el contexto actual
2. Prioriza las acciones más importantes
3. Proporciona un roadmap claro
4. Sugiere recursos o herramientas adicionales
5. Define indicadores de éxito

Sé práctico y orientado a la acción.""",

        Intencion.CONVERSACION_GENERAL: """Eres un asistente experto en consultoría empresarial.
Respondes de manera profesional, clara y útil."""
    }

    # Contexto adicional por tema
    CONTEXTO_TEMA = {
        Tema.ESTRATEGIA: """
CONTEXTO: El usuario está trabajando en temas de ESTRATEGIA.
- Enfócate en visión de largo plazo, objetivos, competencia y posicionamiento
- Usa frameworks como FODA/SWOT, Océano Azul, Fuerzas de Porter cuando sea relevante
- Piensa en términos de ventaja competitiva y diferenciación""",

        Tema.PROCESOS: """
CONTEXTO: El usuario está trabajando en temas de PROCESOS.
- Enfócate en eficiencia, optimización y mejora continua
- Usa metodologías como Lean, Six Sigma, BPM cuando sea relevante
- Piensa en términos de workflows, automatización y productividad""",

        Tema.INNOVACION: """
CONTEXTO: El usuario está trabajando en temas de INNOVACIÓN.
- Enfócate en transformación, nuevas tecnologías y creatividad
- Usa enfoques como Design Thinking, Agile, Scrum cuando sea relevante
- Piensa en términos de disrupción, experimentación y adaptación""",

        Tema.GENERAL: ""
    }

    @staticmethod
    def construir_prompt_sistema(intencion: str, tema: str) -> str:
        """
        Construye el prompt del sistema basado en intención y tema.

        Args:
            intencion: Intención detectada
            tema: Tema detectado

        Returns:
            Prompt del sistema personalizado
        """
        try:
            intencion_enum = Intencion(intencion)
            tema_enum = Tema(tema)
        except ValueError:
            intencion_enum = Intencion.CONVERSACION_GENERAL
            tema_enum = Tema.GENERAL

        prompt_base = PromptBuilder.PROMPTS_INTENCION.get(
            intencion_enum,
            PromptBuilder.PROMPTS_INTENCION[Intencion.CONVERSACION_GENERAL]
        )

        contexto_tema = PromptBuilder.CONTEXTO_TEMA.get(tema_enum, "")

        return f"{prompt_base}\n{contexto_tema}".strip()
