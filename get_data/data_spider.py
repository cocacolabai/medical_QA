# coding: utf-8
import urllib.request
import urllib.parse
from lxml import etree
import time
import re
import json

class CrimeSpider:
    def __init__(self):
        self.f = open('symptom_detail.txt','a')

    def get_html(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('gbk')
        return html


    def spider_main(self):
        start = time.time()
        for page in range(0, 11000):
            print("page:{}, time:{}".format(page, time.time()-start))
            try:
                #basic_url = 'http://jib.xywy.com/il_sii/gaishu/%s.htm'%page
                #cause_url = 'http://jib.xywy.com/il_sii/cause/%s.htm'%page
                #prevent_url = 'http://jib.xywy.com/il_sii/prevent/%s.htm'%page
                symptom_url = 'http://jib.xywy.com/il_sii/symptom/%s.htm'%page
                #inspect_url = 'http://jib.xywy.com/il_sii/inspect/%s.htm'%page
                #treat_url = 'http://jib.xywy.com/il_sii/treat/%s.htm'%page
                #food_url = 'http://jib.xywy.com/il_sii/food/%s.htm'%page
                #drug_url = 'http://jib.xywy.com/il_sii/drug/%s.htm'%page
                data = {}
                #data['url'] = basic_url
                #data['basic_info'] = self.basicinfo_spider(basic_url)
                #data['cause_info'] =  self.common_spider(cause_url)
                #data['prevent_info'] =  self.common_spider(prevent_url)
                symptom, detail = self.symptom_spider(symptom_url)
                #data['inspect_info'] = self.inspect_spider(inspect_url)
                #data['treat_info'] = self.treat_spider(treat_url)
                #data['food_info'] = self.food_spider(food_url)
                #data['drug_info'] = self.drug_spider(drug_url)

                #json.dump(data, self.f, ensure_ascii=False)
                #self.f.write('\n')
            
                detail_str = ""
                for each in detail:
                    detail_str+=each
                if detail_str!="":
                    self.f.write(detail_str+"\n")

            except Exception as e:
                print(e, page)
       


        return


    def basicinfo_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        title = selector.xpath('//title/text()')[0]
        category = selector.xpath('//div[@class="wrap mt10 nav-bar"]/a/text()')
        desc = selector.xpath('//div[@class="jib-articl-con jib-lh-articl"]/p/text()')
        ps = selector.xpath('//div[@class="mt20 articl-know"]/p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r','').replace('\n','').replace('\xa0', '').replace('   ', '').replace('\t','')
            infobox.append(info)
        basic_data = {}
        basic_data['category'] = category
        basic_data['name'] = title.split('的简介')[0]
        basic_data['desc'] = desc
        basic_data['attributes'] = infobox
        return basic_data


    def treat_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        ps = selector.xpath('//div[starts-with(@class,"mt20 articl-know")]/p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r','').replace('\n','').replace('\xa0', '').replace('   ', '').replace('\t','')
            infobox.append(info)
        return infobox


    def drug_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        drugs = [i.replace('\n','').replace('\t', '').replace(' ','') for i in selector.xpath('//div[@class="fl drug-pic-rec mr30"]/p/a/text()')]
        return drugs


    def food_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        divs = selector.xpath('//div[@class="diet-img clearfix mt20"]')
        try:
            food_data = {}
            food_data['good'] = divs[0].xpath('./div/p/text()')
            food_data['bad'] = divs[1].xpath('./div/p/text()')
            food_data['recommand'] = divs[2].xpath('./div/p/text()')
        except:
            return {}

        return food_data


    def symptom_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        symptoms = selector.xpath('//a[@class="gre" ]/text()')
        ps = selector.xpath('//p')
        detail = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r','').replace('\n','').replace('\xa0', '').replace('   ', '').replace('\t','')
            detail.append(info)
        symptoms_data = {}
        symptoms_data['symptoms'] = symptoms
        symptoms_data['symptoms_detail'] = detail
        #print(detail)
        return symptoms, detail


    def inspect_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        inspects  = selector.xpath('//li[@class="check-item"]/a/@href')
        return inspects


    def common_spider(self, url):
        html = self.get_html(url)
        selector = etree.HTML(html)
        ps = selector.xpath('//p')
        infobox = []
        for p in ps:
            info = p.xpath('string(.)').replace('\r', '').replace('\n', '').replace('\xa0', '').replace('   ','').replace('\t', '')
            if info:
                infobox.append(info)
        return '\n'.join(infobox)

    def inspect_crawl(self):
        f_jc = open("jc.json",'w')
        data = dict()
        for page in range(1, 3700):
            print(page)
            try:
                url = 'http://jck.xywy.com/jc_%s.html'%page
                html = self.get_html(url)

                selector = etree.HTML(html)
                name = selector.xpath('//title/text()')[0].split('结果分析')[0]
                desc = selector.xpath('//meta[@name="description"]/@content')[0].replace('\r\n\t','')
                temp = [name,desc]
                data[url] = temp
                #self.db['jc'].insert(data)
                #print(url)


            except Exception as e:
                print(e)

        json.dump(data, f_jc, ensure_ascii=False)


handler = CrimeSpider()
handler.spider_main()
