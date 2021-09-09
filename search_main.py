# coding='utf-8'

import random
import xlsxwriter as xw
import time

from lxml import etree

from selenium import webdriver


def open_web_driver():
    '''�������'''
    # browser = webdriver.Chrome()
    # file_path = r'C:\Users\zsjw03\AppData\Roaming\Mozilla\Firefox\Profiles\gr2556xd.default'
    # # ��������������ã������cookies���´�ֱ��������½����ҳ��
    # fp = webdriver.FirefoxProfile(file_path)
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser


def close_web_driver(browser):
    '''�ر������'''
    browser.quit()


def driver_scroll(driver, url, keyword,zong_sums):
    '''ģ���������������ҳ����Ϣ�������������ã�����λ�ÿ�����'''
    try:
        browser.get(url)
    except:
        pass


    time.sleep(18)
    scroll_step_list=[1600]

    # �ӵڶ���д��
    sums = zong_sums
    set_list = []
    ks = 1
    # ��������
    js_sum = 1
    # �����¼���
    js2 = 1
    bczz = 1
    k11 = 1
    for i in range(5000000):
        # ������ֹ
        try:
            browser.execute_script("window.scrollBy(0, {});".format(scroll_step_list[0]))
            # browser.execute_script("window.scrollTo(0, 300);")
            # browser.execute_script("window.scrollTo")
            time.sleep(random.randint(15, 20))
            # parser_tweets_info(driver.page_source, keyword)
            # �ӵڶ���д��

            # �������
            if 'û�з������������Ľ��' in driver.page_source:
                print("û�з������������Ľ��-----------")
                return

            html = etree.HTML(driver.page_source)
            tweets_list = html.xpath("//div[@class='css-1dbjc4n']/article/div/div/div/div[2]/div[2]")
            # print('tweets_list',tweets_list)
            # �����˺��ǳ�
            # //div[@class='css-1dbjc4n r-1ifxtd0 r-ymttw5 r-ttdzmv']/div[2]/div/div/div[1]/div/span/span/text()
            name = html.xpath(
                "//div[@class='css-1dbjc4n r-1ifxtd0 r-ymttw5 r-ttdzmv']/div[2]/div/div/div[1]/div/span/span/text()")[0]

            print('��', len(tweets_list), '����')
            if len(tweets_list) == 0:
                print(keyword,'û�з������ӻ��ܱ�����')
                # 0 ����û�з������ӻ��ܱ�����
                row = 'A' + str(sums)
                wsheet1.write_row(row, [keyword,'��','��','��','û�з������ӻ��ܱ�����','��',0,0,0])
                # print("***********",list_data)
                # print('��', sums - 1, 'ҳ����', 'list_data>>>>>>', list_data)
                print('******��', sums - 1, '������******')
                sums += 1
                return sums
            sum11 = 0
            for tweet_info in tweets_list:
                # д��������б�
                list_data = []
                set_list1 = []
                # �˺�ID
                id = keyword  # id
                list_data.append(id)
                print(id)
                # �˺��ǳ�
                list_data.append(name)
                # print(name)
                # print('tweet_info',tweet_info)
                # ����ʱ��
                Time = tweet_info.xpath('.//a/time/text()')[0]
                print('Time----',Time)
                # ��Ҫ��
                # 12Сʱת����
                try:
                    if Time[-1] == '��':
                        TTime = time.time()
                        xs = int(Time.split('����')[0])
                        sjc = xs * 60
                        dq_time = TTime - sjc
                        now_data = time.strftime('%m��%d�� %H:%M', time.localtime(dq_time))
                        now_date = now_data[1:]
                        list_data.append(now_date)
                    else:
                        TTime = time.time()
                        xs = int(Time.split('Сʱ')[0])
                        print('xs',xs)
                        sjc = xs * 60 * 60
                        dq_time = TTime - sjc
                        now_data = time.strftime('%m��%d�� %H:%M', time.localtime(dq_time))
                        now_date = now_data[1:]
                        list_data.append(now_date)
                    # TTime = time.time()
                    # xs = int(Time.split('Сʱ')[0])
                    # sjc = xs * 60 * 60
                    # dq_time = TTime - sjc
                    # now_data = time.strftime('%m��%d�� %H:%M', time.localtime(dq_time))
                    # now_date = now_data[1:]
                    # list_data.append(now_date)
                except:
                    # ��������д��
                    try:
                        by = int(Time.split('��')[0])
                        if by == 8:
                            list_data.append(Time)
                        else:
                            print("���Ǳ������ݣ�������",js2)
                            js2 +=1
                            if js2 == 15:
                                print(id,'****��',sums-2,'������****')
                                time.sleep(random.randint(50, 60))
                                return sums
                            else:
                                continue
                    except:
                        if k11 == 8:
                            print(id, '****��', sums - 2, '������****')
                            time.sleep(random.randint(40, 50))
                            return sums
                        else:
                            print("----�꿪ͷ���Ǳ������ݣ�----",k11)
                            k11 += 1
                            continue


                set_list1.append(Time)

                # print('list_data2', list_data)
                # ��������
                # //div[2]/div[@class='css-1dbjc4n']/div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']//text()
                data_biaoti = tweet_info.xpath(
                    ".//div[2]/div[@class='css-1dbjc4n']/div[@class='css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0']//text()")
                # print(data_biaoti)
                # data_biaoti
                # print('data_biaoti:',data_biaoti)

                biaoti = "".join(data_biaoti)
                print(biaoti)
                list_data.append(biaoti)
                set_list1.append(biaoti)

                # ����
                try:
                    # ��ȡ�����ı�
                    data_neirong = tweet_info.xpath(
                        ".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # print('data_neirong>>>>>>>>>>>>>',data_neirong)
                    if data_neirong == []:
                        neirong = 'ͼƬ'
                    else:
                        neirong = "".join(data_neirong)
                    # print(neirong)
                    list_data.append(neirong)
                    # ��ȡ����ͼƬ����
                    # imgs = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # for img in imgs:
                    #     list_data.append(img)
                except:
                    neirong = '������ȡ����'
                    list_data.append(neirong)
                    # imgs = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n']//text()")
                    # for img in imgs:
                    #     list_data.append(img)

                # ��������
                lianjie = tweet_info.xpath(".//div[@class='css-1dbjc4n']/div[@class='css-1dbjc4n r-zl2h9q']/div[1]/div/a/@href")[0]
                # https://twitter.com/ConfuciusNZ/status/1400768126665457664
                data_lianjie = 'https://twitter.com' + lianjie
                print(data_lianjie)
                list_data.append(data_lianjie)
                set_list1.append(data_lianjie)
                # ��
                try:
                    ping_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[1]/div/div//text()")[
                        0]
                    if ',' in ping_data1:
                        ping = ping_data1.replace(',', '')
                    elif '��' in ping_data1:
                        ping2 = ping_data1.replace('��', '')
                        ping = float(ping2) * 10000
                    else:
                        ping = ping_data1
                    print('ping', ping)
                    list_data.append(int(ping))
                except:
                    ping_data1 = 0
                    print(ping_data1)
                    list_data.append(ping_data1)
                # ת
                try:
                    zhuan_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[2]/div/div//text()")[
                        0]
                    if ',' in zhuan_data1:
                        zhuan = zhuan_data1.replace(',', '')
                    elif '��' in zhuan_data1:
                        zhuan2 = zhuan_data1.replace('��', '')
                        zhuan = float(zhuan2) * 10000
                    else:
                        zhuan = zhuan_data1
                    print('zhuan', zhuan)
                    list_data.append(int(zhuan))
                except:
                    zhuan_data1 = 0
                    list_data.append(zhuan_data1)
                # ��
                try:
                    zan_data1 = tweet_info.xpath(
                        ".//div[3]/div/div[3]/div/div//text()")[
                        0]
                    # print('zan',zan_data1)
                    if ',' in zan_data1:
                        zan = zan_data1.replace(',', '')
                    elif '��' in zan_data1:
                        zan2 = zan_data1.replace('��', '')
                        zan = float(zan2) * 10000
                    else:
                        zan = zan_data1
                    print('zan',zan)
                    list_data.append(int(zan))
                except:
                    zan_data1 = 0
                    list_data.append(zan_data1)

                # �˺���ҳ����
                list_data.append(url)
                # �ж������Ƿ񵽵�
                if set_list1 in set_list:
                    # print("*******���ظ���ȡ*********",sum11)
                    # print('set_list1',set_list1)
                    sum11 += 1
                    if sum11 == len(tweets_list):
                        print("<<<<<<<<<<<<<����ҳ���ظ�",js_sum,'��>>>>>>>>>>>>>>')
                        js_sum +=1
                        if js_sum ==3:
                            print(id,'****��',sums-2,'������****')
                            time.sleep(random.randint(50, 65))
                            return sums
                else:
                    # print('list_data1',list_data)
                    set_list.append(set_list1)
                    row = 'A' + str(sums)
                    wsheet1.write_row(row, list_data)
                    # print("***********",list_data)
                    # print('��', sums - 1, 'ҳ����', 'list_data>>>>>>', list_data)
                    print('******��', sums - 1, '������******')
                    sums += 1
                    # print('set_list>>>>>>>>>>>>',set_list)
                    # print('set_list1>>>>>>>>>>>>',set_list1)

            # scroll_step_list[0]=(browser.execute_script("return document.body.scrollHeight;"))
        except Exception as e:
            time.sleep(random.randint(10, 20))
            print("��������",e,bczz)
            bczz +=1
            if bczz == 4:
                row = 'A' + str(sums)
                wsheet1.write_row(row, [keyword,'id�޷����˺�','��','��','��','��',0,0,0])
                # print("***********",list_data)
                # print('��', sums - 1, 'ҳ����', 'list_data>>>>>>', list_data)
                print('******��', sums - 1, '������******')
                sums += 1
                print('****��', sums - 2, '������****')
                time.sleep(random.randint(10, 15))
                return sums
        ks += 1

    print('����ѭ������������һλ------')



