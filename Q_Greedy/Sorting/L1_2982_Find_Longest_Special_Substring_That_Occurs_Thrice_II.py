""" https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/
1. group continuous substrings
2. The maximum value of the third largest in each group is the answer.
"""
from header import *

class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(list)
        for k, v in groupby(s):
            v = list(v)
            l = len(v)
            for i in range(3):
                if l-i>0:
                    cnt[k].append(l-i)
        ans = -1
        for k, v in cnt.items():
            v.sort(reverse=True)
            if len(v)>=3:
                ans = max(ans, v[2])
        return ans
    
# group + categorization
class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(list)
        for k, v in groupby(s):
            v = list(v)
            cnt[k].append(len(v))
        ans = -1
        for k, v in cnt.items():
            v.sort(reverse=True)
            if len(v)>=3:
                if v[0]==v[1] and v[1]!=v[2]:
                    ans = max(ans, v[0]-1)
                else:
                    ans = max(ans, v[2], v[0]-2)
            elif len(v)==2:
                if v[0]==v[1]:
                    if v[0]>1:
                        ans = max(ans, v[0]-1)
                else:
                    ans = max(ans, v[0]-2, v[1])
            elif len(v)==1 and v[0]>2:
                ans = max(ans, v[0]-2)
        return ans
                
        
# binary search solution will TLE
class Solution:
    def maximumLength(self, s: str) -> int:
        def fn(l):
            # return True if there not exist a substring that occurs thrice
            for c in range(26):
                cnt = 0
                t = chr(c+97)*l
                if t not in s: # pruning
                    continue
                t = list(chr(c+97)*l)
                sw = list(s[:l-1])
                for i in range(l-1, len(s)):
                    sw.append(s[i])
                    if sw==t:
                        cnt += 1
                        if cnt==3:
                            return False
                    sw.pop(0)
            return True
        
        l, r = 1, len(s)
        while l<r:
            m = (l+r)//2
            x = fn(m)
            if x:
                r = m
            else:
                l = m+1
        return l-1 if l-1!=0 else -1
        
