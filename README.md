<<<<<<< HEAD
# scrapy-zhihu
=======
# scrapy-zhihu
基于scrapy框架采用异步高并发的方式抓取知乎千万用户信息
## 概述
 > 抓取的原理是根据用户与关注他的用户和被他关注的用户之间建立联系，从而形成一个庞大的树形网络结构，理论上能抓取知乎所有活跃用户信息。由于数据量巨大，所以选择用scrapy搭建分布式集群抓取，用redis维护爬取队列，使爬取的数据不会重复，意外中断还能继续爬取，抓到的数据存储到MongoDB。由于知乎有反爬虫机制，所以还要用上IP动态代理池。
 
## 运行环境
* Python 3.6
* Scrapy-Redis
* Scrapyd
* MongoDB
* linux
## 运行启动
 > 每台主机都需要分别启动，可以使用scrapyd部署，也可以手动部署，redis必须要有，抓取主机数量不限制。
`$ scrapy3 crawl zhihu `
## 运行必要配置
* settings.py
 > 想要正常运行必须设置正确的MongoDB连接信息和Redis连接信息
```
MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_URL = 'redis://root:@192.168.2.100:6379'
SCHEDULER_PERSIST = True
```
>>>>>>> 81413805bcaf6483b5bb7697cdea87dc85d313d2
