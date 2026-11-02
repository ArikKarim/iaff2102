"""Run each starter test suite in its own process and project directory."""
import os
from pathlib import Path
import subprocess
import sys

PROJECTS = (
    'mean-variance-standard-deviation-calculator',
    'demographic-data-analyzer',
    'medical-data-visualizer',
    'page-view-time-series-visualizer',
    'sea-level-predictor',
)


def main():
    root = Path(__file__).resolve().parent
    environment = dict(os.environ, MPLBACKEND='Agg')
    failed = []
    for project in PROJECTS:
        print(f'\nRunning {project}', flush=True)
        result = subprocess.run(
            [sys.executable, '-m', 'unittest', 'test_module', '-v'],
            cwd=root / project, env=environment,
        )
        if result.returncode:
            failed.append(project)
    if failed:
        print('\nFailed: ' + ', '.join(failed))
        return 1
    print('\nAll five project test suites passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
