# -*- coding: utf-8 -*-


class HolidayUtil:
    """
    法定节假日工具（自2001年12月29日起）
    """

    __SIZE = 18
    __ZERO = 48
    __TAG_REMOVE = "~"
    NAMES = ("元旦节", "春节", "清明节", "劳动节", "端午节", "中秋节", "国庆节", "国庆中秋", "抗战胜利日")
    __DATA = "200112290020020101200112300020020101200201010120020101200201020120020101200201030120020101200202091020020212200202101020020212200202121120020212200202131120020212200202141120020212200202151120020212200202161120020212200202171120020212200202181120020212200204273020020501200204283020020501200205013120020501200205023120020501200205033120020501200205043120020501200205053120020501200205063120020501200205073120021001200209286020021001200209296020021001200210016120021001200210026120021001200210036120021001200210046120021001200210056120021001200210066120021001200210076120021001200301010120030101200302011120030201200302021120030201200302031120030201200302041120030201200302051120030201200302061120030201200302071120030201200302081020030201200302091020030201200304263020030501200304273020030501200305013120030501200305023120030501200305033120030501200305043120030501200305053120030501200305063120030501200305073120031001200309276020031001200309286020031001200310016120031001200310026120031001200310036120031001200310046120031001200310056120031001200310066120031001200310076120031001200401010120040101200401171020040122200401181020040122200401221120040122200401231120040122200401241120040122200401251120040122200401261120040122200401271120040122200401281120040122200405013120040501200405023120040501200405033120040501200405043120040501200405053120040501200405063120040501200405073120041001200405083020040501200405093020040501200410016120041001200410026120041001200410036120041001200410046120041001200410056120041001200410066120041001200410076120041001200410096020041001200410106020041001200501010120050101200501020120050101200501030120050101200502051020050209200502061020050209200502091120050209200502101120050209200502111120050209200502121120050209200502131120050209200502141120050209200502151120050209200504303020050501200505013120050501200505023120050501200505033120050501200505043120050501200505053120050501200505063120050501200505073120051001200505083020050501200510016120051001200510026120051001200510036120051001200510046120051001200510056120051001200510066120051001200510076120051001200510086020051001200510096020051001200512310020060101200601010120060101200601020120060101200601030120060101200601281020060129200601291120060129200601301120060129200601311120060129200602011120060129200602021120060129200602031120060129200602041120060129200602051020060129200604293020060501200604303020060501200605013120060501200605023120060501200605033120060501200605043120060501200605053120060501200605063120060501200605073120061001200609306020061001200610016120061001200610026120061001200610036120061001200610046120061001200610056120061001200610066120061001200610076120061001200610086020061001200612300020070101200612310020070101200701010120070101200701020120070101200701030120070101200702171020070218200702181120070218200702191120070218200702201120070218200702211120070218200702221120070218200702231120070218200702241120070218200702251020070218200704283020070501200704293020070501200705013120070501200705023120070501200705033120070501200705043120070501200705053120070501200705063120070501200705073120070501200709296020071001200709306020071001200710016120071001200710026120071001200710036120071001200710046120071001200710056120071001200710066120071001200710076120071001200712290020080101200712300120080101200712310120080101200801010120080101200802021020080206200802031020080206200802061120080206200802071120080206200802081120080206200802091120080206200802101120080206200802111120080206200802121120080206200804042120080404200804052120080404200804062120080404200805013120080501200805023120080501200805033120080501200805043020080501200806074120080608200806084120080608200806094120080608200809135120080914200809145120080914200809155120080914200809276020081001200809286020081001200809296120081001200809306120081001200810016120081001200810026120081001200810036120081001200810046120081001200810056120081001200901010120090101200901020120090101200901030120090101200901040020090101200901241020090125200901251120090125200901261120090125200901271120090125200901281120090125200901291120090125200901301120090125200901311120090125200902011020090125200904042120090404200904052120090404200904062120090404200905013120090501200905023120090501200905033120090501200905284120090528200905294120090528200905304120090528200905314020090528200909276020091001200910016120091001200910026120091001200910036120091001200910046120091001200910055120091003200910065120091003200910075120091003200910085120091003200910105020091003201001010120100101201001020120100101201001030120100101201002131120100213201002141120100213201002151120100213201002161120100213201002171120100213201002181120100213201002191120100213201002201020100213201002211020100213201004032120100405201004042120100405201004052120100405201005013120100501201005023120100501201005033120100501201006124020100616201006134020100616201006144120100616201006154120100616201006164120100616201009195020100922201009225120100922201009235120100922201009245120100922201009255020100922201009266020101001201010016120101001201010026120101001201010036120101001201010046120101001201010056120101001201010066120101001201010076120101001201010096020101001201101010120110101201101020120110101201101030120110101201101301020110203201102021120110203201102031120110203201102041120110203201102051120110203201102061120110203201102071120110203201102081120110203201102121020110203201104022020110405201104032120110405201104042120110405201104052120110405201104303120110501201105013120110501201105023120110501201106044120110606201106054120110606201106064120110606201109105120110912201109115120110912201109125120110912201110016120111001201110026120111001201110036120111001201110046120111001201110056120111001201110066120111001201110076120111001201110086020111001201110096020111001201112310020120101201201010120120101201201020120120101201201030120120101201201211020120123201201221120120123201201231120120123201201241120120123201201251120120123201201261120120123201201271120120123201201281120120123201201291020120123201203312020120404201204012020120404201204022120120404201204032120120404201204042120120404201204283020120501201204293120120501201204303120120501201205013120120501201205023020120501201206224120120623201206234120120623201206244120120623201209295020120930201209305120120930201210016120121001201210026120121001201210036120121001201210046120121001201210056120121001201210066120121001201210076120121001201210086020121001201301010120130101201301020120130101201301030120130101201301050020130101201301060020130101201302091120130210201302101120130210201302111120130210201302121120130210201302131120130210201302141120130210201302151120130210201302161020130210201302171020130210201304042120130404201304052120130404201304062120130404201304273020130501201304283020130501201304293120130501201304303120130501201305013120130501201306084020130612201306094020130612201306104120130612201306114120130612201306124120130612201309195120130919201309205120130919201309215120130919201309225020130919201309296020131001201310016120131001201310026120131001201310036120131001201310046120131001201310056120131001201310066120131001201310076120131001201401010120140101201401261020140131201401311120140131201402011120140131201402021120140131201402031120140131201402041120140131201402051120140131201402061120140131201402081020140131201404052120140405201404062120140405201404072120140405201405013120140501201405023120140501201405033120140501201405043020140501201405314120140602201406014120140602201406024120140602201409065120140908201409075120140908201409085120140908201409286020141001201410016120141001201410026120141001201410036120141001201410046120141004201410056120141001201410066120141001201410076120141001201410116020141001201501010120150101201501020120150101201501030120150101201501040020150101201502151020150219201502181120150219201502191120150219201502201120150219201502211120150219201502221120150219201502231120150219201502241120150219201502281020150219201504042120150405201504052120150405201504062120150405201505013120150501201505023120150501201505033120150501201506204120150620201506214120150620201506224120150620201509038120150903201509048120150903201509058120150903201509068020150903201509265120150927201509275120150927201510016120151001201510026120151001201510036120151001201510046120151004201510056120151001201510066120151001201510076120151001201510106020151001201601010120160101201601020120160101201601030120160101201602061020160208201602071120160208201602081120160208201602091120160208201602101120160208201602111120160208201602121120160208201602131120160208201602141020160208201604022120160404201604032120160404201604042120160404201604303120160501201605013120160501201605023120160501201606094120160609201606104120160609201606114120160609201606124020160609201609155120160915201609165120160915201609175120160915201609185020160915201610016120161001201610026120161001201610036120161001201610046120161004201610056120161001201610066120161001201610076120161001201610086020161001201610096020161001201612310120170101201701010120170101201701020120170101201701221020170128201701271120170128201701281120170128201701291120170128201701301120170128201701311120170128201702011120170128201702021120170128201702041020170128201704012020170404201704022120170404201704032120170404201704042120170404201704293120170501201704303120170501201705013120170501201705274020170530201705284120170530201705294120170530201705304120170530201709306020171001201710016120171001201710026120171001201710036120171001201710045120171004201710056120171001201710066120171001201710076120171001201710086120171001201712300120180101201712310120180101201801010120180101201802111020180216201802151120180216201802161120180216201802171120180216201802181120180216201802191120180216201802201120180216201802211120180216201802241020180216201804052120180405201804062120180405201804072120180405201804082020180405201804283020180501201804293120180501201804303120180501201805013120180501201806164120180618201806174120180618201806184120180618201809225120180924201809235120180924201809245120180924201809296020181001201809306020181001201810016120181001201810026120181001201810036120181001201810046120181001201810056120181001201810066120181001201810076120181001201812290020190101201812300120190101201812310120190101201901010120190101201902021020190205201902031020190205201902041120190205201902051120190205201902061120190205201902071120190205201902081120190205201902091120190205201902101120190205201904052120190405201904062120190405201904072120190405201904283020190501201905013120190501201905023120190501201905033120190501201905043120190501201905053020190501201906074120190607201906084120190607201906094120190607201909135120190913201909145120190913201909155120190913201909296020191001201910016120191001201910026120191001201910036120191001201910046120191001201910056120191001201910066120191001201910076120191001201910126020191001202001010120200101202001191020200125202001241120200125202001251120200125202001261120200125202001271120200125202001281120200125202001291120200125202001301120200125202001311120200125202002011120200125202002021120200125202004042120200404202004052120200404202004062120200404202004263020200501202005013120200501202005023120200501202005033120200501202005043120200501202005053120200501202005093020200501202006254120200625202006264120200625202006274120200625202006284020200625202009277020201001202010017120201001202010026120201001202010036120201001202010046120201001202010056120201001202010066120201001202010076120201001202010086120201001202010106020201001202101010120210101202101020120210101202101030120210101202102071020210212202102111120210212202102121120210212202102131120210212202102141120210212202102151120210212202102161120210212202102171120210212202102201020210212202104032120210404202104042120210404202104052120210404202104253020210501202105013120210501202105023120210501202105033120210501202105043120210501202105053120210501202105083020210501202106124120210614202106134120210614202106144120210614202109185020210921202109195120210921202109205120210921202109215120210921202109266020211001202110016120211001202110026120211001202110036120211001202110046120211001202110056120211001202110066120211001202110076120211001202110096020211001202201010120220101202201020120220101202201030120220101202201291020220201202201301020220201202201311120220201202202011120220201202202021120220201202202031120220201202202041120220201202202051120220201202202061120220201202204022020220405202204032120220405202204042120220405202204052120220405202204243020220501202204303120220501202205013120220501202205023120220501202205033120220501202205043120220501202205073020220501202206034120220603202206044120220603202206054120220603202209105120220910202209115120220910202209125120220910202210016120221001202210026120221001202210036120221001202210046120221001202210056120221001202210066120221001202210076120221001202210086020221001202210096020221001202212310120230101202301010120230101202301020120230101202301211120230122202301221120230122202301231120230122202301241120230122202301251120230122202301261120230122202301271120230122202301281020230122202301291020230122202304052120230405202304233020230501202304293120230501202304303120230501202305013120230501202305023120230501202305033120230501202305063020230501202306224120230622202306234120230622202306244120230622202306254020230622202309295120230929202309306120231001202310016120231001202310026120231001202310036120231001202310046120231001202310056120231001202310066120231001202310076020231001202310086020231001202312300120240101202312310120240101202401010120240101202402041020240210202402101120240210202402111120240210202402121120240210202402131120240210202402141120240210202402151120240210202402161120240210202402171120240210202402181020240210202404042120240404202404052120240404202404062120240404202404072020240404202404283020240501202405013120240501202405023120240501202405033120240501202405043120240501202405053120240501202405113020240501202406084120240610202406094120240610202406104120240610202409145020240917202409155120240917202409165120240917202409175120240917202409296020241001202410016120241001202410026120241001202410036120241001202410046120241001202410056120241001202410066120241001202410076120241001202410126020241001"

    __NAMES_IN_USE = NAMES
    __DATA_IN_USE = __DATA

    def __init__(self):
        pass

    @staticmethod
    def __padding(n):
        return ("0" if n < 10 else "") + str(n)

    @staticmethod
    def __buildHolidayForward(s):
        day = s[0:8]
        name = HolidayUtil.__NAMES_IN_USE[ord(s[8:9]) - HolidayUtil.__ZERO]
        work = ord(s[9:10]) == HolidayUtil.__ZERO
        target = s[10:18]
        from .. import Holiday
        return Holiday(day, name, work, target)

    @staticmethod
    def __buildHolidayBackward(s):
        size = len(s)
        day = s[size - 18:size - 10]
        name = HolidayUtil.__NAMES_IN_USE[ord(s[size - 10:size - 9]) - HolidayUtil.__ZERO]
        work = ord(s[size - 9:size - 8]) == HolidayUtil.__ZERO
        target = s[size - 8:]
        from .. import Holiday
        return Holiday(day, name, work, target)

    @staticmethod
    def __findForward(key):
        start = HolidayUtil.__DATA_IN_USE.find(key)
        if start < 0:
            return None
        right = HolidayUtil.__DATA_IN_USE[start:]
        n = len(right) % HolidayUtil.__SIZE
        if n > 0:
            right = right[n:]
        while not right.startswith(key) and len(right) >= HolidayUtil.__SIZE:
            right = right[HolidayUtil.__SIZE:]
        return right

    @staticmethod
    def __findBackward(key):
        start = HolidayUtil.__DATA_IN_USE.rfind(key)
        if start < 0:
            return None
        key_size = len(key)
        left = HolidayUtil.__DATA_IN_USE[0:start + key_size]
        size = len(left)
        n = size % HolidayUtil.__SIZE
        if n > 0:
            left = left[0:size - n]
        size = len(left)
        while size - key_size != left.rfind(key) and size >= HolidayUtil.__SIZE:
            left = left[0:size - HolidayUtil.__SIZE]
            size = len(left)
        return left

    @staticmethod
    def __findHolidaysForward(key):
        arr = []
        s = HolidayUtil.__findForward(key)
        if s is None:
            return arr
        while s.startswith(key):
            arr.append(HolidayUtil.__buildHolidayForward(s))
            s = s[HolidayUtil.__SIZE:]
        return arr

    @staticmethod
    def __findHolidaysBackward(key):
        arr = []
        s = HolidayUtil.__findBackward(key)
        if s is None:
            return arr
        size = len(s)
        key_size = len(key)

        while size - key_size == s.rfind(key):
            arr.append(HolidayUtil.__buildHolidayBackward(s))
            s = s[0:size - HolidayUtil.__SIZE:]
            size = len(s)
        arr.reverse()
        return arr

    @staticmethod
    def __getHoliday(year, month=0, day=0):
        y = str(year)
        if month == 0 or day == 0:
            arr = HolidayUtil.__findHolidaysForward(y.replace("-", ""))
        else:
            arr = HolidayUtil.__findHolidaysForward(y + HolidayUtil.__padding(month) + HolidayUtil.__padding(day))
        return None if len(arr) < 1 else arr[0]

    @staticmethod
    def __getHolidays(year, month=0):
        y = str(year)
        if month == 0:
            arr = HolidayUtil.__findHolidaysForward(y.replace("-", ""))
        else:
            arr = HolidayUtil.__findHolidaysForward(y + HolidayUtil.__padding(month))
        return arr

    @staticmethod
    def __getHolidaysByTarget(year, month=0, day=0):
        y = str(year)
        if month == 0 or day == 0:
            arr = HolidayUtil.__findHolidaysBackward(y.replace("-", ""))
        else:
            arr = HolidayUtil.__findHolidaysBackward(y + HolidayUtil.__padding(month) + HolidayUtil.__padding(day))
        return arr

    @staticmethod
    def getHoliday(year, month=0, day=0):
        """
        获取指定年月日的节假日信息，如果不存在，返回None
        :param year: 年或者yyyy-mm-dd格式的日期
        :param month: 月，数字1到12，如果year使用yyyy-mm-dd则不传该参数或设为0
        :param day: 日，数字1到31，如果year使用yyyy-mm-dd则不传该参数或设为0
        :return: Holiday或者None
        """
        return HolidayUtil.__getHoliday(year, month, day)

    @staticmethod
    def getHolidays(year, month=0):
        return HolidayUtil.__getHolidays(year, month)

    @staticmethod
    def getHolidaysByTarget(year, month=0, day=0):
        return HolidayUtil.__getHolidaysByTarget(year, month, day)

    @staticmethod
    def fix(names, data):
        """
        修正或追加节假日数据。节假日名称下标从0开始，超过9的，按ASCII码表依次往后排列；调休标识0为上班，否则放假
        :param names: 用于替换默认的节假日名称列表，传None即可使用默认名称
        :param data: 需要修正或追加的节假日数据，每18位表示1天依次排列，格式：当天年月日YYYYMMDD(8位)+节假日名称下标(1位)+调休标识(1位)+节假日当天YYYYMMDD(8位)。例：202005023120200501代表2020-05-02为劳动节放假，对应节假日为2020-05-01
        :return:
        """
        if names is not None:
            HolidayUtil.__NAMES_IN_USE = names
        if data is None:
            return
        append = ""
        while len(data) >= HolidayUtil.__SIZE:
            segment = data[:HolidayUtil.__SIZE]
            day = segment[:8]
            remove = HolidayUtil.__TAG_REMOVE == segment[8:9]
            holiday = HolidayUtil.getHoliday(day)
            if holiday is None:
                if not remove:
                    append += segment
            else:
                name_index = -1
                for i in range(0, len(HolidayUtil.__NAMES_IN_USE)):
                    if HolidayUtil.__NAMES_IN_USE[i] == holiday.getName():
                        name_index = i
                        break
                if name_index > -1:
                    old = day + chr(name_index + HolidayUtil.__ZERO) + ("0" if holiday.isWork() else "1") + holiday.getTarget().replace("-", "")
                    HolidayUtil.__DATA_IN_USE = HolidayUtil.__DATA_IN_USE.replace(old, "" if remove else segment)
            data = data[HolidayUtil.__SIZE:]
        if len(append) > 0:
            HolidayUtil.__DATA_IN_USE += append