def main(browser):

    global wbook
    # wbook = xw.Workbook('ʦ�ʴ�--�Ƿǣ�����;������������4��.xlsx')
    # wbook = xw.Workbook('ʦ�ʴ�--ŷ�޽�ʦ��Ը����������4��.xlsx')
    # wbook = xw.Workbook('ʦ�ʴ�--ŷ�޽�ʦ��Ը����������4��.xlsx')
    # wbook = xw.Workbook('ʦ�ʴ�--�Ƿǣ�����;������������8��.xlsx')
    wbook = xw.Workbook('���������ý�������˺�����8��.xlsx')
    # wbook = xw.Workbook('ȱʧinterpretaatioo.xlsx')
    global wsheet1
    wsheet1 = wbook.add_worksheet('Sheet1')  # ����������
    wsheet1.activate()  # �����
    title = ['�˺�ID', '�����˻�', 'ʱ��', '����', '��������','��������', '������', 'ת����','������','�˺���ҳ����']  # ���ñ�ͷ
    wsheet1.write_row('A1', title)  # ��A1��Ԫ��д���ͷ

    # keyword_list = ['interpretaatioo','jul_shii','mazakiiz','sarahzhang','Lucyliu0866','silkroadproject','daisy','hann_lh','Maggie']
    # keyword_list = ['jul_shii','mazakiiz','sarahzhang','Lucyliu0866','silkroadproject','daisy','MadridConfucio']
    # keyword_list = ['interpretaatioo']
    # ���������ý�������˺�����7��.xlsx
    keyword_list=['ConfuciusNZ','henrylshenGZU','XiaoduanE','ShuZhu18','ybwang1109','Jijun29364265','HuiqunYu','XuemingTeng','diego_ic_unam','heartslens','LiweiHuang10','Francis514','3721Bunny','gxiaomin','DavidLu15687799','QiangDing@CIB','tci@griffith.edu.au','Angela_Muzi','wangna20']
    # 2 ŷ�޵�����ý�������˺�����4��.xlsx
    # keyword_list=['CISSStrathclyde','ConfucioRoma','confuciouclm','Confucius_HWU','Confucius_UoS','Confucius17000','ConfuciusCovuni','ConfuciusInst10','ConfuciusInst13','ConfuciusMCR','DMU_CI','GCI_tweets','GoldsmithsCI','HullConfucius','IC_PLA','instituteucc','kongzi_muc','LeuvenKongYuan','MadridConfucio','MandarinLondon1','OBUConfucius','UCL_IOE_CI','confuciusedgehi','KITrier','LCI_SOAS','icbretagne','ConfuciusNeoma','KonfInstitut']
    # 3 ʦ�ʴ�--�����ʦ��ý����������4��.xlsx
    # keyword_list=['ConfucioUES','SusanaWu7','15144410400Demi','Jingjin46354268','Louis_SUS','Yan28552197','Daisy98325175','springsy2016','BrendaBai1','EveLyn05828561','hannah72906108','Hebby49272252','Yveline22823356','JingleBelle168','Kailin10600780','Changhai117','Phoebe57385651','xu81915375','caicai93813838','Cynthia53765775','JingWen95221653','weiqian52497967','Joanna19406205','Julia90977387','Sophia46603189','Helen90034416','Natalie08345170','RUILIU76752215','yinseyueguang','Na99402397','GraceWang11','ChineseWems','Xiao50579103','zliina1','wLY5X6D8zCDlVe2','jingkang1','ssJudyzhu','JingjiaoC','tracyzhao19','Wang46444323','JenniferFu15','sam76104491','Guoshangwei','dengwenyi','Li82404363','Li88606719','Jamie78036488','Siyu_Zhang_','peile_tian','Chines3Mandarin','Michaelgong17']
    # 4 ʦ�ʴ�--ŷ�޽�ʦ��Ը����������4��.xlsx
    # keyword_list=['Alexljy1','Chris2388102','FengLiang20','HongyeLyu','jul_shii','Lanmei89027111','mina_talks','Sandycoco9','Tootielovely','XHaoying','ASandyyyyy','Esmi_shera','LunaMandarin','LunaDai4','LuoSufang','Melodywei9','Mia78881800','xiaowan08414204','YAN76368323','breath032','CallBoring','cestlav54663890','smiledoreen3','baoyinhui','limeiwang7','ProChinois','song_yajun','sunmaobian','Wenhui_FFM','Mingzhu69857844','MissH31988166','wuqian12076413','junmei','YunfeiLiang','AlexS98697900','chowcho51355522','ClemenceBon','estrellacork171','IcebergTom','Kenneth71886531','Lucas72676614','NiuXingyuan','Stacy27021975','GuizhiZhu','Chineseresourc1','bo4BGdzXaQ6sCQ8','Clara46679600','LingyuChen6','MVicky1031','PengFu20','Shi61S','XuanZeng1','XuyangJiang','Lili23460734','xuehanyu5','EmiliaZhou','joyxuan','lee71321195']
    # 5 ʦ�ʴ�--�Ƿǣ�����;������������4��.xlsx
    # keyword_list = ['AliZafarsays','cocojournalist','della_cool','gaowei2009','interpretaatioo','joce_cheng','jyfchen','KWangESPN','leisunZH','liu_tongxi','mazakiiz','photoft45','rhyme_andreason','sarahzhang','xiaohuawang4','XiaoliHuffman','XinyuLiu201202','xuzhe','YangRuby','Benlxiang','grace_c_liu','lilyarieslee','rrrlisarrr','yezhangyezhang','elleforlife','YanWang82488122','sandyliu12','ShanZha01828221','jjgod','weimin2008','YingWang_CHI','cuipengke','KapaluRichard','pacatuspraeses','laiying_yu','PurpleGrapes5','HungweiZhang','TonyZhang607','Yuhao_lim','Yueqing_AVH','yuee_li','shuypsusu','Yanmeili8','zengyan0807','legendyard','WeiWangArt','wangshuhua1','wxjhahaha','wangenjie1','VeraShen8','vanessachenbe','uropb123','yitingtan','suhang189_su','zhang_shzhang','XaythaZ','jiao_qun','QingyiChen6','qiaoxiaL','PingDeng7','paul_jaky','MerlinXu3','WangMeiYu4','tiv92','meganwbyy','marinebeans','zhanluyu0528','liyinbo41','Liuxiao98822538','lishenyu16','Irene_lingfangZ','mcluxun','li_yuanzheng','miischinese','kaixianli','JinYaqoob','jinger_zhao','jilinzhiwang','hyesuk47','huangzhongtian','HuaidongZhang','Huahuare','HoweLAU1','HongSun55833628','mimmzy011214','Haiyankang81','GShoujing','fushunma','dongbinfeeds','dingdang','DengBing7','DaviaLee','chen_dafu','confuciusbuu','foodjetaime','ChengfeiHe','chenlei199012','tri_bona','anthonywang','annaliu','Yingmeister','lulucc2008','Zhangliyan4','Silvana_Ling','XiaoRong_123','YukeWang4','WangBingxinA','StormieLei1','SherryYao20','NingTsan','YueLiArt','YLaiping','jianglulu1987','huilingliu8','HRWang3','QiyingH','GuanghuiLu','feifeidai','DaiJiawei1']
    # keyword_list = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',]
    # 6 ʦ�ʴ�--�Ƿǣ�����;������������4��.xlsx
    # keyword_list = ['gaoxing0103', 'sara08737544', 'annieri24224646', 'Bali20995725', 'guoxy0913', 'nambiagu', 'WangDarcie1', 'Faye202008', 'lihualai2', 'seniorking89', 'yangmo64234393']
    # 7 �ǷǴ�--�ٷ���վ��������4��.xlsx
    # keyword_list = ['5FUt4qpva4fUdQU','at_unima','CI_RDC','CiurCe','confuciu8','institut_a','kousigakudo','MakConfucius','Okan_Confucius','uj_confucius','hallaconfucius','IRISWU67055151','ktjycjustv','metuconfucius','CiUDSM','jinzi94400885','ccccieec','FuqingIn','KenyaKuci','LJoyrunner','icnaustp','kzxymsd','icultogo','confuciusucc','FamilyOnCI','ateneoconfucius','ConfuciusYonsei','kogakuin_cik','CKelaniya','CIPU_JORDAN']
    # 8 �ǷǴ�--�з�Ժ��������ý�������˺�4��.xlsx
    # keyword_list = ['Lucyliu0866','silkroadproject','YonghongYou','Youjiexuxin','lusunam1','chen_mingkun','TWoodfourth','ShirleyWang','AdolpheQiang','RockyLi44017918','laoerlang','beiyuchenlaoshi','bo_wu3','BorisjasonShi','jane42928513','MrFrankWU','wbx1101','zuyunyun','TingSmr','Wpan2003','marontion','Cynthialiang7','Michael_wjs','hiroshi20183','WeiHuan95253386']
    # ־Ը�ߴ������˺�����4��.xlsx
    # keyword_list = ['0327Gul','daisy','hann_lh','lenka','Maggie','nanCy','Rachlai','yang','limonian0617','louissssssmile','PzEnll','Benice58179573','Lydia69299359','CedricChang7','GatheringV','PeipeiZhang610','YeyeYzw','amandaypj','elie50651039','qingaqing1','63X4tttxq4MXArA','Bless_Lucky_','cccccci9','ErjinP','FionaYue3','HCaixiang','HUIZI92123','JOJO61611444','kepluence','Liana63845353','Lily_haruharu','maria03024','MWangcito','Nicolee59490329','SallyYangyang','Yvonne45364843','yyybeier','ZhangFang666','zorazc2625','1S3ihe790TII317','Aria96367818','Cabiwoo0618','Christi63119299','cswsantiniketan','DawnMarrrr','DeonLeowzk','djS8fYXDvKwgypG','Eleven42835322','Esquilo_Hanz','Estella58429332','Eva12291209','ft1sLE1dLRE3kCF','fugui42112644','Heya_rong','Ivyki2','Jene38893014','Jia49537324','jiamin84403979','jiumia','JKmuCqWGq24PKrF','junjunjingsheng','Kiki44204778','KishiShen','LIANGYU99531912','LiChen92047456','lily91152252','lilyc_loveart','Lilytan16722889','LingzhiWang6','linpinru2020','Lowboom233','LuluAdela_Yu','mingduo4','Nadya83567533','Niki22878835','peng34114638','qinqinlin7','queyuhe','saijun_jin','shanshan_meow','Siqin52813699','sourfishxy','svenjaindeu','TreeSerene','yizhidaidai','YueyuanChen230','YvetteYu1','zfW4b8j97KdO4eB','Zhang26999732','Melon75275430','a402651181','diego87122390','5v2qcDHGu9Khl4','LilihuangSA','della08231','Jasnelly','Delia','chen0801','esytella1','alisony','ciellexd','AliciaChen','dilidili','ChelseaDSQ','ahuang','Felicia','forence','LeoLiu','Anitawbb','BRAD_SHEN','fusuluobo','kun_hoa','Cecilia_S','jingyi_qin','win_y','LILAS','MAYMAY','Xuejiao91551097','Meiya20532615','Ximena0707','oneday','Yenni','liuying']
    # keyword_list = ['Rachlai']
    # �ڶ��п�ʼд��
    zong_sums = 2

    for keyword in keyword_list:
        # search_url = "https://twitter.com/search?f=live&q=coronavirus%20until%3A2020-01-31%20since%3A2020-01-30&src=typed_query".format(keyword)  #��������
        # search_url = """https://twitter.com/search?q="{}"%20-"Լ��"-%20until%3A2020-12-06%20since%3A2020-06-01&src=typed_query&f=live""".format(keyword)  # ��������
        search_url = "https://twitter.com/{}".format(keyword)
        print("���ڻ�ȡ�û���{}���µ�������Ϣ----".format(keyword), '\n', search_url)
        time.sleep(2)

        try:
            print('browser',browser)
            # driver_scroll(browser, search_url, keyword, zong_sums)
            zong_sums = driver_scroll(browser, search_url, keyword, zong_sums)
            print('zong_sums:',zong_sums)
        except Exception as WebDriverErr:
            print("ģ�����", WebDriverErr)
            continue
        # break
    wbook.close()

if __name__ == '__main__':
    # main()  Rachlai
    domain_name = 'https://twitter.com'
    browser = open_web_driver()
    try:
        main(browser)
    except Exception as mainErr:
        print(mainErr)
        close_web_driver(browser)
    close_web_driver(browser)
    print("����ץȡ��������ȴ�s������һ��ץȡ!!!")
    # while True:
    #     browser = open_web_driver()
    #     try:
    #         main(browser)
    #     except Exception as mainErr:
    #         print(mainErr)
    #         close_web_driver(browser)
    #         continue
    #     close_web_driver(browser)
    #     t = random.randrange(60, 100)
    #     print("����ץȡ��������ȴ�{}s������һ��ץȡ!!!".format(t))
    #     time.sleep(t)
