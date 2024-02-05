# ! /usr/bin/python3.11
# -*- coding:utf-8 -*-

import pymysql

from utils.paper_utils import DealPaperInformation
from utils.paper_utils import get_titles

class MysqlService:

    def __init__(self, db_connection):
        self.db = db_connection
        self.cursor = self.db.cursor()
        pass

    def import_to_mysql(self, titles):
        # 分批次导入mysql
        num_paper = 0
        num_author = 0
        for title in titles:
            AF = ''
            wos_data = DealPaperInformation(title)
            if wos_data.TI_name == "":
                continue
            for af in wos_data.AF:
                AF += af.AuthorName + '; '
            wos_data.WC = str(wos_data.WC).replace("]", "").replace("[", "").replace("\'", "").replace('\"', '')
            wos_data.DE = str(wos_data.DE).replace(']', '').replace('[', '').replace('\"', '').replace('\'', '')

            try:
                self.cursor.callproc("insert_or_update_paper",
                                args=(wos_data.TI_name, AF, wos_data.DE, wos_data.SO, wos_data.PY, wos_data.WC,
                                      wos_data.ESI, wos_data.TC, wos_data.NR, wos_data.AB, ""))
                num_paper += 1
                # 提交到数据库执行
                self.db.commit()
            except Exception as e:
                print(e)
                self.db.rollback()
            for i in range(len(wos_data.AF)):
                wos_data.AF[i].AuthorOrganization = sorted(wos_data.AF[i].AuthorOrganization)
                wos_data.AF[i].AuthorOrganization = \
                    (str(wos_data.AF[i].AuthorOrganization)
                     .replace('[', '')
                     .replace(']', '')
                     .replace("\'", "").replace("\"", ""))

                try:
                    self.cursor.callproc("insert_or_update_author_record",
                                    args=(wos_data.AF[i].AuthorName, wos_data.AF[i].AuthorNation,
                                          wos_data.AF[i].AuthorOrganization, wos_data.WC))
                    # 提交到数据库执行
                    self.db.commit()
                except Exception as e:
                    # 如果发生错误回滚
                    print(e)
                    self.db.rollback()
                num_author += 1
        # 关闭数据库连接
        self.db.close()


    # 测试
if __name__ == '__main__':
    # 打开数据库连接,设置路径，端口，用户名，密码，数据库名。
    db = pymysql.connect(host='localhost', user='zsl', passwd='Lish145210@', port=3306, db='RDService')
    # 批量处理数据
    # 将txt文本切割成文献列表
    paper = get_titles(r"path")
    a = MysqlService(db)
    a.import_to_mysql(paper)