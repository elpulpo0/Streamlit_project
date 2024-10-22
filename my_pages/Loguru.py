from loguru import logger
from io import StringIO
import streamlit as st

log_buffer = StringIO()

logger.remove()

if not any(level.name == "POULPE" for level in logger._core.levels.values()):
    logger.level("POULPE", no=15, color="<cyan>", icon="🐙")

logger.add(log_buffer, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name}:{function}:{line} - {message}")

fake_console = """
        <span style="color:green;">chris@pc</span>
        <span style="color:purple;">CUSTOM</span>
        <span style="color:yellow;">~Documents/Github/Projects/Apps/Streamlit/</span>
        <span style="color:#bd93f9;">(main)</span><br>
        <span style="color:white;">$ streamlit run main.py</span><br><br>
        <span style="color:#bd93f9;">You can now view your Streamlit app in your browser.</span><br>
        <span style="color:#bd93f9;">Local URL:</span>
        <span style="color:white;">http://localhost:8501</span><br>
        <span style="color:#bd93f9;">Network URL:</span>
        <span style="color:white;">https://chris4simplon.streamlit.app</span><br>
    """
def delete_logs():
    log_buffer.truncate(0)
    log_buffer.seek(0)

def format_logs(log_output):
    lines = log_output.splitlines()
    formatted_lines = []
    formatted_lines.append(fake_console)
    for line in lines:
        if "DEBUG" in line:
            formatted_lines.append(f'<span style="color: green;">{line}</span>')
        elif "INFO" in line:
            formatted_lines.append(f'<span style="color: light blue;">{line}</span>')
        elif "WARNING" in line:
            formatted_lines.append(f'<span style="color: yellow;">{line}</span>')
        elif "ERROR" in line:
            formatted_lines.append(f'<span style="color: red;">{line}</span>')
        elif "CRITICAL" in line:
            formatted_lines.append(f'<span style="color: orange;">{line}</span>')
        elif "POULPE" in line:
            formatted_lines.append(f'<span style="color: cyan;">{line}</span>')
        else:
            formatted_lines.append(line)
    return "<br>".join(formatted_lines)

def run_page4():

    st.header('Exploration des logs avec Loguru')

    st.subheader('Paramètres des logs')

    log_level = st.selectbox("Choisissez un niveau de log", ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "POULPE"])

    log_message = st.text_input("Entrez un message de log")

    def generate_log(log_level, log_message):
        log_levels = {
            "DEBUG": logger.debug,
            "INFO": logger.info,
            "WARNING": logger.warning,
            "ERROR": logger.error,
            "CRITICAL": logger.critical,
            "POULPE": lambda msg: logger.log("POULPE", msg),
        }

        if log_message:
            log_function = log_levels.get(log_level)
            if log_function:
                log_function(log_message)

    if st.button("Générer le log"):
        if log_message:
            generate_log(log_level, log_message)
        else:
            st.warning("Veuillez entrer un message de log.")

    if st.button("Supprimer les logs"):
        delete_logs()


    st.subheader("Console des logs")
    log_output = log_buffer.getvalue()

    formatted_log_output = format_logs(log_output)

    st.markdown(f'<div style="background:black; color:white; padding:10px; border-radius:5px; height:300px; overflow:auto;">{formatted_log_output}</div>', unsafe_allow_html=True)
