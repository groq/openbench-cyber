# openbench-cyber

Cybersecurity evaluation plugin for [openbench](https://github.com/groq/openbench).

This package moves all cybersecurity-heavy benchmarks (CTI-Bench + CyBench) into a
separate optional dependency so that the core `openbench` distribution stays lean
while still supporting advanced security workloads.

## Installation

Install directly from Git or rely on the optional extra exposed by `openbench`:

```bash
uv pip install "openbench-cyber @ git+https://github.com/groq/openbench-cyber.git@main"

# or pull it in automatically via the optional extra
uv pip install "openbench[cyber]"
```

After installation, the new benchmarks automatically appear in `bench list` because
they are registered through openbench's entry-point based plugin system.

## Included Benchmarks

- `cti_bench_ate` – MITRE ATT&CK technique extraction
- `cti_bench_mcq` – CTI multiple-choice knowledge assessments
- `cti_bench_rcm` – CVE→CWE vulnerability classification
- `cti_bench_vsp` – CVSS severity regression
- `cybench` – Agentic CTF-style challenges powered by `inspect-cyber`

Run them exactly like any other benchmark:

```bash
bench eval cti_bench_vsp --model groq/llama-3.3-70b-versatile
bench eval cybench --env CYBENCH_ACKNOWLEDGE_RISKS=1
```

## Development

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
pre-commit install
```

The repository mirrors openbench's release automation (Release Please + PyPI publish)
so that security benchmarks can ship independently from the main project.
