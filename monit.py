from config import *
import sqlite3 as lite

class Firm:

    def __init__(self, firm_name, firm_url, firm_tag, firm_tag_title):
        self.firm_name = firm_name
        self.firm_url = firm_url
        self.firm_tag = firm_tag
        self.firm_tag_title = firm_tag_title
    def __str__(self):
        s = "firm_name = {}, firm_url = {}, firm_tag = {}, firm_tag_title = {}".format(self.firm_name, self.firm_url, self.firm_tag, self.firm_tag_title)
        return s

aequo = Firm("Aequo", "https://aequo.ua/ua/career/vacancies/","a", {"class": "trigger", "href":"#"})
sk = Firm("Sayenko Kharenko", "https://sk.ua/uk/careers/", "span", {"class": "careers__item-desc"})
asters = Firm("Asters", "https://www.asterslaw.com/ua/career/vacancies/", "div",{"class": "title ua"})
equity = Firm("Equity", "https://equity.law/career/vacancies/", "div", {"class": "title en"})
lcf = Firm("LCF", "https://lcf.ua/career-2/", "ul",{"class": "tabs-vacancy"})
ilf = Firm("ILF", "https://www.ilf-ua.com/uk/karyera/vakanciyi/", "h5", {"class": "blog-preview vacancy-preview"})
vkp = Firm("Василь Кісіль і Партнери", "https://vkp.ua/career", "span", {"class": "accordion-btn-title"})
antika = Firm("Антіка", "http://antikalaw.com.ua/uk/about-firm/career/", "div", {"class": "wpb_accordion_section group"})
evris = Firm("Evris", "https://evris.law/uk/kariera/", "h3", None)
redcliffe = Firm("Redcliffe Partners", "https://redcliffe-partners.com/en/careers/", "li", {"class": 'vacancy-list__head'})
ilyashev = Firm("Ілляшев та Партнери", "http://attorneys.ua/uk/careers/", "h2", {"class": 'attnewsh'})
avellum = Firm("Avellum", "https://avellum.com/ua/company/career", "div", {"class": 'vacancy-title'})
cms = Firm("CMS", "https://cms.law/en/ukr/cms-job-opportunities", "strong", None)
dla = Firm("DLA Piper", "https://www.dlapiper.com/ru/ukraine/focus/ukraine-vacancies/", "strong", None)
eterna = Firm ("Eterna Law", "http://eterna.law/join-us/vacancies/", 'div', {"class": "col-md-8 col-sm-12 col-xs-12"})
km_partners = Firm("КМ Партнери", "http://wts.ua/ua/about-vacancies/", "h1", None)
golaw = Firm ("GOLAW", "https://www.golaw.ua/vacancies", "h3", {"class":"jobs__position"})
deloitte = Firm("Deloitte", "https://careers.deloitte.ru/go/Legal/3213101/?q=&q2=&alertId=&locationsearch=&title=&location=Kiev&date=", "span", {"class":"jobTitle hidden-phone"})
integrites = Firm("Integrites", "https://www.integrites.com/uk/careers/", "h3", {"class":"vacancy__title"})
firm_list = [asters,sk,ilyashev, aequo, golaw, avellum, equity, lcf,cms, eterna, ilf, vkp,dla, evris, antika, redcliffe, km_partners, deloitte,integrites]

