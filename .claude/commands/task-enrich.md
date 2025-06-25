# Task Enrichment Protocol (TEP)

Analiza y enriquece la tarea actual de Task Master para crear todos más informados y aplicar mejores prácticas de desarrollo.

## Uso

```
/task-enrich
```

## Descripción

Este protocolo analiza profundamente una tarea de Task Master y genera un archivo enriquecido con:
- Análisis de complejidad y tecnologías
- División en subtareas lógicas
- Estructura TDD completa
- Referencias de documentación
- Estrategia de paralelización
- Checkpoints de actualización

## Pasos del Protocolo

### 1. Selección y Análisis de Tarea

```bash
# Obtén la siguiente tarea disponible
npx task-master next
npx task-master show <id>
```

**Analiza:**
- Complejidad estimada (1-10)
- Tecnologías involucradas
- Dependencias con otras tareas
- Criterios de aceptación implícitos

### 2. Evaluación de División en Subtareas

**Criterios de División:**
- Si involucra múltiples capas (DB, Backend, Frontend) → DIVIDIR
- Si cada parte puede tener sus propios tests → DIVIDIR
- Si las partes tienen dependencias claras → DIVIDIR
- Si una parte puede reutilizarse en otra → DIVIDIR

**Estructura de Subtareas:**
```yaml
x.1: Capa de Datos (Database, Models)
x.2: Capa de Lógica (Backend, API)
x.3: Capa de Presentación (Frontend, UI)
x.4: Integración y Testing
```

### 3. Identificación de Documentación Necesaria

Para cada tecnología identificada:
1. Usa `mcp__context7__resolve-library-id` para encontrar la librería
2. Consulta topics específicos: "testing", "setup", "best-practices", "typescript"
3. Guarda referencias específicas para cada subtarea

### 4. Análisis de Paralelización

**Evalúa si las subtareas pueden ejecutarse en paralelo:**
- ¿Hay dependencias fuertes entre ellas?
- ¿Pueden escribirse tests independientes?
- ¿El overhead de coordinación vale la pena?
- ¿Qué información de una subtarea necesita otra?

**Estrategias comunes:**
- Sequential: Una tras otra
- Parallel-after-base: Base primero, resto en paralelo
- Full-parallel: Todas al mismo tiempo con contratos

### 5. Estructura TDD

Para cada subtarea, define:

1. **Failing Tests** - Tests que deben escribirse primero
   - Unit tests para funcionalidad core
   - Integration tests para conexiones
   - Edge cases críticos

2. **Minimal Implementation** - Código mínimo para pasar tests
   - Solo lo necesario para verde
   - Sin optimizaciones prematuras
   - Foco en claridad

3. **Refactoring Goals** - Mejoras post-verde
   - Patterns a aplicar
   - Optimizaciones identificadas
   - Abstracciones necesarias

4. **Integration Points** - Cómo se conecta con otras partes
   - Interfaces/Contratos
   - Dependencias
   - Puntos de prueba

### 6. Crear Archivo de Tarea Enriquecida

**Ubicación:** `.taskmaster/enriched/<task-id>-enriched.json`

**Estructura:**
```json
{
  "taskId": "string",
  "originalTask": { /* task from task-master */ },
  "enrichedAt": "ISO-8601 timestamp",
  "analysis": {
    "complexity": 1-10,
    "estimatedMinutes": number,
    "technologies": ["tech1", "tech2"],
    "recommendedApproach": "sequential|parallel|hybrid"
  },
  "subtasks": [
    {
      "id": "x.y",
      "title": "string",
      "description": "string",
      "technologies": ["tech"],
      "dependencies": ["subtask-ids"],
      "tddStructure": {
        "failingTests": [
          {
            "name": "test_name",
            "description": "what it tests",
            "expectedFailure": "why it should fail initially"
          }
        ],
        "minimalImplementation": {
          "description": "string",
          "keyComponents": ["component1", "component2"],
          "estimatedLines": number
        },
        "refactoringGoals": ["goal1", "goal2"],
        "integrationPoints": ["point1", "point2"]
      },
      "documentation": {
        "library": {
          "contextId": "context7-id",
          "topics": ["topic1", "topic2"],
          "keySnippets": ["snippet-ref"]
        }
      }
    }
  ],
  "parallelization": {
    "possible": boolean,
    "strategy": "sequential|parallel-after-base|full-parallel",
    "subagentTasks": [
      {
        "agentId": "agent-1",
        "subtaskIds": ["1.1", "1.2"],
        "dependencies": []
      }
    ],
    "coordinationPoints": ["checkpoint1", "checkpoint2"]
  },
  "updateStrategy": {
    "checkpointTriggers": ["after-3-todos", "after-subtask-complete"],
    "updateTemplate": "template for task-master update-subtask"
  },
  "todoGenerationGuidance": {
    "groupingStrategy": "by-subtask|by-technology|by-test-cycle",
    "priorityOrder": ["subtask-ids in order"],
    "estimatedTotalTodos": number
  }
}
```

### 7. Generar TodoWrite Informado

Con el archivo enriquecido, genera todos que incluyan:

1. **Referencia al enriquecimiento:** `[TEP:1-enriched.json]`
2. **Fase TDD actual:** `[TDD:Red]`, `[TDD:Green]`, `[TDD:Refactor]`
3. **Subtarea asociada:** `[Subtask:1.1]`
4. **Documentación a consultar:** `[Doc:FastAPI-testing]`
5. **Checkpoint:** `[Checkpoint:after-db-setup]`

**Ejemplo de Todo:**
```
"[TEP:1][Subtask:1.1][TDD:Red] Write test_database_wal_mode_enabled - verify SQLite WAL pragma"
```

## Proceso de Ejecución

1. **Analiza** la tarea actual con `task-master show`
2. **Razona** sobre cada aspecto siguiendo los pasos
3. **Consulta** Context7 para documentación relevante
4. **Crea** el archivo JSON enriquecido
5. **Genera** TodoWrite basados en el enriquecimiento
6. **Referencia** el archivo durante toda la implementación

## Beneficios

- **Todos más informados:** Cada todo sabe exactamente qué hacer
- **Mejor estructura TDD:** Tests definidos antes de empezar
- **Documentación lista:** No hay que buscar durante desarrollo
- **Checkpoints claros:** Sé cuándo actualizar Task Master
- **Recuperación fácil:** El archivo persiste entre sesiones

## Ejemplo de Uso

```
Usuario: /task-enrich

Claude: Analizando Task #1: Setup Project Infrastructure...
        
        ✅ Análisis completado:
        - Complejidad: 8/10
        - Subtareas identificadas: 3
        - Documentación: SQLite, FastAPI, React, TypeScript
        - Estrategia: Database primero, luego Backend/Frontend en paralelo
        
        📄 Archivo creado: .taskmaster/enriched/1-enriched.json
        
        He generado 15 todos optimizados con estructura TDD.
        ¿Comenzamos con la implementación?
```