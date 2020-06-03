#!venv/bin/python
from config import *
from search import find_firm

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
firm_list = [asters,sk,ilyashev, aequo, golaw, avellum, equity, lcf,cms, eterna, ilf, vkp,dla, antika, redcliffe, km_partners, deloitte,integrites]

feedback_list = ['Asters', 'Sayenko Kharenko', "Ілляшев та Партнери", "Aequo","Arzinger","Baker McKenzie","GOLAW", "Avellum", "Equity",
                 "LCF","CMS", "Eterna Law", "Dentons","ILF","Aver Lex", "Василь Кісіль і Партнери", "Грамацький і Партнери",
                 "Алєксєєв, Боярчуков та партнери", "Everlegal","Moris Group", "DLA Piper", "Ader Haber", "Салком", "KPMG",
                 "L.I.Group", "Evris", "Integrites", "Антіка", "Juscutum", "Eucon", "Redcliffe Partners", "EY", "Dynasty LF", "Пахаренко і Партнери",
                 "КМ Партнери", "Kinstellar", "Соколовський і Партнери", "Дубинський Ошарова", "Lavrynovych &  Partners", "Barristers",
                 "Hillmont Partners", "Pavlenko Legal Group", "Коннов і Созановський", "VB Partners", "АНК", "Шкребець і Партнери", "Mitrax",
                 "Юрлайн", "Амбер", "Gryphon Legal","Lexwell Partners", "ОМП", "ARIO","LES","Interlegal", "Alexandrov & Partners", "Абсолют",
                 "VDA Group", "InHelp", "SDM Partners", "Kodex", "Ecovis Бондар і Бондар", "Totum", "TCM Group", "Legrant", "Axon Partners",
                 "Правовий Альянс", "Esquires", "Грищенко і Партнери", "Gracers", "Sergii Koziakov & Partners", "Ostin", "Вдовичен і Партнери",
                 "Михайлюк, Сороколат і Партнери", "LS Group", "Матвіїв і Партнери", "ASA Group", "Quantum Attorneys", "Де-юре", "Клочков і Партнери",
                 "Law Bussiness Association", "KPLT", "Pravo Grant", "Кушнір, Яким'як та Партнери", "Гесторс", "Легітимус", "Lezo",
                 "Advice Group", "JN Legal", "Шевердін і Партнери", "АНТЕ", "Маршаллєр і Партнери", "Андрій Кравець і Партнери", "Peterka & Partners",
                 "Colares", "Могильницький і Партнери", "Юридичне Бюро Сергєєвих", "Nobili", "Teffi Law Firm", "Кролевецький і Партнери"]

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Хей, " +("@"+ str(message.from_user.username) if message.from_user.username != None
                                                       else str(message.from_user.first_name)) + "!")
    bot.send_chat_action(message.chat.id, action="typing")
    time.sleep(2)
    bot.send_message(message.chat.id, "Всі знають Харві Спектра, а я знаю тих, кого варто знати. Хочеш дізнатися інсайди юридичних фірм? Чи, може, підкинути тобі декілька вакансій? Думаю, я зможу допомогти.")

    bot.send_chat_action(message.chat.id, action="typing")

    con = lite.connect('harvey_bot.db')
    with con:
        cur = con.cursor()
        users = cur.execute('SELECT user FROM sheet8').fetchall()
        le = len(users)
        try:
            cur.execute("INSERT INTO sheet8 (id, user, choises) VALUES (?,?,?)", (le+1, str(message.chat.id), None))
        except:
            pass
    con.close()


    print("Пользователь " + str(message.chat.id) + " начал взаимодействие с ботом")
    time.sleep(2)
    bot.send_message(message.chat.id,
                             "Ось що я можу: \n" +
                             "*/search* — актуальні вакансії \n" +
                             "*/monitoring* — відслідковую появу та зникнення вакансій \n" +
                             "*/feedback* — відгуки про роботодавців \n" +
                             "*/salary* — середня зарплата в фірмі\n" +
                             "*/sendmail* — пошти фірм для розсилки резюме\n" +
                             "*/help* — список команд\n" +
                             "*/information* — інформація про мене",
                             parse_mode = 'Markdown')

@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id,
                         "Ось що я можу: \n" +
                         "*/search* — актуальні вакансії \n" +
                         "*/monitoring* — відслідковую появу та зникнення вакансій \n" +
                         "*/feedback* — відгуки про роботодавців \n" +
                         "*/salary* — середня зарплата в фірмі \n" +
                         "*/sendmail* — пошти фірм для розсилки резюме\n" +
                         "*/help* — список команд\n" +
                         "*/information* — інформація про мене",
                         parse_mode='Markdown')

@bot.message_handler(commands=["search"])
def handle_search(message):
    print("Пользователь " + str (message.chat.id) + " выполнил поиск вакансий")
    l = ["Хвилинку, зроблю декілька дзвінків, попитаю знайомих...", "Один партнер якраз питав мене, чи не маю я когось, хто шукає роботу. Зараз пригадаю...",
         "О, я якраз тебе шукав. За тебе питали. В мене десь була візитка...", "Наші конкуренти виклали нову вакансію. Бачив?", "Ходять чутки, що наші конкуренти шукають собі нового працівника. Ти ж не перейдеш до них?",
         ]
    i = random.randint(0,4)
    t = l[i]
    bot.send_message(message.chat.id, text=t)
    bot.send_chat_action(message.chat.id, action="typing")
    firm_title_list = []
    for firm in firm_list:
        firm_title_list.append(firm.firm_name)

    firm_list_list = []



    for title in firm_title_list:
        con = lite.connect("harvey_bot.db")
        with con:
            firm_id = firm_title_list.index(title)
            cur = con.cursor()
            vacancies = cur.execute("SELECT * FROM sheet1 WHERE id = ?", (firm_id,)).fetchall()[0]
            vacancies = vacancies[1]
        con.close()



        if vacancies != None:
            vacancies = vacancies.split("//")
        else:
            vacancies = []

        firm_list_list.append(vacancies)



    firm_title_list = tuple(firm_title_list)
    firm_vac_dict = dict(zip(firm_title_list,firm_list_list))
    def gen_markup():
        markup = InlineKeyboardMarkup()
        for title in firm_vac_dict:
            print(str(firm_vac_dict[title]))
            if len(str(firm_vac_dict[title])) > 5:
                markup.add(InlineKeyboardButton("Вакансії в " + str(title) + " — " + str(len(firm_vac_dict[title]) ), callback_data=str(title)+"vacancy"))
        return markup
    time.sleep(2)
    bot.send_message(message.chat.id, "Ось що я знайшов:", reply_markup=gen_markup())

@bot.message_handler(commands=['monitoring'])
def handle_monitoring(message):
    print("Пользователь " + str(message.chat.id) + " начал выбор мониторинга")
    try:
        l = ["Якщо я щось дізнаюсь про нові вакансії, маякну тобі!",
             "Кар'єрні можливості з'являються кожного дня. Не пропусти свій шанс!",
             "Оперативність важлива. Дізнайся про нові вакансії першим!",
             ]
        i = random.randint(0, 2)
        t = l[i]
        bot.send_message(chat_id=message.chat.id, text=t)
        bot.send_chat_action(message.chat.id, action="typing")
        time.sleep(3)
        user = str(message.chat.id)
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            choises = cur.execute("SELECT choises FROM sheet8 WHERE user = ?", (user,)).fetchall()[0]
        con.close()
        choises = choises[0]
        if choises != None:
            choises = choises.split("//")
            choises = [i for i in choises if i]

            if len(choises) != 0:
                pass
            else:
                choises = []
        else:
            choises = []

        if len(choises) == 0:
            def monitoring_markup():
                monitoring_markup = InlineKeyboardMarkup()
                for firm in firm_list:
                    monitoring_markup.add(InlineKeyboardButton(str(firm.firm_name),
                                                               callback_data=(str(
                                                                   firm_list.index(firm))+"start_monitoring")))
                return monitoring_markup
            bot.send_message(message.chat.id, "Обери фірми, які хочеш відслідковувати. \n"
                                              "Для припинення відслідковування натисни ще раз.",
                             reply_markup=monitoring_markup()
                             )

        else:
            def monitoring_markup():
                monitoring_markup = InlineKeyboardMarkup()
                for firm in firm_list:
                    if str(firm_list.index(firm)) in choises:
                        monitoring_markup.add(InlineKeyboardButton("\u2705 " + firm.firm_name,
                                                                                callback_data=str(
                                                                                    firm_list.index(firm)) + "stop_monitoring")
                                              )
                    else:
                        monitoring_markup.add(InlineKeyboardButton(str(firm.firm_name),
                                                                                callback_data=str(
                                                                                    firm_list.index(firm)) + "start_monitoring")
                                              )

                return monitoring_markup

            bot.send_chat_action(message.chat.id, action="typing")
            bot.send_message(message.chat.id, "Обери фірми, які хочеш відслідковувати. \n"
                                              "Для припинення відслідковування натисни ще раз.",
                             reply_markup=monitoring_markup())
    except:
        bot.send_message(message.chat.id, "Твій user_id відсутній в базі.Натисни /start ще раз, після чого знов виконай моніторинг")

