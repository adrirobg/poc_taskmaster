# ULTRATHINK: Análisis de Estrategias de Documentación

## 🎯 Problema Real Identificado

**NO es obsolescencia de docs**, sino **relevancia específica**:
- ❌ Buscar documentación genérica muy temprano
- ❌ No saber QUÉ partes específicas necesitamos
- ❌ Subagents pierden tiempo filtrando información irrelevante
- ❌ Context pollution por docs no relacionadas a la subtarea

## 📊 Análisis de Estrategias

### Estrategia A: Research Temprano + MD File
```
TEP Planning:
1. Buscar TODA la documentación
2. Generar .md con snippets genéricos
3. Subagents referencian secciones

Problems:
❌ No sabemos qué snippets serán útiles
❌ Desperdicio de tokens en research masivo
❌ Snippets pueden no cubrir necesidades específicas
❌ Subagents aún necesitan filtrar información
❌ File .md se vuelve un knowledge dump inútil
```

### Estrategia B: Just-in-Time Research (Current v2.1)
```
TEP Planning: Solo Context IDs
Execution: Cada subagent busca lo que necesita

Problems:
❌ Duplicación de búsquedas
❌ Subagents buscan sin contexto de qué necesitan
❌ Ineficiencia por búsquedas paralelas similares
```

### Estrategia C: Task-Specific Research (OPTIMAL)
```
TEP Planning: Mapear QUÉ docs necesita cada subtarea
Execution: Búsqueda dirigida por subtarea específica

Benefits:
✅ Research dirigido a necesidades específicas
✅ No duplicación de esfuerzo
✅ Context optimization per subagent
✅ Tokens usados eficientemente
```

## 🔧 Estrategia Óptima: Task-Specific Research

### TEP v2.2 Optimizado

#### Phase 2: Task-Specific Documentation Mapping
```
4. [Doc:SQLAlchemy-Database] Map DeclarativeBase + session management for subtask 1.2
5. [Doc:FastAPI-Backend] Map controller-service-repository for subtask 1.3
6. [Doc:React-Frontend] Map TypeScript + Vite setup for subtask 1.4
7. [Doc:Pytest-Database] Map database testing fixtures for subtask 1.2
8. [Doc:Vitest-Frontend] Map React testing patterns for subtask 1.4
```

#### Enriched.json con Mapeo Específico
```json
{
  "subtasks": [
    {
      "id": "1.2",
      "title": "Database Setup",
      "documentation": {
        "required": [
          {
            "contextId": "/sqlalchemy/sqlalchemy",
            "specificTopics": ["DeclarativeBase", "create_engine", "sessionmaker"],
            "searchQuery": "SQLite engine setup with WAL mode",
            "priority": "high"
          },
          {
            "contextId": "/pytest/docs", 
            "specificTopics": ["fixtures", "database testing"],
            "searchQuery": "pytest database fixtures with SQLAlchemy",
            "priority": "medium"
          }
        ]
      }
    },
    {
      "id": "1.3", 
      "title": "FastAPI Backend",
      "documentation": {
        "required": [
          {
            "contextId": "/tiangolo/fastapi",
            "specificTopics": ["project structure", "dependency injection"],
            "searchQuery": "controller-service-repository pattern FastAPI",
            "priority": "high"
          }
        ]
      }
    }
  ]
}
```

#### Subagent Deployment con Research Dirigido
```python
Task(f"""
Database Implementation Subagent (Track A):

DIRECTED RESEARCH (use specific queries):
1. Search /sqlalchemy/sqlalchemy for: "DeclarativeBase SQLite engine WAL mode"
2. Search /pytest/docs for: "database testing fixtures SQLAlchemy"
3. STOP - no other documentation needed

IMPLEMENT with focused context:
- Apply SQLAlchemy DeclarativeBase patterns
- Configure SQLite with WAL mode  
- Create pytest fixtures for database testing

Research Queries: {subtask['documentation']['required']}
""")
```

### Comparación de Estrategias

| Aspecto | A: Research+MD | B: Just-in-Time | C: Task-Specific |
|---------|----------------|------------------|------------------|
| Token Efficiency | ❌ Muy bajo | ⚠️ Medio | ✅ Alto |
| Context Relevance | ❌ Genérico | ⚠️ Amplio | ✅ Específico |
| Duplicación | ❌ Alta | ⚠️ Media | ✅ Mínima |
| Implementation Quality | ❌ Filtrado manual | ⚠️ Búsqueda ciega | ✅ Dirigida |
| Maintenance | ❌ .md se vuelve obsoleto | ✅ Siempre fresco | ✅ Siempre fresco |

## 🎯 Conclusión

**Estrategia C (Task-Specific) es óptima porque:**

1. **Mapea necesidades específicas** durante planning
2. **Subagents buscan solo lo que necesitan** 
3. **Research dirigido** por queries específicas
4. **No duplicación** de esfuerzo entre subagents
5. **Context pollution mínimo**

### Implementación Inmediata

1. **TEP Planning**: Mapear qué docs específicas necesita cada subtarea
2. **Enriched.json**: Include specific search queries per subtask
3. **Subagent prompts**: Research dirigido con queries precisas
4. **Execution**: Cada subagent busca SOLO lo que su subtarea requiere

**El problema NO es obsolescencia, sino RELEVANCIA específica.**