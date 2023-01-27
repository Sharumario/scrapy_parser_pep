from pathlib import Path


PEP_PARSE_SPIDERS = 'pep_parse.spiders'
SPIDER_MODULES = [PEP_PARSE_SPIDERS]
NEWSPIDER_MODULE = PEP_PARSE_SPIDERS

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

BOT_NAME = 'pep_parse'
FILE_NAME = 'status_summary_{now}.csv'
HEAD_TABLE = ('Status', 'Count')
PEPS_DOMAINS = 'peps.python.org'
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS
TOTAL = 'Total'
URL = 'https://{url}/'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
