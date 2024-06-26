FROM seleniumbase
WORKDIR /casedir
COPY . /casedir/
RUN pip install -r requirements.txt
CMD ["pytest","./TestCase/","--alluredir","allureResults"]
