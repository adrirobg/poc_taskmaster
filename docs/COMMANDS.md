# Claude Code Custom Commands Reference

## Task Enhancement Commands

### `/task-enrich`
**Purpose:** Transform Task Master task into detailed implementation plan  
**Process:** 7-step analysis protocol  
**Output:** Enriched task file + informed TodoWrite  
**Use when:** Complex tasks (≥7 complexity, >60min, multiple layers)

### `/session-save`  
**Purpose:** Preserve context before /clear  
**Process:** Capture TodoWrite + decisions + workspace state  
**Output:** Session file for recovery  
**Use when:** Approaching context limit, end of session

### `/context-recover`
**Purpose:** Restore complete context after /clear  
**Process:** Load session + TEP files + verify git state  
**Output:** Exact context restoration  
**Use when:** After /clear, starting new session, resuming work

## Command Workflow Patterns

### TEP Analysis → Implementation
```bash
/task-enrich     # Analyze task, create enriched file
# Follow generated todos with TDD structure
# Use checkpoints to update task-master
```

### Context Preservation
```bash
/session-save    # Before context limit
/clear           # Reset context
/context-recover # Restore state
# Continue exactly where left off
```

### Daily Development
```bash
# Day 1
/task-enrich     # Plan task
# Implement partially
/session-save    # End session

# Day 2  
/context-recover # Resume
# Continue implementation
```

## File Organization
```
.taskmaster/
├── enriched/           # TEP analysis files
│   └── <id>-enriched.json
├── sessions/           # Context preservation
│   └── session-<timestamp>-task-<id>.json
└── tasks/
    └── tasks.json      # Official Task Master (don't modify)
```

## Todo Naming Convention
```
[TEP:taskId][Subtask:x.y][TDD:Phase] Description
```
- TEP: Links to enriched file
- Subtask: Current component
- TDD: Red/Green/Refactor/Integrate
- Checkpoint: Update task-master

## Integration Points
- **Task Master:** Official task tracking
- **TodoWrite:** Session-local task execution  
- **Git:** Code progress tracking
- **Context7:** Documentation integration

## Success Criteria
- Context never lost due to limits
- Systematic analysis replaces ad-hoc planning
- TDD structure maintained throughout
- Progress trackable across sessions