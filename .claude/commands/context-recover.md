# Context Recovery Command

Recupera el contexto de una sesión previa para continuar desarrollo sin perder información.

## Uso

```
/context-recover
```

## Descripción

Este comando busca automáticamente la sesión más reciente y carga:
- Estado de TodoWrite actual
- Análisis TEP previo
- Decisiones tomadas
- Próximos pasos planificados

## Proceso de Recuperación

### 1. Localizar Sesión Activa

```bash
# Encuentra la sesión más reciente
ls -la .taskmaster/sessions/

# Lee el archivo de sesión
cat .taskmaster/sessions/session-2024-12-25-task-1.json
```

### 2. Verificar Estado del Proyecto

```bash
# Verifica el estado de Task Master
npx task-master show <taskId>

# Verifica el estado de Git
git status
git log --oneline -3
```

### 3. Cargar Contexto Enriquecido

```bash
# Lee el archivo enriquecido asociado
cat .taskmaster/enriched/<taskId>-enriched.json
```

### 4. Restaurar TodoWrite

Basándose en el archivo de sesión, carga los todos en el estado exacto donde se quedaron:
- Todos completados marcados como tal
- Todo actual identificado
- Próximos pasos claros

### 5. Verificar Documentación Context7

Si es necesario, recarga las referencias de documentación:
- Verifica que las librerías Context7 estén disponibles
- Restaura las referencias específicas guardadas

## Output Esperado

```
📋 Contexto Recuperado para Task #1:

✅ Sesión encontrada: session-2024-12-25-task-1.json
✅ TEP analysis cargado: 1-enriched.json  
✅ TodoWrite restaurado: 17 todos, 0 completados
✅ Próximo paso: [TEP:1][Subtask:1.1][TDD:Red] Write test_database_wal_mode_enabled

🎯 Estado actual:
- Task: Setup Project Infrastructure  
- Subtask actual: 1.1 - Database Configuration
- Fase TDD: Red (escribir tests que fallan)
- Documentación: SQLite, FastAPI, React ready

¿Continuar con la implementación?
```

## Beneficios

- **Recuperación instantánea** del contexto completo
- **No hay pérdida** de análisis o decisiones previas  
- **Continuidad perfecta** en el flujo de trabajo
- **Estado sincronizado** entre Claude y archivos

## Casos de Uso

1. **Después de /clear:** Recuperar sesión interrumpida
2. **Nueva sesión diaria:** Retomar trabajo del día anterior
3. **Cambio de contexto:** Alternar entre múltiples tareas
4. **Colaboración:** Otro desarrollador puede cargar el contexto

## Archivos Utilizados

- `.taskmaster/sessions/session-*.json` - Estado de sesión
- `.taskmaster/enriched/<id>-enriched.json` - Análisis TEP
- Task Master `tasks.json` - Estado oficial de tareas
- Git log - Progreso en código

## Ejemplo de Uso

```
Usuario: /context-recover

Claude: [Lee archivos de sesión]
        [Restaura todos]
        [Verifica git status]
        [Carga TEP analysis]

        "📋 Contexto restaurado. Estabas trabajando en Task 1,
        Subtask 1.1 - Database config. Próximo: escribir test
        test_database_wal_mode_enabled. ¿Continuamos?"
```