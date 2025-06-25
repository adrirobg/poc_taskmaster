# Session Save Command

Guarda el contexto actual completo antes de /clear para poder recuperarlo después.

## Uso

```
/session-save
```

## Descripción

Este comando crea un archivo de sesión que preserva:
- Estado actual de TodoWrite
- Decisiones de análisis tomadas
- Referencias TEP y archivos enriquecidos
- Próximos pasos planificados
- Información del workspace (git status, archivos modificados)

## Cuándo Usar

- **Antes de /clear:** Preservar contexto cuando se alcanza límite
- **Al finalizar sesión:** Guardar progreso para continuar mañana
- **Antes de cambiar tareas:** Preservar estado de tarea actual
- **Checkpoint importante:** Guardar estado tras análisis complejo

## Proceso de Guardado

### 1. Detectar Contexto Actual

```bash
# Identifica la tarea activa en Task Master
npx task-master next
npx task-master show <currentTaskId>

# Verifica estado del workspace
git status
git log --oneline -3
```

### 2. Capturar Estado TodoWrite

- Lista completa de todos actuales
- Índice del todo en progreso
- Contador de todos completados
- Estado de cada todo (pending/in-progress/completed)

### 3. Referenciar Archivos TEP

- Archivo enriquecido asociado (si existe)
- Análisis previos realizados
- Decisiones de arquitectura tomadas

### 4. Documentar Decisiones

- Estrategia de paralelización elegida
- Enfoque TDD decidido
- Fuentes de documentación identificadas
- Orden de implementación planificado

### 5. Crear Archivo de Sesión

**Ubicación:** `.taskmaster/sessions/session-<timestamp>-task-<id>.json`

**Contenido:**
```json
{
  "sessionId": "session-YYYY-MM-DD-HH:MM",
  "savedAt": "ISO-8601 timestamp",
  "taskContext": {
    "currentTaskId": "string",
    "taskTitle": "string", 
    "enrichedFile": "path|null",
    "status": "analysis-complete|implementation-started|blocked"
  },
  "workspaceState": {
    "gitBranch": "current-branch",
    "gitStatus": "git status output",
    "modifiedFiles": ["list of files"],
    "lastCommit": "commit hash and message"
  },
  "todoState": {
    "todos": [
      {
        "id": "string",
        "content": "todo description with prefixes",
        "status": "pending|in-progress|completed",
        "completedAt": "timestamp|null"
      }
    ],
    "currentTodoIndex": number,
    "completedCount": number,
    "estimatedRemaining": number
  },
  "decisions": {
    "parallelizationStrategy": "sequential|parallel|hybrid",
    "subtaskOrder": ["ordered list"],
    "tddApproach": "strict|flexible|test-after",
    "documentationSources": {
      "library": "context7-id"
    }
  },
  "progress": {
    "timeElapsed": "minutes since start",
    "estimatedRemaining": "minutes to completion",
    "blockers": ["current blockers"],
    "achievements": ["completed milestones"]
  },
  "nextSteps": [
    "immediate next action",
    "follow-up tasks",
    "integration points to verify"
  ],
  "recoveryInstructions": "specific instructions for /context-recover"
}
```

## Output del Comando

```
💾 Guardando sesión actual...

✅ Contexto capturado:
- Task: #1 - Setup Project Infrastructure
- TodoWrite: 17 todos (3 completados, 14 pendientes)  
- TEP analysis: .taskmaster/enriched/1-enriched.json
- Git status: 2 modified files
- Decisiones: TDD estricto, parallelización hybrid

📄 Sesión guardada: .taskmaster/sessions/session-2024-12-25-16:45-task-1.json

🎯 Para recuperar después de /clear:
   Usa: /context-recover

⚠️  Recuerda hacer commit de cambios importantes antes de /clear
```

## Verificaciones Previas

Antes de guardar, el comando verifica:

1. **TodoWrite activos:** ¿Hay todos en memoria?
2. **TEP analysis:** ¿Existe archivo enriquecido?
3. **Task Master state:** ¿Cuál es la tarea actual?
4. **Git clean:** ¿Hay cambios sin commitear?
5. **Directorio sessions:** ¿Existe la estructura?

## Mejores Prácticas

### Antes de Guardar
```bash
# Commit cambios importantes
git add -A && git commit -m "WIP: progress checkpoint"

# Actualizar Task Master si es necesario
task-master update-subtask --id=X --prompt="current progress"
```

### Nombramiento de Sesiones
- **Automático:** `session-YYYY-MM-DD-HH:MM-task-<id>`
- **Descriptivo:** Include task number and status
- **Único:** Timestamp prevents conflicts

### Limpieza de Sesiones
```bash
# Limpiar sesiones antiguas (opcional)
find .taskmaster/sessions -name "*.json" -mtime +7 -delete
```

## Integración con Context Recovery

La sesión guardada debe ser compatible con `/context-recover`:
- **Formato estándar** para facilitar parsing
- **Información completa** para recuperación sin pérdida
- **Referencias válidas** a archivos TEP y Task Master
- **Instrucciones claras** para retomar el trabajo

## Casos de Uso Específicos

### 1. Análisis Largo Completado
```
Usuario: He terminado el análisis TEP, necesito /clear
Claude: /session-save
         "Sesión guardada. Análisis TEP preservado para implementación."
Usuario: /clear
```

### 2. Implementación a Medias
```
Usuario: Voy a tomar un descanso, guarda el progreso
Claude: /session-save
         "17 todos preservados, 5 completados. Estado listo para recuperar."
```

### 3. Cambio de Contexto
```
Usuario: Necesito cambiar a otra tarea urgente
Claude: /session-save
         "Contexto de Task 1 guardado. Puedes usar /context-recover después."
```

## Seguridad y Backup

- **No incluir** API keys o secretos
- **Referencias relativas** a archivos del proyecto
- **Backup automático** en git (si sessions/ está en .gitignore)
- **Compresión** para sesiones muy grandes (futuro enhancement)

---

**Objetivo:** Nunca perder progreso por límites de contexto.