# Context Preservation Protocol (CPP)

## Overview
System for preserving and recovering Claude Code context across sessions, preventing loss of analysis and progress due to context limits.

## Problem Solved
```
Long Planning → Context Limit → /clear Required → Context Lost
                                                        ↓
                                                 CPP Solves This
```

## Commands

### `/session-save`
Captures complete current context before /clear.

**Saves:**
- TodoWrite complete state
- Current task references
- TEP analysis links
- Git workspace status
- Implementation decisions
- Progress metrics

**Output:** `.taskmaster/sessions/session-<timestamp>-task-<id>.json`

**When to use:**
- Before hitting context limit
- End of work session
- Before task switching
- After complex analysis

### `/context-recover`
Restores complete context from saved session.

**Process:**
1. Find latest session file
2. Load TodoWrite state
3. Reference TEP analysis
4. Check git status
5. Resume exact position

**Output:**
```
📋 Context Recovered for Task #X
✅ Session: session-2024-12-25-task-1.json
✅ TodoWrite: 17 todos (5 completed)
✅ Next: [TEP:1][Subtask:1.1][TDD:Red] Write test_x
```

## Session File Structure
```json
{
  "sessionId": "session-<timestamp>-task-<id>",
  "taskContext": {
    "currentTaskId": "1",
    "enrichedFile": "path/to/enriched.json",
    "status": "ready|in-progress|blocked"
  },
  "todoState": {
    "todos": [/* complete todo array */],
    "currentTodoIndex": 5,
    "completedCount": 5
  },
  "workspaceState": {
    "gitBranch": "master",
    "modifiedFiles": ["file1.py", "file2.ts"]
  },
  "decisions": {/* preserved decisions */},
  "nextSteps": ["immediate actions"]
}
```

## Workflow Integration

### Standard Development
```
/task-enrich → implement → reach limit → /session-save → /clear → /context-recover → continue
```

### Daily Work Pattern
```
Day 1: analyze → implement → /session-save
Day 2: /context-recover → continue exactly where left off
```

## Best Practices

**Before Saving:**
- Commit important changes
- Update task-master if needed
- Complete current todo if possible

**Session Management:**
- Auto-cleanup old sessions after 7 days
- One session per task
- Timestamp prevents conflicts

**Recovery Verification:**
- Check todo index matches
- Verify git status clean
- Confirm TEP file exists

## Implementation Notes
- Session files are project-local
- No sensitive data stored
- Compatible with git workflow
- Integrates with TEP system