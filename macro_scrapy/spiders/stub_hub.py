from scrapy.spiders import Spider
from scrapy import Request
from macro_scrapy.items import EventItem
import scrapy
# scrapy crawl StubHubSpider
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash
def range_query_gen(url, _min, _max):
    range_query='?sliderMin={}%2C50.74&sliderMax={}%2C36.49'
    query =  range_query.format(_min, _max)
    return url + query
class StubHubSpider(Spider):
    name = 'StubHubSpider'
    url = 'https://www.stubhub.com/oregon-ducks-football-tickets-oregon-ducks-football-eugene-autzen-stadium-9-5-2020/event/104551640/?sliderMin=90%2C50.74&sliderMax=95%2C36.49'
    start_urls = ['https://seatgeek.com/baltimore-ravens-tickets']  # LEVEL 1
    download_delay = 30

    def start_requests(self):

        urls =    [
            # 'https://seatgeek.com/baltimore-ravens-tickets',
            # 'https://seatgeek.com/pittsburgh-steelers-tickets',
            # 'https://seatgeek.com/dallas-cowboys-tickets',
     'https://www.stubhub.com/oregon-ducks-football-tickets-oregon-ducks-football-eugene-autzen-stadium-9-5-2020/event/104551640/?sliderMin=90%2C20.74&sliderMax=115%2C60.49'
            ]

        for url in urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=45,
                screenshot=True,
                wait_until=EC.presence_of_element_located((By.XPATH,
                    '/html/body/div[1]/div[1]/div/main/div/div/div[1]/div[2]/section[1]/div[1]/ul/div/li[1]'
                    ))
            )
