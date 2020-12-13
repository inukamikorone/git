import scrapy


class X89ipSpider(scrapy.Spider):
    name = 'x89ip'
    allowed_domains = ['89ip.cn']
    # start_urls = ['https://www.89ip.cn/index_{page}.html' for page in range(1,10)]
    start_urls = ['https://www.89ip.cn/index_{page}.html']



    def parse(self, response):
        select = response.xpath('//tr')
        for i in select:
            ip = i.xpath('./td[1]/text()').get()
            post = i.xpath('./td[2]/text()').get()
            add = i.xpath('./td[3]/text()').get()
            Operator = i.xpath('./td[4]/text()').get()
            time = i.xpath('./td[5]/text()').get()
            # with open('../../../../89ip.txt','w') as f:
            #     f.write(ip)
            #     f.write('\n')
            #     f.write(post)
            #     f.write(add)
            #     f.write(Operator)
            #     f.write(time)
            # print(ip,post,Operator,add,time)



        next_page = response.xpath('//a[@class="layui-laypage-next"]/@href').get()
        if next_page:
            # next_url = 'https://www.89ip.cn/' + next_page
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url,callback=self.parse)