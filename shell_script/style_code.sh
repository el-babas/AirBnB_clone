#!/bin/bash
set -e

cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/.."
{
  ## Check file style python3
  pycodestyle ./*.py ./models/*.py ./models/engine/*.py ./tests/*.py ./tests/test_models/*.py ./tests/test_models/test_engine/*.py
  ## Check file style shell script
  shellcheck ./shell_script/*.sh
}
