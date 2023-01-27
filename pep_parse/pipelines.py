import csv
import datetime as dt
from collections import defaultdict

from .settings import (
    BASE_DIR, DATETIME_FORMAT, FILE_NAME, HEAD_TABLE, RESULTS, TOTAL
)


class PepParsePipeline:
    def open_spider(self, spider):
        self.count_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS
        #pytest не даёт закинуть в settings results_dir
        results_dir.mkdir(exist_ok=True)
        #закинул в конструктор _init_ но pytest выдаёт ошибку
        file_path = results_dir / FILE_NAME.format(
            now=dt.datetime.utcnow().strftime(DATETIME_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows([
                HEAD_TABLE,
                *self.count_status.items(),
                (TOTAL, sum(self.count_status.values()))
            ])