@bot.message_handler(commands=["feedback"])
def handle_feedback(message):
    l = ["Якраз хотів у тебе запитати, як тобі одна фірма...",
         "Чув, що говорять про наших конкурентів?",
         "Факти брешуть, а чутки видають з головою...",
         "Все ніяк не міг зрозуміти, в чому секрет наших колег. А ось воно що...",
         ]
    i = random.randint(0, 3)
    t = l[i]
    bot.send_message(chat_id=message.chat.id, text=t)
    bot.send_chat_action(message.chat.id, action="typing")
    time.sleep(3)
    def feedback_markup(start, stop):
        feedback_markup = InlineKeyboardMarkup()
        for i in feedback_list:
            if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                feedback_markup.add(InlineKeyboardButton(i, callback_data="feedback"+str(feedback_list.index(i))))
        if stop > 10:
            feedback_markup.row(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),InlineKeyboardButton("⬅ Назад", callback_data="bk_f"+str(start)),InlineKeyboardButton("Вперед ➡", callback_data="fd_f "+str(stop)))
        else:
            feedback_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),InlineKeyboardButton("Вперед ➡", callback_data="fd_f"+str(stop)))
        return feedback_markup
    bot.send_message(message.chat.id, "Обери фірму:", reply_markup=feedback_markup(0,10))

@bot.message_handler(commands=['salary'])
def handle_salary(message):
    l = ["Бачив, яку машину придбав собі їх партнер? Все одно у мене краща!",
         "Цікаво, звідки в молодшого юриста гроші",
         "Я все думаю чи не забагато плачу своїм підлеглим...",
         ]
    i = random.randint(0, 2)
    t = l[i]
    bot.send_message(chat_id=message.chat.id, text=t)
    bot.send_chat_action(message.chat.id, action="typing")
    time.sleep(3)
    def salary_markup(start,stop):
        salary_markup = InlineKeyboardMarkup()
        for i in feedback_list:
            if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                salary_markup.add(InlineKeyboardButton(i, callback_data="salary"+str(feedback_list.index(i))))
        if stop > 10:
            salary_markup.row(InlineKeyboardButton(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),"⬅ Назад", callback_data="sal_b"+str(start)),InlineKeyboardButton("Вперед ➡", callback_data="sal_f"+str(stop)))
        else:
            salary_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("Вперед ➡", callback_data="sal_f"+str(stop)))
        return salary_markup

    bot.send_message(message.chat.id, "Обери фірму:", reply_markup=salary_markup(0, 10))

@bot.message_handler(commands=['sendmail'])
def sendmail(message):
    def mail_link():
        mail_link = InlineKeyboardMarkup()
        mail_link.add(InlineKeyboardButton("📝 Декілька порад", url="https://telegra.ph/Deyakі-poradi-shchodo-skladannya-rezyume-02-02"))
        mail_link.add(InlineKeyboardButton("📑 Створити резюме",url="https://resume.io"))
        return mail_link
    text0 = "Не всі наші колеги з інших юридичних фірм розміщують вакансії у себе на сайті. Але деякі з них запрошують надсилати резюме їм на пошту. \n" \
           "Ось список тих фірм, що розмістили на своєму сайті запрошення до надсилання CV. А нижче декілька порад щодо створення резюме і сервіс для його створення."
    text = "" \
           "*ARZINGER*\n" \
           "📎: https://arzinger.ua\n" \
           "✉: cv@arzinger.ua\n\n" \
           "*AVER LEX*\n" \
           "📎: http://averlex.com.ua\n" \
           "✉: info@averlex.com.ua\n\n" \
           "*Грамацький і Партнери*\n" \
           "📎: http://gramatskiy.com\n" \
           "✉: hr@gramatskiy.com\n\n" \
           "*Салком*\n" \
           "📎: https://www.salkom.ua/ru\n" \
           "✉: salkom@salkom.kiev.ua\n\n" \
           "*EVERLEGAL*\n" \
           "📎: https://everlegal.ua\n" \
           "✉: cv@everlegal.ua\n\n" \
           "*Lexwell & Partners*\n" \
           "📎: https://lexwell.com.ua\n" \
           "✉: lexwell@lexwell.com.ua\n\n" \
           "*Юрлайн*\n" \
           "📎: http://jurline.ua/uk/\n" \
           "✉: career@jurline.ua\n\n" \
           "*VDA Group*\n" \
           "📎: http://www.vdagroup.com.ua\n" \
           "✉: office@vdagroup.com.ua\n\n" \
           "*SBH*\n" \
           "📎: https://sbh-partners.com\n" \
           "✉: hr@sbh-partners.com\n\n" \
           "*Crowe LF*\n" \
           "📎: https://www.crowe.com/ua/crowelf\n" \
           "✉: hr@crowe.com.ua\n\n" \
           "*Esquires*\n" \
           "📎: https://esquires.ua\n" \
           "✉: hr@esquires.ua\n\n" \
           "*Клочков і Партнери*\n" \
           "📎: http://klochkov.partners/ua/\n" \
           "✉: info@klochkov.partners\n\n" \
           "*Андрій Кравець та Партнери*\n" \
           "📎: http://www.akp-law.com\n" \
           "✉: info@akp-law.com\n\n" \
           "*Kinstellar*\n" \
           "📎: https://www.kinstellar.com\n" \
           "✉: hr.kyiv@kinstellar.com\n\n" \
           "*ECOVIS*\n" \
           "📎: https://www.ecovis.com/ua/ukrainian/\n" \
           "✉: kyiv-law@ecovis.ua",
    bot.send_message(message.chat.id, text0)
    bot.send_chat_action(message.chat.id, action="typing")
    time.sleep(5)
    bot.send_chat_action(message.chat.id, action="typing")
    time.sleep(2)
    bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=mail_link())

@bot.message_handler(commands=["superuser"])
def auth(message):
    if str(message.from_user.id) == creat:
        msg = bot.send_message(message.chat.id,"Яке повідомлення надіслати всім користувачам?")
        bot.register_next_step_handler(msg, message_from_creator)

@bot.message_handler(commands=["count"])
def count(message):
    if str(message.from_user.id) == creat:
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT user FROM sheet8").fetchall()
        con.close()
        lenth_of_users_list = list(set(a))
        bot.send_message(message.chat.id, "Кількість користувачів бота: " + str(len(lenth_of_users_list)))

@bot.message_handler(commands=["information"])
def handle_help(message):
    def information_markup():
        inf_mk = InlineKeyboardMarkup()
        inf_mk.add(InlineKeyboardButton("❓ FAQ", url="https://telegra.ph/SHCHo-treba-znati-pro-HarveySpecterBot-02-11"),
                   InlineKeyboardButton("✒ Розробник", url="https://t.me/holdencaufield"))
        return inf_mk
    bot.send_message(message.chat.id, "@HarveySpecterBot — бот, який має полегшити життя всім тим,"\
                                      "хто шукає роботу на юридичному ринку України.\n\n " \
                                      "Якщо у тебе є пропозиції щодо нових функцій або ти знайшов баг, будь ласка, напиши про це на пошту m.a.procaylo@gmail.com або за посиланням внизу"
                                      "\nВерсія 1.0.0 \n[BetaTest]", reply_markup=information_markup()
                     )

