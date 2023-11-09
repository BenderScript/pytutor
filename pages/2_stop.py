import os
import shutil
import time

import keyboard
import psutil
import streamlit as st

time.sleep(2)

# check if the directory exists
if os.path.exists(st.session_state.temp_dir):
    # remove the directory and all its contents
    shutil.rmtree(st.session_state.temp_dir)
# Close streamlit browser tab
keyboard.press_and_release('ctrl+w')
# Terminate streamlit python process
pid = os.getpid()
p = psutil.Process(pid)
p.terminate()
