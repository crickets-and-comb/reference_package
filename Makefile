PYTHON_VERSION := 3.12
PACKAGE_NAME := $(shell python -c "import configparser; cfg = configparser.ConfigParser(); cfg.read('setup.cfg'); print(cfg['metadata']['name'])")
REPO_ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# Typechecker configuration
# Recommended: Enable mypy (comprehensive) and ty (fast)
RUN_MYPY := 1
RUN_TY := 1
# Optional: Disable slower or redundant checkers for faster CI/CD
RUN_PYRIGHT := 0
RUN_BASEDPYRIGHT := 0
RUN_PYREFLY := 0
# Note: RUN_PYTYPE is controlled by shared/Makefile based on Python version

export
include shared/Makefile