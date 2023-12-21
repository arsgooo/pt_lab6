FROM python:3
WORKDIR /
COPY . .
RUN pip install flask
RUN pip install flask_restful
RUN pip install flask_testing
EXPOSE 8080
CMD [ "python", "./pawnshop.py" ]