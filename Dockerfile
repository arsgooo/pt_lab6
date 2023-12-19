FROM python
ADD pawnshop.py /
RUN pip install flask
RUN pip install flask_testing
EXPOSE 8080
CMD [ "python", "./pawnshop.py" ]