curl "https://www.stubhub.com/bfx/api/search/inventory/v2/listings?additionalPricingInfo=true^&allSectionZoneStats=true^&edgeControlEnabled=true^&eventLevelStats=true^&eventPricingSummary=true^&listingAttributeCategorySummary=true^&pricingSummary=true^&quantitySummary=true^&sectionStats=true^&shstore=1^&start=20^&urgencyMessaging=true^&valuePercentage=true^&zoneStats=true^&scoreVersion=v2^&eventId=104551640^&quantity=^&rows=20^&sort=price^%^20asc^%^2C^%^20value^%^20desc^&priceType=nonBundledPrice^&listingAttributeCategoryList=^&excludeListingAttributeCategoryList=^&deliveryTypeList=^&sectionIdList=^&zoneIdList=^&pricemin=63.06^&pricemax=219.06^&listingRows=" ^
  -H "authority: www.stubhub.com" ^
  -H "accept: application/json" ^
  -H "authorization: Hawk id=^\^"1593913343.6411495581db73e3^\^", ts=^\^"1593912461^\^", nonce=^\^"fgb8yj^\^", mac=^\^"zQTLuLh8LOGSAzaTF+r2vZhukktKmfcx8X7jeotqBqs=^\^"" ^
  -H "accept-language: en-US" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58" ^
  -H "sec-fetch-site: same-origin" ^
  -H "sec-fetch-mode: cors" ^
  -H "sec-fetch-dest: empty" ^
  -H "referer: https://www.stubhub.com/oregon-ducks-football-tickets-oregon-ducks-football-eugene-autzen-stadium-9-5-2020/event/104551640/?sliderMax=219.06^%^2C80.32^&sliderMin=63.06^%^2C5.32" ^
  -H "cookie: bff-activity=2a684a55-907a-4593-adab-1952d0890b8f; SH_VI=2b95b2f36411495581db73e34ae0edb5; _sim_si=00C7EC6D-3627-440F-A5D1-20C59E9667C5; _sim_uuid=283D9D09-6C5F-4317-8CF5-051542135067; _gcl_au=1.1.1108479576.1592234330; s_ecid=MCMID^%^7C46626207844130676803196963989911135569; AMCVS_1AEC46735278551A0A490D45^%^40AdobeOrg=1; _fbp=fb.1.1592234332677.1319181848; joe-chnlcustid=-1498868730; spd-custhash=b9f2017b6ff52106c183796f189a386b2ff3a02d; s_vi=^[CS^]v1^|2F73C8B70515F0D9-4000088249AD25E0^[CE^]; QuantumMetricUserID=b87c88876ea603f7053a3fd6282e0831; xdVisitorId=10A3nTtt7RrRt59qunz6ZhyxX48A3dhlOtIvHv_qMzaGsLg941D; atgRecVisitorId=10A3nTtt7RrRt59qunz6ZhyxX48A3dhlOtIvHv_qMzaGsLg941D; STUB_SESS=filler^%^7E^%^5E^%^7E0^%^7Capp_token^%^7E^%^5E^%^7EBImXAmYKv7MZjdJqQiBaUOcoa2HXA3Bgr5nl^%^2Fie9i9Y^%^3D^%^7E^%^5E^%^7E06^%^2F22^%^2F2020; optimizelyEndUserId=oeu1592833915557r0.42987514280138606; SH_SI=862BE1891F3945E892C07A8B1D9E407A; session_userGUID=A718F7ACD10676BFE0540010E0E2332E; track_session_userGUID=A718F7ACD10676BFE0540010E0E2332E; session_uAuthenticated=1; session_login_type=stubhub; session_CSRFtoken=AJfNm5O6BJ8ZI/wMXCTS+UfzOHiVGw0mlNFLFhAlxn3KJDbJn6JEbfnTCwLLrtMiV9MZli5wLtbgEafXF1fuZPa++FI9lMc0tLpvtZW/93E=; session_sessionId=862BE1891F3945E892C07A8B1D9E407A; session_contactGUID=6VCcpPviei-xnhHU; SH_UT=o7ea6zizI81BHnS28Jx26FVnyvzGm^%^2FBsynb9lakySYibUq4qGzeanA8ewuQN3A4vxo2WQjIfrVy3U4c^%^2FKteG9NUF3Na^%^2FJ9QXRkmoFp8klUNQCIkJWzh1jjWPjj^%^2FayxauiSyABbI^%^2BhwKDJXctuOrXHKZX1FJuRnjCqcaEiAYnmDD57OopUvDz^%^2FDoP1J97sTvunGHVY1GfherKgNzbgJGsXKGPQKh4bPkm5at4ff368SGqSuxI^%^2Fcf1g5CJcEsIpBD^%^2F1RZEXvJEbjB3MhaFkvI1Jw^%^3D^%^3D; S_ACCT=stubhub^%^2Cstubhubglobal; tracker_device=1907cd66-dbda-49ce-a5f5-260e47ef3f82; QSI_HistorySession=https^%^3A^%^2F^%^2Fwww.stubhub.com^%^2F~1592234360423^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fncaa-football-tickets^%^2Fgrouping^%^2F122^%^2F~1592243673098^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2F~1592247725869^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Ferror~1592798731835^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2F~1592798790503^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fmy^%^2Fprofile^%^2F~1592833989941^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fmy^%^2Fprofile~1592837652296^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2F~1593061403146^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fabout-us~1593062162857^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fabout-us^%^2F~1593062206094^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2F~1593062279066^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fmy^%^2Fsettings~1593379169050^%^7Chttps^%^3A^%^2F^%^2Fwww.stubhub.com^%^2Fmy^%^2Fprofile~1593379199637; QuantumMetricSessionID=1cd4480f01ea3e515d95af29aaa9afe5; SH6_USER_PREF=^%^7B^%^22location^%^22^%^3A^%^7B^%^22geoNameId^%^22^%^3A4671654^%^2C^%^22city^%^22^%^3A^%^22Austin^%^22^%^2C^%^22stateCode^%^22^%^3A^%^22TX^%^22^%^2C^%^22state^%^22^%^3A^%^22Texas^%^22^%^2C^%^22countryCode^%^22^%^3A^%^22US^%^22^%^2C^%^22country^%^22^%^3A^%^22United^%^20States^%^22^%^2C^%^22latitude^%^22^%^3A30.26715^%^2C^%^22longitude^%^22^%^3A-97.74306^%^2C^%^22key^%^22^%^3A4671654^%^2C^%^22name^%^22^%^3A^%^22Austin^%^2C^%^20TX^%^22^%^7D^%^7D; _sim_cr=eyJkZXZpY2VfaWQiOiJiNDQ5ZTAzNGU2NDM2MTNiNTgyNjAxNWExMjk5MjJhZSIsInMiOiJkMjg3ZDM1OTgzMTk0ODg2OTU5ODllYWY5NmNiYTE5YSIsImUiOjE1OTQwNTE5NDg4Nzl9; session_loginStatus=true; S_ACCT=stubhub; atgRecSessionId=h5ManYUXV_WX00C2NBUXeWTAQsY6LnWZeRyKkEepcvqjkQ4oPQ2V^!-632622553^!-1657022320; _4c_=Fcw9DsIhDAfQu^%^2FxmhtKWQrnNX4FoTBw08SOEu6PT297E^%^2B9LvqDG5lOwa2SwF3Pr3iTrxuLY^%^2FL1QUJdJjSJTexLlpGS4mp8F2nFkcAZ^%^2FfY0QpaxYmprXWBg^%^3D^%^3D; TLTHID=12D17E2CBE1210BE22A8BCF94CF38AC1; TLTSID=12D17E2CBE1210BE22A8BCF94CF38AC1; SH_AT=1XNOHCPxzhOmYfQsadRFfX^%^2FOMRCZ0KKzhzQg^%^2BzAtaxxW5pfv1Rx11KOIF7aMprwA6O6l8xTs7T3zEPsZub5i1euhDev2QbF^%^2F^%^2B4kbeKOuLuk^%^3D; AKA_A2=A; bm_sz=201E3036A4654F93D0EBEA9723D38B47~YAAQq4gauPKoU85yAQAAlXOVHAhBcGBizgQN6ZbcBWnSL/Buf4TLknETySyg0NMi541u1AORk+ycvEKHmeLucYKiBXxksLL57txQ/J77gAyWhyIIVdprFDXxHiv16VFnX2BttO9e+ica24GLakLoc5/e59T0qeas+MKbtHgjok63b0pu5sUqEHgnion+144y8g==; ak_bmsc=F83FF018278A15615839D96DA110C1D9B81A88ABB8540000672C015FF221FF4E~plVYOO8kEWueCDHN4B3WgHfIVDhY4c+FgmNIyMd5P6s3lS9Nyrc73umzihu36wWtQYFWcjkmgB5HkxEzhFOtvtnhHByw37kwVWP83U49EDsdp5Wr1y8yS352E95J6h+MI1UhJiCCaDf8bpa4oYLB5U2CLfw0J0Bl/XV+hhTjrDCG6HJZEeuCVbfDNFy5VpWb00gImFMF27CkplW4+ugLJcuZ0ZwJGrFLYcspNu0KkcTGCmQ6FITRy3ozhQO6uM+6TN; _dpm_ses.8d04=*; _dpm_id.8d04=2fbdb3d7-4cb2-4db5-9094-511fec2ad37d.1592243585.38.1593912427.1593892999.08c0e13b-c47f-4a20-8c77-21029fc54322; AMCV_1AEC46735278551A0A490D45^%^40AdobeOrg=1075005958^%^7CMCIDTS^%^7C18449^%^7CMCMID^%^7C46626207844130676803196963989911135569^%^7CMCAID^%^7CNONE^%^7CMCOPTOUT-1593919627s^%^7CNONE^%^7CMCAAMLH-1594517227^%^7C9^%^7CMCAAMB-1594517227^%^7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI^%^7CMCSYNCSOP^%^7C411-18450^%^7CvVersion^%^7C4.4.1; _sim_li=NGY0NDE3MWQtNmUwYy00Njc2LTg2M2ItYmZmMmMxNjAzZWEyLmxvY2FsLDEzNi40OS42OC40MA==; RT=^\^"sl=1^&ss=kc8eavnj^&tt=8py^&z=1^&dm=stubhub.com^&si=df952824-a9bb-43c6-9ac0-99b5f96ef805^&ld=8qi^\^"; s_sess=^%^20s_sq^%^3D^%^3B^%^20s_cpc^%^3D1^%^3B^%^20s_cc^%^3Dtrue^%^3B^%^20s_tp^%^3D780^%^3B^%^20s_ptc^%^3D0.02^%^255E^%^255E0.02^%^255E^%^255E0.00^%^255E^%^255E0.50^%^255E^%^255E1.24^%^255E^%^255E0.26^%^255E^%^255E9.40^%^255E^%^255E0.09^%^255E^%^255E11.30^%^3B^%^20s_ppv^%^3DEvent^%^252520details^%^252C100^%^252C100^%^252C780^%^3B; _uetsid=dbc25b07-5607-bfb9-c347-e2da82aee149; _uetvid=5c3ab57f-2e0b-7347-f42e-e6f4a23abe44; cto_bundle=CxwF919ZRHFvamo2Vmt2QlAzQzgwd00wbnhDaEJqTG9BUGFnTEMlMkJzMVRWbWJDSk55clFDSCUyQkVQVzEyZm5MbVAxcDAzT25RbG5ya0JMUGRSMllpZ0VHZnJ0YTI5bkx4QXQxZnZzRno3bUIwV0JuUnlESng0TEx4dXZaWkpKVUpTdCUyRklLZHA1VERMUVpQTnIxWEdESzdjN1lPeGclM0QlM0Q; utag_main=v_id:0172b88fb719000f04cb435a5a6403082001807a00900^$_sn:42^$_se:2^$_ss:0^$_st:1593914241275^$dc_visit:40^$ses_id:1593912425651^%^3Bexp-session^$_pn:1^%^3Bexp-session^$dc_event:2^%^3Bexp-session^$dc_region:us-east-1^%^3Bexp-session; s_pers=^%^20s_cpm1^%^3D^%^255B^%^255B^%^2527chEMAIL-_-geoUS-_-cmpFORGOT_PASSWORD_RESET^%^2527^%^252C^%^25271593379110516^%^2527^%^255D^%^255D^%^7C1751145510516^%^3B^%^20s_fid^%^3D6F34F89A2B9D050B-3D1E120DBF3FBA8B^%^7C1751378495656^%^3B^%^20s_dfa^%^3Dstubhub^%^252Cstubhubglobal^%^7C1593914226760^%^3B^%^20s_vs^%^3D1^%^7C1593914241304^%^3B^%^20gpv_v9^%^3DEvent^%^2520details^%^7C1593914241310^%^3B^%^20s_nr^%^3D1593912441317-Repeat^%^7C1628040441317^%^3B; _abck=94CDA16B3AE9496AB4AE1E14C9093B07~-1~YAAQq4gauAmpU85yAQAAhb+VHAT94LZVO4wbpi63H2DaF+3MZqQ9UduOWAU8b1E6wh7w5rRRiCyMMHAQumBaKRgiCYQ/GigeH4yXHmjhShEjwpB1F27juIgBgTa42Z83FLDN3BVGEQh/N4URsDFSMJZXIkuou28VUKcMgaUwm3k8iHTBZXMGk3dDSPDAJPtgewmz921LL5ONYfogQkhtUowMzGeUs0xV/+Kd2+pqHphC4m/cZ8KYdRwCjFLxUAwyYDww5tzwDgYuU8yEDuIIrwzQb67/ro/CkcVahvgjA7my59GTpV7mVuA+DUEhbyfTReck7Ktdf0AAycBBWiiogJPqU0IN~-1~-1~-1; SH_BAU=^%^7B^%^22id^%^22^%^3A^%^221593913343.6411495581db73e3^%^22^%^2C^%^22key^%^22^%^3A^%^22yGJGwWU36NgdF2MmbwB1bZACRn0AMEw5wvljmQds0yU^%^3D^%^22^%^2C^%^22algorithm^%^22^%^3A^%^22sha256^%^22^%^7D; ADRUM_BT=R:171^|i:38465^|g:55589228-db14-4958-8423-cfdf6fdda0644409211^|e:172^|n:stubhub_265eecb8-d565-4dc1-8f9e-d80fa9fe2b31; akacd_PCF_Prod=1593998843~rv=37~id=94d30e4469a0aea771115f3bbd4bd6ae; s_tps=32; s_pvs=141" ^
  --compressed
    # 1. FOLLOWING LEVEL 1
    def parse(self, response):
        self.log(response.request.meta)
        self.log(response.request)
        self.log(response)
        self.log(response.selector.xpath('//title/@text'))
        page = response.url.split("/")[-2]  # getting the page number from the URL
        filename = 'local_output/' + '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        # with open('image.png', 'wb') as image_file:
        #     image_file.write(response.meta['screenshot'])
        self.log('Saved file %s' % filename)
        self.log('source file %s' % response.url)


        # # event_class = 'li.Desktop__DesktopEventListItem-sc-7xzvm2-17'
        # event_class = 'li.gMXTbB'
        # # main_col_class = 'div.Desktop__MainColumn-sc-7xzvm2-9'
        # main_col_class = 'div.ifgpyY'
        # # date_col_class = 'div.Desktop__DateColumn-sc-7xzvm2-8'
        # date_col_class = 'div.koCdzW'
        # # button_col_class = 'div.Desktop__ButtonColumn-sc-7xzvm2-10'
        # button_col_class = 'div.dGpRaR'
        # # button_class = 'span.Button__ButtonContents-ui1y7a-1'
        # button_class = 'span.cGpKQs'
        # # title_class = 'p.Desktop__Title-sc-7xzvm2-1'
        # title_class = 'p.ejNLVa'
        # # sub_title_class = 'p.Desktop__Subtitle-sc-7xzvm2-3'
        # sub_title_class = 'p.imOfJF'
        items = []
        # self.log(response.css('script::text'))
        # self.log(response.css('ul').css('li').css('a').css('div').css('div').css('p').getall())
        # self.log(response.css('ul').css('li').css('div').css('script'))
        # self.log(response.xpath('//span[has-class("bMjfIb")]'))

        # for event in response.css(event_class):
        #     item = EventItem()
        #     item.date = event.css(date_col_class).css(f'{title_class}::text').get()
        #     item.day_n_time = event.css(date_col_class).css(f'{sub_title_class}::text').get()
        #     item.title = event.css(main_col_class).css(f'{title_class}::text').get()
        #     item.location = event.css(main_col_class).css(f'{sub_title_class}::text').get()
        #     item.price = event.css(button_col_class).css(f'{button_class}::text').get()
        #     item.data = event.css('script::text').get()
        #     item.item_type = "event"
        #     self.log(item)
        #     items.append(item)
        return items



        # for follow_url in response.css("").extract():
        #     yield response.follow(follow_url, self.populate_item)
        # yield self.paginate(response)

    # 2. SCRAPING LEVEL 2
    # def populate_item(self, response):
        # item_loader = ItemLoader(item=MySpiderItem(), response=response)
        # item_loader.default_input_processor = MapCompose(remove_tags)

        # item_loader.add_css("", "")
        # yield item_loader.load_item()

    # 3. PAGINATION LEVEL 1
    # def paginate(self, response):
        # next_page_url = response.css("").extract_first()  # pagination("next button") <a> element here
        # if next_page_url is not None:
        #     return response.follow(next_page_url, self.parse)





