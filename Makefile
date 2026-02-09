PYTHON_VERSION := 3.12
PACKAGE_NAME := $(shell python -c "import configparser; cfg = configparser.ConfigParser(); cfg.read('setup.cfg'); print(cfg['metadata']['name'])")
REPO_ROOT := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# Typechecker configuration
RUN_MYPY ?= 1
RUN_PYRIGHT ?= 1
RUN_BASEDPYRIGHT ?= 1
RUN_TY ?= 1
RUN_PYREFLY ?= 1

export
include shared/Makefile