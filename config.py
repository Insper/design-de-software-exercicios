from pathlib import Path


CUR_DIR = Path(__file__).parent
TRACES = CUR_DIR / 'traces'
CHALLENGES = CUR_DIR / 'challenges'
RAW_DIR = 'raw'
DETAILS = 'details.json'
QUESTION = 'question.md'
TRACE_CODE = 'code.py'
TRACE_DATA = 'trace.json'
TESTS = 'tests.py'
with open(CUR_DIR / 'concepts.txt') as f:
    CONCEPTS = [t.split(',')[1] for t in f.read().split() if t and len(t.split(',')) == 3]
