use uvicorn app_fastapi:app --host 0.0.0.0 --port 8000 to run fastapi
use streamlit run app_streamlit.py to run streamlit app
 

 If you want to build the docker Image use:
 use docker build -t students .
 docker run -p 8000:8000 -p 8501:8501 students

