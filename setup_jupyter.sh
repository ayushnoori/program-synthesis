#!/bin/bash
conda deactivate
source synthesis_env/bin/activate
jupyter notebook --port=54321 --browser='none'
