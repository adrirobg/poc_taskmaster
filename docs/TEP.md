# Task Enrichment Protocol (TEP)

## Overview
Protocol for transforming Task Master tasks into detailed implementation plans with TDD structure, documentation references, and parallelization strategies.

## Commands

### `/task-enrich`
Analyzes current task following enhanced 8-step protocol:
1. Complexity analysis (1-10 scale)
2. Subtask division by logical layers
3. Context7 documentation lookup (MANDATORY per subtask)
4. Parallelization strategy evaluation
5. TDD test structure definition
6. Create enriched JSON file
6.5. Generate parallelization TODOs
7. Generate balanced TodoWrite

**Output:** `.taskmaster/enriched/<id>-enriched.json`

**TODO Distribution Target:**
- 40% TDD (test-driven development)
- 20% Doc (documentation consultation)
- 20% Impl (implementation)
- 10% Parallel (orchestration)
- 10% Validate (checkpoints)

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
    "documentation": {
      "library": {"contextId": "/org/proj"},
      "mandatoryConsultation": true,
      "topics": ["specific-pattern", "best-practices"]
    }
  }],
  "parallelization": {
    "strategy": "sequential|parallel|hybrid",
    "phases": [{"phase": 1, "subtasks": ["1.1"]}],
    "subagentAllocation": {
      "agent1": ["subtask1.1", "subtask1.2"],
      "agent2": ["subtask1.3"],
      "supervisor": "validation"
    }
  },
  "todoGeneration": {
    "distribution": {
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
[TEP:taskId][Type:category][Target:specific] Description
```
- **TEP**: Task reference (e.g., TEP:1)
- **Type**: Todo category
  - `Doc`: Documentation consultation (Context7)
  - `TDD`: Test-driven development (Red/Green/Refactor)
  - `Impl`: Implementation work
  - `Parallel`: Subagent orchestration
  - `Validate`: Checkpoints/supervision
- **Target**: Specific target (e.g., SQLAlchemy, Backend, Subtask:1.1)

### Examples:
```
[TEP:1][Doc:FastAPI] Consult /tiangolo/fastapi for middleware patterns
[TEP:1][TDD:Red] Write test_database_connection
[TEP:1][Impl:Backend] Create FastAPI app with consulted patterns
[TEP:1][Parallel:Launch] Deploy 3 subagents for concurrent work
[TEP:1][Validate:Integration] Supervisor validates cross-layer compatibility
```

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
- Pre-identified documentation MUST be consulted during implementation
- TDD structure defined before coding starts
- Context persists across sessions
- Parallelization opportunities executed via subagents
- Balanced TODO distribution prevents over-emphasis on any single aspect

## Critical Implementation Rules

1. **Documentation is MANDATORY**: Every subtask must have at least one [Doc] TODO that references the contextId from enriched JSON. This documentation MUST be consulted BEFORE implementation.

2. **Parallelization MUST be executed**: If strategy identifies parallel opportunities, [Parallel] TODOs must be generated and subagents deployed.

3. **TODO Balance**: No single type should exceed 50% of total TODOs. Target distribution must be maintained.

4. **Subagent Usage**: For parallel execution, use Task() tool to deploy subagents. Main agent supervises with [Validate] TODOs.

## Integration Notes
- Never modifies `tasks.json` directly
- Creates separate enriched/session files
- Uses official task-master commands for updates
- Compatible with git workflow