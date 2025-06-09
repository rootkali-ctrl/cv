#!/bin/bash
# Make sure we're in the right directory
ls -la
echo "Current directory: $(pwd)"
echo "Python path: $(which python)"
python -c "import sys; print('Python version:', sys.version)"
uvicorn main:app --host 0.0.0.0 --port $PORT
