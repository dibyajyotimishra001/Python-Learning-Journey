# Object-Oriented Calculator (v3.0)

A high-performance command-line calculation engine engineered in Python, utilizing strict Object-Oriented Programming (OOP) paradigms and rigorous input-boundary validation.

## Architecture Evolution
* **v1.0**: Core mathematical logic executed via linear script architecture.
* **v2.0**: Refactored execution using modular procedural functions.
* **v3.0 (Current)**: Transitioned to full Object-Oriented Programming (OOP), encapsulating behavioral logic within an independent class structures.

## Core Architectural Features

| Optimization Domain | Implementation Strategy |
| :--- | :--- |
| **Object-Oriented Design** | Encapsulates mathematical operations inside a dedicated `Calculator` class, keeping the execution logic entirely decoupled from the main operational runtime. |
| **Defensive Exception Handling** | Employs an aggressive top-level `try-except` structure to trap explicit runtime anomalies such as `ValueError` during input parsing, achieving high structural resilience. |
| **Pre-emptive Zero-Division Check** | Implements an immediate short-circuit check via `sys.exit()` before class invocation to neutralize mathematical undefined states (`/0`) at the application entry point. |

## Verification & Execution

### Prerequisites
* Python 3.x runtime environment.

### Local Execution Pipeline
1. Clone or download the source repository.
2. Initialize the terminal interface and navigate to the target directory.
3. Execute the script using the native Python engine:
   ```bash
   python "Calculator with oops.py"