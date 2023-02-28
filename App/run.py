from streamlit.web import bootstrap

real_script = 'main_script.py'
bootstrap.run(real_script, f'run.py {real_script}', [], {})