import json
arrSite = ["yandex.ru"," google.ru"," vk.com"," ozon.ru"," mail.ru"," wildberries.ru"," gosuslugi.ru"," rbc.ru"," lenta.ru"," dzen.ru"," ya.ru"," ok.ru"," t.me"," wikipedia.org"," whatsapp.com"," telegram.org"," market.yandex.ru"," gismeteo.ru"," rutube.ru"," cloud.mail.ru"," kinopoisk.ru"," rambler.ru"," twitch.tv"," pikabu.ru"," news.mail.ru"," tbank.ru"," ria.ru"," sex-studentki.link"," sportbox.ru"," drom.ru"," music.yandex.ru"," aliexpress.ru"," dns-shop.ru"," hh.ru"," kp.ru"," pornhub.com"," 2gis.ru"," tinkoff.ru"," animego.org"," jut.su"," drive2.ru"," mts.ru"," gazeta.ru"," rutor.info"," kinopoisk.ru"," vesti.ru"," sportmail.ru"," mos.ru"," sberbank.ru"," avito.ru"," zen.yandex.ru"," rbc.ru"," prodoctorov.ru"," kino-teatr.ru"," kinozal.tv"," amedia.ru"," m24.ru"," nashideti.site"," foxnotes.ru"," kinogo.zone"," gov.ru"," wikimart.ru"," zen.yandex.ru"," championat.com"," putin-today.ru"," kinogo.site"," vashmolochnik.ru"," rabota.ru"," kwork.ru"," bigfishgames.ru"," twirpx.com"," nadomoney.ru"," kinobaza.tv"," mirtesen.ru"," freemovie.one"," domashniy.ru"," citilink.ru"," kinopoisk.com"," ivi.ru"," yaplakal.com"," superjob.ru"," abbyy.ru"," rbc.ru"," afisha.ru"," novostimira.com"," invest-bazar.ru"," leprosorium.ru"," onliner.by"," rabota.yandex.ru"," wildberries.ru"," market.yandex.ru"," gismeteo.ru"," kaspersky.ru"," habr.com"," fssp.gov.ru"," gazeta.ru"," alfabank.ru"," rt.com"," lenta.ru"," cyberleninka.ru"," eapteka.ru"," drom.ru"," rutracker.org"," tproger.ru"," ria.ru"," serbianforum.org"," mdoyke.ru"," kolesa.ru"," lenta.ru"," ivi.ru"," rabota.ru"," rzd.ru"," ivi.tv"," sozdik.kz"," lenta.com"," acca.ru"," zapovedniks.ru"," bash.org.ru"," yota.ru"," mail.ru"," myshows.me"," mirf.ru"," maski-tut.ru"," openbank.ru"," banki.ru"," kolobok.us"," btcsale.pro"," iwebp.com"," kaspersky.ru"," novayagazeta.ru"," lenta.ru"," autogear.ru"," help-wifi.com"," balancer.ru"," lenta.ru"," littered.ru"," nashideti.site"," gosuslugi.ru"," xakep.ru"," roem.ru"," nalog.ru"," vesti.ru"," it-world.ru"," diasp.org.ru"," nginx.org"," dou.ua"," amedia.ru"," vizitka.com"," mskguru.ru"," newsland.com"," orabote.top"," onlinesim.ru"," natashaclub.com"," extremecentrepoint.ru"," nashideti.site"," ruvds.com"," securenotes.ru"," imperia.forum24.ru"," sport.ru"," sprosy.ru"," nuancier.ru"," avito.ru"," rbc.ru"," love2fly.ru"," mytask.ru"," e-katerina.ru"," goglaz.ru"," duckduckgo.com"," kinobar.club"," domfilm.tv"," docs.microsoft.com"," domkino.tv"," lostfilm.tv"," ladno.ru"," kino-torrent.club"," ivi.ru"," kinomax.ru"," ru-board.com"," goodfon.ru"," gazeta.ru"," rbc.ru"," market.yandex.ru"," rutracker.org"," habrahabr.ru"," ag.ru"," vestikavkaza.ru"," onlinetv.fun"," kinozal.tv"," metacritic.com"," internetto.ru"," minecraft.net"," muzofond.org"," labirint.ru"," kinohleb.club"," torrent-games.net"," city-travel.site"," labirint.ru"," downkin.uz"," lostfilm.tv"," comss.ru"," 2ip.ru"," kino-torrent.club"," forum.vi.ru"," ykt.ru"," reg.ru"," skidka-goda.ru"," hdd.tomsk.ru"," cool-d.net"," mybook.ru"," tvp.net.ru"," novostimira.com"," torg.mail.ru"," teresheva-svadba.ru"," zen.yandex.ru"," amedia.ru"," wotblitz.com"," tvp.net.ru"," rutracker.org"," yandex.ru"," animego.tv"," nashideti.site"," habrahabr.ru"," dvhab.ru"," u-torrent.ru"," s9x.ru"," vshkole.com"," joblab.ru"," kinopoisk.ru"," smi.ru"," kinomax.ru"," kinobar.club"," multikland.net"," torrent4you.org"," wotblitz.com"," novayagazeta.ru"," ladno.ru"," google.com"," lenizdat.ru"," ogo.ua"," lenina74.ru"," 7kino.tv"," filehunter.ru"," goha.ru"," kino-v-online.tv"," habr.com"," animego.org"," macruc.ru"," kino-dom.tv"," lenta.ru"," kinobaza.tv"," prognoz-pogoda.ru"," gazeta.ru"," kino-v-hd.ru"," rutracker.org"," apple.com"," habr.com"," goha.ru"," proproger.ru"," kinoman.club"," kinopoisk.com"," online-gdz.net"," transfermarkt.ru"," kinozal.tv"," rutracker.org"," habr.com"," kino-torrent.club"," ivi.ru"," rzd.ru"," lenta.ru"," mybook.ru"," kinogo.zone"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru"," alfabank.ru"," gazeta.ru"," lenta.ru"," kinozal.tv"," rutracker.org"," ru-board.com"," mangaonline.ru"," kinogo.zone"," ivi.ru"," kinozal.tv"," gamez.by"," kinohleb.club"," kino-teatr.ru"," kino-max.org"," gazeta.ru"," kinogo.zone"," kinozal.tv"," kino-bar.club"," rutracker.org"," letitbit.net"," rambler.ru"," zen.yandex.ru", "alfabank"]
arrSite = set(arrSite)
class Website:
    def __init__(self,name,url):
        self._name = name
        self._url = url
    def getSite(self):
        return {"name":self._name,"url":self._url}
websites = [Website(name,f"https://{name.lower()}".replace(" ","")) for name in arrSite ]
dic = {"webSite":[t.getSite() for t in websites]}


with open("../site.json", 'w', encoding='utf-8') as f:
    json.dump(dic,f,indent=4,ensure_ascii=False)

print("Данные сохранены в site.json")

