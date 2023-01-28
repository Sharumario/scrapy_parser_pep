from pathlib import Path


PEP_PARSE_SPIDER = 'pep_parse.spiders'
SPIDER_MODULES = [PEP_PARSE_SPIDER]
NEWSPIDER_MODULE = PEP_PARSE_SPIDER

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

BOT_NAME = 'pep_parse'
FILE_NAME = 'status_summary_{now}.csv'
HEAD_TABLE = ('Status', 'Count')
PEPS_DOMAIN = 'peps.python.org'
RESULTS_DIR_NAME = 'results'
TOTAL = 'Total'
URL = 'https://{url}/'

FEEDS = {
    f'{RESULTS_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