"""
"aaaa"
"abcdef"
"abcaba"
"qqq"
"bbc"
"aada"
"jicja"
"ozozpixpvbmzqzjdbfhausmbbzmqelltrxngtcrhtxniedmgmxuvnjmcbekrhaoezqvmhdamjjbaiogmrejmpcrystgdrttkfucecgkuhwftckqfvrhmfboiijlhvuwytuzluglnhggvxoebgsypadqenvbqesvhnggktohfqkpltybgglusjywfisegyrwcwonanamtumapmpzantsdympbgmhwmhndvbszlecvhrauchawfsqpfzvhxykbwrldbbmyhtwmbewtaqjbwahsokprldlzhcioblkzmhbqetzwsjswbngufqkfwtqprwgrnnvydwwrdronbldltxctznodcssyvlhgixeibbbbdbriykhymdzrhsdhhifedlnupqeszsxrbifgmxlccksmuefwdegstabuduulaeqsiqwsifevvejhgimizqpjgssyyexswktohevfjpszqpovtcyomzpcpswxrglwfpskqvgxwozobgqsrddvxaaumzbpoqbsaoyahjtpbqzdkjusnhtozyksfuhtvzqglytmathobzaekpnajxpelebuaxqyacqmgcuuagjhcqmooforfwswgwugvzwyvhlrjswdwxofhsynnhltpauobdcdcoqzogwbojlwtccedglquduioxqitajtjoangujlgntsawolirhnziimxrtiiuylnyvrztubicyssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssspppppppppppppppppppppppppppppppppppppppppppppppilqabkhyuwreumkuikinvbidfisvbeshawaaecvkcaqcvfynuivbhrxselfunakhszpxukphooapjanujumldfvkiwwdgkuhzjmjjcdcvkqzvtvvgdgexlnzlsicjcztxfbqwxjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjlwqvlhefecwgxuecowlirbaxscflmabhabnzyzfhqbkoctckjswtqlbbtumqtwkalecfvquxqgjyzdqlcjtygxcvrxlxsjcahbaywuivzkswyasyytdvubjlbytpgivpqactwvkxelpyayycsxpbmdsrbxjarlftlqqulugihgxgcgypewmebjmwczygaxjgxdbxbziiutxhwqprxovauxoqjbxxxmnghgrkmbicblajbeypzfrpwynpmawzwkboroybilsbvtnygousskzrlgiczoqarvfrxawuxouwtsldkrylvudsfuxrzcxbwfwpzqefdppwzhkwsudflbsgkuqosdcyrlggkrgyuskknslshiuznonlezndzkkadftkzvqswbcvnauzmvikrplnezovhaqqtxytrchxezwxsizrpfdknljxuofwrbpjefhredftyrubpgaasirhmcjyhthobjvtjqrmkxzasulbidmtmfoctotdhngxflzbrglbzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznxatppsmiyvwonuyolrspctghyywskvjnlgfahgtjgzznnpknbnrqpxwlnklvbcicdqbguctkqbrtyeqebhpnvpsnlnoaspdridvcqlvnepagkofawbobsnptiztbrhioebjagsltdadvpkljfzvjzdyynsuppyridtolpnosgwzeohjbiczwonysikfbrauugwkkydkscarzsjmbayiofqahjtklxunudompowznbgldrfsqqxafycteulyqzcnupfbslacwlmhgyirjootfpijuztkedbrfzhzeoauuuorhlbguyasoksjzvypbfsifgeyuiyykkntqwbqkasmklnomqcdkbrrkwhyydcpdjskihjgzankmamoxdozrulzsoazpkrtnjdbzshxmsmpfyjpbcsyksbqekyaaqduhxsflwrbsajhhfjhgfkgjuajquvsmohjwtsojsstptbhjsgaebutuoodyysdapuklabtnslspvnukpondsctpcstcdbtevohmcpegxabgzetfnptkfqfujdmjdzyojduzaqwwsiswngnebvlabapulxahlxkyndhdacjmaaslhnrcjbbzkmirwzzmxqgopamqretwmnfxmfbpldqnzemqhqvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvuzhqtsbuitetswhozvyhfxpbyyihtuhjqdzvxeqbgkatmohweqrfdmmjfghswkqmzcdhqladzgfcsxuwgrsuujwdqjtcijagyjqoagcrrjuykwmyayhtnsuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuwjrpdggutwlismtirxubvlhgemorqmottruutwncfgthkkdxwixdoojkjjryuyalfehkddfgnqyvlcylynoqxizqjwnqucarcqcodnfcikxecqurwxxxmksqhwakzxosfbzhkbvzywtohttepomtdwuloqoytoybnmkboibwdiwyrjdjmynqaymtnddtvanilrscyfiqobohzvpmjnakqxbnhrcxtvlsfzylogrnybhxpqmrjmblejpmzctffquwhuvtlfshhdgaqzrijcqhqocttuayobfglzrmeqtzbnfhcvurnbwweedwmepukfgabrqrklvpngmnnlkgikwfigywrtulovumaiadwkprotfnwblxculwprcitgvsqakmvezlvsohdnmerknraofsmioorzrtghxifozpzfmgxldfsunxeyqvikevoomwqioxqitqcpnsegbdqvgivsscoriootbuhsqcylgkeqmrznuxkbslyewsrwskjytjkxwjdmjkfpngxrpxfzebfuirwltyccjeunvwihzgmgptxplkhrpevduhpxrvixxqgpdnwghbqnukffvcodinmsvxokcgnenfgpcujnkjusuxdnubxzekygkuguwrjocatyevayqpwdkitnlkeijbwvjqvrhktiwvspmbwgvbdzzdavpmqbwvimpxcsmokfrxsxfnmzjvnmzyykbnkfhhpimwqngormhpqftjgvrjrtitxlgysbtlqtlgtwtnigqjtnttcvzwdclcwrratvtkyoqyyjcjzcyizbdbjcmclujyopyiisghsccxxaqaqdnbzjlcygvvutgvfyhrpnfkumjemgikkehrlzfvsqkkdiukpnipaozcklsrerlfifzyjtxzrdicpolgwarlxmiwyjdhrjlblhmckappivmpebvjjbfvwmabrbkhzzymjlekscwwqtbdykslrstpgglzjxktdqjmrecovkwsfzrrjjknktxctpbgeyocsrjqfbucaeysqigatkuwwovgxagroznhutakaypihrnibgukqcoyvmkdptoczjnqsgrvimypcewrzgybqpfdijekghtowsycnunyakenzsjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjmkdrqtvvpnwnvmehhfdgjbdvwidxgtncegpmaoybdqefyuipgkpomwwqqmksznwebunwdjnrewpnasviejfxxghouiyoeipktkgsbzposphtpapztcmkrnkltaerzttvkjgazzlrhtgifmrkemddbxnyuatiqsydecyqjbkfxxzsyyxhhysiyangfiusyqwulikiqtpslfkjygyzhanuazywpcojavmsjkrinzytdylwbtuodkxolsqrphazkptvkdtefyxeqchzdadkcwfzdhlluvxzggxzwhktsjsvefjrzwkarefpmwtumufdiiprwezdmhyzpqytesnztujulireqfsuczliywlkaemsrkvupldnczbhlwgyainfguvuxbesqwmmapmzseetcsmofymcvkkfxactemtospxfcfeyyfuldmpbiudgaezasjghwbibebylavpmnzcckkevbhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhltbtyqmrzcdcldvuycccdqlkbnikadfuqonqxfmxjubkbysqojpbeiommxhdebdvcotppblvwritguqkbwodchqlsaxktlvwfejjwsqcxmjcejobjnrtuxtskzmfvpmqccjrfqrkzblbkdnupcuapyymkfpqlywiwyhffvztgehxmnrevxgkbqstrgleloisotvhgznfixoktawaqapipvfyjenpgbmjxzikpbsuqohuqbpmvpryctptakpaeouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuydomxnojdxycqcdjdiovcdgdystlnlxlolwfvdtcjiymlvijmqkycmgsxrejflxmazswxiwynygafrpzqkipjcnaqiivtsrqanzlpzqsqfmrwquxuvkuwwhtsnpndjeomylgjypbpvqdkzigowusjepahitjapiyslshacnmdnxvmpiwwhlddccccccccccccccccccccccccccccccccccccccccccccccccccccccccgjdhhkzmnvqekaxfkoyeuiqudykuukwwxbmncamihguiokzqhtwoijknruyntnoxbtzgcoovdwkztvxrlqxequkmigibvuvbrygzhbypbottyonkqfhoeerpgcaqznuywrshgunfmwxljizscxephokobkdgkyqjdjusekntcwfwosbsegtemzxqaojjrcujrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrnezgfnoekdboynaaccixgaccrexzpqfszgflfzcwijiwwnjmlsydocccccitsemaqvhdtvyvdqkkzuxqavdvzwduhttmxdmqadtgrvlwukitnolprffssprtfzopmrudoqnresjfmclbxrkonmkttssxgnzsnsaaruyeauhpehxbyiulhvltugeqyfmblrhrctghzzsvvqbqowqiwyjjevyqiyrhqjsjyznuzxlwdrjrlcddgkdurnwvpkvoleonhgpcuskaozxkqgeklwzaiwasmofpuiyifahydybcmzlbjelksfkpjefzxqihoqbssqaiullgimxqznhbppqblnzwmqwiohqsyjafnxsgbsbisnwtjdrcgwxjbuzhgbjmxskzapzjvetwjzkpjgknnxvsdoqbvqxehwxaiwychuwukoxusoghbfhqixojltywuexklpoijztpfdpoxqgebkkuypyihchsaxtnhupjtrrttneeesaqyoqtzlxywxmlkuoymjdrifimqlmgeayjejcrnyepymystyvhyajbnmyceklgccdnyeyfimydxygzpbvbkfgbgybnjerkdzxnicjbxaywtndsznjvdplxrkrrbldfanbvfihhhnjkvhhnujrvzrhymwpowtubemdpblwnjxnknuqevuzdqpetikcsbhiuocjpwubzgmocovziuuubmbvtbvbzduhbsxfvhhuhzpjebjleuknxygpalaseilluhkubwusoeldprdtxgnqlfykemzpzzbwbkaineufachkipyedgpmnmodttqldqjawdziplmjlmrphhdqfyvgimddoawzunsnxqqeidsurvqofzckehmvuidsxpxdabguctpsctmiarlwycprojxzwnzavnznpioywoyrfikryxgjsedjomjfkrtrmmgvxlrhdhkwvveduqbcaxttjwutlixjtzavccewiubravihcclsfqcziusebndenfcbdwckmyauosgvxulkftasnstmzssfqgagjjqeafxnzixgicbuvowiewzjzezatnqjusergjpslkmmolcjaqpehywwgwkmeumaydysvcsuazmgtnlsxzhnkyamkumfykpjzbzzavzafaddxljmuhjydxnpjoaskddxgvrzrsfawmbpsasvzlkitoolnwmsnxbgqfcibemxgztmgyzrogprtkwyfbszmjwgihifjzkardicrpkeagxbepalydwabnxsczjaikcbqsblqeznfvtfakaiogfquefgftrzbyvummvxtsotohxfggjivgnxanhqvcbkmjkemtmahaiefdxnynwuqpghxxprjqflrsugumzsfurvnwxkvedamudkuhmmunwvfayliouqwvjvkbniqrqfydfjlsyndfrmyfffflpwwrasfcfksmqawxrkboecfnlsujaqmdicwoutxvhzshazjfkjgbrxoznqstpahzcccwgogftntiyeaivrbilqgkzihdikolokjycxmnjttnawbvwlyomopborozzxabbjpgwpivawsxkjuyomthhwlrhyyrngjxrdwoullaqxrhcbsulpzhnwtwktzwvpjyyvahazuponxuidlslgdyxzsnggtijqdxjxlyeplmpaoxnuxzpvrnidwbtxxglnhtpdfcqcmyeqkpbwfmxvuonzstvnabtnlqsxvfimdejdehefjnyycbewyjsbkyxjliduxggjkmweuwxmmvoizknxgouyiwqgymrujexmtjgjdovkxjplpfhjwzpytgxvexeujmdusuyamjwlghdxuhbudpqiuagemzgtynmedxmrxeelgweonhfmzatadjwdrceptcuhtvkykpniphxzxiwqwrlrwywhyfhgxnjarhybkvtmgwhsulksjnhvyvtnzctlmdsvstxtsjojhjnmdmiargfdsvgijckjhwjxxkbschzdpcoctfmtozxvwuofksnbazurkgdascvrfwyefhrhpxqxmyouykmvbmbehmotjudlzwtfsyfjsuyadmslvpzrcbxuptgbyisywgrpfxynpewuleyekvyseutdijdssoprnaxvucmhrivjfmbvsaqanklwbyarghcaxlynpvokrbrivqgtiyambgzzjpjkswvijfcfqehwzkyvpziigblusjkaxbrrgnahtrecvlkzexiwqgwyjcxxwukexehyivmcmczqarranoumqjyywtbswzvssbkhntbltsxhtamdpzoyhprztrlkmsiagtgvjjbsuctbzarixrjveyknrmincbkfcauwdfmvablbtgpdossvovebpxnugjunatosjepyorccsmqtjiwuuynsiqateviqbwszptpjmttswtaukucxpxhnaohrxvlxtjhzwhuwpajcjikffyttpneavyufdtxrhdshterpjgkfhwueymjogqwuaaoofickaotgaemsytheqxgmdqlwanlasdcgrslzwjlldzyetfgjizyppihezyzjuyxukqhhuchlwtzurlcqnwjsnjcunadkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtcmzoelawwwuxxrhajqcsvdxephadmzvqghmjfghywqagkpmwfghmfsiwnmxosnvvpeaxlyzblqmtiokncesjnbfnoipzqvohvuaxjgrxchfxiwzsouapjvdsfmtqzzkscrdmppfzcqtdcuxzzmgcbexkzcyrzzbivefdiwnvwdzrloeqmwophzbnakrrgcbcvnixmgwxypcgigitpepztdfltcjjfvtvxxmhstwpookfegxyjzixlszawbyiyetnbuojkhbfhqhsyepslcfdjzarlctkzuaxneqcnhnaxecygfsdbjoarzutvgzzulbqripguuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnemljidojfntvnlgmbadowwrwrglmjapfqlbvgpgaodkoogexgjppxkegvxmurnxuaasmlzmgmlhjcdtsyksiqbczomjuezxntmvyubxkrutfqseghwjbgjbndbjrkkedcfjjykxqitbekwwikzmbrlvgbdjsikfhafsponykyvsjzbepdgtwknbzalduyydquzzrymqrnhjfgkcjtuwrszsefzpfruwnibycxmeikpbufzuselizghevodllxvkikvfplocccqgzhxqffbthpgaexffrujcswygaongaisygsjfyweqjluozxjxpnfzqrxmjnncdcihxgmrxrpqioyskuthynyhndoroctxxncwalaiolzrliqtddddddddddddddddddddddddddddddddddddddddddddddddddddddddddxocnoftxvoxjtodoujcderxspsitewxukagrwududhfbcycubuefhopoxmjfhdfqbxapxjgtwunweeqyuxosnfkdfjieismbvoqjwezvblstewownlgnaglofsihbqwntcopnzhdmipggoaztvlytgbegtlpfuwzmpuqbyswtwhbsilvermnflcnyztjezivwwnjcejcbaaslpqpwytdneonikzqulnpxyqqczgdzgjprxtzdkolubozzorvjfyuapelgjlrslbsdxfhvcyqjjmyxrpfzhgtiubowkubcbxcbaesplgrzdgwvsmmxjnkfeyyydjvtsjblvhdbpagqugokitwnwcwpirjyaybonevzquaehotfvkbepgyjgghbpirefsuqoulrzlfyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyaxlywglbbphfoodyjzspoqnshmdzxmwlzukzfjsqbainfjtfdbjcfmwozzvxzmvktaplaqmogvfohowmiyjwtrrdlszfezqlczdiqnabjkwraponqdbdufnvalvdidpspjyqdazbkrzbiljlrxsqvcsekkkkkkkkkkkkkkkkkkkkzjobsabxdjsieftygkswzrupczjxvpwkmpxeaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiihqjhxefkwsrkhmarunpwvvnvzwgmbvlsjtjnvmlvnecwopbbdg"
"jinhhhtttttttefffffjjjjjjjjjfffffjjjjjjjjjqvvvvvvg"
"""