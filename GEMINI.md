<claude_instructions project="Personal PKM Application">

# **Core Directives for Claude Code: Personal PKM Application**

## **1. Core Philosophy: Precision, Planning, and Protocol**

<core_philosophy>
Your primary function is to translate the meticulously planned architecture from the **Product Requirements Document (PRD)** into clean, efficient, and correct code. You are an implementation tool, not a creative designer.

- **The PRD is the single source of truth.** All development is a direct translation of its requirements.
- **The C7DD protocol is your only development methodology.** It is non-negotiable.
- **Simplicity and adherence are paramount.** Avoid complexity and any deviation from the specified technology stack and patterns. Your goal is to build exactly what is defined, nothing more.
</core_philosophy>

## **2. Project Context: The Blueprint**

<project_context>
This context is your permanent memory for this project. Refer to it for every task.

### **2.1. Technology Stack**
<technologies>
  - **Frontend:** React 18 + TypeScript (Strict) + Vite + CSS Modules
  - **Backend:** Python 3.11+ + FastAPI + SQLAlchemy 2.0
  - **Database:** SQLite 3.40+ con FTS5
  - **Architecture:** Local-First, Single-User
</technologies>

### **2.2. Core Data Models (Source of Truth)**
<data_models>
  These are the exact schemas. Implement them without modification.
    ```python
    # Pydantic Schemas derived from PRD for API validation
    # These MUST be used for all API operations.

    from pydantic import BaseModel, Field
    from uuid import UUID, uuid4
    from datetime import datetime

    class Project(BaseModel):
      id: UUID = Field(default_factory=uuid4)
      name: str = Field(..., min_length=1, max_length=100)
      description: str | None = Field(None, max_length=500)
      color: str = "#FFFFFF"
      icon: str = "📄"
      created_at: datetime = Field(default_factory=datetime.utcnow)
      updated_at: datetime = Field(default_factory=datetime.utcnow)
      archived_at: datetime | None = None
      metadata: dict = {}

    class Note(BaseModel):
      id: UUID = Field(default_factory=uuid4)
      title: str = Field(..., min_length=1, max_length=200)
      content: str = ""
      project_id: UUID | None = None
      created_at: datetime = Field(default_factory=datetime.utcnow)
      updated_at: datetime = Field(default_factory=datetime.utcnow)
      deleted_at: datetime | None = None # For soft delete
      version: int = 1
      word_count: int = 0
      reading_time: int = 0
    ```
</data_models>

### **2.3. API Structure Overview**
<api_structure>
  - **Base Path:** `/api/v1`
  - **Resources:** `/projects`, `/notes`, `/tags`, `/search`
  - **Authentication:** Simple single-user token (defined in PRD).
  - **Operations:** Standard RESTful patterns (GET, POST, PUT, PATCH, DELETE).
</api_structure>

</project_context>

## **3. 🚨 Context7-Driven Development (C7DD) - Mandatory Code Generation Protocol**

<development_protocol name="Context7-Driven Development">
<c7dd_protocol>
	<immutable_rules>
    ALL code generation MUST follow this exact sequence:
    1. VALIDATE → 2. SEARCH → 3. ANALYZE → 4. SYNTHESIZE → 5. VERIFY
    Breaking this sequence = INVALID CODE. No exceptions.
	</immutable_rules>

	<forbidden_actions>
    - Writing code without Context7 search.
    - Skipping Context7 search for any reason.
    - Inventing syntax, patterns, or solutions.
    - Proceeding if Context7 yields no relevant snippets, good practices, or patterns.
    - Using ONLY personal knowledge or memory for code generation. This is strictly forbidden.
	</forbidden_actions>
	<required_process>

    <step name="1_VALIDATE">
    Output: "✓ TASK: [exact description of what needs to be implemented based on the PRD]"
    Action: Confirm your understanding of the specific, planned task before any other action.
    </step>

    <step name="2_SEARCH">
    Output: "🔍 SEARCHING: [specific capability needed for the task]"
        "📡 Context7: [library/id] → '[precise query for a pattern or example]'"
    Action: Execute ONE focused Context7 query per required capability. The query must be for a pattern, not a complete solution.
    </step>

    <step name="3_ANALYZE">
    Output: "📋 SNIPPETS FOUND:"
        "  - L[line#]: [description of pattern/practice] - [how it will be adapted for our task]"
        "  - L[line#]: [description of another pattern/practice] - [what parts will be used]"
    Action: List ALL relevant snippets, patterns, and best practices found, citing their line numbers. Explicitly state how each will be used or adapted.
    </step>

    <step name="4_SYNTHESIZE">
    Output: "✅ SYNTHESIZING:"
        "```[language]"
        "# From L[line#] (pattern) + L[line#] (data model)"
        "[generated code with inline citations to the source snippets]"
        "```"
    Action: Generate code ONLY by combining and adapting the identified snippets. Every line of generated code must be traceable to a source pattern or the PRD.
    </step>

    <step name="5_VERIFY">
    Output: "✓ VERIFIED: Code synthesized from pattern at L[line#], adapted for the `Project` model as per the PRD."
    Action: Confirm that the generated code directly implements the patterns found and adheres to the project's data models and architecture.
    </step>

	</required_process>

	<failure_protocol>
	  When Context7 returns no relevant results for a specific, well-formed query:
    ```
    ❌ NO SNIPPETS FOUND
    Queries attempted:
    1. [library] → "[query1]" - No results
    2. [library] → "[query2]" - Results not relevant to the required pattern

    ⚠️ BLOCKED: Cannot proceed without documented examples or patterns. Inventing a solution is a protocol violation.
    Options:
    A) Suggest alternative query: "[new, more specific query]"
    B) Suggest checking different library: "[alternative library, if applicable]"
    C) Request manual guidance from the architect.
    ```
	  NEVER invent solutions when blocked. Halting is the correct procedure.
	</failure_protocol>

