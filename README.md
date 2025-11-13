# Chat con Memoria usando OpenAI GPT-4

Bot de chat inteligente que utiliza la API de OpenAI (GPT-4) con capacidad de memoria de conversación para mantener el contexto a lo largo de la interacción.

## 🆕 Dos Versiones Disponibles

### Versión Básica (`chat_gpt4.py`)
Chat simple con memoria de conversación.

### Versión Avanzada (`chat_gpt4_advanced.py`) ⭐ NUEVO
Chat inteligente con **detección automática de intenciones y clasificación por temas**.

## Características

### Características Básicas
- 🤖 Utiliza GPT-4 de OpenAI
- 💾 Mantiene memoria de toda la conversación
- 🔄 Capacidad de reiniciar la conversación
- 📊 Visualización del historial de mensajes
- ⚡ Interfaz de línea de comandos simple y fácil de usar

### Características Avanzadas ⭐ NUEVO
- 🎯 **Detección Automática de Intenciones**: El agente detecta si quieres diagnosticar, elegir herramienta, usar herramienta, analizar resultado, o pedir recomendaciones
- 🎨 **Clasificación por Temas**: Clasifica automáticamente en Estrategia, Procesos, o Innovación
- 🧠 **Prompts Especializados**: Adapta su comportamiento según la intención y tema detectados
- 🚀 **3 Modos de Clasificación**: Auto (GPT), Rápido (keywords), o Manual
- 📈 **Feedback de Clasificación**: Muestra qué intención y tema detectó

## Requisitos

