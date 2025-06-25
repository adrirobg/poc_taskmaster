# Task Enrichment Protocol (TEP) v2.1

Analiza y enriquece la tarea actual de Task Master para crear todos más informados y aplicar mejores prácticas de desarrollo con distribución balanceada y ordenamiento por flujo de ejecución.

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

### 7.1. Análisis de Dependencias (NUEVO v2.1)

**OBLIGATORIO:** Mapear dependencias entre subtareas y TODOs antes de generar la lista:

**Dependencias Técnicas:**
- Structure TODOs no requieren prerequisites
- TDD TODOs requieren structure correspondiente creada
- Doc TODOs deben preceder a Impl de la misma subtarea
- Parallel TODOs requieren foundation (structure + tests básicos)
- Backend subtareas dependen de Database subtareas completadas

**Dependencias Entre Subtareas:**
```yaml
1.1 (Structure): Sin dependencias
1.2 (Database): Depende de 1.1
1.3 (Backend): Depende de 1.1 + 1.2  
1.4 (Frontend): Depende solo de 1.1
1.5 (DevEnv): Depende de 1.1 + 1.2 + 1.3 + 1.4
```

**Oportunidades de Paralelización:**
- Database (1.2) + Frontend (1.4) pueden ejecutarse en paralelo
- Backend (1.3) debe esperar a Database (1.2)
- Integration requiere todos los componentes

### 7.2. Generar TodoWrite con Flujo Optimizado (v2.1)

**CAMBIO CRÍTICO:** Generar TODOs en orden de EJECUCIÓN, no por categoría.

**ALGORITMO OBLIGATORIO DE ORDENAMIENTO:**

#### Phase 1: Foundation (Items 1-3)
```
1. [Impl:Structure] Create project directories and initialization files
2. [TDD:Red] Write test_project_structure_exists for directory validation  
3. [TDD:Green] Implement minimal directory structure to pass tests
```

#### Phase 2: Research (Items 4-9)
```
4. [Doc:SQLAlchemy] Search /sqlalchemy/sqlalchemy for DeclarativeBase patterns
5. [Doc:FastAPI] Search /tiangolo/fastapi for controller-service-repository
6. [Doc:React] Search /reactjs/react.dev for TypeScript + Vite setup
7. [Doc:SQLite] Research SQLite WAL mode and FTS5 configuration
8. [Doc:Pytest] Search pytest docs for database testing fixtures
9. [Doc:Vitest] Search vitest docs for React + TypeScript testing
```

#### Phase 3: Parallel Launch (Item 10)
```
10. [Parallel:Launch] Deploy 2 subagents for parallel DB setup (1.2) and React frontend (1.4)
```

#### Phase 3a: Database Track - Subagent 1 (Items 11-15)
```
11. [TDD:Red] Write test_sqlite_connection and test_wal_mode_enabled
12. [TDD:Red] Write test_sqlalchemy_engine_creation with proper session factory
13. [TDD:Green] Implement SQLite connection with WAL mode
14. [Impl:Database] Implement SQLAlchemy models and database config
15. [TDD:Refactor] Clean up database configuration code
```

#### Phase 3b: Frontend Track - Subagent 2 (Items 16-20)
```
16. [TDD:Red] Write test_react_app_renders with TypeScript compilation check
17. [TDD:Green] Implement React app with TypeScript
18. [Impl:Frontend] Setup React with Vite and TypeScript configuration
19. [TDD:Refactor] Enhance React component organization
20. [Parallel:Coordinate] Synchronize frontend track with database completion
```

#### Phase 4: Backend Sequential (Items 21-25)
```
21. [Parallel:Merge] Integrate results from Database + Frontend parallel tracks
22. [TDD:Red] Write test_fastapi_app_creation and test_health_endpoint
23. [TDD:Green] Implement FastAPI app initialization
24. [Impl:Backend] Build FastAPI app with controller-service-repository pattern
25. [TDD:Refactor] Optimize FastAPI project structure
```

