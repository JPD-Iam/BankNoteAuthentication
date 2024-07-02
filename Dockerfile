# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim
WORKDIR /app
COPY . /app/
RUN python -m pip install -r requirements.txt

EXPOSE 5000
CMD ["flask","run","--host","0.0.0.0"]
