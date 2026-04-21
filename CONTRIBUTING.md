# Contributing

Thank you for your interest in improving the Human-Confabulated Hallucination Benchmark. This project welcomes contributions that extend the dataset, improve the tooling, or replicate results across new settings.

## Ways to contribute

### Extend the dataset

The core contribution of this project is the methodology, not the 212-pair proof of concept. The most valuable contributions add new confabulated pairs following the construction protocol:

1. Pick a domain (existing or new).
2. Write a question that a domain professional would answer confidently.
3. Generate a grounded response using a capable LLM and verify it against an authoritative source.
4. Write a confabulated response from memory — no sources, no lookups. The response must sound convincing to a non-expert.
5. Submit a pull request adding rows to `data/human_confabulations.csv`.

Each confabulated response should be written by someone who is **not** a domain expert in the topic. This is what produces genuine confabulation rather than deliberate falsification.

### Add new languages

The current dataset is English-only. Confabulation patterns may differ across languages — contributions that replicate the methodology in other languages are particularly welcome.

### Replicate with new embedding models

Run `scripts/validate.py --model <your-model>` and report results. If you test a model family not covered in the paper (e.g., multilingual models, domain-specific models, or models released after publication), open an issue or PR with your findings.

### Improve the tooling

Bug fixes, new analysis scripts, or visualization tools are welcome. Please follow the code standards below.

## Code standards

- Python 3.10+ with `from __future__ import annotations`.
- Full PEP 484 type annotations on all function signatures and return types.
- Use `dataclasses` for structured return values.
- Format with [ruff](https://docs.astral.sh/ruff/) (`ruff format`) and lint with `ruff check`.
- Docstrings on all public functions (Google style or NumPy style, be consistent within a file).

## Submitting a pull request

1. Fork the repository and create a feature branch from `main`.
2. Make your changes following the standards above.
3. If extending the dataset, verify the CSV parses correctly: `python examples/basic_usage.py`.
4. If modifying scripts, run `python scripts/validate.py` to confirm nothing breaks.
5. Write a clear PR description explaining what you changed and why.

## Reporting issues

Open an issue for:

- Errors in the grounded responses (we verified against sources, but mistakes happen).
- CSV parsing problems in specific environments.
- Suggestions for new domains or methodological improvements.

## Citation

If you use or extend this benchmark in published work, please cite the paper:

```bibtex
@misc{marin2026confabulation,
  author       = {Mar{\'\i}n, Javier},
  title        = {A Methodology for Building Human-Confabulated Hallucination Benchmarks},
  year         = {2026},
  url          = {https://github.com/Javihaus/cert-confabulation-benchmark}
}
```

## License

By contributing, you agree that your contributions will be licensed under CC BY 4.0 (dataset) and MIT (code), consistent with the existing project licenses.
