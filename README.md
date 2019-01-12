# Histrock

A django application for historic stock data analysis along with real-time stock charts and economic calender.

## Features

* Check historical stock trend analysis on responsive charts which can be exported as png.
* Realtime economic calender displaying latest events. 
* Automatically selects oldest or most records if start or end date not given.
* Realtime stock chart. 

* Easy-to-implement REST API. 

## Screenshots
![Screenshot](https://i.imgur.com/AuKMLKCg.png "Screenshot")
![Screenshot](https://i.imgur.com/9tPKT3l.png "Screenshot")
![REST API](https://i.imgur.com/I6FsVud.png "REST API")

## Demonstration 
Click on the below image to watch a short video demonstration. 

[![Histrock Video Demonstration](http://img.youtube.com/vi/GxMvHH_aJm0/0.jpg)](http://www.youtube.com/watch?v=GxMvHH_aJm0 "Histrock ")

## Installation

Clone the repository locally. 
```bash
git clone https://github.com/defcon-007/histrock 

```

Now create a virtual environment for the project 
```bash
pip3 install virtualenv
virtualenv -p python3 ./venvhistrock
```

Activate the virtual environment
```bash 
source venvhistrock/bin/activate
```


Install the required modules 
```bash
cd histrock
pip install -r requirements.txt
```

Now make a local copy of the `config-template.ini` and complete the fields accordingly. (Postgresql database is recommended)
```bash
cp ./config-templat.ini ./config.ini
vim config.ini
```

Collect static django assets
```bash
python manage.py collectstatic
```

Run migrations
```bash
python manage.py migrate
```

Now download the Postgresql database dump using `curl` or any other downloader of your choice or by clicking [here](https://s3.ap-south-1.amazonaws.com/defcon-public-static-assets/histrockDump.dump). 

```bash
curl https://s3.ap-south-1.amazonaws.com/defcon-public-static-assets/histrockDump.dump -o ../histrock.dump
```

Assuming you have setup the postgres database with name "histrockdatabase" use the following command as root to add data to database. 
```bash
pg_restore -U postgres --data-only -d histrockdatabase -t api_stock ../histrockDump.dump
pg_restore -U postgres --data-only -d histrockdatabase -t api_stockhistoricdata ../histrockDump.dump
```

Now everything is setup run `python manage.py runserver` to run the local development server.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
