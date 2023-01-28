import csv
import datetime as dt
from collections import defaultdict

from .settings import (
    BASE_DIR, DATETIME_FORMAT, FILE_NAME, HEAD_TABLE, RESULTS_DIR_NAME, TOTAL
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_dir = BASE_DIR / RESULTS_DIR_NAME
        result_dir.mkdir(exist_ok=True)
        with open(
            result_dir / FILE_NAME.format(
                now=dt.datetime.utcnow().strftime(DATETIME_FORMAT)
            ),
            'w',
            encoding='utf-8'
        ) as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows([
                HEAD_TABLE,
                *self.count_status.items(),
                (TOTAL, sum(self.count_status.values()))
            ])
