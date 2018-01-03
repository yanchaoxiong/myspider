import requests


class BaidutiebaSpider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/mo/q/m?word=" + tieba_name + "%E7%A7%91%E5%B9%BB%E7%89%87&page_from_search=index&tn6=bdISP&tn4=bdKSW&tn7=bdPSB&lm=16842752&lp=6093&sub4=%E8%BF%9B%E5%90%A7&pn={}&"
        self.headers = {
            "Use-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

    def get_url_list(self):
        url_list = [self.url_temp.format(i * 50) for i in range(0, 1000)]
        return url_list

    def parse_url(self, url):
        response = requests.get(url)
        return response.content.decode()

    def save_content(self, html_str, page_num):
        path_file = "{}_第{}_页.html".format(self.tieba_name, page_num)
        with open(path_file, "w", encoding="utf-8") as f:
            f.write(html_str)
        print("保存成功！")

    def run(self):
        # url 列表
        # 发送请求
        url_list = self.get_url_list()
        # 获取数据
        for url in url_list:
            html_str = self.parse_url(url)
            # 保存数据
            page_num = url_list.index(url) + 1
            self.save_content(html_str, page_num)


if __name__ == '__main__':
    tieba = BaidutiebaSpider("科幻片")
    tieba.run()
