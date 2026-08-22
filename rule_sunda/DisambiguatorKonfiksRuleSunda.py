import re

# =========================================================
# RULE 74 : PREFIX MA-, SUFFIX N
# contoh : mamangsan -> mangsa
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda74(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ma([a-z]{4,})n$', word)

        if matches:

            hasil = (
                matches.group(1)
            )

            if hasil in kamus_dasar:
                return hasil
        return None

    
# =========================================================
# RULE 75 : PREFIX N-, SUFFIX AN
# contoh : nangenan -> tangen
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda75(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^n([a-z|é]{4,})an$', word)

        if matches:
            hasil = (
                "t" + matches.group(1)
            )

            if hasil in kamus_dasar:
                return hasil
        return None

    
# =========================================================
# RULE 76 : PREFIX PA-, INFIX DU, SUFFIX AN
# contoh : paduduaan -> dua
# =========================================================
class DisambiguatorPrefixInfixSuffixRuleSunda76(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^pa([a-z]{2})\1([a-z]*)an$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 77 : PREFIX PA-, SUFFIX AN
# contoh : papacangan -> pacang
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda77(object):
    def disambiguate(self, word, kamus_dasar):
        
        if word in kamus_dasar:
            return None

        matches = re.match(r'^([a-z]{2})\1([a-z|é]+)an$', word)

        if matches:
            hasil = (matches.group(1) + matches.group(2))

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 78 : PREFIX m-, SUFFIX an
# contoh : mamanahan -> panah
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda78(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^([m][a-z])\1([a-z]+)an$', word)

        if matches:
            hasil = ('p' + (matches.group(1) + matches.group(2))[1:])

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 79 : PREFIX ka-, SUFFIX na
# contoh : kapalayna -> palay
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda79(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^ka(?P<root>[a-z|é]{3,})na$', word)

        if matches:
            hasil = (
                matches.group('root')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 80 : PREFIX sa-, SUFFIX na
# contoh : saenyana -> enya
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda80(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^sa(?P<root>[a-z|é]{3,})na$', word)

        if matches:
            hasil = (
                matches.group('root')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 81 : PREFIX pang-, SUFFIX na
# contoh : panggedéna -> gede
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda81(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^pang(?P<root>[a-z|é]{3,})na$', word)

        if matches:
            hasil = (
                matches.group('root')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 82 : PREFIX bu-, SUFFIX na
# contoh : bubulakna -> bulak
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda82(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^([a-z]{2})\1([a-z]+)na$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 83 : PREFIX di-, SUFFIX keun
# contoh : dirérémokeun -> remo
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda83(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^(([a-z|é]{2})\2([a-z|é]*))keun$', word)

        if matches:
            hasil = (
                matches.group(2) + matches.group(3)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 84 : PREFIX ka-, SUFFIX an
# contoh : kasedihan -> sedih
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda84(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^ka(?P<root>[a-z|é]{3,})an$', word)

        if matches:
            hasil = (
                matches.group('root')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 85 : PREFIX po-, SUFFIX anana
# contoh : popohoanana -> poho
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda85(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^([a-z]{2})\1([a-z]+)anana$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 86 : PREFIX ny-, SUFFIX na
# contoh : nyebatna -> sebat
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda86(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^ny(?P<sisa>[a-z|é]+)na$', word)

        if matches:
            hasil = ('s' + matches.group('sisa'))

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 87 : PREFIX mang-, SUFFIX keun
# contoh : mangnyiduhkeun -> ciduh
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda87(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^mangny(?P<sisa>[a-z|é]+)keun$', word)

        if matches:
            hasil = (
                'c' + matches.group('sisa')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 88 : PREFIX pan-, SUFFIX an
# contoh : panungtungan -> tungtung
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda88(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^pan(?P<sisa>[a-z|é]+)an$', word)

        if matches:
            hasil = (
                't' + matches.group('sisa')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
# =========================================================
# RULE 89 : PREFIX ka-, SUFFIX lan
# contoh : katutuyulan -> tuluy
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda89(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(
            r'^ka(?P<ulang>[a-z]{2})\1(?P<sisa>[a-z|é]*)an$',
            word
        )

        if matches:
            hasil = (
                matches.group('ulang') + matches.group('sisa')
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 90 : PREFIX pi-, SUFFIX eun
# contoh : pibahayaeun -> bahaya
# =========================================================
class DisambiguatorPrefixSuffixRuleSunda90(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        
        matches = re.match(r'^pi(?P<root>[a-z|é]+)eun$', word)

        if matches:
            hasil = (
                matches.group('root')
            )

            if hasil in kamus_dasar:
                return hasil
        return None