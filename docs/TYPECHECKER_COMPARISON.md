# Type Checker Comparison for reference_package

This document compares the performance and characteristics of different Python type checkers integrated into the `reference_package` project.

## Executive Summary

**Recommended Primary Type Checker: `mypy`**

**Secondary Recommendation: `ty` (for speed) or `basedpyright` (for strictness)**

All type checkers have been successfully integrated and are passing without errors. Based on performance testing, community support, and feature analysis, `mypy` is recommended as the primary type checker, with `ty` as an excellent secondary choice for rapid feedback during development.

## Type Checkers Evaluated

1. **pytype** (Google) - Legacy tool, Python 3.12 only
2. **mypy** (Python community standard)
3. **pyright** (Microsoft)
4. **basedpyright** (Community fork of pyright)
5. **ty** (Astral/Ruff team)
6. **pyrefly** (Meta/Instagram)

## Performance Comparison

Performance measured on reference_package codebase (19 Python files):

| Tool          | Avg Runtime | Speed Rank | Notes                           |
|---------------|-------------|------------|---------------------------------|
| ty            | 0.034s      | 1 (Fastest)| Rust-based, extremely fast      |
| mypy          | 0.193s      | 2          | Python-based, well-optimized    |
| pyrefly       | 0.213s      | 3          | Rust-based, good performance    |
| pytype        | 0.837s      | 4          | Python-based, moderate speed    |
| pyright       | 1.078s      | 5          | TypeScript/Node.js based        |
| basedpyright  | 1.105s      | 6          | TypeScript/Node.js based        |

### Speed Analysis

- **ty** is ~6x faster than mypy and ~30x faster than pyright
- **mypy** provides excellent balance of speed and features
- **pytype** has reasonable performance but is deprecated for Python 3.13+
- **pyright/basedpyright** are slower due to Node.js runtime overhead

**Note on Performance:** Performance can vary significantly between systems. On macOS, mypy may show different performance characteristics compared to Linux. The timings above were measured on Linux x86_64.

### Cache Management

To ensure accurate performance measurements, you may want to clear type checker caches:

- **pytype**: `rm -rf .pytype` (creates `.pytype` directory)
- **mypy**: `rm -rf .mypy_cache` (creates `.mypy_cache` directory)
- **pyright**: No persistent cache directory (uses in-memory cache)
- **basedpyright**: No persistent cache directory (uses in-memory cache)
- **ty**: No persistent cache directory (uses in-memory cache)
- **pyrefly**: No persistent cache directory (uses in-memory cache)

The `make clean` target clears pytype cache but not mypy cache. For a complete clean state:
```bash
rm -rf .pytype .mypy_cache
```

## Feature Comparison

### Strictness and Error Detection

1. **basedpyright** - Most configurable strictness, community-driven improvements
2. **pyright** - Microsoft-maintained, well-documented
3. **mypy** - De facto standard, excellent type inference
4. **ty** - Fast and strict, vendored stdlib stubs
5. **pyrefly** - Meta's tool, production-tested at scale
6. **pytype** - Good inference, but deprecated for Python 3.13+

### Community Support and Maintenance

| Tool          | Maintainer     | GitHub Stars | Active Development | Python 3.13+ Support |
|---------------|----------------|--------------|-------------------|----------------------|
| mypy          | Python/Community| ~18k        | Very Active       | ✓ Yes                |
| pyright       | Microsoft      | ~13k         | Very Active       | ✓ Yes                |
| basedpyright  | Community      | ~2k          | Active            | ✓ Yes                |
| ty            | Astral (Ruff)  | New (~2k)    | Very Active       | ✓ Yes                |
| pyrefly       | Meta           | Limited      | Active            | ✓ Yes                |
| pytype        | Google         | ~5k          | Deprecated        | ✗ No (3.12 max)      |

### Configuration Complexity

| Tool          | Config Location    | Complexity | Conflicts with Others |
|---------------|--------------------|------------|-----------------------|
| mypy          | pyproject.toml     | Medium     | No                    |
| pyright       | pyproject.toml     | Low        | Yes (basedpyright)    |
| basedpyright  | basedpyright.toml  | Low        | Yes (pyright)         |
| ty            | pyproject.toml     | Low        | No                    |
| pyrefly       | Default            | Very Low   | No                    |
| pytype        | pytype.cfg         | Low        | No                    |

## Detailed Recommendations

