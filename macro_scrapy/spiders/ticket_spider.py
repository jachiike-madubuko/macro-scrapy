from scrapy.spiders import Spider
from scrapy import Request
from macro_scrapy.items import EventItem
import scrapy


# maybe the issue is just  js heavy website like seatgeek
# try an easier website
# also try pyquery on another parser lib
#ideally headless

class TicketSpider(Spider):
    name = 'TicketSpider'
    start_urls = ['https://seatgeek.com/baltimore-ravens-tickets']  # LEVEL 1


    def start_requests(self):

        urls =    [
            # 'https://seatgeek.com/baltimore-ravens-tickets',
            # 'https://seatgeek.com/pittsburgh-steelers-tickets',
            # 'https://seatgeek.com/dallas-cowboys-tickets',
            'https://www.foxsports.com/soccer/news',

            ]

        for url in urls:
            yield  scrapy.Request(url=url, callback=self.parse)

    # 1. FOLLOWING LEVEL 1
    def parse(self, response):
        page = response.url.split("/")[-1]  # getting the page number from the URL
        filename = 'local_output/' + '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # event_class = 'li.Desktop__DesktopEventListItem-sc-7xzvm2-17'
        event_class = 'li.gMXTbB'
        # main_col_class = 'div.Desktop__MainColumn-sc-7xzvm2-9'
        main_col_class = 'div.ifgpyY'
        # date_col_class = 'div.Desktop__DateColumn-sc-7xzvm2-8'
        date_col_class = 'div.koCdzW'
        # button_col_class = 'div.Desktop__ButtonColumn-sc-7xzvm2-10'
        button_col_class = 'div.dGpRaR'
        # button_class = 'span.Button__ButtonContents-ui1y7a-1'
        button_class = 'span.cGpKQs'
        # title_class = 'p.Desktop__Title-sc-7xzvm2-1'
        title_class = 'p.ejNLVa'
        # sub_title_class = 'p.Desktop__Subtitle-sc-7xzvm2-3'
        sub_title_class = 'p.imOfJF'
        items = []
        self.log(response.css('script::text'))
        # self.log(response.css('ul').css('li').css('a').css('div').css('div').css('p').getall())
        # self.log(response.css('ul').css('li').css('div').css('script'))
        # self.log(response.xpath('//span[has-class("bMjfIb")]'))

        for event in response.css(event_class):
            item = EventItem()
            item.date = event.css(date_col_class).css(f'{title_class}::text').get()
            item.day_n_time = event.css(date_col_class).css(f'{sub_title_class}::text').get()
            item.title = event.css(main_col_class).css(f'{title_class}::text').get()
            item.location = event.css(main_col_class).css(f'{sub_title_class}::text').get()
            item.price = event.css(button_col_class).css(f'{button_class}::text').get()
            item.data = event.css('script::text').get()
            item.item_type = "event"
            self.log(item)
            items.append(item)
        return items



        # for follow_url in response.css("").extract():
        #     yield response.follow(follow_url, self.populate_item)
        # yield self.paginate(response)

    # 2. SCRAPING LEVEL 2
    # def populate_item(self, response):
        # item_loader = ItemLoader(item=MySpiderItem(), response=response)
        # item_loader.default_input_processor = MapCompose(remove_tags)

        # item_loader.add_css("", "")
        # yield item_loader.load_item()

    # 3. PAGINATION LEVEL 1
    # def paginate(self, response):
        # next_page_url = response.css("").extract_first()  # pagination("next button") <a> element here
        # if next_page_url is not None:
        #     return response.follow(next_page_url, self.parse)