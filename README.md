## Very simple sherdog api

I created this api for help me in my project about sports social networks ranking.

### Cloning and Install

```
git clone https://github.com/drcoelho/sherdog
```

```
sudo python setup.py install
```

### Usage

```
from sherdog import Sherdog
sherdog = Sherdog('http://www.sherdog.com/fighter/')
print sherdog.find('Jose-Aldo-1150')
```
