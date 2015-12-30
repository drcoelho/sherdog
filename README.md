## Very simple sherdog api

I created this api for help me in my project about sports social networks ranking. I needed to build a graph with all mma fighters, so I wrote this code to help in that job.

It is very simple, class Sherdog receive the url root and fighter id, make a request and parse html. The return is a json representation of a fighter.

Fighter id can be complete fighter id or just the code id. Example: Jose-Aldo-11506 or 11506 works as same for sherdog website.

### Requirements 

* BeautifulSoup - http://www.crummy.com/software/BeautifulSoup/
* Python lxml - http://lxml.de/

### Cloning and Install

```
git clone https://github.com/drcoelho/sherdog
cd sherdog
sudo python setup.py install
```

### Usage

```
from sherdog import Sherdog
sherdog = Sherdog('http://www.sherdog.com/fighter/')
response_code, json = sherdog.find('Jose-Aldo-11506')
print(json)
```

You'll get a print console like this

```
{
	"weight": "145 lbs",
	"fighter_id": "Jose-Aldo-11506",
	"full_name": "Jose Aldo",
	"nationality": "Brazil",
	"height": "5'7\"",
	"nickname": "Scarface",
	"association": "Nova Uniao",
	"fighter_code_id": "Jose-Aldo-11506",
	"amateur_history": [],
	"weight_class": "Featherweight",
	"address_locality": "Manaus, Amazonas",
	"birth_date": "1986-09-09",
	"fight_results": [{
		"opponent_name": "Conor McGregor",
		"event_url": "/events/UFC-194-Aldo-vs-McGregor-42245",
		"result": "loss",
		"time": "0:13",
		"event_name": "UFC 194 - Aldo vs. McGregor",
		"event_date": "N/A",
		"referee": "John McCarthy",
		"method": "KO (Punch)",
		"round": "1",
		"opponent": "/fighter/Conor-McGregor-29688"
	}, {
		"opponent_name": "Chad Mendes",
		"event_url": "/events/UFC-179-Aldo-vs-Mendes-2-37749",
		"result": "win",
		"time": "5:00",
		"event_name": "UFC 179 - Aldo vs. Mendes 2",
		"event_date": "N/A",
		"referee": "Marc Goddard",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Chad-Mendes-38393"
	}, {
		"opponent_name": "Ricardo Lamas",
		"event_url": "/events/UFC-169-Barao-vs-Faber-2-32773",
		"result": "win",
		"time": "5:00",
		"event_name": "UFC 169 - Barao vs. Faber 2",
		"event_date": "N/A",
		"referee": "Keith Peterson",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Ricardo-Lamas-32051"
	}, {
		"opponent_name": "Chan Sung Jung",
		"event_url": "/events/UFC-163-Aldo-vs-Korean-Zombie-28015",
		"result": "win",
		"time": "2:00",
		"event_name": "UFC 163 - Aldo vs. Korean Zombie",
		"event_date": "N/A",
		"referee": "Herb Dean",
		"method": "TKO (Punches)",
		"round": "4",
		"opponent": "/fighter/Chan-Sung-Jung-36155"
	}, {
		"opponent_name": "Frankie Edgar",
		"event_url": "/events/UFC-156-Aldo-vs-Edgar-26099",
		"result": "win",
		"time": "5:00",
		"event_name": "UFC 156 - Aldo vs. Edgar",
		"event_date": "N/A",
		"referee": "Steve Mazzagatti",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Frankie-Edgar-14204"
	}, {
		"opponent_name": "Chad Mendes",
		"event_url": "/events/UFC-142-Aldo-vs-Mendes-18901",
		"result": "win",
		"time": "4:59",
		"event_name": "UFC 142 - Aldo vs. Mendes",
		"event_date": "N/A",
		"referee": "Mario Yamasaki",
		"method": "KO (Knee)",
		"round": "1",
		"opponent": "/fighter/Chad-Mendes-38393"
	}, {
		"opponent_name": "Kenny Florian",
		"event_url": "/events/UFC-136-Edgar-vs-Maynard-3-17391",
		"result": "win",
		"time": "5:00",
		"event_name": "UFC 136 - Edgar vs. Maynard 3",
		"event_date": "N/A",
		"referee": "Dan Miragliotta",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Kenny-Florian-8021"
	}, {
		"opponent_name": "Mark Hominick",
		"event_url": "/events/UFC-129-St-Pierre-vs-Shields-15427",
		"result": "win",
		"time": "5:00",
		"event_name": "UFC 129 - St. Pierre vs. Shields",
		"event_date": "N/A",
		"referee": "John McCarthy",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Mark-Hominick-4728"
	}, {
		"opponent_name": "Manny Gamburyan",
		"event_url": "/events/WEC-51-Aldo-vs-Gamburyan-14014",
		"result": "win",
		"time": "1:32",
		"event_name": "WEC 51 - Aldo vs. Gamburyan",
		"event_date": "N/A",
		"referee": "Herb Dean",
		"method": "KO (Punches)",
		"round": "2",
		"opponent": "/fighter/Manny-Gamburyan-5185"
	}, {
		"opponent_name": "Urijah Faber",
		"event_url": "/events/WEC-48-Aldo-vs-Faber-12597",
		"result": "win",
		"time": "5:00",
		"event_name": "WEC 48 - Aldo vs. Faber",
		"event_date": "N/A",
		"referee": "Josh Rosenthal",
		"method": "Decision (Unanimous)",
		"round": "5",
		"opponent": "/fighter/Urijah-Faber-8847"
	}, {
		"opponent_name": "Mike Thomas Brown",
		"event_url": "/events/WEC-44-Brown-vs-Aldo-11238",
		"result": "win",
		"time": "1:20",
		"event_name": "WEC 44 - Brown vs. Aldo",
		"event_date": "N/A",
		"referee": "Steve Mazzagatti",
		"method": "TKO (Punches)",
		"round": "2",
		"opponent": "/fighter/Mike-Thomas-Brown-3069"
	}, {
		"opponent_name": "Cub Swanson",
		"event_url": "/events/WEC-41-Brown-vs-Faber-2-9864",
		"result": "win",
		"time": "0:08",
		"event_name": "WEC 41 - Brown vs. Faber 2",
		"event_date": "N/A",
		"referee": "Steve Mazzagatti",
		"method": "TKO (Flying Knee and Punches)",
		"round": "1",
		"opponent": "/fighter/Cub-Swanson-11002"
	}, {
		"opponent_name": "Chris Mickle",
		"event_url": "/events/WEC-39-Brown-vs-Garcia-9492",
		"result": "win",
		"time": "1:39",
		"event_name": "WEC 39 - Brown vs. Garcia",
		"event_date": "N/A",
		"referee": "Rafael Ramos",
		"method": "TKO (Punches)",
		"round": "1",
		"opponent": "/fighter/Chris-Mickle-12021"
	}, {
		"opponent_name": "Rolando Perez",
		"event_url": "/events/WEC-38-Varner-vs-Cerrone-9329",
		"result": "win",
		"time": "4:15",
		"event_name": "WEC 38 - Varner vs. Cerrone",
		"event_date": "N/A",
		"referee": "Jon Schorle",
		"method": "KO (Knee and Punches)",
		"round": "1",
		"opponent": "/fighter/Rolando-Perez-13525"
	}, {
		"opponent_name": "Jonathan Brookins",
		"event_url": "/events/WEC-36-Faber-vs-Brown-7810",
		"result": "win",
		"time": "0:45",
		"event_name": "WEC 36 - Faber vs. Brown",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO (Punches)",
		"round": "3",
		"opponent": "/fighter/Jonathan-Brookins-17316"
	}, {
		"opponent_name": "Alexandre Franca Nogueira",
		"event_url": "/events/WEC-34-Sacramento-6995",
		"result": "win",
		"time": "3:22",
		"event_name": "WEC 34 - Sacramento",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO (Punches)",
		"round": "2",
		"opponent": "/fighter/Alexandre-Franca-Nogueira-431"
	}, {
		"opponent_name": "Shoji Maruyama",
		"event_url": "/events/Pancrase-2007-NeoBlood-Tournament-Finals-5151",
		"result": "win",
		"time": "5:00",
		"event_name": "Pancrase - 2007 Neo-Blood Tournament Finals",
		"event_date": "N/A",
		"referee": "Soichi Hiroto",
		"method": "Decision (Unanimous)",
		"round": "3",
		"opponent": "/fighter/Shoji-Maruyama-18886"
	}, {
		"opponent_name": "Fabio Mello",
		"event_url": "/events/TFC-3-Top-Fighting-Championships-3-5178",
		"result": "win",
		"time": "5:00",
		"event_name": "TFC 3 - Top Fighting Championships 3",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Decision (Unanimous)",
		"round": "3",
		"opponent": "/fighter/Fabio-Mello-2195"
	}, {
		"opponent_name": "Thiago Meller",
		"event_url": "/events/GFC-1-Gold-Fighters-Championship-3892",
		"result": "win",
		"time": "5:00",
		"event_name": "GFC 1 - Gold Fighters Championship",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Decision (Majority)",
		"round": "3",
		"opponent": "/fighter/Thiago-Meller-8186"
	}, {
		"opponent_name": "Luciano Azevedo",
		"event_url": "/events/JF-5-Jungle-Fight-5-3424",
		"result": "loss",
		"time": "3:37",
		"event_name": "JF 5 - Jungle Fight 5",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Rear-Naked Choke)",
		"round": "2",
		"opponent": "/fighter/Luciano-Azevedo-7919"
	}, {
		"opponent_name": "Micky Young",
		"event_url": "/events/FX3-Battle-of-Britain-3316",
		"result": "win",
		"time": "1:05",
		"event_name": "FX3 - Battle of Britain",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO (Punches)",
		"round": "1",
		"opponent": "/fighter/Micky-Young-12546"
	}, {
		"opponent_name": "Phil Harris",
		"event_url": "/events/UK1-Fight-Night-3282",
		"result": "win",
		"time": "0:00",
		"event_name": "UK-1 - Fight Night",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO (Doctor Stoppage)",
		"round": "1",
		"opponent": "/fighter/Phil-Harris-8753"
	}, {
		"opponent_name": "Anderson Silverio",
		"event_url": "/events/Meca-12-Meca-World-Vale-Tudo-12-3158",
		"result": "win",
		"time": "8:33",
		"event_name": "Meca 12 - Meca World Vale Tudo 12",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Soccer Kicks)",
		"round": "1",
		"opponent": "/fighter/Anderson-Silverio-13383"
	}, {
		"opponent_name": "Aritano Silva Barbosa",
		"event_url": "/events/RMMAC-Rio-MMA-Challenge-1-3056",
		"result": "win",
		"time": "0:20",
		"event_name": "RMMAC - Rio MMA Challenge 1",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "KO (Soccer Kicks)",
		"round": "1",
		"opponent": "/fighter/Aritano-Silva-Barbosa-2196"
	}, {
		"opponent_name": "Luiz de Paula",
		"event_url": "/events/Shooto-Brazil-7-2934",
		"result": "win",
		"time": "1:54",
		"event_name": "Shooto - Brazil 7",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Arm-Triangle Choke)",
		"round": "1",
		"opponent": "/fighter/Luiz-de-Paula-12515"
	}, {
		"opponent_name": "Hudson Rocha",
		"event_url": "/events/Shooto-Brazil-Never-Shake-2636",
		"result": "win",
		"time": "5:00",
		"event_name": "Shooto Brazil - Never Shake",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO (Doctor Stoppage)",
		"round": "1",
		"opponent": "/fighter/Hudson-Rocha-3922"
	}, {
		"opponent_name": "Mario Bigola",
		"event_url": "/events/EFC-1-Eco-Fight-Championship-1-8243",
		"result": "win",
		"time": "0:18",
		"event_name": "EFC 1 - Eco Fight Championship 1",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "KO (Head Kick)",
		"round": "1",
		"opponent": "/fighter/Mario-Bigola-58130"
	}]
}
```
