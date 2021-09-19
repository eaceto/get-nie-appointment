# get-nie-appointment
A Python script that automates the process of getting an appointment for NIE assignation. It can be modified in order to change the type of appointment.

## Requirements

* Python3
* Selenium
* Firefox installed
* Gecko Driver

### Installing in Debian based distributions

* Install pip3 and geckodriver
```sh
sudo apt-get install pip3 firefox-geckodriver
```

* Install selenium
```sh
pip3 install selenium
```

### Installing in macOS

* Get pip
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

* Install pip
```sh
python3 get-pip.py
```

* Install selenium
```sh
pip3 install selenium
```

* Install
```sh
brew install geckodriver
```

## Running the script

```sh
python3 nie.py <city> <passport> <full name> <country> <year of birth> <telephone> <email> <appointment type>
```

for example

```sh
python3 nie.py  Madrid AAE1111111 "Ezequiel Leonardo Aceto" ARGENTINA XXXX 64XXXXXXX my-persona-email@gmail.com "POLICIA-ASIGNACIÓN DE NIE"
```

## Parameters

For getting the requiered parameters, city and appointment type, visit: https://sede.administracionespublicas.gob.es/icpplustieb/index/ and complete the process one type manually. Then get the appointment type based on your city (which may vary from city to city).