curl 'https://www.stubhub.com/bfx/api/search/inventory/v2/listings?additionalPricingInfo=true&allSectionZoneStats=true&edgeControlEnabled=true&eventLevelStats=true&eventPricingSummary=true&listingAttributeCategorySummary=true&pricingSummary=true&quantitySummary=true&sectionStats=true&shstore=1&start=20&urgencyMessaging=true&valuePercentage=true&zoneStats=true&scoreVersion=v2&eventId=104551640&quantity=&rows=20&sort=price%20asc%2C%20value%20desc&priceType=nonBundledPrice&listingAttributeCategoryList=&excludeListingAttributeCategoryList=&deliveryTypeList=&sectionIdList=&zoneIdList=&pricemin=63.06&pricemax=219.06&listingRows=' \
  -H 'authority: www.stubhub.com' \
  -H 'accept: application/json' \
  -H 'authorization: Hawk id="1593913343.6411495581db73e3", ts="1593912461", nonce="fgb8yj", mac="zQTLuLh8LOGSAzaTF+r2vZhukktKmfcx8X7jeotqBqs="' \
  -H 'accept-language: en-US' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.stubhub.com/oregon-ducks-football-tickets-oregon-ducks-football-eugene-autzen-stadium-9-5-2020/event/104551640/?sliderMax=219.06%2C80.32&sliderMin=63.06%2C5.32' \
  -H $'cookie: bff-activity=2a684a55-907a-4593-adab-1952d0890b8f; SH_VI=2b95b2f36411495581db73e34ae0edb5; _sim_si=00C7EC6D-3627-440F-A5D1-20C59E9667C5; _sim_uuid=283D9D09-6C5F-4317-8CF5-051542135067; _gcl_au=1.1.1108479576.1592234330; s_ecid=MCMID%7C46626207844130676803196963989911135569; AMCVS_1AEC46735278551A0A490D45%40AdobeOrg=1; _fbp=fb.1.1592234332677.1319181848; joe-chnlcustid=-1498868730; spd-custhash=b9f2017b6ff52106c183796f189a386b2ff3a02d; s_vi=[CS]v1|2F73C8B70515F0D9-4000088249AD25E0[CE]; QuantumMetricUserID=b87c88876ea603f7053a3fd6282e0831; xdVisitorId=10A3nTtt7RrRt59qunz6ZhyxX48A3dhlOtIvHv_qMzaGsLg941D; atgRecVisitorId=10A3nTtt7RrRt59qunz6ZhyxX48A3dhlOtIvHv_qMzaGsLg941D; STUB_SESS=filler%7E%5E%7E0%7Capp_token%7E%5E%7EBImXAmYKv7MZjdJqQiBaUOcoa2HXA3Bgr5nl%2Fie9i9Y%3D%7E%5E%7E06%2F22%2F2020; optimizelyEndUserId=oeu1592833915557r0.42987514280138606; SH_SI=862BE1891F3945E892C07A8B1D9E407A; session_userGUID=A718F7ACD10676BFE0540010E0E2332E; track_session_userGUID=A718F7ACD10676BFE0540010E0E2332E; session_uAuthenticated=1; session_login_type=stubhub; session_CSRFtoken=AJfNm5O6BJ8ZI/wMXCTS+UfzOHiVGw0mlNFLFhAlxn3KJDbJn6JEbfnTCwLLrtMiV9MZli5wLtbgEafXF1fuZPa++FI9lMc0tLpvtZW/93E=; session_sessionId=862BE1891F3945E892C07A8B1D9E407A; session_contactGUID=6VCcpPviei-xnhHU; SH_UT=o7ea6zizI81BHnS28Jx26FVnyvzGm%2FBsynb9lakySYibUq4qGzeanA8ewuQN3A4vxo2WQjIfrVy3U4c%2FKteG9NUF3Na%2FJ9QXRkmoFp8klUNQCIkJWzh1jjWPjj%2FayxauiSyABbI%2BhwKDJXctuOrXHKZX1FJuRnjCqcaEiAYnmDD57OopUvDz%2FDoP1J97sTvunGHVY1GfherKgNzbgJGsXKGPQKh4bPkm5at4ff368SGqSuxI%2Fcf1g5CJcEsIpBD%2F1RZEXvJEbjB3MhaFkvI1Jw%3D%3D; S_ACCT=stubhub%2Cstubhubglobal; tracker_device=1907cd66-dbda-49ce-a5f5-260e47ef3f82; QSI_HistorySession=https%3A%2F%2Fwww.stubhub.com%2F~1592234360423%7Chttps%3A%2F%2Fwww.stubhub.com%2Fncaa-football-tickets%2Fgrouping%2F122%2F~1592243673098%7Chttps%3A%2F%2Fwww.stubhub.com%2F~1592247725869%7Chttps%3A%2F%2Fwww.stubhub.com%2Ferror~1592798731835%7Chttps%3A%2F%2Fwww.stubhub.com%2F~1592798790503%7Chttps%3A%2F%2Fwww.stubhub.com%2Fmy%2Fprofile%2F~1592833989941%7Chttps%3A%2F%2Fwww.stubhub.com%2Fmy%2Fprofile~1592837652296%7Chttps%3A%2F%2Fwww.stubhub.com%2F~1593061403146%7Chttps%3A%2F%2Fwww.stubhub.com%2Fabout-us~1593062162857%7Chttps%3A%2F%2Fwww.stubhub.com%2Fabout-us%2F~1593062206094%7Chttps%3A%2F%2Fwww.stubhub.com%2F~1593062279066%7Chttps%3A%2F%2Fwww.stubhub.com%2Fmy%2Fsettings~1593379169050%7Chttps%3A%2F%2Fwww.stubhub.com%2Fmy%2Fprofile~1593379199637; QuantumMetricSessionID=1cd4480f01ea3e515d95af29aaa9afe5; SH6_USER_PREF=%7B%22location%22%3A%7B%22geoNameId%22%3A4671654%2C%22city%22%3A%22Austin%22%2C%22stateCode%22%3A%22TX%22%2C%22state%22%3A%22Texas%22%2C%22countryCode%22%3A%22US%22%2C%22country%22%3A%22United%20States%22%2C%22latitude%22%3A30.26715%2C%22longitude%22%3A-97.74306%2C%22key%22%3A4671654%2C%22name%22%3A%22Austin%2C%20TX%22%7D%7D; _sim_cr=eyJkZXZpY2VfaWQiOiJiNDQ5ZTAzNGU2NDM2MTNiNTgyNjAxNWExMjk5MjJhZSIsInMiOiJkMjg3ZDM1OTgzMTk0ODg2OTU5ODllYWY5NmNiYTE5YSIsImUiOjE1OTQwNTE5NDg4Nzl9; session_loginStatus=true; S_ACCT=stubhub; atgRecSessionId=h5ManYUXV_WX00C2NBUXeWTAQsY6LnWZeRyKkEepcvqjkQ4oPQ2V\u0021-632622553\u0021-1657022320; _4c_=Fcw9DsIhDAfQu%2FxmhtKWQrnNX4FoTBw08SOEu6PT297E%2B9LvqDG5lOwa2SwF3Pr3iTrxuLY%2FL1QUJdJjSJTexLlpGS4mp8F2nFkcAZ%2FfY0QpaxYmprXWBg%3D%3D; TLTHID=12D17E2CBE1210BE22A8BCF94CF38AC1; TLTSID=12D17E2CBE1210BE22A8BCF94CF38AC1; SH_AT=1XNOHCPxzhOmYfQsadRFfX%2FOMRCZ0KKzhzQg%2BzAtaxxW5pfv1Rx11KOIF7aMprwA6O6l8xTs7T3zEPsZub5i1euhDev2QbF%2F%2B4kbeKOuLuk%3D; AKA_A2=A; bm_sz=201E3036A4654F93D0EBEA9723D38B47~YAAQq4gauPKoU85yAQAAlXOVHAhBcGBizgQN6ZbcBWnSL/Buf4TLknETySyg0NMi541u1AORk+ycvEKHmeLucYKiBXxksLL57txQ/J77gAyWhyIIVdprFDXxHiv16VFnX2BttO9e+ica24GLakLoc5/e59T0qeas+MKbtHgjok63b0pu5sUqEHgnion+144y8g==; ak_bmsc=F83FF018278A15615839D96DA110C1D9B81A88ABB8540000672C015FF221FF4E~plVYOO8kEWueCDHN4B3WgHfIVDhY4c+FgmNIyMd5P6s3lS9Nyrc73umzihu36wWtQYFWcjkmgB5HkxEzhFOtvtnhHByw37kwVWP83U49EDsdp5Wr1y8yS352E95J6h+MI1UhJiCCaDf8bpa4oYLB5U2CLfw0J0Bl/XV+hhTjrDCG6HJZEeuCVbfDNFy5VpWb00gImFMF27CkplW4+ugLJcuZ0ZwJGrFLYcspNu0KkcTGCmQ6FITRy3ozhQO6uM+6TN; _dpm_ses.8d04=*; _dpm_id.8d04=2fbdb3d7-4cb2-4db5-9094-511fec2ad37d.1592243585.38.1593912427.1593892999.08c0e13b-c47f-4a20-8c77-21029fc54322; AMCV_1AEC46735278551A0A490D45%40AdobeOrg=1075005958%7CMCIDTS%7C18449%7CMCMID%7C46626207844130676803196963989911135569%7CMCAID%7CNONE%7CMCOPTOUT-1593919627s%7CNONE%7CMCAAMLH-1594517227%7C9%7CMCAAMB-1594517227%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-18450%7CvVersion%7C4.4.1; _sim_li=NGY0NDE3MWQtNmUwYy00Njc2LTg2M2ItYmZmMmMxNjAzZWEyLmxvY2FsLDEzNi40OS42OC40MA==; RT="sl=1&ss=kc8eavnj&tt=8py&z=1&dm=stubhub.com&si=df952824-a9bb-43c6-9ac0-99b5f96ef805&ld=8qi"; s_sess=%20s_sq%3D%3B%20s_cpc%3D1%3B%20s_cc%3Dtrue%3B%20s_tp%3D780%3B%20s_ptc%3D0.02%255E%255E0.02%255E%255E0.00%255E%255E0.50%255E%255E1.24%255E%255E0.26%255E%255E9.40%255E%255E0.09%255E%255E11.30%3B%20s_ppv%3DEvent%252520details%252C100%252C100%252C780%3B; _uetsid=dbc25b07-5607-bfb9-c347-e2da82aee149; _uetvid=5c3ab57f-2e0b-7347-f42e-e6f4a23abe44; cto_bundle=CxwF919ZRHFvamo2Vmt2QlAzQzgwd00wbnhDaEJqTG9BUGFnTEMlMkJzMVRWbWJDSk55clFDSCUyQkVQVzEyZm5MbVAxcDAzT25RbG5ya0JMUGRSMllpZ0VHZnJ0YTI5bkx4QXQxZnZzRno3bUIwV0JuUnlESng0TEx4dXZaWkpKVUpTdCUyRklLZHA1VERMUVpQTnIxWEdESzdjN1lPeGclM0QlM0Q; utag_main=v_id:0172b88fb719000f04cb435a5a6403082001807a00900$_sn:42$_se:2$_ss:0$_st:1593914241275$dc_visit:40$ses_id:1593912425651%3Bexp-session$_pn:1%3Bexp-session$dc_event:2%3Bexp-session$dc_region:us-east-1%3Bexp-session; s_pers=%20s_cpm1%3D%255B%255B%2527chEMAIL-_-geoUS-_-cmpFORGOT_PASSWORD_RESET%2527%252C%25271593379110516%2527%255D%255D%7C1751145510516%3B%20s_fid%3D6F34F89A2B9D050B-3D1E120DBF3FBA8B%7C1751378495656%3B%20s_dfa%3Dstubhub%252Cstubhubglobal%7C1593914226760%3B%20s_vs%3D1%7C1593914241304%3B%20gpv_v9%3DEvent%2520details%7C1593914241310%3B%20s_nr%3D1593912441317-Repeat%7C1628040441317%3B; _abck=94CDA16B3AE9496AB4AE1E14C9093B07~-1~YAAQq4gauAmpU85yAQAAhb+VHAT94LZVO4wbpi63H2DaF+3MZqQ9UduOWAU8b1E6wh7w5rRRiCyMMHAQumBaKRgiCYQ/GigeH4yXHmjhShEjwpB1F27juIgBgTa42Z83FLDN3BVGEQh/N4URsDFSMJZXIkuou28VUKcMgaUwm3k8iHTBZXMGk3dDSPDAJPtgewmz921LL5ONYfogQkhtUowMzGeUs0xV/+Kd2+pqHphC4m/cZ8KYdRwCjFLxUAwyYDww5tzwDgYuU8yEDuIIrwzQb67/ro/CkcVahvgjA7my59GTpV7mVuA+DUEhbyfTReck7Ktdf0AAycBBWiiogJPqU0IN~-1~-1~-1; SH_BAU=%7B%22id%22%3A%221593913343.6411495581db73e3%22%2C%22key%22%3A%22yGJGwWU36NgdF2MmbwB1bZACRn0AMEw5wvljmQds0yU%3D%22%2C%22algorithm%22%3A%22sha256%22%7D; ADRUM_BT=R:171|i:38465|g:55589228-db14-4958-8423-cfdf6fdda0644409211|e:172|n:stubhub_265eecb8-d565-4dc1-8f9e-d80fa9fe2b31; akacd_PCF_Prod=1593998843~rv=37~id=94d30e4469a0aea771115f3bbd4bd6ae; s_tps=32; s_pvs=141' \
  --compressed