### Primary Recommendation: mypy

**Strengths:**
- Industry standard with widespread adoption
- Excellent documentation and community support
- Good balance of speed (0.193s) and features
- Rich ecosystem of plugins and type stubs
- Works well with all Python versions including 3.13+
- Actively maintained by Python community

**Configuration:**
```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
ignore_missing_imports = true
files = ["src", "tests"]
```

### Secondary Recommendation: ty

**Strengths:**
- Extremely fast (0.034s - 6x faster than mypy)
- Written in Rust for maximum performance
- From Astral team (creators of Ruff, uv)
- Modern architecture with vendored stdlib stubs
- Excellent for rapid development feedback
- Growing community support

**Use Case:** Run `ty` during development for instant feedback, use `mypy` for comprehensive CI/CD checks.

**Configuration:**
```toml
[tool.ty]
[tool.ty.rules]
unresolved-import = "ignore"
```

### Alternative: basedpyright (for strictness)

**Strengths:**
- Community-driven improvements over pyright
- Very configurable strictness levels
- Good error messages
- Active development

**Weaknesses:**
- Slower than mypy and ty (1.105s)
- Requires Node.js runtime
- Cannot coexist with pyright config in pyproject.toml

**Use Case:** Teams wanting Microsoft pyright features with community enhancements.

## Tools to Phase Out

### pytype (Deprecation Recommended)

**Reason:** Google has deprecated pytype for Python 3.13+. While it still works for Python 3.12, it should be phased out in favor of actively maintained alternatives.

**Migration Path:** Replace with mypy as primary checker.

## Implementation Status

All type checkers are currently enabled and configured:

```makefile
# Makefile
RUN_MYPY ?= 1
RUN_PYRIGHT ?= 1
RUN_BASEDPYRIGHT ?= 1
RUN_TY ?= 1
RUN_PYREFLY ?= 1
RUN_PYTYPE ?= 1  # Only for Python 3.12
```

## Final Recommendations

### Immediate Actions

1. **Keep mypy enabled** as the primary type checker
2. **Keep ty enabled** for fast feedback during development
3. **Consider disabling** slower tools (pyright, basedpyright) to speed up CI/CD
4. **Keep pyrefly** as a third opinion for production code
5. **Plan to disable pytype** when upgrading to Python 3.13

### Minimal Configuration (Recommended)

For optimal CI/CD performance, enable only:
- **mypy** (primary, comprehensive)
- **ty** (secondary, speed)

Disable or make optional:
- pyright (redundant with mypy)
- basedpyright (redundant with mypy)
- pyrefly (optional, third opinion)
- pytype (deprecated)

### Configuration Variables for Minimal Setup

```makefile
# Makefile - Recommended minimal configuration
RUN_MYPY ?= 1
RUN_TY ?= 1
RUN_PYRIGHT ?= 0
RUN_BASEDPYRIGHT ?= 0
RUN_PYREFLY ?= 0
RUN_PYTYPE ?= 0
```

## Appendix: Runtime Details

### Test Environment
- Python version: 3.12.3
- Files analyzed: 19 Python source files
- Test runs: 3 iterations per tool
- Platform: Linux x86_64

### Individual Tool Runtimes

**ty:**
- Run 1: 0.033s
- Run 2: 0.035s
- Run 3: 0.035s
- Average: 0.034s

**mypy:**
- Run 1: 0.193s
- Run 2: 0.193s
- Run 3: 0.194s
- Average: 0.193s

**pyrefly:**
- Run 1: 0.213s
- Run 2: 0.206s
- Run 3: 0.219s
- Average: 0.213s

**pytype:**
- Run 1: 0.839s
- Run 2: 0.830s
- Run 3: 0.841s
- Average: 0.837s

**pyright:**
- Run 1: 1.079s
- Run 2: 1.100s
- Run 3: 1.056s
- Average: 1.078s

**basedpyright:**
- Run 1: 1.110s
- Run 2: 1.113s
- Run 3: 1.091s
- Average: 1.105s

## References

- [mypy documentation](https://mypy.readthedocs.io/)
- [pyright documentation](https://github.com/microsoft/pyright)
- [basedpyright documentation](https://github.com/DetachHead/basedpyright)
- [ty documentation](https://docs.astral.sh/ty/)
- [pyrefly documentation](https://github.com/facebook/pyrefly)
- [pytype documentation](https://google.github.io/pytype/)
