# Task Enrichment Protocol (TEP)

## Overview
Protocol for transforming Task Master tasks into detailed implementation plans with TDD structure, documentation references, and parallelization strategies.

## Commands

### `/task-enrich`
Analyzes current task following 7-step protocol:
1. Complexity analysis (1-10 scale)
2. Subtask division by logical layers
3. Context7 documentation lookup
4. Parallelization strategy evaluation
5. TDD test structure definition
6. Create enriched JSON file
7. Generate informed TodoWrite

**Output:** `.taskmaster/enriched/<id>-enriched.json`

### `/session-save`
Preserves current context before /clear:
- TodoWrite state (all todos + progress)
- TEP analysis references
- Git workspace state
- Implementation decisions

**Output:** `.taskmaster/sessions/session-<timestamp>-task-<id>.json`

### `/context-recover`
Restores context after /clear:
1. Find latest session file
2. Load TodoWrite from saved state
3. Reference TEP analysis
4. Check git status
5. Resume from exact position

## File Structures

### Enriched Task (TEP Output)
```json
{
  "taskId": "1",
  "analysis": {
    "complexity": 8,
    "technologies": ["SQLite", "FastAPI", "React"],
    "recommendedApproach": "sequential-then-parallel"
  },
  "subtasks": [{
    "id": "1.1",
    "tddStructure": {
      "failingTests": [{"name": "test_x", "file": "path"}],
      "minimalImplementation": {"keyComponents": []},
      "integrationPoints": []
    },
    "documentation": {"library": {"contextId": "/org/proj"}}
  }],
  "parallelization": {
    "strategy": "sequential|parallel|hybrid",
    "phases": [{"phase": 1, "subtasks": ["1.1"]}]
  }
}
```

### Session State
```json
{
  "sessionId": "session-2024-12-25-task-1",
  "taskContext": {
    "currentTaskId": "1",
    "enrichedFile": ".taskmaster/enriched/1-enriched.json"
  },
  "todoState": {
    "todos": [{"id": "tep-1", "content": "[TEP:1]...", "status": "pending"}],
    "currentTodoIndex": 0
  },
  "decisions": {
    "parallelizationStrategy": "sequential-foundation-then-parallel",
    "tddApproach": "strict-red-green-refactor"
  }
}
```

## Workflow

### Standard Flow
```
task-master next → /task-enrich → implement todos → update checkpoints
```

### Context Preservation Flow
```
long analysis → /session-save → /clear → /context-recover → continue
```

## Todo Prefix Convention
```
[TEP:taskId][Subtask:x.y][TDD:Phase] Description
```
- TEP: Task reference
- Subtask: Current subtask 
- TDD: Red|Green|Refactor|Integrate
- Checkpoint: Update points

## When to Use

**Use TEP when:**
- Task complexity ≥ 7
- Multiple technology layers
- Time estimate > 60 minutes
- Clear test boundaries exist

**Skip TEP when:**
- Simple single-file changes
- Exploratory/undefined work
- Tasks < 30 minutes

## Key Benefits
- Systematic analysis replaces ad-hoc planning
- Pre-identified documentation saves search time
- TDD structure defined before coding starts
- Context persists across sessions
- Parallelization opportunities identified early

## Integration Notes
- Never modifies `tasks.json` directly
- Creates separate enriched/session files
- Uses official task-master commands for updates
- Compatible with git workflow