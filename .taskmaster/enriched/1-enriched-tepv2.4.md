# Task Enrichment: Setup Project Infrastructure and Database Foundation

## Análisis de la Tarea
Crear una estructura de proyecto full-stack con FastAPI backend (patrón controller-service-repository), SQLite optimizado (WAL mode, FTS5), y React+TypeScript frontend con Vite. Todo debe incluir configuración de desarrollo y dependencias listas.

## Tecnologías Identificadas
- **FastAPI**: `/tiangolo/fastapi`
- **SQLAlchemy 2.0**: `/sqlalchemy/sqlalchemy`
- **Pydantic v2**: `/pydantic/pydantic`
- **React 18+**: `/reactjs/react.dev`
- **Vite**: `/vitejs/vite`

## Documentación a Consultar
Antes de implementar cada parte:
- Para **FastAPI setup**: Context7 `/tiangolo/fastapi` topic: "project structure controller service repository pattern"
- Para **SQLite con SQLAlchemy**: Context7 `/sqlalchemy/sqlalchemy` topic: "sqlite wal mode pragma fts5 configuration"
- Para **Pydantic Settings**: Context7 `/pydantic/pydantic` topic: "pydantic settings environment variables config"
- Para **React con TypeScript**: Context7 `/reactjs/react.dev` topic: "typescript setup project structure"
- Para **Vite config**: Context7 `/vitejs/vite` topic: "react typescript proxy backend configuration"

## Enfoque TDD
1. **Tests primero**
   - Backend: Test que FastAPI app inicie correctamente con health endpoint
   - Database: Test de conexión SQLite con WAL mode activado
   - Frontend: Test que Vite dev server compile TypeScript sin errores
   - Integration: Test que frontend proxy requests al backend correctamente

2. **Implementación mínima**
   - Crear estructura de directorios básica
   - FastAPI app mínima con `/health` endpoint
   - SQLAlchemy engine con configuración SQLite
   - React app inicial con un componente TypeScript
   - Scripts de desarrollo en package.json/Makefile

3. **Refactoring**
   - Extraer configuración a archivos .env con Pydantic Settings
   - Implementar patrón repository completo para futuras entidades
   - Configurar linting (ruff/mypy para Python, ESLint para TS)

## Oportunidades de Paralelización
Después del setup inicial de directorios:
- **Agent A**: Configurar backend (FastAPI + SQLAlchemy + tests)
- **Agent B**: Configurar frontend (React + Vite + TypeScript)
- **Punto de sincronización**: Cuando ambos tengan servers corriendo, configurar proxy en Vite