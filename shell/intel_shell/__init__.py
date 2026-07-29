"""intel_shell: the product layer of the intel-platform core-shell split.

Everything in this package is deliberately hot-editable: prompts, brief
copy, subscription logic, API shapes, pipeline orchestration. None of it
requires touching (or recompiling) the Rust core, whose internal JSON contract
is wrapped by `core_client.CoreClient`.
"""

__version__ = "0.15.5"
