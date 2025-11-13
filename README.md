# Chat con Memoria usando OpenAI GPT-4

Bot de chat inteligente que utiliza la API de OpenAI (GPT-4) con capacidad de memoria de conversación para mantener el contexto a lo largo de la interacción.

## Características

- 🤖 Utiliza GPT-4 de OpenAI
- 💾 Mantiene memoria de toda la conversación
- 🔄 Capacidad de reiniciar la conversación
- 📊 Visualización del historial de mensajes
- ⚡ Interfaz de línea de comandos simple y fácil de usar

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

### Modo Interactivo

Ejecuta el script principal para iniciar el chat interactivo:

```bash
python chat_gpt4.py
```

### Comandos Disponibles

Durante la conversación, puedes usar los siguientes comandos especiales:

- `salir` o `exit` - Termina la sesión del chat
- `reset` - Reinicia la conversación (borra el historial)
- `historial` - Muestra el número de mensajes en memoria

### Uso Programático

También puedes usar la clase `ChatGPT4` en tus propios scripts:

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

## Estructura del Proyecto

```
openai_bot_utq/
├── chat_gpt4.py          # Script principal con la clase ChatGPT4
├── requirements.txt      # Dependencias del proyecto
├── .env.example         # Ejemplo de configuración
├── .env                 # Tu configuración (no se sube a git)
├── .gitignore          # Archivos ignorados por git
└── README.md           # Este archivo
```

## Cómo Funciona la Memoria

El bot mantiene un historial completo de la conversación (`conversation_history`) que incluye:

1. **Mensaje del sistema**: Define el comportamiento del asistente
2. **Mensajes del usuario**: Todas tus preguntas
3. **Respuestas del asistente**: Todas las respuestas de GPT-4

En cada nueva pregunta, se envía todo el historial a la API de OpenAI, lo que permite que el modelo mantenga el contexto de la conversación completa.

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

- Cada mensaje enviado incluye todo el historial de conversación
- Conversaciones largas consumen más tokens
- GPT-4 es más costoso que GPT-3.5-turbo
- Usa el comando `reset` para limpiar el historial si la conversación se vuelve muy larga

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
