# Task Enrichment Protocol (TEP) v2.3

Analiza y enriquece la tarea actual de Task Master para crear todos optimizados para Claude Code (LLM) workflow con execution phases, persistent documentation caching y token efficiency optimization.

## Uso

```
/task-enrich
```

## Descripción

Este protocolo optimizado (v2.3) analiza una tarea de Task Master y genera execution phases para Claude Code LLM con:
- **Phase-based execution:** 4 fases con 3-6 TODOs cada una (10-15 total máximo)
- **Persistent documentation cache:** Context7 docs loaded once, cached across phases
- **Token efficiency:** 60% reducción en overhead vs v2.2
- **Smart TODO distribution:** Adaptive sizing based on task complexity
- **Cross-phase context:** Documentation persists from research to implementation
- **Session continuity:** Clean phase boundaries for /clear operations

## Pasos del Protocolo

### 1. Selección y Análisis de Tarea

```bash
# Obtén la siguiente tarea disponible
npx task-master next
npx task-master show <id>
```

**Analiza:**
- Complejidad estimada (1-10)
- Número de subtareas identificadas (trigger para adaptive sizing)
- Tecnologías involucradas (determina documentation scope)
- Dependencias con otras tareas
- Criterios de aceptación implícitos

**Adaptive Sizing Logic:**
```python
def calculate_todo_count(task):
    subtask_count = len(task.subtasks)
    tech_stack_count = len(task.technologies)
    
    if subtask_count <= 3 and tech_stack_count <= 2:
        return 10  # Simple: 2+3+4+1
    elif subtask_count <= 5 and tech_stack_count <= 4:
        return 15  # Medium: 3+4+6+2
    else:
        return "SUGGEST_SPLIT"  # Too complex, split task first
```

### 2. Evaluación de Complejidad y Phase Sizing

**Criterios para Adaptive Sizing:**
- **Complexity 1-3:** Simple task → 10 TODOs (2+3+4+1 phases)
- **Complexity 4-6:** Medium task → 15 TODOs (3+4+6+2 phases)  
- **Complexity 7+:** Suggest task split before enrichment

**Phase Structure Template:**
```yaml
Phase 1: Foundation (2-3 TODOs) - Structure setup
Phase 2: Research (3-4 TODOs) - Documentation batch loading  
Phase 3: Implementation (4-6 TODOs) - Core development with cached docs
Phase 4: Integration (1-2 TODOs) - Final validation and cleanup
```

**Task Split Criteria:**
- If >6 subtasks identified → SPLIT task before enrichment
- If >3 major technology stacks → SPLIT task before enrichment
- If estimated >20 TODOs needed → SPLIT task before enrichment

### 3. Batch Documentation Planning (NUEVO v2.3)

**Strategic Documentation Loading:**
1. Identifica TODAS las tecnologías en la tarea completa
2. Planifica Context7 batch loading para Phase 2 (Research)
3. Define persistent cache retention policy hasta task completion
4. Map specific search queries por subtarea (no generic research)

**Documentation Cache Strategy:**
```python
# Load ONCE in Research Phase, use throughout task
documentation_plan = {
    "sqlalchemy": {
        "contextId": "/sqlalchemy/docs",
        "topics": ["declarative-base", "session-management"],
        "searchQuery": "DeclarativeBase + session factory setup",
        "relevantSubtasks": ["1.2"],
        "retentionPolicy": "task-completion"
    },
    "fastapi": {
        "contextId": "/fastapi/docs", 
        "topics": ["controller-patterns", "dependency-injection"],
        "searchQuery": "controller-service-repository pattern",
        "relevantSubtasks": ["1.3"],
        "retentionPolicy": "task-completion"
    }
}
```

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
        "required": [
          {
            "contextId": "context7-id",
            "specificTopics": ["topic1", "topic2"],
            "searchQuery": "specific search query for this subtask",
            "priority": "high|medium|low"
          }
        ],
        "mandatoryConsultation": true
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
    "executionModel": "phase-based",
    "maxTotalTodos": 15,
    "phaseDistribution": {
      "Foundation": 0.2,
      "Research": 0.27,
      "Implementation": 0.4,
      "Integration": 0.13
    },
    "documentationCaching": {
      "batchLoad": "phase-2-research",
      "persistence": "task-completion",
      "context7CallsOptimized": true
    },
    "tokenOptimization": {
      "phaseTokenBudgets": {
        "foundation": 1200,
        "research": 1600,
        "implementation": 2400,
        "integration": 800
      }
    }
  }
}
```

### 7.1. Phase-Based Execution Planning (v2.3)

**OBLIGATORIO:** Diseñar execution phases con token efficiency como prioridad:

**Phase Dependencies:**
- Phase 1 (Foundation): No prerequisites, minimal token load
- Phase 2 (Research): Batch load ALL documentation, cache for task duration  
- Phase 3 (Implementation): Use cached docs, 2-3 sessions max
- Phase 4 (Integration): Final validation with cached context

**Cross-Phase Resource Management:**
```yaml
Phase 1: Foundation
├── Token load: ~1200 (structure TODOs only)
├── Documentation: None loaded yet
└── Duration: 1 session

