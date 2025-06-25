# Task Master + TEP + CPP Workflow Tutorial

## Overview

This tutorial guides LLMs through the complete enhanced Task Master workflow, including Task Enrichment Protocol (TEP) and Context Preservation Protocol (CPP).

## Core Workflow

```
Task Selection → TEP Analysis → Implementation → Context Management → Completion
```

## Step 1: Initial Task Selection

```bash
# Find next available task
npx task-master next

# View task details
npx task-master show 1
```

**Output Example:**
```
Task #1: Setup Project Infrastructure
- Database, Backend, Frontend setup needed
- Complexity: High
- No existing subtasks
```

## Step 2: Task Enrichment Protocol (TEP)

### Execute TEP Analysis

```
User: /task-enrich

LLM Actions:
1. Read task details from task-master
2. Analyze complexity (1-10 scale)
3. Identify technologies involved
4. Plan subtask division
5. Lookup documentation with Context7
6. Design TDD structure
7. Create enriched file
8. Generate informed TodoWrite
```

### TEP Output Files

**Created:** `.taskmaster/enriched/1-enriched.json`

```json
{
  "taskId": "1",
  "analysis": {
    "complexity": 8,
    "technologies": ["SQLite", "FastAPI", "React"]
  },
  "subtasks": [
    {
      "id": "1.1",
      "title": "Database Setup",
      "tddStructure": {
        "failingTests": ["test_wal_mode", "test_cache_size"],
        "minimalImplementation": "DatabaseConfig class"
      }
    }
  ]
}
```

### Generated TodoWrite

```
[TEP:1][Subtask:1.1][TDD:Red] Write test_database_wal_mode_enabled
[TEP:1][Subtask:1.1][TDD:Red] Write test_database_cache_size_64mb
[TEP:1][Subtask:1.1][TDD:Green] Implement DatabaseConfig.get_engine()
[TEP:1][Subtask:1.1][Checkpoint] Update Task Master progress
```

## Step 3: Implementation Phase

### TDD Cycle Execution

```python
# 1. RED Phase - Write failing tests
def test_database_wal_mode_enabled():
    engine = get_engine()
    # This will fail initially
    assert get_pragma(engine, "journal_mode") == "wal"

# 2. GREEN Phase - Minimal implementation
def get_engine():
    engine = create_engine("sqlite:///pkm.db")
    # Make test pass with minimal code
    set_pragma(engine, "journal_mode", "wal")
    return engine

# 3. REFACTOR Phase - Improve code
class DatabaseConfig:
    def get_engine(self):
        # Refactored clean implementation
```

### Progress Updates

At checkpoints:
```bash
npx task-master update-subtask --id=1.1 --prompt="Database config complete: WAL mode, cache, FTS5 enabled"
```

## Step 4: Context Management

### When Approaching Context Limit

**Indicators:**
- Long conversation history
- Complex analysis completed
- Multiple files created/modified

### Save Context Before /clear

```
User: Need to clear context, save progress

LLM: /session-save

Actions:
1. Capture current TodoWrite state
2. Save task references  
3. Record decisions made
4. Note git status
5. Create session file
```

**Created:** `.taskmaster/sessions/session-2024-12-25-16:45-task-1.json`

```json
{
  "sessionId": "session-2024-12-25-16:45-task-1",
  "todoState": {
    "todos": [/* all todos with status */],
    "currentTodoIndex": 5,
    "completedCount": 5
  },
  "taskContext": {
    "currentTaskId": "1",
    "enrichedFile": ".taskmaster/enriched/1-enriched.json"
  }
}
```

### Clear and Recover

```
User: /clear
[Context reset occurs]

User: Continue where we left off

LLM: /context-recover

Actions:
1. Find latest session file
2. Load TodoWrite from saved state
3. Reference TEP enriched file
4. Check git status
5. Resume from exact position
```

**Recovery Output:**
```
📋 Context Recovered:
- Task: #1 Infrastructure Setup
- Progress: 5/17 todos completed
- Current: [TEP:1][Subtask:1.2][TDD:Red] Write test_fastapi_app_startup
- Git: 3 modified files

Ready to continue implementation.
```

## Step 5: Task Completion

### Final Steps

```bash
# Complete remaining todos
# Run integration tests
# Final checkpoint update

npx task-master set-status --id=1 --status=done
```

## Complete Workflow Example

### Day 1: Analysis and Start

```
1. npx task-master next
   → Task #1 identified

2. /task-enrich
   → Analysis complete, 17 todos generated

3. Start implementation
   → Complete todos 1-5 (database setup)

4. /session-save
   → Context preserved before ending

5. /clear
```

### Day 2: Resume and Complete

```
1. /context-recover
   → Restored at todo #6

2. Continue implementation
   → Complete todos 6-11 (backend setup)

3. Parallel work possible
   → Frontend can start (todos 12-15)

4. Integration testing
   → Todo 16-17

5. npx task-master set-status --id=1 --status=done
   → Task complete
```

## Key Benefits

### With TEP
- **Systematic Analysis**: No ad-hoc planning
- **Pre-identified Docs**: Context7 references ready
- **TDD Structure**: Tests planned before coding
- **Clear Subtasks**: Logical division of work

### With CPP
- **No Context Loss**: Seamless session continuity
- **Progress Tracking**: Exact position preserved
- **Decision Memory**: Architectural choices saved
- **Team Friendly**: Anyone can pick up where left off

## Common Patterns

### Complex Task Pattern
```
/task-enrich → Heavy analysis → /session-save → /clear → /context-recover → Implement
```

### Daily Work Pattern
```
Morning: /context-recover → Continue todos
Evening: /session-save → Log off
```

### Quick Task Pattern
```
Simple task → Skip TEP → Direct implementation → Complete
```

## File Reference

### TEP Files
- **Location**: `.taskmaster/enriched/<id>-enriched.json`
- **Purpose**: Detailed task analysis and plan
- **Lifetime**: Permanent reference

### CPP Files
- **Location**: `.taskmaster/sessions/session-*.json`
- **Purpose**: Context state preservation
- **Lifetime**: 7 days (auto-cleanup)

### Integration Points
- **Task Master**: Official task tracking
- **TodoWrite**: LLM's execution list
- **Git**: Code version control
- **Context7**: Documentation lookup

## Troubleshooting

### Lost Context Without Save
- Check git log for recent commits
- Use `npx task-master show <id>` for task state
- Look for WIP commits

### Session File Not Found
- List sessions: `ls .taskmaster/sessions/`
- Use most recent file
- Verify task ID matches

### TEP Analysis Outdated
- Re-run `/task-enrich` if requirements changed
- Update enriched file reflects new understanding

## Summary

The enhanced workflow provides:
1. **Structured Planning** via TEP
2. **Continuous Progress** via CPP
3. **Quality Code** via TDD
4. **No Lost Work** via session management

This system transforms ad-hoc development into a systematic, resumable, and trackable process optimized for LLM-assisted development.