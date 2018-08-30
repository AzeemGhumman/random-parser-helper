import scrapy
import os
import time


class DawnSpider(scrapy.Spider):
    name = "Dawn"

    def start_requests(self):
        # url = 'https://www.dawn.com/news/' + str(1427548)
        # url_file = 'dawn_url_list_4000_5001.txt'
        log_file = []
        with open('logfile.txt', 'r') as f:
            for line in f:
                log_file.append(line.strip('\r\n'))
        f.close()
        print('************')
        print(log_file)
        print('************')
        all_files = os.listdir('URL_Folder')
        for url_file in all_files:
            if url_file not in log_file:
                print('Processing file = ', url_file)
                with open('URL_Folder\\' + url_file, 'r') as f:
                    urls = f.readlines()
                f.close()
                for url in urls:
                    yield scrapy.Request(url.strip('\r\n'), callback=self.parse)
                # yield scrapy.Request(url.strip('\r\n'), callback=self.parse)
                time.sleep(10)

                with open('logfile.txt', 'a') as f:
                    f.write(url_file + '\n')
                f.close()

    def parse(self, response):
        page_id = response.url.split('/')[-1]
        filename = 'Downloads\\' + 'page' + page_id + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
