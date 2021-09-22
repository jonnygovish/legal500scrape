from legal500scrape.firms import websrapper
# import webscrapper
import scrapy

from legal500scrape.items import FirmscrapeItem


class Firm_infoSpider(scrapy.Spider):
    name = 'firms_info'


    def start_requests(self):
        urls = websrapper()
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        item = FirmscrapeItem()

        item['Company'] = response.css(".nav-header::text").get().strip()

        item['image_urls'] = [response.urljoin(response.css("img.firm-profile-logo ::attr(src)").getall()[1])]

        item["City"] = ''.join(response.css(".page-title-editorial ::text").getall()).split('> ')[-1]

        item["Address"] = ' '.join(''.join(response.css('address *::text').getall()).strip().split())

        item["Website"] = response.css("a.firm-website").attrib['href']

        item["Phone_number"] = [phone.strip() for phone in response.css('.contact-links  ::text').getall() if phone.strip()][-2]

        item["Email_address"] = response.css("a.firm-email").attrib['href']

        item["Practice_heads"] = list(set([head.strip() for head in ' '.join(response.css('.practice-heads-list ::text').getall()).replace(";", "\n ").strip().split('\n')]))

        item["Key_clients"] = ' '.join(response.css(".client-list ::text").getall()).strip().split("\n")

        item["Membership"] = [membership.strip()for membership in ''.join(response.css("#memberships_section::text").getall()).strip().split('\t') if membership.strip()]

        item["Lawyer_list"] = response.css(".profile-name::text").getall()

        yield item

