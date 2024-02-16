class NormalityResult:
    test: str
    statistics: dict[str, float]
    pvalues: dict[str, float]
    conclusions: dict[str, str]
    passed: bool
