"""One way to call any model: ask(text, system, model), with model given as provider:name.

    claude:sonnet   the `claude` command line in print mode (your Claude Code login, no API key)
    gemini:<name>   the Gemini API, with the key in GEMINI_API_KEY (not built yet)

A bare name ("sonnet") means claude.
"""
import subprocess
import sys
import tempfile


def split(model):
    provider, _, name = model.partition(":")
    return (provider, name) if name else ("claude", provider)


def ask_claude(text, system, name):
    """From an empty directory, with no tools, settings or MCP servers: it sees only the prompt."""
    cmd = ["claude", "-p", "--model", name, "--tools", "", "--no-session-persistence",
           "--setting-sources", "", "--strict-mcp-config", "--system-prompt", system,
           "--output-format", "text"]
    with tempfile.TemporaryDirectory() as empty:
        out = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=empty, timeout=900)
    if out.returncode != 0:
        sys.exit(f"claude failed ({out.returncode}): {out.stderr.strip() or out.stdout.strip()}")
    return out.stdout.strip()


def ask(text, system, model):
    provider, name = split(model)
    if provider == "claude":
        return ask_claude(text, system, name)
    if provider == "gemini":
        raise NotImplementedError("Gemini is a later step: see backlog #7")
    raise ValueError(f"unknown provider {provider!r}")
