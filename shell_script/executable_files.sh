#!/bin/bash
set -e

cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/.."
{
  ## Executable file style python3
  chmod u+x ./*.py ./models/*.py ./models/engine/*.py ./tests/*.py ./tests/test_models/*.py ./tests/test_models/test_engine/*.py
  ## Executable shell script
  chmod u+x ./shell_script/*.sh
}