@bot.message_handler(commands=["bill"])
def handle_bill(message):
    def bill_markup():
        bot.send_chat_action(message.chat.id, action=["typing"])
        con = lite.connect('zp_monitoring.db')
        with con:
            cur = con.cursor()
            users = cur.execute('SELECT id FROM users').fetchall()
            if str(message.chat.id) not in users:
                try:
                    cur.execute("INSERT INTO users (id, choises, names) VALUES (?,?,?)",
                                (str(message.chat.id), None, None))
                except:
                    pass
        con.close()

        bill_mk = InlineKeyboardMarkup()
        bill_mk.add(InlineKeyboardButton("Так", callback_data="bill_10010"),
                    InlineKeyboardButton("Змінити скликання", callback_data="change_bl"))
        return bill_mk
    bot.send_message(message.chat.id, "Хочеш відстежувати законопроект? Без проблем.\n\n📣 Обране скликання Верховної Ради - IX",reply_markup=bill_markup())

@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    if "change_bl" in call.data:
        def chg_bl_mk():
            chg_bl_mk = InlineKeyboardMarkup()
            chg_bl_mk.add(InlineKeyboardButton("IX скликання", callback_data="bill_10010"))
            chg_bl_mk.add(InlineKeyboardButton("VIII скликання", callback_data="bill_10009"))
            chg_bl_mk.add(InlineKeyboardButton("VII скликання", callback_data="bill_10008"))
            chg_bl_mk.add(InlineKeyboardButton("VI скликання", callback_data="bill_10007"))
            chg_bl_mk.add(InlineKeyboardButton("V скликання", callback_data="bill_10006"))
            chg_bl_mk.add(InlineKeyboardButton("IV скликання", callback_data="bill_10005"))
            chg_bl_mk.add(InlineKeyboardButton("III скликання", callback_data="bill_10004"))
            return chg_bl_mk

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Обери скликання:", reply_markup=chg_bl_mk())

    if "bill" in call.data:

        bill = re.sub(r"bill_","",str(call.data))
        bill = int(bill)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Введи номер законопроекту або фрагмент назви")
        bot.register_next_step_handler(msg, zp_monit, bill, 0)

    elif "zp_mon" in call.data:

        url0 = re.sub("zp_mon", "", str(call.data))
        url = "http://w1.c1.rada.gov.ua/pls/zweb2/"+ str(url0)
        r = requests.get(url)
        html = bs(r.text, 'html.parser')
        h = html.find_all("h3")
        a = html.find_all("td")
        stan = a[1].text
        b = html.find_all("th")
        status = b[1].text


        def zp_mon():
            zp_mon = InlineKeyboardMarkup()
            con = lite.connect('zp_monitoring.db')
            with con:
                cur = con.cursor()
                u = cur.execute('SELECT * FROM users WHERE id = ?', (str(call.message.chat.id),)).fetchall()
                if str(url0) not in str(u[0][1]) or len(u) == 0:
                    zp_mon.add(InlineKeyboardButton("\u2705 Відслідковувати зміни", callback_data="mzp"+str(call.message.chat.id)+"//" +str(url0)),InlineKeyboardButton("💻 Деталі", url= url))
                elif str(url0) in str(u[0][1]):
                    zp_mon.add(InlineKeyboardButton("⛔ Припинити відслідковувати", callback_data="stp" + str(call.message.chat.id) + "//" + str(url0)), InlineKeyboardButton("💻 Деталі", url=url))
            return zp_mon
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Документ: \n" + str(h[-1].text) + "\n\n📬 Стан: " + str(stan) + "\n\n🏷 Статус: " + str(status), reply_markup=zp_mon())

    elif "stp" in call.data:
        s = re.sub("st_zp", "", str(call.data))
        s = s.split("//")
        cht = s[0]
        zp = s[1]
        print(zp)
        url = "http://w1.c1.rada.gov.ua/pls/zweb2/"+ str(zp)
        r = requests.get(url)
        html = bs(r.text, 'html.parser')
        h = html.find_all("h3")
        h = h[-1].text

        con = lite.connect('zp_monitoring.db')
        with con:
            cur = con.cursor()
            choises = cur.execute('SELECT * FROM users WHERE id = ?', (str(call.message.chat.id),)).fetchall()
            choises = choises[0][1]
            print(choises)
            choises = re.sub(r"\(", "", str(choises))
            choises = re.sub(r"None", "", str(choises))
            choises = re.sub(r",", "", str(choises))
            choises = re.sub(r"\)", "", str(choises))
            choises = re.sub(r"'", "", str(choises))
            choises = re.sub(r'"', "", str(choises))
            choises = re.sub(r'\[', "", str(choises))
            choises = re.sub(r']', "", str(choises))

            choises = choises.split('//')

            choises.remove(str(zp))
            print(choises)
            choises = '//'.join(choises)
            cur.execute("UPDATE users SET choises = ? WHERE id = ?", (choises, str(call.message.chat.id)))
            try:
                cur.execute("UPDATE users SET choises = ? WHERE id = ?", (choises, str(call.message.chat.id)))
            except:
                print("error")
                pass

            names = cur.execute('SELECT * FROM users WHERE id = ?', (str(call.message.chat.id),)).fetchall()
            names = str(names[0][2])
            names = names.split('//')

            names.remove(str(h))

            names = '//'.join(names)
            cur.execute("UPDATE users SET names = ? WHERE id = ?", (names, (str(call.message.chat.id))))
            try:
                cur.execute("UPDATE users SET names = ? WHERE id = ?", (names, (str(call.message.chat.id))))
            except:
                print("error")
                pass

            users = cur.execute('SELECT * FROM choises WHERE zp = ?', (str(zp),)).fetchall()[0][1]
            users = str(users).split('//')
            users.remove(str(call.message.chat.id))
            users = '//'.join(users)
            try:
                cur.execute("UPDATE choises SET users = ? WHERE zp = ?", (str(users), (str(zp))))
            except:
                print("error")
                pass
        con.close()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Більше не відслідковую зміни в документі:\n\n "+str(h))
    elif "mzp" in call.data:
        s = re.sub("mzp", "", str(call.data))
        s = s.split("//")
        cht = s[0]
        zp = s[1]
        print(cht, zp)

        url = "http://w1.c1.rada.gov.ua/pls/zweb2/"+ str(zp)
        r = requests.get(url)
        html = bs(r.text, 'html.parser')
        h = html.find_all("h3")
        h = h[-1].text
        a = html.find_all("td")
        stan = a[1].text
        b = html.find_all("th")
        status = b[1].text
        base = str(stan)+"//"+str(status)
        con = lite.connect('zp_monitoring.db')
        with con:
            cur = con.cursor()
            choises = cur.execute('SELECT choises FROM users WHERE id = ?', (str(cht),)).fetchall()
            choises = re.sub(r"\(", "", str(choises))
            choises = re.sub(r"None", "", str(choises))
            choises = re.sub(r",", "", str(choises))
            choises = re.sub(r"\)", "", str(choises))
            choises = re.sub(r"'", "", str(choises))
            choises = re.sub(r'"', "", str(choises))
            if str(zp) not in str(choises):
                choises = choises + "//" + zp
            else:
                pass
            try:
                cur.execute("UPDATE users SET choises = ? WHERE id = ?", (choises, str(call.message.chat.id)))
            except:
                pass

            a = cur.execute('SELECT * FROM users where id = ?',(cht,)).fetchall()
            names = a[0][2]
            if names == None:
                names = str(h)
            else:
                if str(h) not in str(names):
                    names = str(names) + "//" + str(h)
            try:
                cur.execute("UPDATE users SET names = ? WHERE id = ?", (names, cht))
            except:
                pass

            a = cur.execute("SELECT zp FROM choises").fetchall()
            print(a)
            for y in a:
                yy = y[0]
                print(yy)
                if str(zp) == str(yy):
                        print(yy)
                        users = cur.execute('SELECT * FROM choises WHERE zp = ?', (str(zp),)).fetchall()
                        users = users[0][1]
                        if users == None or str(users) == "":
                            users = ""
                            if str(cht) not in str(users):
                                users = str(users) + "//" + str(call.message.chat.id)
                            else:
                                pass
                        else:
                            if str(cht) not in str(users):
                                users = str(users) + "//" + str(call.message.chat.id)
                            else:
                                pass
                            pass


                        cur.execute("UPDATE choises SET users = ? WHERE zp = ?", (users, zp))

                        print("users are here")
            try:
                cur.execute("INSERT INTO choises (zp, users, status) VALUES (?,?,?)",
                            (str(zp), str(call.message.chat.id), str(base)))
            except:
                pass

        con.close()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Окей, починаю слідкувати за документом:\n\n" + str(h)+"\n\nДля нового пошуку натисни /bill")


    elif "vacancy" in call.data:
        for firm_call in firm_list:
            call.data = re.sub(r"vacancy", "", str(call.data))
            if call.data == firm_call.firm_name:
                site = []
                for i in firm_list:
                    site.append(i.firm_url)
                right_site = site[firm_list.index(firm_call)]
                def reply_keyboard():
                    reply_markup = InlineKeyboardMarkup()
                    reply_markup.add(InlineKeyboardButton("⬅ Назад", callback_data="back"))
                    reply_markup.add(InlineKeyboardButton(text='💻 Сайт', url=right_site))
                    return reply_markup
                print(firm_call.firm_url)
        text = []

        for x in firm_list:
            if call.data == x.firm_name:
                t = str(firm_list.index(x))
                con = lite.connect("harvey_bot.db")
                with con:
                    cur = con.cursor()
                    a = cur.execute("SELECT * FROM sheet1 WHERE id= ?", (t,)).fetchall()[0]
                con.close()
                a = a[1]
                text = a.split("//")
                text = "\n💼 ".join( repr(e) for e in text)
                text = re.sub("'","", text)

                print(text)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Вакансії " + str(call.data) +":\n💼 " + text, reply_markup=reply_keyboard())

    elif call.data == "back":
        firm_title_list = []
        for firm in firm_list:
            firm_title_list.append(firm.firm_name)

        firm_vac_dict = {}
        firm_list_list = []
        for xx in firm_title_list:
            con = lite.connect("harvey_bot.db")
            with con:
                c = firm_title_list.index(xx)
                cur = con.cursor()
                a = cur.execute("SELECT * FROM sheet1 WHERE id = ?", (c,)).fetchall()[0]
                b = a[1]
            con.close()
            b = b.split("//")
            firm_list_list.append(b)

        firm_title_list = tuple(firm_title_list)
        firm_vac_dict = dict(zip(firm_title_list, firm_list_list))
        print(firm_vac_dict)

        def gen_markup_back():
            markup = InlineKeyboardMarkup()
            for name in firm_vac_dict:
                if len(str(firm_vac_dict[name])) > 5:
                    markup.add(
                        InlineKeyboardButton("Вакансії в " + str(name) + " — " + str(len(firm_vac_dict[name])),
                                            callback_data=str(name)+"vacancy"))
            return markup

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ось що я знайшов:", reply_markup=gen_markup_back())

    elif "start_monitoring" in call.data:
        call.data = re.sub(r"start_monitoring", "", str(call.data))
        user = str(call.message.chat.id)
        id = str(call.data)
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            users = cur.execute("SELECT users FROM sheet7 WHERE id_of_firm = ?", (id,)).fetchall()[0]
            choises = cur.execute("SELECT choises FROM sheet8 WHERE user = ?", (user,)).fetchall()[0]

        if users != None:
            users = list(users)
            if len(users) != 0:
                users = users

        else:
            users = []

        users.append(str(user))
        users = [x for x in users if x]
        users = list(set(users))
        text_user = str("//".join(users))

        choises = choises[0]

        if choises != None:
            choises = choises.split("//")
            if len(choises) != 0:
                pass
        else:
            choises = []

        choises.append(str(id))
        choises = list(set(choises))
        text_choises = str("//".join(choises))

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            cur.execute("UPDATE sheet7 SET users = ? WHERE id_of_firm = ?", (text_user, id))
            cur.execute("UPDATE sheet8 SET choises = ? WHERE user = ?", (text_choises, user))
        con.close()

        print("Пользователь " + str(call.from_user.id) + " добавил в список мониторинга " + str(call.data))
        def dynamic_monitoring_markup():
            dynamic_monitoring_markup = InlineKeyboardMarkup()
            for firm in firm_list:
                if str(firm_list.index(firm)) in choises:
                    dynamic_monitoring_markup.add(InlineKeyboardButton("\u2705 " + firm.firm_name,
                                                                           callback_data=str(
                                                                               firm_list.index(firm)) + "stop_monitoring"))
                else:
                    dynamic_monitoring_markup.add(InlineKeyboardButton(str(firm.firm_name),
                                                                                                callback_data=str(
                                                                                                    firm_list.index(firm))+"start_monitoring"))
            return dynamic_monitoring_markup

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Обери фірми, що бажаєш відслідковувати. \n" + "Для припинення відслідковування натисни ще раз.",
                              reply_markup=dynamic_monitoring_markup())

    elif "stop_monitoring" in call.data:
        call.data = re.sub(r"stop_monitoring", "", str(call.data))
        user = str(call.message.chat.id)
        id = str(call.data)
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            users = cur.execute("SELECT users FROM sheet7 WHERE id_of_firm = ?", (id,)).fetchall()[0]
            choises = cur.execute("SELECT choises FROM sheet8 WHERE user = ?", (user,)).fetchall()[0]

        users = users[0].split("//")

        users.remove(user)
        users = list(set(users))
        text_users = str("//".join(users))

        choises = choises[0].split("//")

        choises.remove(id)
        choises = list(set(choises))
        text_choises = str("//".join(choises))

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            cur.execute("UPDATE sheet7 SET users = ? WHERE id_of_firm = ?", (text_users, id))
            cur.execute("UPDATE sheet8 SET choises = ? WHERE user = ?", (text_choises, user))
        con.close()


        print("Пользователь "+ str(call.from_user.id) + " удалил из списка мониторинга " + str(call.data))
        def dynamic_monitoring_markup_stop():
            dynamic_monitoring_markup_stop = InlineKeyboardMarkup()
            for firm in firm_list:
                if str(firm_list.index(firm)) in choises:
                    dynamic_monitoring_markup_stop.add(InlineKeyboardButton("\u2705 " + firm.firm_name,
                                                                           callback_data=str(
                                                                               firm_list.index(firm)) + "stop_monitoring"))
                else:
                    dynamic_monitoring_markup_stop.add(InlineKeyboardButton(str(firm.firm_name),
                                                                                callback_data=str(
                                                                                    firm_list.index(firm)) + "start_monitoring"))

            return dynamic_monitoring_markup_stop

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Обери фірми, що бажаєш відслідковувати. \n" + "Для припинення відслідковування натисни ще раз.",
                              reply_markup=dynamic_monitoring_markup_stop())

    elif "bk_f" in call.data:
        cd_start = re.sub(r"bk_f", "", str(call.data))
        stop = int(cd_start)
        start = stop - 10
        def feedback_markup(start, stop):
            feedback_markup = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                    feedback_markup.add(InlineKeyboardButton(i, callback_data="feedback" + str(feedback_list.index(i))))

            if stop > 10 and stop <100 :
                feedback_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(start)),
                                    InlineKeyboardButton("Вперед ➡", callback_data="fd_f" + str(stop)))
            elif stop <= 10:
                feedback_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                    InlineKeyboardButton("Вперед ➡", callback_data="fd_f" + str(stop)))
            elif stop >= 100:
                feedback_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(start)))
            return feedback_markup

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Оберіть фірму:",
                              reply_markup=feedback_markup(start, stop))

    elif "fd_f" in call.data:
        cd_start = re.sub(r"fd_f", "", str(call.data))
        start = int(cd_start)
        stop = int(start+10)
        def feedback_markup1(start, stop):
            feedback_markup1 = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= int(start) and feedback_list.index(i) < stop:
                    feedback_markup1.add(InlineKeyboardButton(i, callback_data="feedback" + str(feedback_list.index(i))))

            if stop > 10 and stop <100 :
                feedback_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                     InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(start)),
                                    InlineKeyboardButton("Вперед ➡", callback_data="fd_f" + str(stop)))
            elif stop <= 10:
                feedback_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                     InlineKeyboardButton("Вперед ➡", callback_data="fd_f" + str(stop)))
            elif stop >= 100:
                feedback_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                     InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(start)))
            return feedback_markup1

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Оберіть фірму:",
                              reply_markup=feedback_markup1(start, stop))

    elif "feedback" in call.data:
        firm = re.sub(r"feedback", "", str(call.data))
        firm = int(firm)

        firm = re.sub(r"feedback", "", str(call.data))
        firm = int(firm)
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm + 1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        if len(a) != 0:
            a = [x for x in a if x]
            if len(a) > 4:
                text = a[-4:-1]
            else:
                text = a
            text = "\n\n 💬 ".join(repr(e) for e in text)
            text = re.sub("'", "", text)
            text = re.sub(r"\\n", '\n', text)
        else:
            text = "На жаль, відгуки відсутні\nБудь першим, хто залишить відгук!"

        def feedback_firm_markup():
            feedback_firm_markup = InlineKeyboardMarkup()
            if firm <= 9:
                feedback_firm_markup.add(InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(10)))
            elif firm > 9 and int(str(firm)[1]) <= 4:
                feedback_firm_markup.add(
                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1) + 10)))
            elif firm > 9 and int(str(firm)[1]) == 5 and int(str(firm)[0]) % 2 == 0:
                feedback_firm_markup.add(
                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1) + 10)))
            else:
                feedback_firm_markup.add(InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1))))
            feedback_firm_markup.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd" + str(firm)))
            if len(a) > 3:
                feedback_firm_markup.add(InlineKeyboardButton("📖 Всі відгуки", callback_data="all_fd" + str(firm)))
            return feedback_firm_markup

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=(str(feedback_list[firm]) + "\n\n💬 " +
                                    text),
                              reply_markup=feedback_firm_markup())

    elif "all_fd" in call.data:
        firm = re.sub(r"all_fd", "", str(call.data))
        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        a = [x for x in a if x]
        text = a[0:5]
        text = "\n\n💬 ".join(repr(e) for e in text)
        text = re.sub("'", "", text)

        def navigation_fd(start, stop):
            navigation_fd = InlineKeyboardMarkup()
            if stop > 5:
                navigation_fd.row(InlineKeyboardButton("◀ Попередні відгуки", callback_data="fd_nav_b" + str(firm) + "/" + str(stop)),
                                    InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
            elif len(a) <= 5:
                navigation_fd.add(InlineKeyboardButton("⬅ Назад до списку фірм", callback_data="bk_f" + str(10)))
                navigation_fd.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd" + str(firm)))
            else:
                navigation_fd.add(InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
                navigation_fd.add(InlineKeyboardButton("⬅ Назад до списку фірм", callback_data="bk_f" + str(10)))
                navigation_fd.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd" + str(firm)))
            return navigation_fd

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(feedback_list[firm]) + "\n\n💬 " + str(text),reply_markup=navigation_fd(0,5))

    elif "fd_nav_f" in call.data:
        st = re.sub(r"fd_nav_f", "", str(call.data))
        st = str(st).split("/")
        print(st)
        firm = int(st[0])
        st.remove(str(firm))
        start = int(st[0])
        stop = start + 5

        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []


        a = [x for x in a if x]
        text = a[start:stop]
        text = "\n\n💬 ".join(repr(e) for e in text)
        text = re.sub("'", "", text)

        def nav_fd_mk(start,stop):
            nav_fd_mk = InlineKeyboardMarkup()
            if stop > 5 and stop < len(a):
                nav_fd_mk.add(InlineKeyboardButton("◀ Попередні відгуки", callback_data="fd_nav_b" + str(firm) + "/" + str(start)),
                                    InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
            elif stop <= 5:
                nav_fd_mk.add(InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
            elif stop >= len(a):
                nav_fd_mk.add(InlineKeyboardButton("◀ Попередні відгуки", callback_data="fd_nav_b" + str(firm) + "/" + str(start)))
            nav_fd_mk.add(InlineKeyboardButton("⬅ Назад до списку фірм", callback_data="bk_f"+str(10)))
            nav_fd_mk.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd"+str(firm)))
            return nav_fd_mk
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(feedback_list[firm]) + "\n\n💬 " + str(text),reply_markup=nav_fd_mk(start,stop))

    elif "fd_nav_b" in call.data:
        st = re.sub(r"fd_nav_b", "", str(call.data))
        st = str(st).split("/")
        firm = int(st[0])
        st.remove(str(firm))
        stop = int(st[0])
        start = stop - 5

        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []


        a = [x for x in a if x]
        text = a[start:stop]
        text = "\n\n💬 ".join(repr(e) for e in text)
        text = re.sub("'", "", text)

        def nav_fd_mk1(start,stop):
            nav_fd_mk1 = InlineKeyboardMarkup()
            if stop > 5 and stop < len(a):
                nav_fd_mk1.add(InlineKeyboardButton("◀ Попередні відгуки", callback_data="fd_nav_b" + str(firm) + "/" + str(start)),
                                    InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
            elif stop <= 5:
                nav_fd_mk1.add(InlineKeyboardButton("Інші відгуки ▶", callback_data="fd_nav_f" + str(firm) + "/" + str(stop)))
            elif stop >= len(a):
                nav_fd_mk1.add(InlineKeyboardButton("◀ Попередні відгуки", callback_data="fd_nav_b" + str(firm) + "/" + str(start)))
            nav_fd_mk1.add(InlineKeyboardButton("⬅ Назад до списку фірм", callback_data="bk_f"+str(10)))
            nav_fd_mk1.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd"+str(firm)))
            return nav_fd_mk1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(feedback_list[firm]) + "\n\n💬 " + str(text),reply_markup=nav_fd_mk1(start,stop))

    elif "leave_fd" in call.data:
        firm = re.sub(r"leave_fd", "", str(call.data))
        firm = int(firm)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Залиш свій відгук про " + str(feedback_list[firm]) + ".\nПам'ятай, писати треба правду і нічого крім правди! \nЯкщо ти передумав, натисни /cancel")
        bot.register_next_step_handler(msg, leave_fd, firm)

    elif "sal_b" in call.data:
        cd_start = re.sub(r"sal_b", "", str(call.data))
        stop = int(cd_start)
        start = stop - 10
        def salary_markup(start, stop):
            salary_markup = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                    salary_markup.add(InlineKeyboardButton(i, callback_data="salary" + str(feedback_list.index(i))))
            if stop > 10 and stop <100 :
                salary_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("⬅ Назад", callback_data="sal_b" + str(start)),
                                    InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            elif stop <= 10:
                salary_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            elif stop >= 100:
                salary_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("⬅ Назад", callback_data="sal_b" + str(start)))
            return salary_markup

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Обери фірму:",
                              reply_markup=salary_markup(start, stop))

    elif "sal_f" in call.data:
        cd_start = re.sub(r"sal_f", "", str(call.data))
        start = int(cd_start)
        stop = int(start+10)
        def salary_markup1(start, stop):
            salary_markup1 = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= int(start) and feedback_list.index(i) < stop:
                    salary_markup1.add(InlineKeyboardButton(i, callback_data="salary" + str(feedback_list.index(i))))
            if stop > 10 and stop <100 :
                salary_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("⬅ Назад", callback_data="sal_b" + str(start)),
                                    InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            elif stop <= 10:
                fsalary_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            elif stop >= 100:
                salary_markup1.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),InlineKeyboardButton("⬅ Назад", callback_data="sal_b" + str(start)))
            return salary_markup1
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Обери фірму:",
                          reply_markup=salary_markup1(start, stop))

    elif "salary" in call.data:
        firm = re.sub(r"salary", "", str(call.data))
        firm = int(firm)
        def level_markup(firm):
            level_markup = InlineKeyboardMarkup()
            level_markup.add(InlineKeyboardButton("⭐⭐⭐Вищий рівень", callback_data="high_level"+str(firm)))
            level_markup.add(InlineKeyboardButton("⭐⭐Середній рівень", callback_data="mid_level" + str(firm)))
            level_markup.add(InlineKeyboardButton("⭐Початковий рівень", callback_data="low_level" + str(firm)))
            level_markup.add(InlineKeyboardButton("🔥Неюридичні професії", callback_data="non_lawyer" + str(firm)))
            return level_markup
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(feedback_list[firm])+"\n\nОберіть рівень: ",
                          reply_markup=level_markup(firm))

    elif "high_level" in call.data:
        firm = re.sub(r"high_level", "", str(call.data))
        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet3 WHERE id = ?",(firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        a = [int(item) for item in a]

        def level_mk(firm):
            level_mk = InlineKeyboardMarkup()
            level_mk.add(InlineKeyboardButton("✒ Додати дані", callback_data="add_sl"+str(firm)+ "/" + str(1)))
            level_mk.add(InlineKeyboardButton("🧾 До списку фірм", callback_data="sal_b" + str(10)))
            return level_mk
        if len(a) != 0:
            s = sum(a)
            av = s / len(a)
            av = float('{:.2f}'.format(av))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Середня зарплата працівника вищого рівня в " +
                                                                                                         str(feedback_list[firm])+" = " + str(av) + "грн",
                          reply_markup=level_mk(firm))
        elif len(a) == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Дані про зарплату в " +
                                       str(feedback_list[firm]) + " відсутні \n\n"  + "Будь першим, хто залишить дані!",
                                  reply_markup=level_mk(firm))

    elif "mid_level" in call.data:
        firm = re.sub(r"mid_level", "", str(call.data))
        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet4 WHERE id = ?",(firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        a = [int(item) for item in a]

        def level_mk(firm):
            level_mk = InlineKeyboardMarkup()
            level_mk.add(InlineKeyboardButton("✒ Додати дані", callback_data="add_sl"+str(firm)+ "/" + str(2)))
            level_mk.add(InlineKeyboardButton("🧾 До списку фірм", callback_data="sal_b" + str(10)))
            return level_mk
        if len(a) != 0:
            s = sum(a)
            av = s / len(a)
            av = float('{:.2f}'.format(av))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Середня зарплата працівника середнього рівня в " +
                                                                                                         str(feedback_list[firm])+" = " + str(av) + "грн",
                          reply_markup=level_mk(firm))
        elif len(a) == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Дані про зарплату в " +
                                       str(feedback_list[firm]) + " відсутні \n\n"  + "Будь першим, хто залишить дані!",
                                  reply_markup=level_mk(firm))

    elif "low_level" in call.data:
        firm = re.sub(r"low_level", "", str(call.data))
        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet5 WHERE id = ?",(firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        a = [int(item) for item in a]

        def level_mk(firm):
            level_mk = InlineKeyboardMarkup()
            level_mk.add(InlineKeyboardButton("✒ Додати дані", callback_data="add_sl"+str(firm)+ "/" + str(3)))
            level_mk.add(InlineKeyboardButton("🧾 До списку фірм", callback_data="sal_b" + str(10)))
            return level_mk
        if len(a) != 0:
            s = sum(a)
            av = s / len(a)
            av = float('{:.2f}'.format(av))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Середня зарплата працівника початкового рівня в " +
                                                                                                         str(feedback_list[firm])+" = " + str(av) + "грн",
                          reply_markup=level_mk(firm))
        elif len(a) == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Дані про зарплату в " +
                                       str(feedback_list[firm]) + " відсутні \n\n" + "Будь першим, хто залишить дані!",
                                  reply_markup=level_mk(firm))

    elif "non_lawyer" in call.data:
        firm = re.sub(r"non_lawyer", "", str(call.data))
        firm = int(firm)

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet6 WHERE id = ?",(firm+1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        a = [int(item) for item in a]

        def level_mk(firm):
            level_mk = InlineKeyboardMarkup()
            level_mk.add(InlineKeyboardButton("✒ Додати дані", callback_data="add_sl"+str(firm)+ "/" + str(4)))
            level_mk.add(InlineKeyboardButton("🧾 До списку фірм", callback_data="sal_b" + str(10)))
            return level_mk
        if len(a) != 0:
            s = sum(a)
            av = s / len(a)
            av = float('{:.2f}'.format(av))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Середня зарплата працівника неюридичного профілю в " +
                                                                                                         str(feedback_list[firm])+" = " + str(av) + "грн",
                          reply_markup=level_mk(firm))
        elif len(a) == 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Дані про зарплату в " +
                                       str(feedback_list[firm]) + " відсутні \n\n" + "Будь першим, хто залишить дані!",
                                  reply_markup=level_mk(firm))

    elif "add_sl" in call.data:
        st = re.sub(r"add_sl", "", str(call.data))
        st = str(st).split("/")
        firm = int(st[0])
        st.remove(str(firm))
        lvl = int(st[0])

        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Залиш дані про зарплату в " + str(feedback_list[firm]) +
                                         "\n\nЗапиши дані в форматі 'XXXX' без ком, пробілів та букв. Якщо передумаєш, натисни /cancel")
        bot.register_next_step_handler(msg, leave_salary, firm, lvl)

    elif "find_f_fd" in call.data:
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Напиши назву фірми для пошуку:")
        bot.register_next_step_handler(msg, findfirm)

    elif "find_f_sal" in call.data:
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text="Напиши назву фірми для пошуку:")
        bot.register_next_step_handler(msg, findfirm2)

    elif "zp_nxt_pg" in call.data:
        base = re.sub("zp_nxt_pg","", str(call.data))
        base = base.split("//")
        start = base[0]
        start = int(start)
        message = base[1]
        bill = base[2]
        url = "http://w1.c1.rada.gov.ua/pls/zweb2/webproc2_5_1_J"
        check = message.isdigit()

        def get_payload(text, bill):
            payload = {}
            if check == True:

                payload = {
                    "ses": bill,
                    "num_s": "2",
                    "num": text,
                    "date1": None,
                    "date2": None,
                    "name_zp": None,
                    "out_type": None,
                    "id": None,
                    "zp_cnt": "-1"
                }

            elif check == False:
                payload = {
                    "ses": bill,
                    "num_s": "2",
                    "num": None,
                    "date1": None,
                    "date2": None,
                    "name_zp": text.encode("WINDOWS-1251"),
                    "out_type": None,
                    "id": None,
                    "zp_cnt": "-1"
                }
            return payload

        r = requests.post(url, data=get_payload(message, bill))
        html = bs(r.text, 'html.parser')
        a = html.find_all("tr")
        zp_list1 = []
        for i in a:
            b = i.find_all("td")
            y = 2
            for x in b:
                if b.index(x) == y:
                    zp_list1.append(x.text)
                    y += 3

        zp_list3 = []
        for i in a:
            b = i.find_all("td")
            for x in b:
                if b.index(x) == 0 or b.index(x) % 3 == 0:
                    zp_list3.append(x.text)

        zp_list2 = []
        for i in a:
            if a.index(i) > 0:
                b = i.find_all("a")
                b = str(b)
                b = b[10:33]
                zp_list2.append(b)

        zp_list_fin = dict(zip(zp_list3, zp_list2))


        def zp_chose_mk():
            zp_chose_mk = InlineKeyboardMarkup()
            btn_list = []
            zp_list_mk = dict(zip(zp_list3[start:start + 10], zp_list2[start:start + 10]))

            for i in range(1, len(zp_list_mk) + 1):
                btn = InlineKeyboardButton(i, callback_data="zp_mon" + str(zp_list_mk[zp_list3[i - 1 + start]]))
                btn_list.append(btn)

            if len(btn_list) <= 5:
                zp_chose_mk.row(*btn_list)
                if start > 9:
                    zp_chose_mk.add(InlineKeyboardButton("⬅ Назад",
                                                         callback_data="zp_nxt_pg" + str(start - 10) + "//" + str(
                                                             message) + "//" + str(bill)))
            elif 5 < len(btn_list) <= 10:
                zp_chose_mk.row(*btn_list[0:5])
                zp_chose_mk.row(*btn_list[5:len(btn_list)])
                if len(zp_list_fin) > start + 10 and start == 0:
                    zp_chose_mk.add(InlineKeyboardButton("Вперед ➡",
                                                         callback_data="zp_nxt_pg" + str(start + 10) + "//" + str(
                                                             message) + "//" + str(bill)))
                elif len(zp_list_fin) > start + 10 and start > 0:
                    zp_chose_mk.add(InlineKeyboardButton("⬅ Назад",
                                                         callback_data="zp_nxt_pg" + str(start - 10) + "//" + str(
                                                             message) + "//" + str(bill)),
                                    InlineKeyboardButton("Вперед ➡",
                                                         callback_data="zp_nxt_pg" + str(start + 10) + "//" + str(
                                                             message) + "//" + str(bill)))
                elif len(zp_list_fin) <= start + 10:
                    zp_chose_mk.add(InlineKeyboardButton("⬅ Назад",
                                                         callback_data="zp_nxt_pg" + str(start - 10) + "//" + str(
                                                             message) + "//" + str(bill)))


            return zp_chose_mk

        text = "🧾"
        n = 1
        for i in zp_list1[start:start+10]:
            if n == 1:
                text =  str(text) + str(n) + ". " + str(i) + "\n\n"
                n = n + 1
                n = "🧾" + str(n)
            else:
                text = str(text) + str(n) + ". " + str(i) + "\n〰️〰️〰️\n\n"
                n = int(re.sub("🧾","",n))
                n = n + 1
                n = "🧾" + str(n)
        if len(zp_list1) != 0:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=str(text) + "Що саме тебе цікавить?", reply_markup=zp_chose_mk())
        else:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="На жаль, я нічого не знайшов. \n\n Спробуй змінити реквізити пошуку. Для нового пошуку натисни /bill")


