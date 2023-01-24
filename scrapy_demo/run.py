import datetime
from scrapy.exceptions import UsageError
from scrapy.utils.project import get_project_settings

class MyCommand(scrapy.cmdline.Command):
    def short_desc(self):
        return "My custom command"

    def run(self, args, opts):
        try:
            index = args[0]
        except IndexError:
            raise UsageError("Missing argument")
        settings = get_project_settings()
        current_date = datetime.datetime.now()
        feed_uri = f'output/{current_date:%Y-%m-%d}/part{index}.csv'
        settings.setdefault('FEED_URI', feed_uri)