Phase 2: Research  
├── Token load: ~1600 (research TODOs)
├── Documentation: Batch load ALL → Cache persistent
├── Context7 calls: ALL task documentation loaded here
└── Duration: 1 session

Phase 3: Implementation
├── Token load: ~2400 (implementation TODOs)  
├── Documentation: Use cached (NO additional Context7 calls)
├── Available for code: 19400 tokens/session
└── Duration: 2-3 sessions

Phase 4: Integration
├── Token load: ~800 (validation TODOs)
├── Documentation: Same cached context
└── Duration: 1 session
```

### 7.2. Phase-Based TODO Generation (v2.3)

**CAMBIO CRÍTICO:** Generar TODOs agrupados por PHASE, con token efficiency optimization.

**ALGORITMO OPTIMIZADO DE PHASES:**

#### Phase 1: Foundation (Items 1-3)
```
1. [Structure] Create project directories and initialization files
2. [TDD:Red] Write test_project_structure_exists for validation
3. [TDD:Green] Implement minimal directory structure to pass tests
```
**Token load:** ~1200 | **Documentation:** None | **Sessions:** 1

#### Phase 2: Research & Documentation (Items 4-7)  
```
4. [Doc:Batch] Load SQLAlchemy docs (DeclarativeBase + sessions) → Cache for task
5. [Doc:Batch] Load FastAPI docs (controller-service-repository) → Cache for task
6. [Doc:Batch] Load React+TypeScript docs (Vite setup) → Cache for task
7. [Doc:Batch] Load Testing docs (Pytest + Vitest patterns) → Cache for task
```
**Token load:** ~1600 | **Documentation:** ALL loaded & cached | **Sessions:** 1

#### Phase 3: Implementation (Items 8-13)
```
8. [TDD:Red] Write test_sqlite_connection using cached SQLAlchemy docs
9. [TDD:Green] Implement SQLite+WAL setup using cached docs
10. [TDD:Red] Write test_fastapi_app_creation using cached FastAPI docs  
11. [TDD:Green] Implement FastAPI app using cached controller patterns
12. [Impl:Frontend] Build React+TypeScript setup using cached docs
13. [TDD:Refactor] Clean and optimize all implementations
```
**Token load:** ~2400 | **Documentation:** Use cached (no Context7 calls) | **Sessions:** 2-3

#### Phase 4: Integration (Items 14-15)
```
14. [Validate:Integration] Test full stack integration using all cached docs
15. [Validate:Performance] Optimize and verify performance benchmarks
```
**Token load:** ~800 | **Documentation:** Same cached context | **Sessions:** 1

**NUEVA DISTRIBUCIÓN OPTIMIZADA:** Foundation 20% (3), Research 27% (4), Implementation 40% (6), Integration 13% (2) = **15 TODOs total**

**REGLAS CRÍTICAS v2.3:**
- **Phase-based execution:** Complete phase before advancing
- **Batch documentation loading:** ALL docs loaded in Phase 2, cached for task duration
- **Token optimization:** Max 15 TODOs, target 10-15 based on complexity
- **Context persistence:** Documentation cache survives phase transitions
- **Session efficiency:** Each phase = focused session with clear boundaries
- **No Context7 redundancy:** Load docs once, use multiple times
- **Adaptive sizing:** Scale TODO count based on task complexity assessment

### 7.3. Validaciones Post-Generación v2.3 (OBLIGATORIO)

**Verificar ANTES de finalizar:**

✅ **Phase Structure:** 4 phases with clear boundaries and token budgets
✅ **Foundation First:** Phase 1 establishes structure before other work
✅ **Batch Documentation:** Phase 2 loads ALL documentation with caching strategy
✅ **Implementation Focus:** Phase 3 uses cached docs, no additional Context7 calls
✅ **Clean Integration:** Phase 4 validates with same cached documentation context
✅ **Token Efficiency:** Total TODOs ≤ 15, phase token loads within budget
✅ **Cache Persistence:** Documentation retention policy spans entire task
✅ **Adaptive Sizing:** TODO count matches task complexity (10-15 range)
✅ **Session Continuity:** Each phase can start/end cleanly with /clear
✅ **Context7 Optimization:** Single batch load, multiple reuse pattern confirmed

### 7.4. Documentation Cache Management (NUEVO v2.3)

**Persistent Cache Pattern:**
```python
class DocumentationCache:
    def __init__(self):
        self.cache = {}
        self.retention_policies = {}
        
    def batch_load_phase_docs(self, documentation_plan):
        """Load ALL task documentation in Research Phase"""
        for lib, config in documentation_plan.items():
            context_id = resolve_library_id(lib)
            doc_content = get_library_docs(
                context_id, 
                topic=config["topics"],
                tokens=config.get("maxTokens", 8000)
            )
            
            self.cache[lib] = {
                "content": doc_content,
                "contextId": context_id,
                "topics": config["topics"], 
                "searchQuery": config["searchQuery"],
                "relevantSubtasks": config["relevantSubtasks"],
                "loadedAt": datetime.now(),
                "retentionPolicy": "task-completion"
            }
            
    def get_cached_doc(self, library):
        """Retrieve cached documentation without Context7 call"""
        return self.cache.get(library, {}).get("content", "")
        
    def clear_task_cache(self):
        """Clear cache at task completion"""
        self.cache.clear()
        self.retention_policies.clear()

