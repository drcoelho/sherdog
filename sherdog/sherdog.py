#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import urllib2
import json
import traceback
import threading
import logging
from time import localtime, strftime, time
from bs4 import BeautifulSoup

# Constants
NONE_VALUE = 'N/A'
LOG_DATE_PATTERN = '%Y-%m-%d %H:%M:%S +0000'

# Result table constants
RESULT_MAX_COLUMNS = 6
RESULT = 0
OPPONENT = 1
EVENT = 2

METHOD_AND_REFEREE = 3
ONLY_METHOD = 0
ONLY_REFEREE = 1
METHOD_AND_REFEREE_SEPARATOR = '|'

ROUND = 4
TIME = 5

# logging.basicConfig(filename='sherdog.log', level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.DEBUG)


class Sherdog:

    def __init__(self, sherdog_fighter_url, request_timeout=10):
        self.sherdog_fighter_url = sherdog_fighter_url
        self.request_timeout = request_timeout

    def find(self, fighter_id, json_format=True):
        start = time()

        fighter_url = self.sherdog_fighter_url + fighter_id

        response = urllib2.urlopen(fighter_url, timeout=self.request_timeout)
        logging.debug("Http request time: %s " % (time() - start))

        response_code = response.getcode()

        start_parse = time()
        fighter_info = self._parse_bio_fighter(response, fighter_id)
        logging.debug("Parse time: %s " % (time() - start_parse))

        if json_format:
            result = json.dumps(fighter_info)
        else:
            result = fighter_info

        logging.debug("Total time: %s " % (time() - start))

        return response_code, result

    def _parse_bio_fighter(self, response, fighter_id):

        start = time()

        html = response.read()
        code_id = self.get_fighter_id_from_url(response.url)

        # soup = BeautifulSoup(html, 'lxml')
        soup = BeautifulSoup(html, 'html.parser')

        bio = soup.find("div", {"class": "bio_fighter"})

        name = bio.find("h1", {"itemprop": "name"})

        fn = soup.find("span", {"class": "fn"})
        nickname_span = name.find("span", {"class": "nickname"})
        nickname = nickname_span.find("em") if nickname_span else None

        nationality = soup.find("strong", {"itemprop": "nationality"})
        address_locality = soup.find("span", {"itemprop": "addressLocality"})
        birth_date = soup.find("span", {"itemprop": "birthDate"})

        association_h5 = soup.find("h5", {"class": "association"})
        association_name = association_h5.find("span", {"itemprop": "name"}) if association_h5 else None

        wclass = soup.find("h6", {"class": "wclass"})
        weight_class = wclass.strong if wclass else None

        size_info = soup.find("div", {"class", "size_info"})

        weight_span = size_info.find("span", {"class": "weight"})
        weight_strong = weight_span.strong if weight_span else None

        height_span = size_info.find("span", {"class": "height"})
        height_strong = height_span.strong if height_span else None

        fight_results, amateur_history = self._crawler_fight_history(soup, code_id)

        fighter = {
            'full_name': fn.string,
            'nickname': self._get_string(nickname),
            'nationality': self._get_string(nationality),
            'address_locality': self._get_string(address_locality),
            'birth_date': self._get_string(birth_date),

            'weight_class': self._get_string(weight_class),
            'weight': self._get_string(weight_strong),
            'height': self._get_string(height_strong),

            'association': self._get_string(association_name),

            'fighter_id': fighter_id,
            'fighter_code_id': code_id,

            'fight_results': fight_results,
            'amateur_history': amateur_history
        }

        return fighter

    def _crawler_fight_history(self, soup, code_id):

        fight_results = []
        amateur_results = []

        fight_history = self._find_table_history(soup, 'History')    # Fight History
        amateur_history = self._find_table_history(soup, 'Amateur')  # Amateur Fights

        if fight_history:
            fight_info_list = self._crawler_fight_info(fight_history.findAll('tr', {'class': ['odd', 'even']}))
            if fight_info_list:
                for info in fight_info_list:
                    fight_results.append(info)

        if amateur_history:
            fight_info_list = self._crawler_fight_info(amateur_history.findAll('tr', {'class': ['odd', 'even']}))
            if fight_info_list:
                for info in fight_info_list:
                    amateur_results.append(info)

        return fight_results, amateur_results

    def _find_table_history(self, soup, text_head):

        fight_history_div_list = soup.findAll('div', {'class': ['module', 'fight_history']})

        if fight_history_div_list:

            for div in fight_history_div_list:

                module_header = div.find('div', {'class': 'module_header'})

                if module_header:
                    h2 = module_header.find('h2')
                    if h2:
                        if h2.string:
                            if text_head.lower() in h2.string.lower():
                                div_table = div.find('div', {'class': ['content', 'table']})
                                if div_table:
                                    table = div_table.find('table')
                                    if self._validate_figther_history_table(table):
                                        return table

        return None

    def _validate_figther_history_table(self, table):

        if table is None:
            return False

        table_head = table.find('tr', {'class': 'table_head'})

        if table_head:
            return \
                self._compare_string(table_head.find('td', {'class': 'col_one'}), 'Result') and \
                self._compare_string(table_head.find('td', {'class': 'col_two'}), 'Fighter') and \
                self._compare_string(table_head.find('td', {'class': 'col_three'}), 'Event') and \
                self._compare_string(table_head.find('td', {'class': 'col_four'}), 'Method/Referee') and \
                self._compare_string(table_head.find('td', {'class': 'col_five'}), 'R') and \
                self._compare_string(table_head.find('td', {'class': 'col_six'}), 'Time')

        else:
            return False

    def _compare_string(self, element, string):
        element_text = element.string.lower().strip()
        return element_text == string.lower().strip()

    def _crawler_fight_info(self, fight_info_tr_list):

        fight_results = []

        if fight_info_tr_list:

            for tr in fight_info_tr_list:

                td_list = tr.findAll('td')

                if len(td_list) != RESULT_MAX_COLUMNS:
                    print('Invalid fight info table. Columns: ' + str(len(td_list)))
                    break

                result = td_list[RESULT].string

                opponent = td_list[OPPONENT].a
                opponent_name = opponent.string
                opponent_id = opponent['href']

                event = td_list[EVENT].a
                event_name = event.string
                event_url = event['href']

                event_date_span = td_list[EVENT].find('span', {'class': 'sub_line'})
                if event_date_span:
                    event_date = event_date_span.string.replace(' ', '')
                else:
                    event_date = NONE_VALUE

                method_and_referee = td_list[METHOD_AND_REFEREE].get_text(METHOD_AND_REFEREE_SEPARATOR)

                if method_and_referee and METHOD_AND_REFEREE_SEPARATOR in method_and_referee:
                    data = method_and_referee.split(METHOD_AND_REFEREE_SEPARATOR)
                    method = data[ONLY_METHOD]
                    referee = data[ONLY_REFEREE]
                else:
                    method = NONE_VALUE
                    referee = NONE_VALUE

                round = td_list[ROUND].string
                time = td_list[TIME].string

                fight_result = {
                    'result': result,
                    'opponent_name': opponent_name,
                    'opponent': opponent_id,
                    'event_name': event_name,
                    'event_url': event_url,
                    'event_date': event_date,
                    'method': method,
                    'referee': referee,
                    'round': round,
                    'time': time
                }

                fight_results.append(fight_result)

        return fight_results

    def _get_string(self, element):
        return element.string if element else None

    def get_fighter_id_from_url(self, url):
        data = url.split('/')
        fighter_id = data[len(data) - 1]
        return fighter_id


def main():
    sherdog = Sherdog("http://www.sherdog.com/fighter/")
    logging.debug(sherdog.find('1', json_format=False))
    logging.debug("-----------------------")
    logging.debug(sherdog.find('165671'))
    print sherdog.find('165671')
    # print sherdog.find('aaa')


if __name__ == '__main__':
    main()
