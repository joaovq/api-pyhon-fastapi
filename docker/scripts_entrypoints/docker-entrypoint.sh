#!/bin/bash
set -e

# Install requirements
uvicorn main:app --host 0.0.0.0 --port "80"