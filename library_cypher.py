import random
import library

symvs_min = {
    "(0(0)0))": "!",
    "(0(02": ".",
    "(0(03": ",",
    "(0(04": ":",
    "(0(05": ";",
    "(0(06": "'",
    "(0(07": '"',
    "(0(08": '?',
    "(0(09": '<',
    "(0()0))0": '>',
    "(0()0)))0))": '/',
    "(0()0))2": '-',
    "(0()0))3": '+',
    "(0()0))4": '=',
    "(0()0))5": '*',
    "(0()0))6": '^',
    "(0()0))9": '&',
    "(0(20": '&',
    "(0(2)0))": '@',
    "(0(22": '#',
    "(0(23": '№',
    "(0(24": '%',
    "(0(25": '$',
    "(0(26": '[',
    "(0(27": ']',
    "(0(28": '{',
    "(0(29": '}',
    "(0(30": '»',
    "(0(3)0))": '«',
    "(0(32": '—',
    "(0(33": '…',
    "(0(34": '_',
    "(0(35": '\n',
    "(0)0))0": "а",
    "(0)0)))0))": "А",
    "(020": "б",
    "(02)0))": "Б",
    "(030": "в",
    "(03)0))": "В",
    "(040": "г",
    "(05)0))": "Г",
    "(060": "д",
    "(06)0))": "Д",
    "(070": "е",
    "(07)0))": "Е",
    "(090": "ё",
    "(09)0))": "Ё",
    "()0))00": "ж",
    "()0))0)0))": "Ж",
    "()0)))0))0": "з",
    "()0)))0)))0))": "З",
    "()0))20": "и",
    "()0))2)0))": "И",
    "()0))30": "й",
    "()0))3)0))": "Й",
    "()0))40": "к",
    "()0))4)0))": "К",
    "()0))50": "л",
    "()0))5)0))": "Л",
    "()0))60": "м",
    "()0))6)0))": "М",
    "()0))70": "н",
    "()0))7)0))": "Н",
    "()0))80": "о",
    "()0))8)0))": "О",
    "()0))90": "п",
    "()0))9)0))": "П",
    "(200": "р",
    "(20)0))": "Р",
    "(2)0))0": "с",
    "(2)0)))0))": "С",
    "(220": "т",
    "(22)0))": "Т",
    "(230": "у",
    "(23)0))": "У",
    "(240": "ф",
    "(24)0))": "Ф",
    "(250": "х",
    "(25)0))": "Х",
    "(260": "ц",
    "(26)0))": "Ц",
    "(270": "ч",
    "(27)0))": "Ч",
    "(280": "ш",
    "(28)0))": "Ш",
    "(290": "щ",
    "(29)0))": "Щ",
    "(300": "ъ",
    "(3)0))0": "ы",
    "(3)0)))0))": "Ы",
    "(320": "ь",
    "(33)0))": "э",
    "(330": "Э",
    "(340": "ю",
    "(34)0))": "Ю",
    "(350": "я",
    "(35)0))": "Я"
}


