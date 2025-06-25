# TEP v2.1 Protocol Modifications - Dependency-Aware TODO Ordering

## 🎯 Problema Identificado

El protocolo TEP v2 genera TODOs agrupados por **tipo** (TDD, Doc, Impl, etc.) en lugar de por **flujo de ejecución**, resultando en:

- Documentation antes de structure
- Tests antes de directories
- Paralelización tardía
- Dependencias ignoradas

## 🔧 Modificaciones Requeridas

### 1. Nuevo Paso 7.1: Análisis de Dependencias

```markdown
### 7.1. Análisis de Dependencias (NUEVO)

**Identificar prerequisitos de cada TODO:**
- Structure TODOs no tienen dependencias
- TDD TODOs dependen de structure correspondiente
- Doc TODOs deben preceder a Impl de la misma subtarea
- Parallel TODOs requieren foundation completa
- Backend TODOs dependen de Database TODOs

**Mapear dependencias entre subtareas:**
- Database (1.2) depende de Structure (1.1)
- Backend (1.3) depende de Database (1.2) + Structure (1.1)
- Frontend (1.4) depende solo de Structure (1.1)
- DevEnv (1.5) depende de todas las anteriores
```

### 2. Modificar Paso 7.2: Algoritmo de Ordenamiento

```markdown
### 7.2. Generar TodoWrite con Flujo Optimizado (v2.1)

**ALGORITMO DE ORDENAMIENTO OBLIGATORIO:**

1. **Foundation Phase**
   - [Impl:Structure] Create base directories
   - [TDD:Red] + [TDD:Green] Test structure exists

2. **Research Phase**  
   - [Doc:*] Research ALL technologies antes de implementar

3. **Parallel Launch Phase**
   - [Parallel:Launch] Deploy subagents APENAS foundation esté lista

4. **Parallel Execution Tracks**
   - Track A (Database): [TDD:Red/Green] + [Impl:Database] 
   - Track B (Frontend): [TDD:Red/Green] + [Impl:Frontend]

5. **Sequential Backend Phase**
   - [TDD:Red/Green] + [Impl:Backend] (requiere Database)

6. **Integration Phase**
   - [Parallel:Merge] + [Impl:Integration] + [Validate:*]

**DISTRIBUCIÓN MANTENIDA:** 40/20/20/10/10
```

### 3. Template de Generación Explícito

```markdown
**TEMPLATE OBLIGATORIO DE ORDENAMIENTO:**

# Phase 1: Foundation (Items 1-3)
1. [Impl:Structure] Create project directories
2. [TDD:Red] Write test_project_structure_exists  
3. [TDD:Green] Implement minimal directory structure

# Phase 2: Research (Items 4-9)
4. [Doc:SQLAlchemy] Search DeclarativeBase patterns
5. [Doc:FastAPI] Search controller-service-repository
6. [Doc:React] Search TypeScript + Vite setup
7. [Doc:SQLite] Research WAL mode configuration
8. [Doc:Pytest] Search database testing fixtures
9. [Doc:Vitest] Search React testing setup

# Phase 3: Parallel Launch (Item 10)
10. [Parallel:Launch] Deploy 2 subagents for DB(1.2) + Frontend(1.4)

# Phase 3a: Database Track - Subagent 1 (Items 11-15)
11. [TDD:Red] Write test_sqlite_connection + test_wal_mode
12. [TDD:Red] Write test_sqlalchemy_engine_creation  
13. [TDD:Green] Implement SQLite connection with WAL
14. [Impl:Database] Implement SQLAlchemy models
15. [TDD:Refactor] Clean up database configuration

# Phase 3b: Frontend Track - Subagent 2 (Items 16-20)  
16. [TDD:Red] Write test_react_app_renders
17. [TDD:Green] Implement React app with TypeScript
18. [Impl:Frontend] Setup React with Vite configuration
19. [TDD:Refactor] Enhance React component organization
20. [Parallel:Coordinate] Sync frontend with other tracks

# Phase 4: Backend Sequential (Items 21-25)
21. [Parallel:Merge] Integrate Database + Frontend results
22. [TDD:Red] Write test_fastapi_app_creation + test_health
23. [TDD:Green] Implement FastAPI app initialization
24. [Impl:Backend] Build FastAPI with controller-service-repository
25. [TDD:Refactor] Optimize FastAPI project structure

# Phase 5: Integration & Validation (Items 26-30)
26. [Impl:DevEnv] Configure development tools
27. [Impl:Integration] Connect all components
28. [Validate:Performance] Check SQLite WAL performance
29. [Validate:Architecture] Verify controller-service-repository
30. [Validate:Integration] Test full stack CRUD operation
```

### 4. Validaciones Post-Generación

```markdown
**VALIDACIONES OBLIGATORIAS:**

✅ Foundation TODOs (Impl:Structure + TDD structure) están primero (items 1-3)
✅ Documentation TODOs preceden a implementación de cada subtarea
✅ Parallel:Launch está después de foundation pero antes de implementation
✅ Database track completo antes de Backend (dependency respected)
✅ Frontend track puede ejecutar en paralelo con Database
✅ Integration y Validation al final
✅ Distribución 40/20/20/10/10 mantenida
✅ Cada subtarea tiene Doc TODO antes de Impl TODO
```

### 5. Modificaciones al Archivo de Comando

**En `.claude/commands/task-enrich.md`, cambiar:**

```markdown
### 7. Generar TodoWrite con Flujo Optimizado (v2.1)

**CAMBIO CRÍTICO:** Generar TODOs en orden de EJECUCIÓN, no por categoría.

**ALGORITMO OBLIGATORIO:**
1. Analizar dependencias entre subtareas
2. Calcular orden topológico de ejecución  
3. Insertar Parallel:Launch en momento óptimo
4. Mantener agrupación por track paralelo
5. Preservar distribución 40/20/20/10/10

**REGLAS DE DEPENDENCIAS:**
- Structure antes que TDD de structure
- Doc antes que Impl para cada subtarea  
- Database antes que Backend
- Parallel:Launch después de foundation
- Integration y Validation al final

**SALIDA:** Lista de 30 TODOs ordenados por flujo de ejecución óptimo
```

### 6. Ejemplo Comparativo

**❌ TEP v2 Actual (por categoría):**
```
1-6: [Doc:*] (todos juntos)
7-18: [TDD:*] (todos juntos)  
19-21: [Parallel:*] (muy tarde)
22-27: [Impl:*] (desconectados)
28-30: [Validate:*]
```

**✅ TEP v2.1 Propuesto (por flujo):**
```
1-3: Foundation (Impl:Structure + TDD structure)
4-9: Research (Doc:* for all techs)
10: Parallel Launch
11-15: Database Track (TDD+Impl database)
16-20: Frontend Track (TDD+Impl frontend)  
21-25: Backend Sequential (TDD+Impl backend)
26-30: Integration & Validation
```

## 🎯 Resultado Esperado

Con estas modificaciones, el protocolo TEP v2.1 generará automáticamente TODOs en orden de ejecución óptimo, respetando:

1. **Dependencias técnicas** (structure antes que tests)
2. **Flujo de información** (doc antes que implementación)
3. **Oportunidades de paralelización** (launch temprano)
4. **Agrupación lógica** (por track cuando es paralelo)
5. **Distribución balanceada** (40/20/20/10/10 mantenida)