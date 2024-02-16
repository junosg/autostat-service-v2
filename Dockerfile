FROM python:3.10-alpine3.17
WORKDIR /src

RUN pip install fastapi
RUN pip install "uvicorn[standard]"
RUN pip install Cython
RUN pip install --upgrade pip
RUN pip install scipy
RUN pip install numpy
RUN pip install pandas
RUN pip install --upgrade patsy
RUN pip install -U statsmodels
RUN pip install scikit-posthocs
RUN pip install python-multipart
RUN pip install openpyxl

COPY . /src
ENV APP=app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]
