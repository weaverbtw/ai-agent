# AI Coding Agent

A command-line AI coding agent built with Python as part of the [Boot.dev](https://www.boot.dev/) Backend Developer Path. The agent uses large language models through OpenRouter to inspect files, modify code, and execute Python scripts.

The project demonstrates LLM API integration, function calling, multi-step task execution, and filesystem operations.

## Features

- **File inspection:** List files and directories and read file contents.
- **File modification:** Create or overwrite files within a configured working directory.
- **Python execution:** Execute Python scripts and capture their output, errors, and exit status.
- **LLM function calling:** Allow the language model to select tools and provide their arguments.
- **Multi-step execution:** Return tool results to the model so it can continue working toward a requested goal.
- **Verbose mode:** Display messages and token usage information for debugging.

## Technologies

- Python 3.12+
- OpenRouter API
- OpenAI Python SDK
- python-dotenv
- uv (dependency management)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/weaverbtw/ai-agent.git
cd ai-agent
```

### 2. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if necessary, then run:

```bash
uv sync
```

### 3. Configure your API key

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Obtain an API key from [OpenRouter](https://openrouter.ai/).

Never commit your API key to GitHub. The `.env` file is excluded through `.gitignore`.

### 4. Run the agent

```bash
uv run python main.py "Explain how the calculator works"
```

For more detailed diagnostic output:

```bash
uv run python main.py "List the files in the project" --verbose
```

The agent currently uses the OpenRouter free-model router. Model availability and usage limits depend on OpenRouter.

## How It Works

1. The user provides a prompt through the command line.
2. The application sends the prompt, system instructions, and available tool definitions to the language model.
3. The model can request a tool call to inspect, modify, or execute code.
4. The application dispatches the tool call to the corresponding Python function.
5. The tool result is returned to the model as additional conversation context.
6. The process repeats until the model responds without another tool call or reaches the configured limit of 20 iterations.

## Project Structure

```text
ai-agent/
├── main.py
├── call_function.py
├── prompts.py
├── functions/
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/
├── pyproject.toml
└── README.md
```

- `main.py`: Command-line interface, LLM API integration, and agent loop.
- `call_function.py`: Tool registration and function dispatch.
- `prompts.py`: System instructions for the agent.
- `functions/`: Implementations of the available tools.
- `calculator/`: Sample Python application used to demonstrate and test the agent.

## Limitations and Security

This is an educational project, not a production-ready or securely sandboxed coding agent.

- File operations use working-directory path checks, but these are not a complete security boundary.
- Python scripts execute as local subprocesses and are not isolated from the host environment.
- The agent can overwrite files within its allowed workspace.
- The agent is limited to 20 model-response iterations per request.
- LLM responses and tool calls can fail or produce unexpected results.

**Only run this agent with trusted local files in a controlled development environment.**

## Project Background

Built through Boot.dev to practice integrating large language models with traditional Python software, implementing function-calling workflows, and managing multi-step program execution.