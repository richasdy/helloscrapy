from scrapy.loader.processors import MapCompose
from helloscrapy.ItemLoaders import ProductLoader
from helloscrapy.utils.xml import remove_cdata

class XmlProductLoader(ProductLoader):
    name_in = MapCompose(remove_cdata, ProductLoader.name_in)