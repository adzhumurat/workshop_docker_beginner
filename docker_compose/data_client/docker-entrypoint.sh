#!/bin/bash -e

case "$1" in
  load)
    bash load_data.sh
    ;;
  *)
    exec "$@"
esac