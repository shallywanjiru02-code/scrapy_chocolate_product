from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst

class ChocolateProductLoader(ItemLoader):
    
    default_output_processor = TakeFirst()
    name_in = MapCompose(str.strip)
    price_in = MapCompose(lambda x : x.split('£') [-1].strip())
    url_in = MapCompose(lambda x : 'https://www.chocolate.co.uk' + x)