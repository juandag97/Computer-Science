import scrapy 

"""
    Title = //h1/a/text()
    Quotes = //span[@class="text" and @itemprop="text"]/text()
    Top ten tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall() 
    Next page buttom = //ul[@class="pager"]//li[@class="next"]/a/@href

"""
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['davidacost321@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'DiracDiran',
        'FEED_EXPORT_ENCODIG': 'utf-8'
    }

    def parse_only_quotes(self, response, **kwargs):
        if kwargs:
            quotes = kwargs['quotes']
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield{
                'quotes': quotes
            }
    def parse(self, response):
        # print('*'*10)
        # print('\n\n')
        #print(response.status, response.headers)
        title = response.xpath('//h1/a/text()').get()
        # print(f'Title: {title}')
        # print('\n\n')

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        # print('Quotes: ')
        # for quote in quotes:
        #     print(f'- {quote}')
        # print('\n\n')
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()    
        # print('Top ten tags: ')
        # for tag in top_tags:
        #     print(f'- {tag}')
        # print('\n\n')
        # print('*'*10)

        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            top_tags = top_tags[:top] 
            
        yield {
            'title': title,
            # 'quotes': quotes,
            'top_tags': top_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        