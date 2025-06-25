# ULTRATHINK: Análisis del Flujo de Documentación en TEP

## 🔍 Problema Identificado

**Desperdicio de recursos:** El protocolo TEP v2.1 busca documentación Context7 durante la **generación del enriched.json** (paso de planning), cuando debería buscarla **justo antes de la implementación** (paso de execution).

## 📊 Análisis del Flujo Actual (INEFICIENTE)

```
TEP Enrichment Phase:
1. Buscar Context7 docs (consume tokens)
2. Almacenar en enriched.json 
3. Archivo queda estático por horas/días
4. Subagentes usan docs potencialmente obsoletas

Problems:
❌ Docs buscadas muy temprano
❌ Información desactualizada en tiempo de uso
❌ Tokens desperdiciados en planning phase
❌ Subagentes no aprovechan contexto fresco
```

## 🎯 Flujo Optimizado Propuesto

### Phase 1: Enrichment (Solo IDs de librerías)
```
TEP v2.2:
1. Resolver library IDs con Context7
2. Almacenar SOLO IDs en enriched.json
3. NO buscar contenido documental
4. Preparar roadmap de qué docs consultar

Output: {"contextIds": ["/sqlalchemy/sqlalchemy", "/tiangolo/fastapi"]}
```

### Phase 2: Execution (Búsqueda Just-in-Time)
```
Subagent Deployment:
1. Leer enriched.json para obtener contextIds
2. Cada subagent busca docs específicas ANTES de coding
3. Contexto fresco + tokens optimizados por subagent
4. Mejor utilización de capacidad de tokens

Benefits:
✅ Docs actualizadas al momento de uso
✅ Subagents con contexto focused
✅ Tokens optimizados por tarea
✅ Paralelización real del research
```

## 📋 Modificaciones Requeridas al TEP

### Cambio en Paso 2: Research Phase
```markdown
#### Phase 2: Context ID Resolution (Items 4-9)
4. [Doc:SQLAlchemy] Resolve /sqlalchemy/sqlalchemy contextId
5. [Doc:FastAPI] Resolve /tiangolo/fastapi contextId  
6. [Doc:React] Resolve /reactjs/react.dev contextId
7. [Doc:SQLite] Identify SQLite documentation sources
8. [Doc:Pytest] Resolve pytest documentation contextId
9. [Doc:Vitest] Resolve vitest documentation contextId
```

### Estructura Enriched.json Optimizada
```json
{
  "taskId": 1,
  "analysis": {...},
  "subtasks": [
    {
      "id": "1.2",
      "documentation": {
        "contextIds": ["/sqlalchemy/sqlalchemy"],
        "topics": ["engine-setup", "session-management"],
        "searchTodos": [
          "[Doc:SQLAlchemy] Search DeclarativeBase patterns before implementing database models"
        ]
      }
    }
  ]
}
```

### Nuevo Patrón de Subagent con Research
```python
# Main Agent deploys with context preparation
Task("""
You are Database Implementation Subagent using Sonnet 4.

BEFORE implementing code:
1. Search Context7: /sqlalchemy/sqlalchemy for "DeclarativeBase" and "engine setup"
2. Search Context7: /sqlalchemy/sqlalchemy for "session management" patterns
3. Study examples for SQLite + SQLAlchemy integration

THEN implement:
- Database configuration with WAL mode
- SQLAlchemy models following Context7 patterns
- Session factory with proper lifecycle

Use fresh documentation context for implementation decisions.
""")
```

## ⚡ Beneficios del Flujo Optimizado

### 1. Token Efficiency
```
Current TEP v2.1:
- Main agent: 20k tokens searching all docs
- Subagents: Use stale cached info
- Total: 20k + (3 × 45k) = 155k tokens

Optimized TEP v2.2:
- Main agent: 5k tokens resolving IDs
- Each subagent: 10k tokens focused search + 45k implementation
- Total: 5k + (3 × 55k) = 170k tokens
- Net: +15k tokens BUT fresh context per subagent
```

### 2. Information Freshness
```
Current: Docs searched once, stale by execution time
Optimized: Docs searched just-in-time per subagent
```

### 3. True Parallelization
```
Current: Sequential doc search, then parallel implementation
Optimized: Parallel doc search + implementation per track
```

### 4. Context Optimization (per subagent_parallelization_patterns.md)
```
"Subagents need 70% less context than main agent"
"Extract only task-relevant context"

Implementation:
- Each subagent searches ONLY its needed docs
- Database subagent: Only SQLAlchemy + SQLite docs  
- Frontend subagent: Only React + Vitest docs
- Backend subagent: Only FastAPI + Pytest docs
```

## 🔧 Implementación Inmediata

### Modificar TEP v2.1 → v2.2:

1. **Phase 2 Research** → **Phase 2 Context ID Resolution**
2. **Enriched.json** almacena IDs, no contenido
3. **Subagent prompts** incluyen búsqueda Context7 ANTES de coding
4. **Just-in-time documentation** por cada subagent

### Template de Subagent Mejorado:
```python
Task(f"""
Database Implementation Subagent (Track A):

RESEARCH FIRST (use your own token context):
- Search {contextId_sqlalchemy} for DeclarativeBase setup patterns
- Search {contextId_sqlite} for WAL mode configuration  
- Find examples of SQLAlchemy + SQLite integration

IMPLEMENT SECOND:
- Apply fresh documentation patterns to code
- Create database configuration following latest practices
- Report implementation with documentation references used

Context Ids: {enriched_data['subtasks'][0]['documentation']['contextIds']}
""")
```

## 🎯 Conclusión

**El flujo actual es ineficiente porque busca docs demasiado temprano.**

**La optimización requiere:**
1. TEP busca solo IDs de librerías
2. Subagents buscan docs just-in-time
3. Cada subagent usa contexto fresco y focused
4. Verdadera paralelización del research + implementation

**Resultado:** Mejor calidad de código con documentación actualizada + utilización optimizada de tokens por subagent.