- Python 3.7 o superior
- Una API Key de OpenAI (puedes obtenerla en [platform.openai.com](https://platform.openai.com))

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd openai_bot_utq
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la API Key:**
   - Copia el archivo `.env.example` a `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edita el archivo `.env` y reemplaza `tu_api_key_aqui` con tu API Key de OpenAI:
     ```
     OPENAI_API_KEY=sk-tu-api-key-real
     ```

## Uso

### Versión Básica

Ejecuta el script básico para iniciar el chat simple:

```bash
python chat_gpt4.py
```

**Comandos disponibles:**
- `salir` o `exit` - Termina la sesión del chat
- `reset` - Reinicia la conversación (borra el historial)
- `historial` - Muestra el número de mensajes en memoria

### Versión Avanzada ⭐ RECOMENDADA

Ejecuta el script avanzado con detección de intenciones:

```bash
python chat_gpt4_advanced.py
```

**Modos de clasificación:**
1. **Auto** (recomendado) - Usa GPT para clasificar con alta precisión
2. **Rápido** - Usa palabras clave (sin costo adicional)
3. **Manual** - Sin clasificación automática

**Comandos adicionales:**
- `clasificacion` - Muestra la intención y tema actual
- `cambiar [intencion] [tema]` - Cambia manualmente la clasificación
- Todos los comandos de la versión básica

**Ejemplo de uso:**

```
Tú: Necesito diagnosticar por qué mi equipo no cumple objetivos
📊 [Intención: diagnosticar | Tema: procesos]

Asistente: Entiendo que quieres identificar las causas raíz.
           Déjame hacerte algunas preguntas para diagnosticar mejor:
           1. ¿Desde cuándo notas este problema?
           2. ¿Los objetivos están claramente definidos?...

Tú: ¿Qué framework me recomiendas para mejorar esto?
📊 [Intención: elegir_herramienta | Tema: procesos]

Asistente: Basándome en tu situación, te sugiero 3 opciones:
           1. LEAN - Para eliminar desperdicios...
```

### Ver Ejemplos Completos

Ejecuta el archivo de ejemplos para ver todos los casos de uso:

```bash
python ejemplos_uso.py
```

### Uso Programático

#### Versión Básica

```python
from chat_gpt4 import ChatGPT4

# Inicializar el chat
chat = ChatGPT4(model="gpt-4")

# Enviar un mensaje
respuesta = chat.chat("¿Cuál es la capital de Francia?")
print(respuesta)

# Continuar la conversación (mantiene el contexto)
respuesta = chat.chat("¿Y cuál es su población?")
print(respuesta)

# Reiniciar la conversación
chat.reset_conversation()

# Ver el historial
historial = chat.get_history()
print(historial)
```

#### Versión Avanzada ⭐

```python
from chat_gpt4_advanced import ChatGPT4Advanced

# Inicializar con detección automática
chat = ChatGPT4Advanced(model="gpt-4", modo_clasificacion="auto")

# Enviar mensaje (clasifica automáticamente)
resultado = chat.chat("¿Qué framework me recomiendas para gestión ágil?")

# Acceder a la respuesta y clasificación
print(f"Respuesta: {resultado['respuesta']}")
print(f"Intención: {resultado['clasificacion']['intencion']}")
print(f"Tema: {resultado['clasificacion']['tema']}")

# Cambiar intención manualmente
chat.cambiar_intencion("diagnosticar", "estrategia")

# Ver clasificación actual
clasificacion = chat.get_clasificacion_actual()
print(clasificacion)
```

## Estructura del Proyecto

```
openai_bot_utq/
├── chat_gpt4.py              # Versión básica del chat
├── chat_gpt4_advanced.py     # Versión avanzada con intenciones ⭐
├── intent_classifier.py      # Motor de clasificación de intenciones
├── ejemplos_uso.py           # Ejemplos ejecutables
├── requirements.txt          # Dependencias del proyecto
├── .env.example             # Ejemplo de configuración
├── .env                     # Tu configuración (no se sube a git)
├── .gitignore              # Archivos ignorados por git
├── README.md               # Este archivo
└── GUIA_INTENCIONES.md     # Guía detallada de intenciones y temas
```

## 🎯 Sistema de Intenciones y Temas

La versión avanzada incluye un sistema inteligente que detecta automáticamente qué quieres hacer y adapta su comportamiento.

### Intenciones Detectables

1. **DIAGNOSTICAR** - Identificar y analizar problemas
   - Ejemplo: "Necesito diagnosticar por qué tenemos baja productividad"

2. **ELEGIR_HERRAMIENTA** - Recomendar frameworks/metodologías
   - Ejemplo: "¿Qué framework me recomiendas para gestión ágil?"

3. **USAR_HERRAMIENTA** - Guía paso a paso
   - Ejemplo: "¿Cómo aplico Design Thinking?"

4. **ANALIZAR_RESULTADO** - Feedback sobre resultados
   - Ejemplo: "Analiza este análisis FODA que hice"

5. **RECOMENDACIONES** - Próximos pasos y conclusiones
   - Ejemplo: "¿Cuáles serían los próximos pasos?"

### Temas de Clasificación

- **ESTRATEGIA** - Visión, objetivos, competencia, posicionamiento
- **PROCESOS** - Optimización, workflows, eficiencia, metodologías
- **INNOVACIÓN** - Tecnología, transformación digital, creatividad

**📚 Guía Completa:** Ver [GUIA_INTENCIONES.md](GUIA_INTENCIONES.md) para ejemplos detallados y mejores prácticas.

---

## 🧠 Cómo Funciona la Memoria

El bot mantiene un historial completo de la conversación (`conversation_history`) que incluye:

1. **Mensaje del sistema**: Define el comportamiento del asistente (se adapta según intención y tema)
2. **Mensajes del usuario**: Todas tus preguntas
3. **Respuestas del asistente**: Todas las respuestas de GPT-4

En cada nueva pregunta, se envía todo el historial a la API de OpenAI, lo que permite que el modelo mantenga el contexto de la conversación completa.

**En la versión avanzada:** El prompt del sistema cambia dinámicamente según la intención y tema detectados, haciendo que el agente sea un experto contextual.

## Modelos Disponibles

Puedes cambiar el modelo al inicializar la clase:

```python
# GPT-4 (por defecto)
chat = ChatGPT4(model="gpt-4")

# GPT-4 Turbo
chat = ChatGPT4(model="gpt-4-turbo-preview")

# GPT-3.5 Turbo (más económico)
chat = ChatGPT4(model="gpt-3.5-turbo")
```

## Consideraciones de Costos

### Versión Básica
- Cada mensaje enviado incluye todo el historial de conversación
- Conversaciones largas consumen más tokens
- GPT-4 es más costoso que GPT-3.5-turbo
- Usa el comando `reset` para limpiar el historial si la conversación se vuelve muy larga

### Versión Avanzada
- **Modo Auto**: Usa GPT-3.5-turbo adicional para clasificación (~$0.002-0.003 por mensaje)
- **Modo Rápido**: Sin costo adicional (clasificación por keywords)
- **Modo Manual**: Sin costo adicional (sin clasificación)
- Recomendación: Modo Rápido para demos/pruebas, Modo Auto para producción

## Solución de Problemas

### Error: "OPENAI_API_KEY no encontrada"
- Asegúrate de haber creado el archivo `.env`
- Verifica que la API Key esté correctamente configurada en `.env`

### Error de autenticación
- Verifica que tu API Key sea válida
- Comprueba que tengas créditos disponibles en tu cuenta de OpenAI

### Respuestas lentas
- GPT-4 puede tomar varios segundos en responder
- Considera usar `gpt-3.5-turbo` para respuestas más rápidas

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerencias o mejoras.
