# LLM Onboarding Guide - Task Master Enhanced Ecosystem

## Quick Start

**You are Claude Code working in a Task Master project enhanced with TEP + CPP protocols.**

### Essential Files to Read First
1. `CLAUDE.md` - Project overview and commands
2. `docs/TEP.md` - Task enrichment process
3. `docs/CPP.md` - Context preservation system

### Project Structure Recognition
```
.taskmaster/
├── tasks/tasks.json          # Official Task Master data (READ-ONLY)
├── enriched/<id>-enriched.json  # TEP analysis files (YOUR OUTPUT)
└── sessions/session-*.json   # CPP context files (YOUR STATE)

.claude/commands/
├── task-enrich.md           # Analysis protocol
├── session-save.md          # Context preservation
└── context-recover.md       # Context restoration
```

## Your Enhanced Capabilities

### Standard Task Master
```bash
npx task-master next        # Find next task
npx task-master show <id>   # View task details
npx task-master list        # See all tasks
```

### Enhanced Protocols
```
/task-enrich               # Deep task analysis
/session-save              # Preserve context before /clear
/context-recover           # Restore context after /clear
```

## Decision Tree: When to Use What

### New Task Encountered
```
Is task complex (>60min, multiple layers)?
├─ YES → Use /task-enrich
│   ├─ Create enriched analysis
│   ├─ Generate structured TodoWrite
│   └─ Follow TDD approach
└─ NO → Direct implementation
    └─ Simple TodoWrite without TEP
```

### Context Management
```
Is context getting full?
├─ YES → /session-save → /clear → /context-recover
└─ NO → Continue current work
```

### Task Progress
```
Every 3-4 completed todos:
└─ Update Task Master with progress
```

## Your Workflow States

### State 1: Fresh Session
**Actions:**
1. Check for existing session: `ls .taskmaster/sessions/`
2. If session exists → `/context-recover`
3. If no session → `npx task-master next`

### State 2: Task Selected
**Actions:**
1. Evaluate complexity
2. If complex → `/task-enrich`
3. Begin implementation following todos

### State 3: Implementation Active
**Actions:**
1. Follow TDD cycle (Red → Green → Refactor)
2. Update progress at checkpoints
3. Monitor context usage

### State 4: Context Limit Approaching
**Actions:**
1. `/session-save`
2. Inform user about /clear need
3. Wait for user to /clear

### State 5: Post-Clear Recovery
**Actions:**
1. `/context-recover`
2. Resume exactly where left off
3. Continue implementation

## Todo Convention You'll Use

### Standard Format
```
[TEP:taskId][Subtask:x.y][TDD:Phase] Description
```

### Examples
```
[TEP:1][Subtask:1.1][TDD:Red] Write test_database_wal_mode_enabled
[TEP:1][Subtask:1.2][TDD:Green] Implement FastAPI app with CORS
[TEP:1][Subtask:1.3][TDD:Refactor] Extract config to separate file
[TEP:1][Checkpoint] Update Task Master with progress
```

## Key Principles

### TDD Enforcement
- RED: Write failing test first
- GREEN: Minimal code to pass
- REFACTOR: Improve code quality

### Context Preservation
- Save state before hitting limits
- Never lose analysis or progress
- Seamless recovery across sessions

### Task Master Integration
- Use official commands for updates
- Don't modify tasks.json directly
- Keep enriched files separate

## Common Scenarios

### Scenario 1: Complex Infrastructure Task
```
User: "Let's work on Task 1"
You: Check task complexity → Use /task-enrich → Create 3 subtasks
     Generate 17 todos with TDD structure
     Start with database setup (TDD cycle)
```

### Scenario 2: Context Limit Hit
```
You: Notice long conversation → /session-save
User: Confirms → /clear
User: "Continue where we left off"
You: /context-recover → Resume from todo #8
```

### Scenario 3: Daily Continuation
```
User: "Good morning, continue yesterday's work"
You: /context-recover → Load session from yesterday
     Resume implementation from exact position
```

## Success Indicators

### You're Doing It Right When:
- Every complex task gets TEP analysis
- TodoWrite has clear TDD structure
- Context is preserved across sessions
- Progress updates happen at checkpoints
- No analysis or decisions are lost

### Red Flags
- Skipping TEP for complex tasks
- Context lost due to /clear
- Generic todos without structure
- Missing progress updates
- Repeating analysis work

## Integration with User

### Your Responses Should Include:
- Current task and subtask reference
- TDD phase indication
- Progress metrics (X/Y todos completed)
- Next step clarity
- Checkpoint timing

### Example Response
```
📋 Continuing Task #1 - Infrastructure Setup
🎯 Current: [TEP:1][Subtask:1.2][TDD:Green] FastAPI implementation
📊 Progress: 8/17 todos completed (database ✅, API in progress)
⏱️ Next checkpoint: After completing subtask 1.2
```

## File Management

### Read-Only Files
- `.taskmaster/tasks/tasks.json` (Task Master official)

### Your Files
- `.taskmaster/enriched/` (TEP analysis output)
- `.taskmaster/sessions/` (CPP state files)

### Temporary
- TodoWrite state (session memory only)

## Remember

You are not just implementing tasks - you are following a systematic approach that:
1. **Analyzes** before acting (TEP)
2. **Preserves** context across interruptions (CPP)
3. **Maintains** quality through TDD
4. **Tracks** progress systematically

This makes you a more effective coding assistant capable of handling complex, long-term development work without losing momentum or context.