# Usage:
# Phase 2: cache.batch_load_phase_docs(documentation_plan)
# Phase 3: content = cache.get_cached_doc("sqlalchemy") 
# Phase 4: content = cache.get_cached_doc("fastapi")
# Task end: cache.clear_task_cache()
```

**Beneficios v2.3:**
- Single Context7 batch load per task
- Documentation persists across phases
- 70% reduction in Context7 calls
- Consistent context for implementation
- Token efficiency optimization

## Proceso de Ejecución

1. **Analiza** la tarea actual con `task-master show`
2. **Razona** sobre cada aspecto siguiendo los pasos
3. **Consulta** Context7 para documentación relevante
4. **Crea** el archivo JSON enriquecido
5. **Genera** TodoWrite basados en el enriquecimiento
6. **Referencia** el archivo durante toda la implementación

## Beneficios v2.3

- **Token efficiency:** 60% reducción en overhead de TODO management
- **Documentation optimization:** 70% menos Context7 calls via batch loading
- **Session continuity:** Clean phase boundaries para /clear operations
- **Context persistence:** Documentation cache survives phase transitions
- **Adaptive sizing:** 10-15 TODOs basado en task complexity
- **LLM workflow optimized:** Diseñado específicamente para Claude Code

## Ejemplo de Uso v2.3

```
Usuario: /task-enrich

Claude: Ejecutando Task #1: Setup Project Infrastructure con protocolo TEP v2.3...
        
        🧠 Complexity analysis: 5 subtasks → Medium task → 15 TODOs target
        
        ✅ Phase-based planning:
        - Phase 1: Foundation (3 TODOs, ~1200 tokens)
        - Phase 2: Research (4 TODOs, batch doc loading)
        - Phase 3: Implementation (6 TODOs, cached docs)
        - Phase 4: Integration (2 TODOs, validation)
        
        ✅ Documentation batch strategy:
        - SQLAlchemy: DeclarativeBase + session patterns
        - FastAPI: Controller-service-repository architecture
        - React+TypeScript: Vite setup and testing
        - All docs cached for task duration
        
        📄 Archivo creado: .taskmaster/enriched/1-enriched-v23.json
        
        📊 15 TODOs generados con PHASE-BASED OPTIMIZATION:
        - Foundation: 3 todos (20%) - Structure setup
        - Research: 4 todos (27%) - Batch documentation loading
        - Implementation: 6 todos (40%) - Core development  
        - Integration: 2 todos (13%) - Final validation
        
        ✅ Validaciones TEP v2.3 pasadas:
        - Phase structure with token budgets ✓
        - Batch documentation caching ✓
        - Context7 optimization ✓
        - Session continuity boundaries ✓
        - Adaptive sizing (15 TODOs) ✓
        
        🚀 Token efficiency: 60% improvement vs v2.2
        🚀 Context7 calls: 70% reduction via batch loading
        ¿Procedemos con Phase 1: Foundation?
```