class cypher_minimum:

    def __init__(self):
        self.syms = {
            'oBlyCaTSaZDXBYUdNNjEzHSMZPzancphDjsOcCQSCSFSeGDFNOxfqG': '!',
            'oEbQfwuhMcVxbUxlyqXemozOjdKykTdEvfggmToKZDbvS': '.',
            'usPqziYepEzgoLJlKuBdhRhnwZfKacUBQDuKTANwuE': ',',
            'knVoesHVscDDTLtUXuvIIAsXgbjziducaKnTuHiiYmfba': ':',
            'yzHIUdQOqPYFQeNzvmquRLeIUPbkJFwMAWO': ';',
            'MTKUOkofkzEYCcBXTqUiEyYyljdakzxCdBG': "'",
            'BaZegcDDzUYvIWeoJJGzFEXmyFPkaHbMpJgCG': '"',
            'ROLfTeLcxdQxTDZhcEApfXiYPoeBlWekvmxoGAH': '?',
            'DtSSNgJscQzzOGkCfvCUtatPISOedLFBzCjUmYIeSXmYpJYTryIGRuVjOS': '<',
            'mITCSfPYIbhGNcKuPJrJWDhKoFYXDTKfAoirjrBgJ': '>',
            'UtsUOpYITszppQUjKZLVcHJCDSxzjGZkXTkSIohVKYAdIeiMZzaqD': '/',
            'xzbBtzkzEzYkiaBMJdhtgcYCgdNpDmXUUGTscRdrdhINpJhWWNYY': '-',
            'KEakhXxltfrRWRVAFXYUoZbWpuXofWDijjdaGClMeHBeCOejjdQduPaHoh': '+',
            'kXhOnahnuDwoEzMUMEfOPodiprMPrNMYAYvJADfgvZYmZBFobzdBoujbHwq': '=',
            'UHFlKmnPzZiyyYjqfiGaOevIQLcOipCoRgDtyTqHPSokbqLWAElUjcqJgK': '*',
            'MxixLmNtszEaOuIMRnPRPvWHcuqVBodKdtzwZnlkoTwADuyttt': '^',
            'PqoKARAvVuDUVdrpMxgFydIkioqszpcWsejRY': '&',
            'gMvSTGYYcZQTTJQXjjINUMjeqzYCZknNdmYggdfQlXWZYBxOctzToaKo': '@',
            'PPLMJQLIasUNABLxwkTONtqzgSrqrnRCnhviixXAzOCKFV': '#',
            'xQRycqkDdOXRWlqCBmkrDYzqjPcHXUTGuyhMqjZJeCZWbUYxgwetnGpO': '№',
            'ScyRSGIDDvAOLIVbquzPpAmdXBKbCxqFksxyOExxVME': '%',
            'nrzeoIIWrPtZSicFlcudzAHFCEklRdrWAsJovyoKBLmjTrhjTZU': '$',
            'EYJUmoDFPXUEIFpTbzalkaBszPadYQeLjkXdTrHjpBRjy': '[',
            'NjTkWslBLXbPrXOKMPYRJNQmkbGNapZbGkAadXURPimiEqZSWmEhGkbXf': ']',
            'eYCENJkuUFAhVHpNgqtgCWmnEGRtdtKFosAqbxTxlmQiFBWNaTQpYpa': '{',
            'SVJVeksporsudrCsDJCePotAmvGoKVZOiAWiNFrDzobiVtYiaEjHDAcZQdX': '}',
            'kgVRGouRZciXWpdBIIANkntDRGMHoxHbWbReHgA': '»',
            'mamRRKFwlmPrgSdFJpbVIyCbqSXGoNohbdPJRQLIgMsmtI': '«',
            'vcrNhOQskIJjjRbBwqahkzzvNjfIgVqJHPOE': '—',
            'bEDbaEwusssLvQoZpSAcTUFkPYNaKsUSsNJivsUvBdDAkQwMwCPTuCwOA': '…',
            'GTdNgMqaSFkrdrRalnniclqYdHGpATyiKIFhfMHzQAfEhijwxVIqXII': '_',
            'uOuMPEMkWRhGYCVeGoujaIRDBgxzmjGKymPcdsahbEtrkfRgqKvC': '\n',
            'bgajAGUbJWtzKojsKHiVRlVTzuvZgWFedBgrfY': 'а',
            'RxAHWljKXFyTRYnblIuverYAwdUZyTjcKoEvNKHbRTRNDIaTertiVuWLFhy': 'А',
            'jlRrqgOJHNIuFSYfDLerYSXlVTooCfiAlYwJEbYsZmGxtNO': 'б',
            'CdJIjSZaDbAyEbKuuSBwEXuqqxzdcUnXWivurCTFWMhklTMpF': 'Б',
            'eqQTcNfrgEUKHZyXKtGjysypSJXegyUcbmISGOpugEWgSZqYHGuzrdOneO': 'в',
            'cGjwTmGfVhVLfJDIgiyKSCSmCqvqnCwMeKNiVgNADKNCSCYtLNrPAneysjC': 'В',
            'tVwFgKqYzuKglKjOTXRiQDhlYjeZapOQYugFYslD': 'г',
            'lKaOIJuynbFXzOMsXHjJNanDlShJbmYZFCPXsr': 'Г',
            'RbHnyYoBlfbCksYBSruttvtFravumZXqVeVPGcJnqQSscxWiBfXLQuyEzUf': 'д',
            'piSiWvOeYeaCDAJXTMGoDEZzGdkYEKghLWpsugVyTULpSfelISNib': 'Д',
            'oQCInoBaDdCXbWVdhkQsRSIIZmkPZBFuruhMuSDfZhQX': 'е',
            'pajOVPIeDmpINPCuHkUBttsrfgvejWkVGxScsJbFROwaiACor': 'Е',
            'GJPeSePPpMsZsZIjinGLDXrKdebLdEfgthYbQErU': 'ё',
            'WsKWltOLxtTZWxEXTERyMTXJZXuzaTsyMrrKRyTnd': 'Ё',
            'tPHrElcydDFiyYiooLhvXlwcJQYbxooUckTzipJJyhHpEgwphskqwlHmEZ': 'ж',
            'WFtsFcyQGxRRFdLpdfqjPNNWkPEREHrTqVpwDXLQPAkEBaNtpHtXXd': 'Ж',
            'PKeqLPeNAReRbzaDVjHLCojuaPqSLMQhAxjb': 'з',
            'xOFCJdccYcAJOGOxJVNTumLeIiyTeuedtdvHkxu': 'З',
            'VaalbCKcjuRKNIOdlnLcadrTuwsFzOTVtbkQnbuKQdzaoteODMNPEq': 'и',
            'cIdBDrNhRGlddHduwVJJupCPDTZLgkhzqtDcwsr': 'И',
            'WZHKquKYbOmPNQNnBtjnPcUUKFOgRoDSajsEsngpIr': 'й',
            'KwpsOXQkdWdYPhOpXuGyMBsctMeMoYnBUjfxBDTduJgjFIFZlOVVXX': 'Й',
            'HsfolGQNtdOBQrPUaklUDaFFzVLsQVynkyCOmkCrZ': 'к',
            'aIqTAHfMnsIZANulcuZWIMDjrQfWQXaMiVHMdNfBunzBPpWIApOzuTf': 'К',
            'QZTkssTmZZhXRtcuVliOuqxFhgfggRzoWitaSSeNvaeGq': 'л',
            'YtGwTzfqJihXMvQtShGidxrQAsVizmCoycpOXPWsnYVDMQzMgmmdhMZMB': 'Л',
            'exMetvMNZjpWcEUHwCzNtFPWOvSoDRqryyiUcxheYguwGJWXJuXGHiWY': 'м',
            'sbiBHruZRluoOinfSupfyhwBkHeYwgvtKGzWGqKlxsyFubMLxTc': 'М',
            'CuqFgtCOTgMYlutmmPagTttWGurHpHuYFfWzMxLTwKRYRWVcxPpyVY': 'н',
            'dNtqOYHhOyGnAWIGbhLREbnYuGQDnfrOxQE': 'Н',
            'JXGvKAIjBOvRfmrNgNuQOKqEFhyQBIfzWHtXXZujbxdOJUFuPmbOM': 'о',
            'TycTSNEetABKvYAYTHWyfXTVbykEMrMlKuKLbfNOpdHHFqbwHR': 'О',
            'OTuhwjrsviaxcOAWzaaXzPMdfcEpcCURGFADHCLtnFwSTNWoiLvmoP': 'п',
            'AtOYJWJGKFpZHIEuDWmxBEggDEVJKOcMVeYeDOhTsd': 'П',
            'tHCzodIeopsYMwjAhTtTIQknbeiSyceyyWcTZgfK': 'р',
            'CekuSEdBJIFvHIQWOnCtTDgxRpyJUeCYvkcXmmBIi': 'Р',
            'YBmAEzvEEcXOuHYhQnglsNxWDMnqEPSNKqgHEyjuUjHODXSuNln': 'с',
            'zIJKMJrHWrMsPKGsKOaZKbZupKzVGxdXLaLkhaYsELurODPLlUWancisB': 'С',
            'vdgmWwEtXqZqxLSlWZOPjmXTLCQXEciBYWx': 'т',
            'IbfPZFmyxXVGhybKHUhZZFedfaxwbHMKPTwK': 'Т',
            'etBHPCxAjAeCvkcCyIBHWeERdiOkueCUDtyquYvqMkSQyOJvAcAkWXzyA': 'у',
            'kdduAjmnEyxJyWIRhliKtThKSSGXTjyavIg': 'У',
            'McTiCjPOTzdtEgbisCDkkGVKTSvsxKUlRYubDZtuDdjTUtnTHp': 'ф',
            'irEoLtFNAObCfvQxsfdIwuwtAHsvRXQLLHbqqrtRDzt': 'Ф',
            'PncfpzCTlhFWSbPzmOuSSGZFeMqIxwSCihfvjSkSPhsr': 'х',
            'NlsOLHojTKqBwrDlRGDWHadddDRquSScPSPyOsQzCMQvttDjiegnCx': 'Х',
            'quxIKhIxBNYzuuqpLfAuBokBjKhMBNKbNGEIckfddVuoYLvgbFKn': 'ц',
            'ErPeLTPGjUZJxQmZXtoNTvEgrGgBCcbfjsRGro': 'Ц',
            'qFjPJETXUVWnnPXIOtaWOnblFHwFaWicKctdpPsRczeiuGFZoghUDhjCYgr': 'ч',
            'JqJFJKQcqDueXCsRVNgqUBlAAMUmdLKenkGgEjlJqBsXv': 'Ч',
            'FKfblxeJZnezHewxFTriiVywFziATNzEPKWvpGPP': 'ш',
            'rGuQSjlXpVfoAmpwctGRExYomzGeJyAUOKxTJjyvijFVTNnPC': 'Ш',
            'fmdLBzKiFvFlVhFftueIIIjsjshYVWAHkQYRFyCktFSgoohh': 'щ',
            'EWuzxWOXYixJXZfEfESrgubEQJcIWpUdKjCuEvVGmytnqZzjvUOvXGnrDBx': 'Щ',
            'wbbyZMsyPWXguIuthOhOrnnIsntHaOwguLcgZQhmmGRKOJjbsmJBBqRT': 'ъ',
            'BOgyioOihXwtBpreiWcLeEfStwEtOBwAeLug': 'ы',
            'YYKpWQpDvpUUNiOixDJQQNELHBRshxoWFSOJLghA': 'Ы',
            'kGFNbPuBbfUWXCXYQkbsRZUsGNEcVxEkQXtCsYfsfEjjx': 'ь',
            'cOuCYtgdmSDXWRbNNHGepRHNsjZDEzQiAHlyMWq': 'э',
            'jBaoCdwvemtyPCEOpZKENgSRmqCyzqbrBIgfflnTePAXfqpKPoHWaMp': 'Э',
            'UwTiqhOydosUHAfFqcwheRNxakkuwoPTGTXMvHgvm': 'ю',
            'aDeZBdjfgzgogJJOtqmPDdCYMUAzQpunpQepeYIXu': 'Ю',
            'TeTQCLgZCptyRrxcNDsWrSfbZsMIBbzVZZUjfRGxRh': 'я',
            'qAImKnBSfycqBalmyTTSzFUyCXBdbiBmOhTCxHLSLfLNZeXuYeck': 'Я'
        }

    def incph(text: str, bll: bool):
        for i in symvs_min.keys():
            if not bll:
                if symvs_min.get(i) == "\n":
                    continue
            text = text.replace(symvs_min.get(i), i)
        return text

    def outcph(text: str):
        for i in symvs_min.keys():
            text = text.replace(i, symvs_min.get(i))
        return text

    def incphkrypto(text: str, bll: bool, krpt: bool):
        massletters, krypto = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'), ""
        for p in range(0, 15):
            krypto += massletters[random.randint(0, len(massletters) - 1)]
        dictp, kryptolist, smv, smv2 = {}, list(krypto)[::-1], list(symvs_min), list(symvs_min.values())[::-1]
        for u, i in enumerate(smv2):
            x, mass = 0, list(smv[u])[::-1]
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 2
            dictp.update({f"{smv[u]}{krypto}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs_min.get(i) == "\n"):
                continue
            text = text.replace(dictp.get(i), i)
        if krpt:
            return krypto, text
        return text

    def outcphkrypto(text: str, bll: bool, krpt):
        dictp, kryptolist, smv, smv2 = {}, list(krpt)[::-1], list(symvs_min), list(symvs_min.values())[::-1]
        for u, i in enumerate(smv2):
            mass, x = list(smv[u])[::-1], 0
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 2
            dictp.update({f"{smv[u]}{krpt}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs_min.get(i) == "\n"):
                continue
            text = text.replace(i, dictp.get(i))
        return text


symvs = {
    'oBlyCaTSaZDXBYUdNNjEzHSMZPzancphDjsOcCQSCSFSeGDFNOxfqG': '!',
    'oEbQfwuhMcVxbUxlyqXemozOjdKykTdEvfggmToKZDbvS': '.',
    'usPqziYepEzgoLJlKuBdhRhnwZfKacUBQDuKTANwuE': ',',
    'knVoesHVscDDTLtUXuvIIAsXgbjziducaKnTuHiiYmfba': ':',
    'yzHIUdQOqPYFQeNzvmquRLeIUPbkJFwMAWO': ';',
    'MTKUOkofkzEYCcBXTqUiEyYyljdakzxCdBG': "'",
    'BaZegcDDzUYvIWeoJJGzFEXmyFPkaHbMpJgCG': '"',
    'ROLfTeLcxdQxTDZhcEApfXiYPoeBlWekvmxoGAH': '?',
    'DtSSNgJscQzzOGkCfvCUtatPISOedLFBzCjUmYIeSXmYpJYTryIGRuVjOS': '<',
    'mITCSfPYIbhGNcKuPJrJWDhKoFYXDTKfAoirjrBgJ': '>',
    'UtsUOpYITszppQUjKZLVcHJCDSxzjGZkXTkSIohVKYAdIeiMZzaqD': '/',
    'xzbBtzkzEzYkiaBMJdhtgcYCgdNpDmXUUGTscRdrdhINpJhWWNYY': '-',
    'KEakhXxltfrRWRVAFXYUoZbWpuXofWDijjdaGClMeHBeCOejjdQduPaHoh': '+',
    'kXhOnahnuDwoEzMUMEfOPodiprMPrNMYAYvJADfgvZYmZBFobzdBoujbHwq': '=',
    'UHFlKmnPzZiyyYjqfiGaOevIQLcOipCoRgDtyTqHPSokbqLWAElUjcqJgK': '*',
    'MxixLmNtszEaOuIMRnPRPvWHcuqVBodKdtzwZnlkoTwADuyttt': '^',
    'PqoKARAvVuDUVdrpMxgFydIkioqszpcWsejRY': '&',
    'gMvSTGYYcZQTTJQXjjINUMjeqzYCZknNdmYggdfQlXWZYBxOctzToaKo': '@',
    'PPLMJQLIasUNABLxwkTONtqzgSrqrnRCnhviixXAzOCKFV': '#',
    'xQRycqkDdOXRWlqCBmkrDYzqjPcHXUTGuyhMqjZJeCZWbUYxgwetnGpO': '№',
    'ScyRSGIDDvAOLIVbquzPpAmdXBKbCxqFksxyOExxVME': '%',
    'nrzeoIIWrPtZSicFlcudzAHFCEklRdrWAsJovyoKBLmjTrhjTZU': '$',
    'EYJUmoDFPXUEIFpTbzalkaBszPadYQeLjkXdTrHjpBRjy': '[',
    'NjTkWslBLXbPrXOKMPYRJNQmkbGNapZbGkAadXURPimiEqZSWmEhGkbXf': ']',
    'eYCENJkuUFAhVHpNgqtgCWmnEGRtdtKFosAqbxTxlmQiFBWNaTQpYpa': '{',
    'SVJVeksporsudrCsDJCePotAmvGoKVZOiAWiNFrDzobiVtYiaEjHDAcZQdX': '}',
    'kgVRGouRZciXWpdBIIANkntDRGMHoxHbWbReHgA': '»',
    'mamRRKFwlmPrgSdFJpbVIyCbqSXGoNohbdPJRQLIgMsmtI': '«',
    'vcrNhOQskIJjjRbBwqahkzzvNjfIgVqJHPOE': '—',
    'bEDbaEwusssLvQoZpSAcTUFkPYNaKsUSsNJivsUvBdDAkQwMwCPTuCwOA': '…',
    'GTdNgMqaSFkrdrRalnniclqYdHGpATyiKIFhfMHzQAfEhijwxVIqXII': '_',
    'uOuMPEMkWRhGYCVeGoujaIRDBgxzmjGKymPcdsahbEtrkfRgqKvC': '\n',
    'bgajAGUbJWtzKojsKHiVRlVTzuvZgWFedBgrfY': 'а',
    'RxAHWljKXFyTRYnblIuverYAwdUZyTjcKoEvNKHbRTRNDIaTertiVuWLFhy': 'А',
    'jlRrqgOJHNIuFSYfDLerYSXlVTooCfiAlYwJEbYsZmGxtNO': 'б',
    'CdJIjSZaDbAyEbKuuSBwEXuqqxzdcUnXWivurCTFWMhklTMpF': 'Б',
    'eqQTcNfrgEUKHZyXKtGjysypSJXegyUcbmISGOpugEWgSZqYHGuzrdOneO': 'в',
    'cGjwTmGfVhVLfJDIgiyKSCSmCqvqnCwMeKNiVgNADKNCSCYtLNrPAneysjC': 'В',
    'tVwFgKqYzuKglKjOTXRiQDhlYjeZapOQYugFYslD': 'г',
    'lKaOIJuynbFXzOMsXHjJNanDlShJbmYZFCPXsr': 'Г',
    'RbHnyYoBlfbCksYBSruttvtFravumZXqVeVPGcJnqQSscxWiBfXLQuyEzUf': 'д',
    'piSiWvOeYeaCDAJXTMGoDEZzGdkYEKghLWpsugVyTULpSfelISNib': 'Д',
    'oQCInoBaDdCXbWVdhkQsRSIIZmkPZBFuruhMuSDfZhQX': 'е',
    'pajOVPIeDmpINPCuHkUBttsrfgvejWkVGxScsJbFROwaiACor': 'Е',
    'GJPeSePPpMsZsZIjinGLDXrKdebLdEfgthYbQErU': 'ё',
    'WsKWltOLxtTZWxEXTERyMTXJZXuzaTsyMrrKRyTnd': 'Ё',
    'tPHrElcydDFiyYiooLhvXlwcJQYbxooUckTzipJJyhHpEgwphskqwlHmEZ': 'ж',
    'WFtsFcyQGxRRFdLpdfqjPNNWkPEREHrTqVpwDXLQPAkEBaNtpHtXXd': 'Ж',
    'PKeqLPeNAReRbzaDVjHLCojuaPqSLMQhAxjb': 'з',
    'xOFCJdccYcAJOGOxJVNTumLeIiyTeuedtdvHkxu': 'З',
    'VaalbCKcjuRKNIOdlnLcadrTuwsFzOTVtbkQnbuKQdzaoteODMNPEq': 'и',
    'cIdBDrNhRGlddHduwVJJupCPDTZLgkhzqtDcwsr': 'И',
    'WZHKquKYbOmPNQNnBtjnPcUUKFOgRoDSajsEsngpIr': 'й',
    'KwpsOXQkdWdYPhOpXuGyMBsctMeMoYnBUjfxBDTduJgjFIFZlOVVXX': 'Й',
    'HsfolGQNtdOBQrPUaklUDaFFzVLsQVynkyCOmkCrZ': 'к',
    'aIqTAHfMnsIZANulcuZWIMDjrQfWQXaMiVHMdNfBunzBPpWIApOzuTf': 'К',
    'QZTkssTmZZhXRtcuVliOuqxFhgfggRzoWitaSSeNvaeGq': 'л',
    'YtGwTzfqJihXMvQtShGidxrQAsVizmCoycpOXPWsnYVDMQzMgmmdhMZMB': 'Л',
    'exMetvMNZjpWcEUHwCzNtFPWOvSoDRqryyiUcxheYguwGJWXJuXGHiWY': 'м',
    'sbiBHruZRluoOinfSupfyhwBkHeYwgvtKGzWGqKlxsyFubMLxTc': 'М',
    'CuqFgtCOTgMYlutmmPagTttWGurHpHuYFfWzMxLTwKRYRWVcxPpyVY': 'н',
    'dNtqOYHhOyGnAWIGbhLREbnYuGQDnfrOxQE': 'Н',
    'JXGvKAIjBOvRfmrNgNuQOKqEFhyQBIfzWHtXXZujbxdOJUFuPmbOM': 'о',
    'TycTSNEetABKvYAYTHWyfXTVbykEMrMlKuKLbfNOpdHHFqbwHR': 'О',
    'OTuhwjrsviaxcOAWzaaXzPMdfcEpcCURGFADHCLtnFwSTNWoiLvmoP': 'п',
    'AtOYJWJGKFpZHIEuDWmxBEggDEVJKOcMVeYeDOhTsd': 'П',
    'tHCzodIeopsYMwjAhTtTIQknbeiSyceyyWcTZgfK': 'р',
    'CekuSEdBJIFvHIQWOnCtTDgxRpyJUeCYvkcXmmBIi': 'Р',
    'YBmAEzvEEcXOuHYhQnglsNxWDMnqEPSNKqgHEyjuUjHODXSuNln': 'с',
    'zIJKMJrHWrMsPKGsKOaZKbZupKzVGxdXLaLkhaYsELurODPLlUWancisB': 'С',
    'vdgmWwEtXqZqxLSlWZOPjmXTLCQXEciBYWx': 'т',
    'IbfPZFmyxXVGhybKHUhZZFedfaxwbHMKPTwK': 'Т',
    'etBHPCxAjAeCvkcCyIBHWeERdiOkueCUDtyquYvqMkSQyOJvAcAkWXzyA': 'у',
    'kdduAjmnEyxJyWIRhliKtThKSSGXTjyavIg': 'У',
    'McTiCjPOTzdtEgbisCDkkGVKTSvsxKUlRYubDZtuDdjTUtnTHp': 'ф',
    'irEoLtFNAObCfvQxsfdIwuwtAHsvRXQLLHbqqrtRDzt': 'Ф',
    'PncfpzCTlhFWSbPzmOuSSGZFeMqIxwSCihfvjSkSPhsr': 'х',
    'NlsOLHojTKqBwrDlRGDWHadddDRquSScPSPyOsQzCMQvttDjiegnCx': 'Х',
    'quxIKhIxBNYzuuqpLfAuBokBjKhMBNKbNGEIckfddVuoYLvgbFKn': 'ц',
    'ErPeLTPGjUZJxQmZXtoNTvEgrGgBCcbfjsRGro': 'Ц',
    'qFjPJETXUVWnnPXIOtaWOnblFHwFaWicKctdpPsRczeiuGFZoghUDhjCYgr': 'ч',
    'JqJFJKQcqDueXCsRVNgqUBlAAMUmdLKenkGgEjlJqBsXv': 'Ч',
    'FKfblxeJZnezHewxFTriiVywFziATNzEPKWvpGPP': 'ш',
    'rGuQSjlXpVfoAmpwctGRExYomzGeJyAUOKxTJjyvijFVTNnPC': 'Ш',
    'fmdLBzKiFvFlVhFftueIIIjsjshYVWAHkQYRFyCktFSgoohh': 'щ',
    'EWuzxWOXYixJXZfEfESrgubEQJcIWpUdKjCuEvVGmytnqZzjvUOvXGnrDBx': 'Щ',
    'wbbyZMsyPWXguIuthOhOrnnIsntHaOwguLcgZQhmmGRKOJjbsmJBBqRT': 'ъ',
    'BOgyioOihXwtBpreiWcLeEfStwEtOBwAeLug': 'ы',
    'YYKpWQpDvpUUNiOixDJQQNELHBRshxoWFSOJLghA': 'Ы',
    'kGFNbPuBbfUWXCXYQkbsRZUsGNEcVxEkQXtCsYfsfEjjx': 'ь',
    'cOuCYtgdmSDXWRbNNHGepRHNsjZDEzQiAHlyMWq': 'э',
    'jBaoCdwvemtyPCEOpZKENgSRmqCyzqbrBIgfflnTePAXfqpKPoHWaMp': 'Э',
    'UwTiqhOydosUHAfFqcwheRNxakkuwoPTGTXMvHgvm': 'ю',
    'aDeZBdjfgzgogJJOtqmPDdCYMUAzQpunpQepeYIXu': 'Ю',
    'TeTQCLgZCptyRrxcNDsWrSfbZsMIBbzVZZUjfRGxRh': 'я',
    'qAImKnBSfycqBalmyTTSzFUyCXBdbiBmOhTCxHLSLfLNZeXuYeck': 'Я'
}


class cypher:

    def incph(text: str, bll: bool):
        for i in symvs.keys():
            if not bll:
                if symvs.get(i) == "\n":
                    continue
            text = text.replace(symvs.get(i), i)
        return text

    def outcph(text: str):
        for i in symvs.keys():
            text = text.replace(i, symvs.get(i))
        return text

    def incphkrypto(text: str, bll: bool, krpt: bool):
        massletters, krypto = list('(())9)()(*&&))'), ""
        for p in range(0, 15):
            krypto += massletters[random.randint(0, len(massletters) - 1)]
        dictp, kryptolist, smv, smv2 = {}, list(krypto)[::-1], list(symvs), list(symvs.values())[::-1]
        for u, i in enumerate(smv2):
            x, mass = 0, list(smv[u])[::-1]
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 1
            dictp.update({f"{smv[u]}{krypto}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs.get(i) == "\n"):
                continue
            text = text.replace(dictp.get(i), i)
        if krpt:
            return krypto, text
        return text

    def outcphkrypto(text: str, bll: bool, krpt):
        dictp, kryptolist, smv, smv2 = {}, list(krpt)[::-1], list(symvs), list(symvs.values())[::-1]
        for u, i in enumerate(smv2):
            mass, x = list(smv[u])[::-1], 0
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 1
            dictp.update({f"{smv[u]}{krpt}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs.get(i) == "\n"):
                continue
            text = text.replace(i, dictp.get(i))
        return text
