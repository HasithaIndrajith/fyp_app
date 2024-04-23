# start by pulling the python image
FROM python:3.8-alpine

# Install Git
RUN apk add --no-cache git

# clone the seq2vec repository
RUN git clone https://github.com/anuradhawick/seq2vec.git /app/seq2vec

# switch working directory to seq2vec
WORKDIR /app/seq2vec

# run the build script
RUN chmod +x build.sh && ./build.sh

# switch back to the app directory
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["view.py" ]


