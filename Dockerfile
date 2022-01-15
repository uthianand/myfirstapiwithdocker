FROM python:3
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r packages.txt
EXPOSE 5000
USER 10001
CMD [ "python", "main.py" ]