@bot.message_handler(content_types=["text"])
def text_pas(message):
    print(message.from_user.id)
    pass

def zp_monit(message, bill, start):
    url = "http://w1.c1.rada.gov.ua/pls/zweb2/webproc2_5_1_J"
    start = int(start)
    check = message.text.isdigit()
    if message.text == "/bill":
        msg = bot.send_message(message.chat.id, "Введи номер законопроекту або фрагмент назви")
        bot.register_next_step_handler(msg, zp_monit, bill, start)
    else:

        def get_payload(text, bill):
            payload = {}
            if check == True:

                payload = {
                    "ses": bill,
                    "num_s": "2",
                    "num": text,
                    "date1": None,
                    "date2": None,
                    "name_zp": None,
                    "out_type": None,
                    "id": None,
                    "zp_cnt": "-1"
                }

            elif check == False:
                payload = {
                    "ses": bill,
                    "num_s": "2",
                    "num": None,
                    "date1": None,
                    "date2": None,
                    "name_zp": text.encode("WINDOWS-1251"),
                    "out_type": None,
                    "id": None,
                    "zp_cnt": "-1"
                }
            return payload
        r = requests.post(url, data = get_payload(message.text, bill))
        html = bs(r.text, 'html.parser')
        a = html.find_all("tr")
        zp_list1 = []
        for i in a:
            b = i.find_all("td")
            y = 2
            for x in b:
                if b.index(x) == y:
                    zp_list1.append(x.text)
                    y += 3

        zp_list3 = []
        for i in a:
            b = i.find_all("td")
            for x in b:
                if b.index(x) == 0 or b.index(x) %3 == 0:
                    zp_list3.append(x.text)

        zp_list2 = []
        for i in a:
            if a.index(i) > 0:
                b = i.find_all("a")
                b = str(b)
                b = b[10:33]
                zp_list2.append(b)

        zp_list_fin = dict(zip(zp_list3,zp_list2))

        def zp_chose_mk ():
            zp_chose_mk = InlineKeyboardMarkup()
            btn_list = []
            zp_list_mk = dict(zip(zp_list3[start:start+10],zp_list2[start:start+10]))
            print(zp_list_mk)
            for i in range(1,len(zp_list_mk)+1):
                btn = InlineKeyboardButton(i, callback_data="zp_mon"+str(zp_list_mk[zp_list3[i-1]]))
                btn_list.append(btn)

            if len(btn_list) <= 5:
                zp_chose_mk.row(*btn_list)
            elif 5 < len(btn_list) <= 10:
                zp_chose_mk.row(*btn_list[start:start+5])
                zp_chose_mk.row(*btn_list[start+5:len(btn_list)])
                if len(zp_list_fin) > start+10 and start == 0:
                    zp_chose_mk.add(InlineKeyboardButton("Вперед ➡", callback_data="zp_nxt_pg"+str(start+10)+"//"+str(message.text)+"//"+str(bill)))
                elif len(zp_list_fin) > start + 10 and start > 0:
                    zp_chose_mk.add(InlineKeyboardButton("⬅ Назад", callback_data="zp_nxt_pg" + str(start - 10) + "//" + str(message.text) + "//" + str(bill)),InlineKeyboardButton("Вперед", callback_data="zp_nxt_pg" + str(start + 10) + "//" + str(message.text) + "//" + str(bill)))
            return zp_chose_mk
        text = "🧾"
        n = 1
        for i in zp_list1[start:start+10]:
            if n == 1:
                text =  str(text) + str(n) + ". " + str(i) + "\n〰️〰️〰️\n\n"
                n = n + 1
                n = "🧾" + str(n)
            else:
                text = str(text) + str(n) + ". " + str(i) + "\n〰️〰️〰️\n\n"
                n = int(re.sub("🧾","",n))
                n = n + 1
                n = "🧾" + str(n)
        if len(zp_list1) != 0:
            bot.send_message(message.chat.id, text=str(text) + "Що саме тебе цікавить?", reply_markup=zp_chose_mk())
        else:
            bot.send_message(message.chat.id, "На жаль, я нічого не знайшов. \n\n Спробуй змінити реквізити пошуку. Для нового пошуку натисни /bill")
