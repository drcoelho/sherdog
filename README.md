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
response_code, json = sherdog.find('Jose-Aldo-1150')
print(json)
```

You'll get a print console like this

```
{
	"weight": "0 lbs",
	"fighter_id": "Jose-Aldo-1150",
	"full_name": "Ryan Roath",
	"nationality": null,
	"height": "0'0\"",
	"nickname": null,
	"association": null,
	"fighter_code_id": "Ryan-Roath-1150",
	"amateur_history": [],
	"weight_class": "N/A",
	"address_locality": null,
	"birth_date": "N/A",
	"fight_results": [{
		"opponent_name": "Kyle Dennis",
		"event_url": "/events/WFC-Rumble-at-the-Ramada-5578",
		"result": "win",
		"time": "0:00",
		"event_name": "WFC - Rumble at the Ramada",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Guillotine Choke)",
		"round": "3",
		"opponent": "/fighter/Kyle-Dennis-22421"
	}, {
		"opponent_name": "Mike Rainier",
		"event_url": "/events/RITC-34-Rage-in-the-Cage-34-764",
		"result": "win",
		"time": "1:39",
		"event_name": "RITC 34 - Rage in the Cage 34",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "DQ",
		"round": "2",
		"opponent": "/fighter/Mike-Rainier-1779"
	}, {
		"opponent_name": "Joe Riggs",
		"event_url": "/events/RITC-30-Soaring-to-New-Heights-528",
		"result": "loss",
		"time": "2:32",
		"event_name": "RITC 30 - Soaring to New Heights",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Punches)",
		"round": "1",
		"opponent": "/fighter/Joe-Riggs-2765"
	}, {
		"opponent_name": "Brian Ryan",
		"event_url": "/events/RITC-29-Rage-in-the-Cage-29-524",
		"result": "loss",
		"time": "2:45",
		"event_name": "RITC 29 - Rage in the Cage 29",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO",
		"round": "3",
		"opponent": "/fighter/Brian-Ryan-1120"
	}, {
		"opponent_name": "Bill Rohlf",
		"event_url": "/events/RITC-28-Rage-in-the-Cage-28-409",
		"result": "win",
		"time": "1:16",
		"event_name": "RITC 28 - Rage in the Cage 28",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Keylock)",
		"round": "1",
		"opponent": "/fighter/Bill-Rohlf-1801"
	}, {
		"opponent_name": "Michael Simpson",
		"event_url": "/events/RITC-27-Rage-in-the-Cage-27-356",
		"result": "win",
		"time": "0:50",
		"event_name": "RITC 27 - Rage in the Cage 27",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Choke)",
		"round": "1",
		"opponent": "/fighter/Michael-Simpson-1820"
	}, {
		"opponent_name": "Elvis Hinkle",
		"event_url": "/events/RITC-25-Rage-in-the-Cage-25-348",
		"result": "win",
		"time": "3:00",
		"event_name": "RITC 25 - Rage in the Cage 25",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "TKO",
		"round": "1",
		"opponent": "/fighter/Elvis-Hinkle-1780"
	}, {
		"opponent_name": "Justin Lyon",
		"event_url": "/events/RITC-24-Rage-in-the-Cage-24-208",
		"result": "loss",
		"time": "0:29",
		"event_name": "RITC 24 - Rage in the Cage 24",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Punches)",
		"round": "2",
		"opponent": "/fighter/Justin-Lyon-1108"
	}, {
		"opponent_name": "Brian Ryan",
		"event_url": "/events/RITC-23-Rage-in-the-Cage-23-207",
		"result": "win",
		"time": "1:44",
		"event_name": "RITC 23 - Rage in the Cage 23",
		"event_date": "N/A",
		"referee": "N/A",
		"method": "Submission (Strikes)",
		"round": "1",
		"opponent": "/fighter/Brian-Ryan-1120"
	}]
}
```
