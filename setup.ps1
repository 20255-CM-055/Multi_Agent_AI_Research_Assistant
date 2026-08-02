# ===========================================
# Multi-Agent AI Research Assistant Bootstrap
# ===========================================

Write-Host ""
Write-Host "Creating project structure..." -ForegroundColor Cyan

# -------------------------
# Folders
# -------------------------

$folders = @(

# Backend
"backend/api/routes",
"backend/api/dependencies",
"backend/api/middleware",

"backend/agents/planner",
"backend/agents/retriever",
"backend/agents/evaluator",
"backend/agents/search",
"backend/agents/writer",
"backend/agents/critic",
"backend/agents/memory",

"backend/graph/nodes",
"backend/graph/edges",
"backend/graph/state",
"backend/graph/builder",

"backend/services",

"backend/memory/conversation",
"backend/memory/history",
"backend/memory/research",
"backend/memory/session",

"backend/vectorstore/chroma",
"backend/vectorstore/indexes",
"backend/vectorstore/collections",

"backend/embeddings",

"backend/prompts",

"backend/tools",

"backend/models",

"backend/repositories",

"backend/schemas",

"backend/database/migrations",

"backend/config",

"backend/core",

"backend/utils",

"backend/logs",

"backend/static",

"backend/generated_reports/pdf",
"backend/generated_reports/html",
"backend/generated_reports/markdown",

# Frontend

"frontend/src",

"frontend/src/assets",

"frontend/src/components/common",
"frontend/src/components/chat",
"frontend/src/components/dashboard",
"frontend/src/components/research",
"frontend/src/components/flow",
"frontend/src/components/agents",
"frontend/src/components/ui",

"frontend/src/pages",

"frontend/src/layouts",

"frontend/src/hooks",

"frontend/src/services",

"frontend/src/api",

"frontend/src/store",

"frontend/src/types",

"frontend/src/utils",

"frontend/src/styles",

"frontend/src/context",

"frontend/src/router",

"frontend/src/features/dashboard",
"frontend/src/features/research",
"frontend/src/features/history",
"frontend/src/features/sessions",
"frontend/src/features/knowledge",

"frontend/src/flow/nodes",
"frontend/src/flow/edges",
"frontend/src/flow/layouts",

# Docs

"docs",

# Scripts

"scripts",

# Docker

"docker",

# Tests

"tests/backend",
"tests/frontend",
"tests/integration"

)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[Folder] $folder"
    }
}

# -------------------------
# Files
# -------------------------

$files = @(

# Backend

"backend/main.py",
"backend/requirements.txt",
"backend/.env",
"backend/.env.example",

"backend/config/settings.py",
"backend/config/constants.py",
"backend/config/logging.py",

"backend/core/exceptions.py",
"backend/core/lifespan.py",
"backend/core/security.py",

"backend/database/sqlite.py",

"backend/embeddings/models.py",
"backend/embeddings/factory.py",
"backend/embeddings/service.py",

"backend/utils/helpers.py",
"backend/utils/validators.py",
"backend/utils/formatters.py",

"backend/graph/state/state.py",
"backend/graph/builder/workflow.py",

"backend/prompts/system.md",

# Root

".gitignore",
"README.md",
"docker-compose.yml"

)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "[File] $file"
    }
}

# -------------------------
# __init__.py
# -------------------------

$pythonPackages = @(

"backend/api",
"backend/api/routes",
"backend/api/dependencies",
"backend/api/middleware",

"backend/agents",
"backend/agents/planner",
"backend/agents/retriever",
"backend/agents/evaluator",
"backend/agents/search",
"backend/agents/writer",
"backend/agents/critic",
"backend/agents/memory",

"backend/graph",
"backend/graph/nodes",
"backend/graph/edges",
"backend/graph/state",
"backend/graph/builder",

"backend/services",

"backend/memory",
"backend/models",
"backend/repositories",
"backend/schemas",
"backend/database",
"backend/config",
"backend/core",
"backend/utils",
"backend/tools",
"backend/vectorstore",
"backend/embeddings"

)

foreach ($pkg in $pythonPackages) {

    $initFile = Join-Path $pkg "__init__.py"

    if (!(Test-Path $initFile)) {
        New-Item -ItemType File -Path $initFile | Out-Null
    }

}

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host " Project structure created successfully! " -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""