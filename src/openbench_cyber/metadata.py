"""
Benchmark metadata definitions for the openbench-cyber plugin.
"""

from openbench.utils import BenchmarkMetadata


def get_benchmark_metadata() -> dict[str, BenchmarkMetadata]:
    """Return benchmark metadata exposed through the entry point."""
    return {
        "cti_bench_ate": BenchmarkMetadata(
            name="CTI-Bench ATE",
            description="Extracting MITRE ATT&CK techniques from malware and threat descriptions",
            category="cybersecurity",
            tags=["extraction", "cybersecurity"],
            module_path="openbench_cyber.evals.cti_bench",
            function_name="cti_bench_ate",
            subtask=True,
        ),
        "cti_bench_mcq": BenchmarkMetadata(
            name="CTI-Bench MCQ",
            description=(
                "Multiple-choice questions evaluating understanding of CTI standards, threats, "
                "detection strategies, and best practices using authoritative sources like NIST and MITRE"
            ),
            category="cybersecurity",
            tags=["multiple-choice", "cybersecurity", "knowledge"],
            module_path="openbench_cyber.evals.cti_bench",
            function_name="cti_bench_mcq",
            subtask=True,
        ),
        "cti_bench_rcm": BenchmarkMetadata(
            name="CTI-Bench RCM",
            description="Mapping CVE descriptions to CWE categories to evaluate vulnerability classification ability",
            category="cybersecurity",
            tags=["classification", "cybersecurity"],
            module_path="openbench_cyber.evals.cti_bench",
            function_name="cti_bench_rcm",
            subtask=True,
        ),
        "cti_bench_vsp": BenchmarkMetadata(
            name="CTI-Bench VSP",
            description="Calculating CVSS scores from vulnerability descriptions to assess severity evaluation skills",
            category="cybersecurity",
            tags=["regression", "cybersecurity"],
            module_path="openbench_cyber.evals.cti_bench",
            function_name="cti_bench_vsp",
            subtask=True,
        ),
        "cybench": BenchmarkMetadata(
            name="CyBench",
            description="CyBench: Cybersecurity CTF challenges benchmark",
            category="cybersecurity",
            tags=["cybersecurity", "ctf", "challenges", "graded"],
            module_path="openbench_cyber.evals.cybench",
            function_name="cybench",
        ),
        "cvebench": BenchmarkMetadata(
            name="CVEBench",
            description=(
                "Agentic exploitation benchmark targeting real-world CVE replicas "
                "with Dockerized victims and graders."
            ),
            category="cybersecurity",
            tags=["cybersecurity", "agentic", "docker", "exploit"],
            module_path="openbench_cyber.evals.cvebench",
            function_name="cvebench",
        ),
    }


__all__ = ["get_benchmark_metadata"]
