@echo off
echo Launching MicroHydro AZ Executive Assistant...
cd /d C:\MircoHydro
C:\MircoHydro\.venv\Scripts\streamlit.exe run research/microhydro_az_assistant.py --server.headless true --server.port 8502
start http://localhost:8502
echo AZ Assistant launched. Browser should open automatically.