</c7dd_protocol>
</development_protocol>

## **4. Non-Negotiable Guardrails**

<guardrails>
These rules are immutable and override any other interpretation. Violation requires immediate correction.

<rule name="TRUST_THE_PLAN">
The PRD and the Development Roadmap define the work. Your task is to implement the *current* phase as specified. Do not implement features from future phases. Do not add functionality not explicitly described in the PRD. The plan is your only scope.
</rule>

<rule name="NO_OVER_ENGINEERING">
Implement the simplest, most direct solution that fulfills the requirement. Do not add abstractions, layers, or configurations for future problems that do not exist today. If the PRD asks for a list, you provide a list, not a paginated, filtered, sorted, and cached data grid. Follow the principle of "You Aren't Gonna Need It" (YAGNI).
</rule>

<rule name="ADHERE_TO_STACK">
Use only the technologies specified in `<project_context>`. Do not introduce new libraries, frameworks, or tools. The stack is fixed. If a task seems to require a new dependency, it's a signal to re-evaluate the approach using existing tools, not to add a new one.
</rule>

<rule name="MODEL_IS_LAW">
The data models in `<data_models>` are absolute. All data structures, database tables, and API payloads must conform to these models exactly. Do not add, remove, or rename fields.
</rule>

</guardrails>

## **5. Code Style and Patterns**

<code_style_and_patterns>
All code must be clean, self-documenting, and consistent.

- **No Code Comments:** Code should explain itself through clear function and variable names. If you need a comment, your code is not clear enough. Refactor it.
- **Immutability:** Do not mutate data. Create new objects/data structures instead of modifying existing ones.
- **Small, Pure Functions:** Compose functionality from small, predictable functions with no side effects.
- **Backend (FastAPI):** Strictly follow the Controller → Service → Repository pattern defined in the PRD. Use Pydantic for all data validation at the API boundary. All functions must have type hints.
- **Frontend (React):** Use functional components with hooks. State management must be explicit and predictable. Use the provided CSS Modules for styling; do not use inline styles or other CSS-in-JS libraries.
</code_style_and_patterns>

## **6. C7DD Workflow Examples**

<examples>
This is how you operate. Study these examples.

<example name="Correct Implementation of a Backend Endpoint">
**Task:** Implement the `GET /api/v1/projects` endpoint to list all projects, as defined in the PRD.

<c7dd_workflow>
<step name="1_VALIDATE">
✓ TASK: Create a FastAPI GET endpoint at `/api/v1/projects` that returns a list of `Project` objects.
</step>

<step name="2_SEARCH">
🔍 SEARCHING: FastAPI pattern for a GET endpoint returning a list of Pydantic models.
📡 Context7: /tiangolo/fastapi → "fastapi get endpoint return list of pydantic models"
</step>

<step name="3_ANALYZE">
📋 SNIPPETS FOUND:
  - L451 (from FastAPI docs): Shows using `response_model=list[Item]` in the decorator. - adapt `Item` to our `Project` model.
  - L455 (from FastAPI docs): Shows a simple `async def` function that returns a list of dictionaries. - use this function structure.
  - L102 (from a repository pattern example): Shows injecting a service/repository via `Depends` to fetch data. - use this dependency injection pattern.
</step>

<step name="4_SYNTHESIZE">
✅ SYNTHESIZING:
```python
# From L451 (response_model pattern), L455 (async def structure), L102 (dependency injection)
# Assumes a 'project_service' exists as per our Repository pattern.

from fastapi import APIRouter, Depends
from ..models.project import Project # Our project model from the PRD
from ..services.project_service import ProjectService # Our service layer

router = APIRouter()

@router.get("/projects", response_model=list[Project])
async def list_projects(
    service: ProjectService = Depends(ProjectService)
):
    """
    Retrieve all projects.
    """
    return service.get_all_projects()
```
</step>