def findfirm(message):
    msg = message.text
    result = find_firm(msg)
    if len(result) == 1:
        firm = feedback_list.index(result[0])

        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm + 1,)).fetchall()[0]
            a = a[1]
        con.close()

        if a != None:
            a = a.split("//")
        else:
            a = []

        if len(a) != 0:
            a = [x for x in a if x]
            if len(a) > 4:
                text = a[-4:-1]
            else:
                text = a
            text = "\n\n".join(repr(e) for e in text)
            text = re.sub("'", "", text)
            text = re.sub(r"\\n", '\n', text)
        else:
            text = "На жаль, відгуки відсутні\nБудь першим, хто залишить відгук!"

        def feedback_firm_markup():
            feedback_firm_markup = InlineKeyboardMarkup()
            if firm <= 9:
                feedback_firm_markup.add(InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(10)))
            elif firm > 9 and int(str(firm)[1]) <= 4:
                feedback_firm_markup.add(
                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1) + 10)))
            elif firm > 9 and int(str(firm)[1]) == 5 and int(str(firm)[0]) % 2 == 0:
                feedback_firm_markup.add(
                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1) + 10)))
            else:
                feedback_firm_markup.add(InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(round(firm, -1))))
            feedback_firm_markup.add(InlineKeyboardButton("✒ Залишити відгук", callback_data="leave_fd" + str(firm)))
            if len(a) > 3:
                feedback_firm_markup.add(InlineKeyboardButton("📖 Всі відгуки", callback_data="all_fd" + str(firm)))
            return feedback_firm_markup

        bot.send_message(message.chat.id,
                              text=(str(feedback_list[firm]) + "\n\n💬 " +
                                    text),
                              reply_markup=feedback_firm_markup())

    elif len(result) > 1:
        def correction():
            correction = InlineKeyboardMarkup()
            for i in result:
                correction.add(InlineKeyboardButton(i, callback_data="feedback"+str(feedback_list.index(i))))
            return correction
        bot.send_message(message.chat.id, "Уточни, яку фірму ти мав на увазі:", reply_markup=correction())

    else:
        def feedback_markup(start, stop):
            feedback_markup = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                    feedback_markup.add(InlineKeyboardButton(i, callback_data="feedback" + str(feedback_list.index(i))))
            if stop > 10:
                feedback_markup.row(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                    InlineKeyboardButton("⬅ Назад", callback_data="bk_f" + str(start)),
                                    InlineKeyboardButton("Вперед ➡", callback_data="fd_f " + str(stop)))
            else:
                feedback_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_fd"),
                                    InlineKeyboardButton("Вперед ➡", callback_data="fd_f" + str(stop)))
            return feedback_markup

        bot.send_message(message.chat.id,  "На жаль, фірму не знайдено. Перевір правильність введення назви або обери фірму в меню пошуку", reply_markup=feedback_markup(0,10))

