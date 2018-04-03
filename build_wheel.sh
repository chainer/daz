#!/bin/bash -uex

# Build wheels using manylinux1 Docker image provided by PyPA:
# https://github.com/pypa/manylinux

PKG_DIR="$(cd "$(dirname $0)"; pwd)"

function run_manylinux() {
  docker run \
    --rm \
    --user $(id -u):$(id -g) \
    --volume "${PKG_DIR}:/package" \
    --workdir /package \
    quay.io/pypa/manylinux1_x86_64 \
    "$@"
}

rm -rf dist
for PYTHON in cp27-cp27m cp27-cp27mu cp33-cp33m cp34-cp34m cp35-cp35m cp36-cp36m; do
  # Compile wheels.
  run_manylinux /opt/python/${PYTHON}/bin/python setup.py bdist_wheel

  # Convert platform tag from `linux` to `manylinux1`.
  run_manylinux auditwheel repair dist/*-*-${PYTHON}-linux_x86_64.whl
done