<step name="5_VERIFY">
✓ VERIFIED: Code synthesized from documented FastAPI patterns at L451/L455, using the dependency injection pattern from L102. It correctly implements the endpoint and uses our `Project` model as the `response_model`, adhering to the PRD.
</step>
</c7dd_workflow>
</example>

<example name="Incorrect Implementation">
**Task:** Implement the `GET /api/v1/projects` endpoint.

<c7dd_workflow>
❌ **WRONG - Protocol Violation**
```python
# Written from memory. No C7DD steps followed.
# This code is invalid regardless of whether it works.

from main import app

@app.get("/api/v1/projects")
def get_all_projects():
    # This logic should be in a service/repository layer.
    # Also, it's not async.
    # It doesn't use the Pydantic response_model for validation and documentation.
    db = get_db_connection()
    projects = db.execute("SELECT * FROM projects").fetchall()
    return projects
```
This is a critical failure because it ignores the C7DD protocol, bypasses the established architecture (service layer), and relies on memory instead of documented best practices. **This type of implementation is forbidden.**
</example>

</examples>

</claude_instructions>


# Task Master AI - Claude Code Integration Guide

**Proyecto:** poc_taskmaster - Sistema de gestión de tareas con IA para desarrollo  
**Repositorio:** https://github.com/adrirobg/poc_taskmaster  
**Desarrollador:** adrirobg

## Essential Commands

### Core Workflow Commands

```bash
# Project Setup
task-master init                                    # Initialize Task Master in current project
task-master parse-prd .taskmaster/docs/prd.txt      # Generate tasks from PRD document
task-master models --setup                        # Configure AI models interactively

# Daily Development Workflow
task-master list                                   # Show all tasks with status
task-master next                                   # Get next available task to work on
task-master show <id>                             # View detailed task information (e.g., task-master show 1.2)
task-master set-status --id=<id> --status=done    # Mark task complete

# Task Management
task-master add-task --prompt="description" --research        # Add new task with AI assistance
task-master expand --id=<id> --research --force              # Break task into subtasks
task-master update-task --id=<id> --prompt="changes"         # Update specific task
task-master update --from=<id> --prompt="changes"            # Update multiple tasks from ID onwards
task-master update-subtask --id=<id> --prompt="notes"        # Add implementation notes to subtask

# Analysis & Planning
task-master analyze-complexity --research          # Analyze task complexity
task-master complexity-report                      # View complexity analysis
task-master expand --all --research               # Expand all eligible tasks

# Dependencies & Organization
task-master add-dependency --id=<id> --depends-on=<id>       # Add task dependency
task-master move --from=<id> --to=<id>                       # Reorganize task hierarchy
task-master validate-dependencies                            # Check for dependency issues
task-master generate                                         # Update task markdown files (usually auto-called)
```

## Key Files & Project Structure

### Core Files

- `.taskmaster/tasks/tasks.json` - Main task data file (auto-managed)
- `.taskmaster/config.json` - AI model configuration (use `task-master models` to modify)
- `.taskmaster/docs/prd.txt` - Product Requirements Document for parsing
- `.taskmaster/tasks/*.txt` - Individual task files (auto-generated from tasks.json)
- `.env` - API keys for CLI usage

### Claude Code Integration Files

- `CLAUDE.md` - Auto-loaded context for Claude Code (this file)
- `.claude/settings.json` - Claude Code tool allowlist and preferences
- `.claude/commands/` - Custom slash commands for repeated workflows
- `.mcp.json` - MCP server configuration (project-specific)

### Directory Structure

```
project/
├── .taskmaster/
│   ├── tasks/              # Task files directory
│   │   ├── tasks.json      # Main task database
│   │   ├── task-1.md      # Individual task files
│   │   └── task-2.md
│   ├── docs/              # Documentation directory
│   │   ├── prd.txt        # Product requirements
│   ├── reports/           # Analysis reports directory
│   │   └── task-complexity-report.json
│   ├── templates/         # Template files
│   │   └── example_prd.txt  # Example PRD template
│   └── config.json        # AI models & settings
├── .claude/
│   ├── settings.json      # Claude Code configuration
│   └── commands/         # Custom slash commands
├── .env                  # API keys
├── .mcp.json            # MCP configuration
└── CLAUDE.md            # This file - auto-loaded by Claude Code
```

## MCP Integration

Task Master provides an MCP server that Claude Code can connect to. Configure in `.mcp.json`:

```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "--package=task-master-ai", "task-master-ai"],
      "env": {
        "ANTHROPIC_API_KEY": "your_key_here",
        "PERPLEXITY_API_KEY": "your_key_here",
        "OPENAI_API_KEY": "OPENAI_API_KEY_HERE",
        "GOOGLE_API_KEY": "GOOGLE_API_KEY_HERE",
        "XAI_API_KEY": "XAI_API_KEY_HERE",
        "OPENROUTER_API_KEY": "OPENROUTER_API_KEY_HERE",
        "MISTRAL_API_KEY": "MISTRAL_API_KEY_HERE",
        "AZURE_OPENAI_API_KEY": "AZURE_OPENAI_API_KEY_HERE",
        "OLLAMA_API_KEY": "OLLAMA_API_KEY_HERE"
      }
    }
  }
}
```

## Claude Code Workflow Integration

### Standard Development Workflow

#### 1. Project Initialization

```bash
# Initialize Task Master
task-master init

# Create or obtain PRD, then parse it
task-master parse-prd .taskmaster/docs/prd.txt

# Analyze complexity and expand tasks
task-master analyze-complexity --research
task-master expand --all --research
```

#### 2. Daily Development Loop

```bash
# Start each session
task-master next                           # Find next available task
task-master show <id>                     # Review task details

# During implementation, check in code context into the tasks and subtasks
task-master update-subtask --id=<id> --prompt="implementation notes..."

# Complete tasks
task-master set-status --id=<id> --status=done
```

## Task Structure & IDs

### Task ID Format

- Main tasks: `1`, `2`, `3`, etc.
- Subtasks: `1.1`, `1.2`, `2.1`, etc.
- Sub-subtasks: `1.1.1`, `1.1.2`, etc.

### Task Status Values

- `pending` - Ready to work on
- `in-progress` - Currently being worked on
- `done` - Completed and verified
- `deferred` - Postponed
- `cancelled` - No longer needed
- `blocked` - Waiting on external factors

### Task Fields

```json
{
  "id": "1.2",
  "title": "Implement user authentication",
  "description": "Set up JWT-based auth system",
  "status": "pending",
  "priority": "high",
  "dependencies": ["1.1"],
  "details": "Use bcrypt for hashing, JWT for tokens...",
  "testStrategy": "Unit tests for auth functions, integration tests for login flow",
  "subtasks": []
}
```

## Claude Code Best Practices with Task Master

### Context Management

- Use `/clear` between different tasks to maintain focus
- This CLAUDE.md file is automatically loaded for context
- Use `task-master show <id>` to pull specific task context when needed

### Iterative Implementation

1. `task-master show <subtask-id>` - Understand requirements
2. Explore codebase and plan implementation
3. `task-master update-subtask --id=<id> --prompt="detailed plan"` - Log plan
4. `task-master set-status --id=<id> --status=in-progress` - Start work
5. Implement code following logged plan
6. `task-master update-subtask --id=<id> --prompt="what worked/didn't work"` - Log progress
7. `task-master set-status --id=<id> --status=done` - Complete task

### Complex Workflows with Checklists

For large migrations or multi-step processes:

1. Create a markdown PRD file describing the new changes: `touch task-migration-checklist.md` (prds can be .txt or .md)
2. Use Taskmaster to parse the new prd with `task-master parse-prd --append` (also available in MCP)
3. Use Taskmaster to expand the newly generated tasks into subtasks. Consdier using `analyze-complexity` with the correct --to and --from IDs (the new ids) to identify the ideal subtask amounts for each task. Then expand them.
4. Work through items systematically, checking them off as completed
5. Use `task-master update-subtask` to log progress on each task/subtask and/or updating/researching them before/during implementation if getting stuck

### Task File Sync Issues

```bash
# Regenerate task files from tasks.json
task-master generate

# Fix dependency issues
task-master fix-dependencies
```

DO NOT RE-INITIALIZE. That will not do anything beyond re-adding the same Taskmaster core files.

## Important Notes

### AI-Powered Operations
- Use `--research` flag for AI-assisted task creation and updates

## File Management

- Never manually edit `tasks.json` - use commands instead
- Never manually edit `.taskmaster/config.json` - use `task-master models`
- Task markdown files in `tasks/` are auto-generated
- Run `task-master generate` after manual changes to tasks.json

### Multi-Task Updates

- Use `update --from=<id>` to update multiple future tasks
- Use `update-task --id=<id>` for single task updates
- Use `update-subtask --id=<id>` for implementation logging

### Research Mode

- Add `--research` flag for research-based AI enhancement
- Requires a research model API key like Perplexity (`PERPLEXITY_API_KEY`) in environment
- Provides more informed task creation and updates
- Recommended for complex technical tasks

---