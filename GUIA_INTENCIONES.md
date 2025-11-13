# Guía de Intenciones y Temas del Agente

Esta guía explica cómo el agente detecta y responde a diferentes intenciones y temas.

## 📋 Índice

1. [Intenciones Disponibles](#intenciones-disponibles)
2. [Temas de Clasificación](#temas-de-clasificación)
3. [Ejemplos por Intención](#ejemplos-por-intención)
4. [Cómo Funciona la Detección](#cómo-funciona-la-detección)
5. [Mejores Prácticas](#mejores-prácticas)

---

## 🎯 Intenciones Disponibles

El agente puede detectar 6 tipos de intenciones principales:

### 1. DIAGNOSTICAR

**¿Cuándo se activa?**
- Cuando quieres identificar o analizar un problema
- Cuando necesitas evaluar una situación
- Cuando buscas entender qué está pasando

**Comportamiento del agente:**
- Hace preguntas clarificadoras
- Identifica síntomas y causas raíz
- Proporciona análisis estructurado
- Sugiere áreas que requieren atención

**Palabras clave que la activan:**
- "diagnosticar", "analizar problema", "identificar"
- "evaluar situación", "qué está pasando"
- "cuál es el problema", "revisar", "examinar"

**Ejemplo de uso:**
```
Usuario: "Necesito diagnosticar por qué mi equipo no cumple los objetivos"
Agente: [Modo diagnóstico] "Entiendo que quieres identificar las causas.
        Déjame hacerte algunas preguntas:
        1. ¿Desde cuándo notas este problema?
        2. ¿Los objetivos están claramente definidos?
        3. ¿El equipo tiene los recursos necesarios?..."
```

---

### 2. ELEGIR_HERRAMIENTA

**¿Cuándo se activa?**
- Cuando buscas recomendación de herramienta/framework
- Cuando no sabes qué metodología usar
- Cuando quieres comparar opciones

**Comportamiento del agente:**
- Entiende el contexto y objetivos
- Presenta 2-3 opciones con pros y contras
- Recomienda la más adecuada
- Explica el razonamiento

**Palabras clave que la activan:**
- "qué herramienta", "qué framework", "qué metodología"
- "recomienda usar", "cuál aplicar", "mejor opción"

**Ejemplo de uso:**
```
Usuario: "¿Qué framework me recomiendas para mejorar procesos?"
Agente: [Modo recomendación] "Para mejorar procesos, te sugiero 3 opciones:

        1. LEAN - Si buscas eliminar desperdicios
           ✓ Pros: Simple, enfoque en valor
           ✗ Contras: Requiere cambio cultural

        2. Six Sigma - Si necesitas reducir variabilidad
           ✓ Pros: Enfoque en datos, resultados medibles
           ✗ Contras: Más complejo, requiere entrenamiento

        3. BPM - Si quieres modelar y automatizar
           ✓ Pros: Visión completa, tecnología
           ✗ Contras: Inversión en software

        Recomendación: LEAN si estás comenzando..."
```

---

### 3. USAR_HERRAMIENTA

**¿Cuándo se activa?**
- Cuando quieres guía paso a paso
- Cuando necesitas instrucciones para aplicar algo
- Cuando pides tutorial o ayuda práctica

**Comportamiento del agente:**
- Confirma qué herramienta quieres usar
- Proporciona pasos claros y secuenciales
- Da ejemplos prácticos
- Anticipa dudas comunes
- Ofrece plantillas si aplica

**Palabras clave que la activan:**
- "cómo usar", "guía", "paso a paso"
- "ayúdame con", "cómo aplico", "instrucciones"
- "tutorial", "enséñame", "muéstrame cómo"

**Ejemplo de uso:**
```
Usuario: "¿Cómo aplico Design Thinking paso a paso?"
Agente: [Modo instructor] "Te guiaré en la aplicación de Design Thinking:

        PASO 1: EMPATIZAR (1-2 semanas)
        - Entrevista a usuarios (mínimo 5-10 personas)
        - Observa cómo usan tu producto/servicio
        - Documenta: necesidades, frustraciones, contexto

        Herramienta: Mapa de Empatía
        [Proporciona plantilla]

        PASO 2: DEFINIR (3-5 días)
        - Analiza insights de la fase anterior
        - Define el problema central
        - Redacta el 'Point of View'

        Formato: [Usuario] necesita [necesidad] porque [insight]

        ¿Quieres que profundice en algún paso específico?"
```

---

### 4. ANALIZAR_RESULTADO

**¿Cuándo se activa?**
- Cuando presentas un resultado y quieres feedback
- Cuando compartes texto o imagen para análisis
- Cuando pides opinión sobre algo que hiciste

**Comportamiento del agente:**
- Reconoce lo que está bien hecho
- Identifica áreas de mejora específicas
- Proporciona sugerencias accionables
- Explica el razonamiento

**Palabras clave que la activan:**
- "qué opinas", "analiza esto", "feedback"
- "retroalimentación", "revisa esto", "que te parece"
- "mira esto", "observa", "evalúa"

**Ejemplo de uso:**
```
Usuario: "Analiza este FODA:
         Fortalezas: Equipo capacitado
         Oportunidades: Mercado creciendo
         Debilidades: Procesos lentos
         Amenazas: Competencia fuerte"

Agente: [Modo evaluador] "Análisis de tu FODA:

        ✓ BIEN HECHO:
        - Identificaste elementos en cada cuadrante
        - Hay balance entre interno/externo

        ⚠️ ÁREAS DE MEJORA:
        1. Las fortalezas son muy genéricas
           → Especifica: ¿capacitados en qué?

        2. Falta conexión entre cuadrantes
           → ¿Cómo usas tu equipo (F) para aprovechar
              el mercado (O)?

        3. Las amenazas necesitan más detalle
           → ¿Quiénes son tus competidores? ¿Qué hacen mejor?

        SUGERENCIA: Crea una matriz FO-FA-DO-DA para
        estrategias cruzadas..."
```

---

### 5. RECOMENDACIONES

**¿Cuándo se activa?**
- Cuando pides próximos pasos
- Cuando buscas conclusiones o cierre
- Cuando necesitas un plan de acción
- Cuando preguntas "¿qué sigue?"

**Comportamiento del agente:**
- Resume el contexto actual
- Prioriza las acciones importantes
- Proporciona roadmap claro
- Sugiere recursos adicionales
- Define indicadores de éxito

**Palabras clave que la activan:**
- "próximos pasos", "qué sigue", "recomendaciones"
- "sugerencias", "qué más", "conclusiones"
- "herramientas extras", "siguiente"

**Ejemplo de uso:**
```
Usuario: "Implementamos Scrum hace 3 meses. ¿Próximos pasos?"
Agente: [Modo asesor] "Basándome en que ya llevan 3 meses con Scrum:

        ROADMAP DE MADUREZ:

        📍 DÓNDE ESTÁS: Fase de Adopción (mes 3)

        🎯 PRÓXIMOS PASOS (Mes 4-6):

        1. CORTO PLAZO (próximo Sprint):
           ☑ Implementar métricas: Velocity, Burn-down
           ☑ Mejorar Retrospectivas con técnicas variadas

        2. MEDIANO PLAZO (2-3 meses):
           ☑ Entrenar a un Scrum Master interno
           ☑ Comenzar refinamiento continuo de backlog
           ☑ Implementar Definition of Done más rigurosa

        3. HERRAMIENTAS COMPLEMENTARIAS:
           - Jira/Trello para gestión visual
           - Miro para colaboración remota
           - Confluence para documentación

        📊 INDICADORES DE ÉXITO:
        - Velocity estable (±20%)
        - Sprints completados al 80%+
        - Satisfacción del equipo >7/10

        ¿Qué área quieres priorizar?"
```

---

### 6. CONVERSACION_GENERAL

**¿Cuándo se activa?**
- Cuando el mensaje no encaja en las otras intenciones
- Preguntas generales o aclaraciones
- Conversación casual

**Comportamiento del agente:**
- Responde de manera profesional y clara
- Se adapta al contexto de la conversación
- Mantiene el tono consultivo

---

## 🎨 Temas de Clasificación

El agente clasifica cada conversación en uno de estos temas:

### TEMA 1: ESTRATEGIA

**¿Qué incluye?**
- Visión, misión, objetivos de largo plazo
- Análisis competitivo y de mercado
- Posicionamiento y diferenciación
- Planificación estratégica

**Frameworks que usa el agente:**
- FODA/SWOT
- Fuerzas de Porter
- Océano Azul
- Análisis PESTEL

**Palabras clave:**
- estrategia, visión, misión, objetivos, metas
- competencia, mercado, posicionamiento
- ventaja competitiva, roadmap estratégico

**Ejemplo:**
```
Usuario: "¿Cómo definimos nuestra ventaja competitiva?"
Tema detectado: ESTRATEGIA
```

---

### TEMA 2: PROCESOS

**¿Qué incluye?**
- Optimización de workflows
- Metodologías de mejora continua
- Eficiencia operacional
- Procedimientos y estandarización

**Frameworks que usa el agente:**
- Lean
- Six Sigma
- BPM (Business Process Management)
- Kaizen

**Palabras clave:**
- proceso, procedimiento, workflow, flujo
- operación, metodología, eficiencia
- optimización, mejora continua, automatización

**Ejemplo:**
```
Usuario: "Necesitamos optimizar nuestro proceso de atención al cliente"
Tema detectado: PROCESOS
```

---

### TEMA 3: INNOVACIÓN

**¿Qué incluye?**
- Transformación digital
- Nuevas tecnologías
- Creatividad y experimentación
- Metodologías ágiles

**Frameworks que usa el agente:**
- Design Thinking
- Agile/Scrum
- Lean Startup
- Jobs to be Done

**Palabras clave:**
- innovación, creatividad, transformación
- digital, IA, automatización, tecnología
- disrupción, agile, scrum

**Ejemplo:**
```
Usuario: "Queremos implementar IA para automatizar tareas"
Tema detectado: INNOVACIÓN
```

---

### TEMA 4: GENERAL

**¿Cuándo se usa?**
- Conversaciones que no encajan claramente en los otros temas
- Temas mixtos o transversales
- Preguntas generales de consultoría

---

## 🔍 Cómo Funciona la Detección

El sistema ofrece 3 modos de clasificación:

### Modo AUTO (Recomendado)

```python
chat = ChatGPT4Advanced(mode_clasificacion="auto")
```

- Usa GPT-3.5-turbo para clasificar cada mensaje
- Mayor precisión
- Entiende contexto y matices
- Costo: ~0.002-0.003 USD por clasificación

**Cuándo usarlo:** Cuando necesitas máxima precisión

---

### Modo RÁPIDO

```python
chat = ChatGPT4Advanced(mode_clasificacion="rapido")
```

- Usa palabras clave predefinidas
- Muy rápido (sin llamadas a API)
- Sin costo adicional
- Precisión: ~70-80%

**Cuándo usarlo:** Para demos, pruebas o bajo presupuesto

---

### Modo MANUAL

```python
chat = ChatGPT4Advanced(mode_clasificacion="manual")
```

- Sin clasificación automática
- Tú controlas la intención manualmente
- Útil para casos específicos

**Cuándo usarlo:** Cuando sabes exactamente qué intención necesitas

---

## 💡 Mejores Prácticas

### 1. Sé Específico en tus Mensajes

❌ **Mal:**
```
"Ayuda con mi empresa"
```

✅ **Bien:**
```
"Necesito diagnosticar por qué tenemos alta rotación de personal"
```

---

### 2. Una Intención por Mensaje

❌ **Mal:**
```
"¿Qué framework usar para innovación y cómo lo aplico paso a paso
y también dame recomendaciones?"
```

✅ **Bien:**
```
Mensaje 1: "¿Qué framework me recomiendas para innovación?"
[Espera respuesta]
Mensaje 2: "Perfecto, ¿cómo aplico Design Thinking paso a paso?"
[Espera respuesta]
Mensaje 3: "¿Cuáles serían los próximos pasos después de empatizar?"
```

---

### 3. Proporciona Contexto

✅ **Mejor:**
```
"Somos una startup de 20 personas. ¿Qué framework ágil nos recomiendas?"
```

Mejor que:
```
"¿Qué framework ágil usar?"
```

---

### 4. Usa Comandos para Control Manual

Si la clasificación automática no es correcta:

```
> cambiar diagnosticar estrategia
```

O en código:
```python
chat.cambiar_intencion("diagnosticar", "estrategia")
```

---

### 5. Monitorea la Clasificación

En modo interactivo:
```
> clasificacion
📊 Clasificación actual:
   Intención: diagnosticar
   Tema: procesos
   Confianza: 0.85
```

En código:
```python
clasificacion = chat.get_clasificacion_actual()
print(f"Intención: {clasificacion['intencion']}")
```

---

## 🎓 Ejercicios Prácticos

### Ejercicio 1: Identifica la Intención

Clasifica estos mensajes:

1. "Tenemos problemas de comunicación entre equipos"
2. "¿Qué opinas de este plan de marketing?"
3. "Enséñame a usar Kanban"
4. "¿Scrum o Kanban para mi equipo?"
5. "Ya implementamos OKRs, ¿qué sigue?"

<details>
<summary>Ver respuestas</summary>

1. DIAGNOSTICAR
2. ANALIZAR_RESULTADO
3. USAR_HERRAMIENTA
4. ELEGIR_HERRAMIENTA
5. RECOMENDACIONES
</details>

---

### Ejercicio 2: Identifica el Tema

Clasifica estos mensajes:

1. "¿Cómo mejoramos nuestra posición en el mercado?"
2. "Nuestro proceso de onboarding es muy lento"
3. "Queremos crear un producto disruptivo"

<details>
<summary>Ver respuestas</summary>

1. ESTRATEGIA (posición en mercado)
2. PROCESOS (optimización de proceso)
3. INNOVACIÓN (producto disruptivo)
</details>

---

## 📚 Recursos Adicionales

- [Ejemplos de Código](ejemplos_uso.py) - Código ejecutable con todos los ejemplos
- [README Principal](README.md) - Documentación general del proyecto
- [Documentación de OpenAI](https://platform.openai.com/docs)

---

## 🆘 Preguntas Frecuentes

**P: ¿Puedo tener múltiples intenciones en un mensaje?**
R: El sistema detecta la intención dominante. Para mejores resultados, separa en mensajes distintos.

**P: ¿La clasificación consume tokens/dinero?**
R: Solo en modo AUTO (usa GPT-3.5-turbo). En modo RÁPIDO es gratis (keywords).

**P: ¿Puedo crear mis propias intenciones?**
R: Sí, puedes extender el código en `intent_classifier.py` agregando nuevas categorías.

**P: ¿Cómo mejoro la precisión de la detección?**
R: Usa modo AUTO y sé específico en tus mensajes. Agrega palabras clave relevantes.

---

**¿Tienes más preguntas?** Abre un issue en el repositorio o consulta el código fuente.