def monitoring():
    while 1>0:
        for x in firm_list:
            try:
                if x.firm_name != lcf.firm_name and x.firm_name != km_partners.firm_name:
                    url = x.firm_url
                    r = requests.get(url)
                    html = bs(r.text, 'html.parser')
                    a = html.find_all(x.firm_tag, x.firm_tag_title)
                    vac = []
                    for vacs in a:
                        if x.firm_name == asters.firm_name or x.firm_name == equity.firm_name or x.firm_name == antika.firm_name:
                            vacs.div.decompose()
                        s = vacs.text
                        vacs = re.sub(r'\n', '', str(s))
                        vacs = re.sub(r'\r', '', str(vacs))
                        vacs = re.sub(r'\t', '', str(vacs))
                        vacs = re.sub(r'\xa0', '', str(vacs))
                        vacs = re.sub(r'  ', '', str(vacs))
                        vacs = re.sub(r"'", '', str(vacs))
                        vacs = re.sub(r"НАША АДРЕСА", '', str(vacs))
                        vac.append(vacs)

                    if x.firm_name == dla.firm_name:
                        iterations = []
                        for dl in range(int(len(vac) / 2)):
                            for dl in vac:
                                if (vac.index(dl)) % 2 == 0:
                                    a = str(dl) + ", " + str(vac[vac.index(dl) + 1])
                                    iterations.append(a)
                                    vac.remove(vac[vac.index(dl) + 1])
                                    vac.remove(dl)
                        vac = iterations.copy()

                elif x.firm_name == lcf.firm_name:
                    url = x.firm_url
                    r = requests.get(url)
                    html = bs(r.text, 'html.parser')
                    a = html.find_all(x.firm_tag, x.firm_tag_title)
                    vac = []
                    for vacs in a:
                        s = vacs.text
                        vacs = re.sub(r"\n", ',', str(s))
                        vacs = re.sub(r"\\", '/', str(vacs))
                        vacs = re.sub(r'\r', '', str(vacs))
                        vacs = re.sub(r'\t', '', str(vacs))
                        vacs = re.sub(r'\xa0', '', str(vacs))
                        vacs = re.sub(r'  ', '', str(vacs))
                        vac.append(vacs)
                    vac = re.sub(r"']", "", str(vac))
                    vac = re.sub(r"\['", "", str(vac))
                    vac = str(vac).split(",")

                elif x.firm_name == km_partners.firm_name:
                    url = x.firm_url
                    r = requests.get(url)
                    html = bs(r.text, 'html.parser')
                    a = html.find_all(x.firm_tag, x.firm_tag_title)
                    vac = []
                    for vacs in a:
                        s = vacs.text
                        vacs = re.sub(r"\n", ',', str(s))
                        vacs = re.sub(r"\\", '/', str(vacs))
                        vacs = re.sub(r'\r', '', str(vacs))
                        vacs = re.sub(r'\t', '', str(vacs))
                        vacs = re.sub(r'\xa0', '', str(vacs))
                        vacs = re.sub(r'  ', '', str(vacs))
                        vac.append(vacs)
                    vac = re.sub(r"']", "", str(vac))
                    vac = re.sub(r"\['", "", str(vac))
                    vac = re.sub(r'\xa0', '', str(vac))
                    vac = re.sub(r"Вакансії", "", str(vac))
                    vac = re.sub(r"'", "", str(vac))
                    vac = str(vac).split(",")

                vac = [x for x in vac if x]
                vac = list(set(vac))

                con = lite.connect("harvey_bot.db")
                with con:
                    cur = con.cursor()
                    t = cur.execute('SELECT * FROM sheet1 WHERE id = ?', (firm_list.index(x),)).fetchall()[0]
                    t = t[1]
                con.close()

                if t != None and len(t) != 0:
                    print(t)
                    vac0 = t.split("//")
                else:
                    vac0 = []

                Res1 = [x for x in vac if not x in vac0]
                Res2 = [x for x in vac0 if not x in vac]
                text1 = []
                text2 = []
                for res in Res1:
                    text1.append(res)
                text1 = [x for x in text1 if x]
                text1 = list(set(text1))
                text1 = "\n✔ ".join(repr(e) for e in text1)
                text1 = re.sub("'", "", text1)

                for res in Res2:
                    text2.append(res)
                text2 = [x for x in text2 if x]
                text2 = list(set(text2))
                text2 = "\n❌ ".join(repr(e) for e in text2)
                text2 = re.sub("'", "", text2)

                con = lite.connect("harvey_bot.db")
                with con:
                    cur = con.cursor()
                    id_of_firm = str(firm_list.index(x))
                    users = cur.execute("SELECT users from sheet7 where id_of_firm = ?",(id_of_firm,)).fetchall()[0]

                users = users[0]
                users = users.split("//")

                if len(Res1) == 0 and len(Res2) == 0:
                    print("Ничего не изменилось")

                elif len(Res1) != 0 and len(Res2) == 0:
                    print("В " + str(x.firm_name) + " з'явилась вакансія:" + str(text1))
                    if len(users) != 0:
                        for i in users:
                            print(i)
                            i = re.sub(",", "", str(i))
                            i = re.sub(r"\('", "", str(i))
                            i = re.sub(r"'\)", "", str(i))
                            try:
                                def mk1(url):
                                    mk1 = InlineKeyboardMarkup()
                                    mk1.add(InlineKeyboardButton("💻 Сайт", url=url))
                                    return mk1

                                bot.send_message(str(i),
                                                 "В " + str(x.firm_name) + " з'явилась вакансія: " + "\n✔ " + str(text1) + "\n",
                                                 reply_markup=mk1(x.firm_url))
                            except:
                                pass

                elif len(Res1) == 0 and len(Res2) != 0:
                    print("В " + str(x.firm_name) + " зникла вакансія: " + str(text2))
                    if len(users) != 0:
                        for i in users:
                            print(i)
                            i = re.sub(",", "", str(i))
                            i = re.sub(r"\('", "", str(i))
                            i = re.sub(r"'\)", "", str(i))
                            try:
                                def mk1(url):
                                    mk1 = InlineKeyboardMarkup()
                                    mk1.add(InlineKeyboardButton("💻 Сайт", url=url))
                                    return mk1

                                bot.send_message(str(i),
                                                 "В " + str(x.firm_name) + "  зникла вакансія: " + "\n❌ " + str(text2) + "\n",
                                                 reply_markup=mk1(x.firm_url))
                            except:
                                pass
                else:
                    print("В " + str(x.firm_name) + " з'явилась вакансія: " + str(text1))
                    print("В " + str(x.firm_name) + " зникла вакансія: " + str(text2))
                    if len(users) != 0:
                        for i in users:
                            i = re.sub(",", "", str(i))
                            i = re.sub(r"\('", "", str(i))
                            i = re.sub(r"'\)", "", str(i))

                            try:
                                def mk1(url):
                                    mk1 = InlineKeyboardMarkup()
                                    mk1.add(InlineKeyboardButton("💻 Сайт", url=url))
                                    return mk1

                                bot.send_message(str(i),
                                                 "В " + str(x.firm_name) + " зникла вакансія: " + "\n❌ " + str(text2) + "\n")
                                bot.send_message(str(i),
                                                 "В " + str(x.firm_name) + " з'явилась вакансія: " + "\n✔ " + str(text1) + "\n",
                                                 reply_markup=mk1(x.firm_url))
                            except:
                                pass

                vac = "//".join(vac)
                vac = str(vac)
                con = lite.connect('harvey_bot.db')
                with con:
                    cur = con.cursor()
                    cur.execute("UPDATE sheet1 SET vacantions = ? WHERE id = ?", (vac, firm_list.index(x)))
                con.close()
            except Exception as ex:
                print(ex)
                bot.send_message(creat, "Помилка оновлення в "+str(x.firm_name))

        time.sleep(1800)


monitoring()