def findfirm2(message):
    msg = message.text
    result = find_firm(msg)
    if len(result) == 1:
        firm = feedback_list.index(result[0])

        def level_markup(firm):
            level_markup = InlineKeyboardMarkup()
            level_markup.add(InlineKeyboardButton("⭐⭐⭐Вищий рівень", callback_data="high_level"+str(firm)))
            level_markup.add(InlineKeyboardButton("⭐⭐Середній рівень", callback_data="mid_level" + str(firm)))
            level_markup.add(InlineKeyboardButton("⭐Початковий рівень", callback_data="low_level" + str(firm)))
            level_markup.add(InlineKeyboardButton("🔥Неюридичні професії", callback_data="non_lawyer" + str(firm)))
            return level_markup
        bot.send_message(message.chat.id, text=str(feedback_list[firm])+"\n\nОберіть рівень: ",
                          reply_markup=level_markup(firm))


    elif len(result) > 1:
        def correction():
            correction = InlineKeyboardMarkup()
            for i in result:
                correction.add(InlineKeyboardButton(i, callback_data="salary"+str(feedback_list.index(i))))
            return correction
        bot.send_message(message.chat.id, "Уточни, яку фірму ти мав на увазі:", reply_markup=correction())

    else:
        def salary_markup(start, stop):
            salary_markup = InlineKeyboardMarkup()
            for i in feedback_list:
                if feedback_list.index(i) >= start and feedback_list.index(i) < stop:
                    salary_markup.add(InlineKeyboardButton(i, callback_data="salary" + str(feedback_list.index(i))))
            if stop > 10:
                salary_markup.row(
                    InlineKeyboardButton(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"), "⬅ Назад",
                                         callback_data="sal_b" + str(start)),
                    InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            else:
                salary_markup.add(InlineKeyboardButton("🔍 Знайти", callback_data="find_f_sal"),
                                  InlineKeyboardButton("Вперед ➡", callback_data="sal_f" + str(stop)))
            return salary_markup
        bot.send_message(message.chat.id,  "На жаль, фірму не знайдено. Перевір правильність введення назви або обери фірму в меню пошуку", reply_markup=salary_markup(0,10))

def leave_fd(message, firm):
    firm = int(firm)
    fdb = str(message.text)
    if fdb == "/cancel":
        bot.send_message(message.chat.id, "Окей, залишимо це в таємниці.😏")
    else:
        con = lite.connect("harvey_bot.db")
        with con:
            cur = con.cursor()
            a = cur.execute("SELECT * FROM sheet2 WHERE id = ?", (firm+1,)).fetchall()[0]
            a = a[1]

        if a != None:
            a = a.split("//")
        else:
            a = []

        fdb = message.text
        a.append(fdb)
        a = str("//".join(a))
        print(fdb)

        with con:
            cur = con.cursor()
            cur.execute("UPDATE sheet2 SET feedbacks = ? WHERE id = ?", (a,firm+1))
        con.close()
        bot.send_message(message.chat.id, "Дякую за відгук!🚀")
        bot.send_message(creat, "Новий відгук про " + feedback_list[firm]+ ":\n"+str(fdb))

def leave_salary(message,firm,lvl):
    lvl = int(lvl)
    firm = int(firm)
    fdb = str(message.text)
    if fdb == "/cancel":
        bot.send_message(message.chat.id, "Окей, залишимо це в таємниці.😏")
    else:
        try:
            fdb = str(message.text)
            fdb = re.sub(r",", ".", str(fdb))

            con = lite.connect("harvey_bot.db")

            if lvl == 1:
                if int(fdb) < 10000 or int(fdb) > 1500000:
                    re_msg = (message.chat.id, "А це точно зарплата вищого рівня? Можливо, спробуєш ще раз? Якщо передумав, натисни /cancel")
                    bot.register_next_step_handler(re_msg, leave_salary, firm, lvl)
                else:
                    with con:
                        cur = con.cursor()
                        a = cur.execute("SELECT * FROM sheet3 WHERE id = ?", (firm + 1,)).fetchall()[0]
                        a = a[1]
                    if a != None:
                        a = a.split("//")
                    else:
                        a = []

                    a.append(fdb)
                    a = "//".join(a)

                    with con:
                        cur = con.cursor()
                        cur.execute("UPDATE sheet3 SET data = ? WHERE id = ?", (a, firm + 1))
                    con.close()
                    bot.send_message(message.chat.id, "Дякую за інформацію!🚀")
                    bot.send_message(creat, "Нова інформація про зарплату в " + feedback_list[firm])


            elif lvl == 2:
                if int(fdb) < 10000 or int(fdb) > 100000:
                    re_msg = (message.chat.id, "А це точно зарплата середнього рівня? Можливо, спробуєш ще раз? Якщо передумав, натисни /cancel")
                    bot.register_next_step_handler(re_msg, leave_salary, firm, lvl)
                else:
                    with con:
                        cur = con.cursor()
                        a = cur.execute("SELECT * FROM sheet4 WHERE id = ?", (firm + 1,)).fetchall()[0]
                        a = a[1]
                    if a != None:
                        a = a.split("//")
                    else:
                        a = []

                    a.append(fdb)

                    a = "//".join(a)

                    with con:
                        cur = con.cursor()
                        cur.execute("UPDATE sheet4 SET data = ? WHERE id = ?", (a, firm + 1))
                    con.close()
                    bot.send_message(message.chat.id, "Дякую за інформацію!🚀")
                    bot.send_message(creat, "Нова інформація про зарплату в " + feedback_list[firm])

            elif lvl == 3:
                if int(fdb) < 1000 or int(fdb) > 25000:
                    re_msg = (message.chat.id, "А це точно зарплата початкового рівня? Можливо, спробуєш ще раз? Якщо передумав, натисни /cancel")
                    bot.register_next_step_handler(re_msg, leave_salary, firm, lvl)
                else:
                    with con:
                        cur = con.cursor()
                        a = cur.execute("SELECT * FROM sheet5 WHERE id = ?", (firm + 1,)).fetchall()[0]
                        a = a[1]
                    if a != None:
                        a = a.split("//")
                    else:
                        a = []

                    a.append(fdb)

                    a = "//".join(a)

                    with con:
                        cur = con.cursor()
                        cur.execute("UPDATE sheet5 SET data = ? WHERE id = ?", (a, firm + 1))

                    con.close()
                    bot.send_message(message.chat.id, "Дякую за інформацію!🚀")
                    bot.send_message(creat, "Нова інформація про зарплату в " + feedback_list[firm])

            elif lvl == 4:
                with con:
                    cur = con.cursor()
                    a = cur.execute("SELECT * FROM sheet6 WHERE id = ?", (firm + 1,)).fetchall()[0]
                    a = a[1]
                if a != None:
                    a = a.split("//")
                else:
                    a = []

                a.append(fdb)

                a = "//".join(a)
                with con:
                    cur = con.cursor()
                    cur.execute("UPDATE sheet6 SET data = ? WHERE id = ?", (a, firm + 1))

                con.close()
                bot.send_message(message.chat.id, "Дякую за інформацію!🚀")
                bot.send_message(creat, "Нова інформація про зарплату в "+feedback_list[firm])

        except:
            re_msg = bot.send_message(message.chat.id, "А ти впевнений, що це правдива інформація?\n" +
                                      "Залиш дані у форматі 'XXXX' без точок та слів.\n\n"+
                                      "Для скасування натисни /cancel")
            bot.register_next_step_handler(re_msg, leave_salary, firm, lvl)

def message_from_creator(message):
    msg = message.text
    con = lite.connect("harvey_bot.db")
    with con:
        cur = con.cursor()
        a = cur.execute("SELECT user FROM sheet8").fetchall()
    con.close()
    a = list(set(a))
    for x in a:
        x = re.sub(",","",str(x))
        x = re.sub('\(*\)*', "", str(x))
        try:
            bot.send_message(chat_id=x, text=msg)
        except:
            pass
        time.sleep(0.5)

if __name__ == '__main__':
    bot.polling(none_stop=True)