#### Phase 5: Integration & Validation (Items 26-30)
```
26. [Impl:DevEnv] Configure development tools and pre-commit hooks
27. [Impl:Integration] Connect all components and verify integration
28. [Validate:Performance] Check SQLite WAL mode performance with 64MB cache
29. [Validate:Architecture] Verify controller-service-repository pattern compliance
30. [Validate:Integration] Test full stack integration with sample CRUD operation
```

**DISTRIBUCIÓN MANTENIDA:** 40% TDD (12), 20% Doc (6), 20% Impl (6), 10% Parallel (3), 10% Validate (3)

**REGLAS CRÍTICAS v2.1:**
- Foundation ANTES que cualquier test o implementación
- Documentation ANTES que implementación de cada subtarea
- Parallel Launch DESPUÉS de foundation pero ANTES de implementation
- Database track COMPLETO antes de Backend (dependency respected)
- Frontend track puede ejecutar EN PARALELO con Database
- Integration y Validation AL FINAL
- Distribución 40/20/20/10/10 MANTENIDA estrictamente

### 7.3. Validaciones Post-Generación (OBLIGATORIO)

**Verificar ANTES de finalizar:**

✅ **Foundation First:** Items 1-3 son [Impl:Structure] + [TDD] de structure
✅ **Research Phase:** Items 4-9 son todos [Doc:*] para cada tecnología
✅ **Parallel Launch:** Item 10 es [Parallel:Launch] después de foundation
✅ **Database Track:** Items 11-15 completamente sobre database antes de backend
✅ **Frontend Track:** Items 16-20 pueden ejecutar en paralelo con database
✅ **Backend Sequential:** Items 21-25 vienen después de database completion
✅ **Integration Final:** Items 26-30 son integration y validation
✅ **Distribution Check:** 12 TDD + 6 Doc + 6 Impl + 3 Parallel + 3 Validate = 30
✅ **Dependency Respect:** Cada TODO puede ejecutarse cuando llega su turno
✅ **Doc Before Impl:** Para cada subtarea, [Doc] precede a [Impl]

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

## Ejemplo de Uso v2.1

```
Usuario: /task-enrich

Claude: Ejecutando Task #1: Setup Project Infrastructure con protocolo TEP v2.1...
        
        ✅ Paso 7.1 - Análisis de dependencias:
        - Subtareas: 1.1→1.2→1.3, 1.1→1.4, 1.5 requiere todas
        - Paralelización: 1.2 (Database) + 1.4 (Frontend) en paralelo
        - Backend 1.3 depende de Database 1.2 completada
        
        ✅ Paso 7.2 - Algoritmo de ordenamiento aplicado:
        - Phase 1: Foundation (items 1-3)
        - Phase 2: Research (items 4-9) 
        - Phase 3: Parallel Launch (item 10)
        - Phase 3a+3b: Database + Frontend tracks (items 11-20)
        - Phase 4: Backend Sequential (items 21-25)
        - Phase 5: Integration & Validation (items 26-30)
        
        📄 Archivo creado: .taskmaster/enriched/1-enriched.json
        
        📊 30 TODOs generados en ORDEN DE EJECUCIÓN:
        - TDD: 12 todos (40%) - distribuidos por fase
        - Doc: 6 todos (20%) - Research phase (items 4-9)
        - Impl: 6 todos (20%) - distribuidos por track
        - Parallel: 3 todos (10%) - Launch/Coordinate/Merge
        - Validate: 3 todos (10%) - Final phase (items 28-30)
        
        ✅ Validaciones TEP v2.1 pasadas:
        - Foundation antes que tests ✓
        - Documentation antes que implementation ✓
        - Paralelización temprana (item 10) ✓
        - Database track completo antes de Backend ✓
        - Distribución 40/20/20/10/10 mantenida ✓
        
        🚀 Tiempo estimado: 2.5h (vs 4h secuencial)
        ¿Procedemos con ejecución optimizada?
```