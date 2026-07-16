@echo off
echo Launching MicroHydro Matrix Monitor...
cd /d C:\MircoHydro
C:\MircoHydro\.venv\Scripts\streamlit.exe run research/microhydro_matrix_monitor.py --server.headless true --server.port 8501
start http://localhost:8501
echo Matrix Monitor launched. Browser should open automatically.