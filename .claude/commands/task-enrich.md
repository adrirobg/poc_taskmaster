# Task Enrichment Protocol (TEP) v2

Analiza y enriquece la tarea actual de Task Master para crear todos más informados y aplicar mejores prácticas de desarrollo con distribución balanceada.

## Uso

```
/task-enrich
```

## Descripción

Este protocolo mejorado (v2) analiza profundamente una tarea de Task Master y genera un archivo enriquecido con:
- Análisis de complejidad y tecnologías
- División en subtareas lógicas
- Estructura TDD completa (40% máximo de TODOs)
- Referencias de documentación OBLIGATORIAS por subtarea (20% de TODOs)
- Estrategia de paralelización con TODOs explícitos (10% de TODOs)
- Implementación balanceada (20% de TODOs)
- Checkpoints de validación (10% de TODOs)

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

### 6.5. Generar TODOs de Paralelización (NUEVO EN v2)

**OBLIGATORIO:** Si la estrategia de paralelización identifica oportunidades, DEBES generar TODOs explícitos:
- `[Parallel:Launch]` - Para lanzar subagentes
- `[Parallel:Coordinate]` - Para sincronización
- `[Parallel:Merge]` - Para integración de resultados

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
        },
        "mandatoryConsultation": true,
        "consultationTodos": ["[Doc:library] Consult documentation before implementation"]
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
    "estimatedTotalTodos": number,
    "mandatoryDistribution": {
      "TDD": 0.4,
      "Doc": 0.2,
      "Impl": 0.2,
      "Parallel": 0.1,
      "Validate": 0.1
    },
    "mandatoryPerSubtask": ["Doc"]
  }
}
```

### 7. Generar TodoWrite Balanceado (v2)

**DISTRIBUCIÓN OBLIGATORIA:**
- 40% TDD - Test-driven development
- 20% Doc - Consulta de documentación (OBLIGATORIO por subtarea)
- 20% Impl - Implementación pura
- 10% Parallel - Orquestación de subagentes
- 10% Validate - Checkpoints y validación

**Tipos de TODO y formato:**
1. `[TEP:1][TDD:Red]` - Escribir tests que fallan
2. `[TEP:1][Doc:SQLite]` - Consultar documentación ANTES de implementar
3. `[TEP:1][Impl:Core]` - Implementación de funcionalidad
4. `[TEP:1][Parallel:Launch]` - Lanzar subagentes para ejecución paralela
5. `[TEP:1][Validate:Integration]` - Validar y supervisar progreso

**Ejemplos de TODOs v2:**
```
"[TEP:1][Doc:SQLAlchemy] Consult /sqlalchemy/sqlalchemy docs for engine setup patterns"
"[TEP:1][TDD:Red] Write test_database_wal_mode_enabled - verify SQLite WAL pragma"
"[TEP:1][Parallel:Launch] Deploy 3 subagents for DB/Backend/Frontend parallel work"
"[TEP:1][Impl:DB] Implement DatabaseConfig class using Context7 patterns"
"[TEP:1][Validate:Checkpoint] Verify all subtask integrations work together"
```

**REGLAS CRÍTICAS:**
- Cada subtarea DEBE tener al menos 1 TODO [Doc]
- Los TODOs [Doc] deben ejecutarse ANTES que [Impl]
- Si hay paralelización, DEBE haber TODOs [Parallel]
- Mantener distribución 40/20/20/10/10 estrictamente

## Proceso de Ejecución

1. **Analiza** la tarea actual con `task-master show`
2. **Razona** sobre cada aspecto siguiendo los pasos
3. **Consulta** Context7 para documentación relevante
4. **Crea** el archivo JSON enriquecido
5. **Genera** TodoWrite basados en el enriquecimiento
6. **Referencia** el archivo durante toda la implementación

## Beneficios v2

- **Distribución balanceada:** No más dominancia TDD (40% máximo)
- **Documentación obligatoria:** 100% de subtareas con consulta Context7
- **Paralelización ejecutada:** TODOs explícitos para subagentes
- **Mejor estructura TDD:** Tests definidos pero balanceados
- **Checkpoints claros:** Validación continua del progreso
- **Métricas comparables:** Permite análisis TEP v1 vs v2

## Ejemplo de Uso v2

```
Usuario: /task-enrich

Claude: Analizando Task #1: Setup Project Infrastructure con TEP v2...
        
        ✅ Análisis completado:
        - Complejidad: 8/10
        - Subtareas identificadas: 3
        - Documentación: SQLite, FastAPI, React (consulta OBLIGATORIA)
        - Estrategia: sequential-then-parallel con TODOs explícitos
        
        📄 Archivo creado: .taskmaster/enriched/1-enriched.json
        
        📊 Distribución de 20 TODOs generados:
        - TDD: 8 todos (40%)
        - Doc: 4 todos (20%) - OBLIGATORIO por subtarea
        - Impl: 4 todos (20%)
        - Parallel: 2 todos (10%)
        - Validate: 2 todos (10%)
        
        ✅ Validaciones TEP v2:
        - Cada subtarea tiene TODO [Doc] ✓
        - Paralelización con TODOs explícitos ✓
        - Distribución balanceada aplicada ✓
        
        ¿Comenzamos con la implementación?
```