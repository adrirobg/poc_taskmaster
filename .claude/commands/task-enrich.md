# Task Enrichment Protocol (TEP) v2.3

Enrich Task Master tasks for optimal Claude Code workflow with Context7 integration.

## Core Features
- **Phase-based execution:** 4 phases, 10-15 TODOs total
- **Context7 integration:** Just-in-time documentation with 90%+ relevance
- **Adaptive sizing:** 10 TODOs (simple) or 15 TODOs (medium)
- **TDD structure:** Test-driven development focus

## Protocol Steps

### 1. Task Analysis
```bash
npx task-master next
npx task-master show <id>
```

**Analyze:**
- Complexity (1-10 scale)
- Subtask count and technology stack
- If >5 subtasks or >3 tech stacks → suggest split

**Adaptive Sizing:**
- **Simple** (1-3 complexity): 10 TODOs  
- **Medium** (4-6 complexity): 15 TODOs
- **Complex** (7+): Split task first

### 2. Phase Planning

| Phase | % | TODOs | Focus |
|-------|---|-------|-------|
| Foundation | 20% | 2-3 | Project structure |
| Research | 27% | 3-4 | Technology setup |
| Implementation | 40% | 4-6 | Core features |
| Integration | 13% | 1-2 | Testing & validation |

### 3. Context7 Integration

**When TODO requires library knowledge:**
1. **Analyze specific need** - What exact patterns does this TODO need?
2. **Extract focused topic** - Be specific, not generic
3. **Make Context7 call** - Use `mcp__context7__resolve-library-id` + `mcp__context7__get-library-docs`
4. **Apply immediately** - Enhance TODO with real patterns

**Token Budget:** 400-1000 tokens based on TODO complexity

**Good Topics Examples:**
- "SQLAlchemy engine configuration with connection pooling"
- "FastAPI dependency injection for database sessions"  
- "React Testing Library async component testing"

### 4. TDD Structure

For each TODO, define:
- **Failing Tests** - Write tests first (unit + integration)
- **Minimal Implementation** - Simplest code to pass tests
- **Refactoring Goals** - Post-green improvements
- **Integration Points** - How it connects to other parts

### 5. Generate Enriched JSON

**Location:** `.taskmaster/enriched/<task-id>-enriched.json`

```json
{
  "taskId": "string",
  "originalTask": { /* from task-master */ },
  "analysis": {
    "complexity": 1-10,
    "technologies": ["tech1", "tech2"],
    "todoCount": 10-15
  },
  "subtasks": [
    {
      "id": "x.y", 
      "title": "string",
      "description": "string",
      "phase": "foundation|research|implementation|integration",
      "tddStructure": {
        "failingTests": ["test descriptions"],
        "implementation": "minimal code to pass",
        "refactoring": ["improvement goals"]
      },
      "context7Notes": "specific topics needed for this TODO"
    }
  ]
}
```

### 6. Generate TODOs

Create 10-15 TODOs following phase distribution:
- Use format: `[Type:Category] Specific action (Context7: topic if needed)`
- Include TDD structure where relevant
- Note Context7 integration opportunities

**Examples:**
- `[Structure] Create project directories`
- `[Setup:Database] Configure SQLite with WAL (Context7: SQLAlchemy engine config)`
- `[TDD:Red] Write test for user creation`
- `[TDD:Green] Implement user model to pass tests`

## Example Workflow

1. **Analyze task:** `task-master show 1` → Complexity 5, FastAPI+SQLAlchemy
2. **Size decision:** Medium complexity → 15 TODOs  
3. **Phase planning:** 3+4+6+2 distribution
4. **Context7 strategy:** Just-in-time calls per TODO with library needs
5. **Generate JSON:** Include analysis, subtasks with Context7 notes
6. **Create TODOs:** Phase-based with specific Context7 integration points

## Key Benefits

- **Phase-based execution** for clean LLM workflow
- **Context7 just-in-time integration** with 90%+ relevance  
- **Adaptive sizing** based on task complexity
- **TDD focus** for quality implementation