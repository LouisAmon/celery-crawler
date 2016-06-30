# coding: utf-8
import logging
import abc

from bs4 import BeautifulSoup


LOGGER = logging.getLogger(__name__)


class Parser(object):

    __metaclass__ = abc.ABCMeta

    def process(self, markup):
        soup = BeautifulSoup(markup, parser='lxml')
        data = self.process_soup(soup)
        return data

    @abc.abstractmethod
    def process_soup(self, soup):
        """
        This is where you define how you extract your HTML data
        """
        raise NotImplemented


class MyParser(Parser):

    def process_soup(self, soup):
        data = {}
        h1_tag = soup.find('h1')
        data['h1'] = h1_tag.text
        return data
