import re

# =========================================================
# RULE 50 : PREFIX NGE-
# contoh :
# ngecet -> cet
# ngebut -> kebut
# =========================================================
class DisambiguatorPrefixRuleSunda50(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^nge(.+)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                sisa,
                'k' + sisa,
                'g' + sisa,
                'c' + sisa,
                'p' + sisa,
                'b' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None

# =========================================================
# RULE 51 : PREFIX NGA-
# contoh : ngadahar -> dahar
# =========================================================
class DisambiguatorPrefixRuleSunda51(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^nga(.+)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                sisa,
                'g' + sisa,
                'k' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 52 : PREFIX NG- + vokal
# contoh :
# nginum -> inum
# ngorek -> korek
# =========================================================
class DisambiguatorPrefixRuleSunda52(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ng([aiueoé].*)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                sisa,
                'k' + sisa,
                'g' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 53 : PREFIX NG- + konsonan
# contoh :
# ngebrak -> gebrak
# =========================================================
class DisambiguatorPrefixRuleSunda53(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ng([bcdfghjklmnpqrstvwxyz].*)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                sisa,
                'k' + sisa,
                'g' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 54 : PREFIX N-
# contoh :
# nulis -> tulis
# =========================================================
class DisambiguatorPrefixRuleSunda54(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^n([aiueoé].*)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                't' + sisa,
                'd' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 55 : PREFIX NY-
# contoh :
# nyapu -> sapu
# nyebut -> sebut
# =========================================================
class DisambiguatorPrefixRuleSunda55(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ny(.+)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                'j' + sisa,
                's' + sisa,
                'c' + sisa, 
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 56 : PREFIX M-
# contoh :
# maca -> baca | ménta -> pénta
# =========================================================
class DisambiguatorPrefixRuleSunda56(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^m([aiueoé].*)$', word)

        if matches:
            sisa = matches.group(1)
            kandidat = [
                'b' + sisa,
                'p' + sisa,
            ]

            for hasil in kandidat:
                if hasil in kamus_dasar:
                    return hasil
        return None


# =========================================================
# RULE 57 : PREFIX DI-
# =========================================================
class DisambiguatorPrefixRuleSunda57(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^di(.+)$', word)

        if matches:
            hasil = matches.group(1)
            if len(hasil) >= 3:
                return hasil
        return None


# =========================================================
# RULE 58 : PREFIX KA-
# =========================================================
class DisambiguatorPrefixRuleSunda58(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ka(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None
    


# =========================================================
# RULE 58A : PREFIX RU-
# =========================================================
class DisambiguatorPrefixRuleSunda58A(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ru(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 59 : PREFIX PA-
# =========================================================
class DisambiguatorPrefixRuleSunda59(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None

        matches = re.match(r'^pa(.+)$', word)

        if matches:
            hasil = matches.group(1)            
            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 59A : PREFIX PAN-
# =========================================================
class DisambiguatorPrefixRuleSunda59A(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^pan(.+)$', word)

        if matches:
            hasil = matches.group(1)
            kandidat = [
                hasil,
                't' + hasil,
            ]

            for item in kandidat:
                if item in kamus_dasar:
                    return item
        return None


# =========================================================
# RULE 60 : PREFIX PANG-
# =========================================================
class DisambiguatorPrefixRuleSunda60(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^pang(.+)$', word )

        if matches:
            hasil = matches.group(1)

            kandidat = [
                hasil,
                'k' + hasil,
                'g' + hasil,
            ]

            for item in kandidat:
                if item in kamus_dasar:
                    return item
        return None


# =========================================================
# RULE 61 : PREFIX TI-
# =========================================================
class DisambiguatorPrefixRuleSunda61(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ti(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 61A : PREFIX ré-
# =========================================================
class DisambiguatorPrefixRuleSunda61A(object):
    def disambiguate(self, word, kamus_dasar):
        
        if word in kamus_dasar:
            return None
        matches = re.match(r'^ré(.+)$', word)

        if matches:
            hasil = matches.group(1)  

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 62 : PREFIX PI-
# =========================================================
class DisambiguatorPrefixRuleSunda62(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(
            r'^pi(.+)$',
            word
        )

        if matches:

            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil

        return None
    

# =========================================================
# RULE 62A : PREFIX PIKA-
# =========================================================
class DisambiguatorPrefixRuleSunda62A(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^pika(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 63 : PREFIX SA-
# =========================================================
class DisambiguatorPrefixRuleSunda63(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^sa(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 63A : PREFIX NYING-
# =========================================================
class DisambiguatorPrefixRuleSunda63A(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^nying(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 64 : PREFIX BA-
# =========================================================
class DisambiguatorPrefixRuleSunda64(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ba(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 65 : PREFIX KU-
# =========================================================
class DisambiguatorPrefixRuleSunda65(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ku(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 66 : PREFIX SI-
# =========================================================
class DisambiguatorPrefixRuleSunda66(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^si(.+)$', word)

        if matches:
            hasil = matches.group(1)

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 67 : PREFIX ting- / pating-
# =========================================================
class DisambiguatorPrefixRuleSunda67(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^(ting|pating)(.+)$', word)

        if matches:
            hasil = matches.group(2)

            if hasil in kamus_dasar:
                return hasil
        return None
    


# =========================================================
# RULE 68 : INFIKS -AL-
# contoh :
# laleumpang -> leumpang
# =========================================================
class DisambiguatorInfixRuleSunda68(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])al(.*)$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 69 : INFIKS -UM-
# contoh :
# gumeulis -> geulis
# =========================================================
class DisambiguatorInfixRuleSunda69(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^([bcdfghjklmnpqrstvwxyz])um(.*)$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None


# =========================================================
# RULE 70 : INFIKS -AR-
# contoh : barudak -> budak
# =========================================================
class DisambiguatorInfixRuleSunda70(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(
            r'^([bcdfghjklmnpqrstvwxyz])ar(.*)$', word
        )

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 70A : INFIKS -AM-
# contoh : 
# =========================================================
class DisambiguatorInfixRuleSunda70A(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(
            r'^([bcdfghjklmnpqrstvwxyz])am(.*)$', word
        )

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None

    
# =========================================================
# RULE 71 : INFIKS -AM-
# contoh : mamanggih -> manggih
# =========================================================
class DisambiguatorInfixRuleSunda71(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^([m])am(.*)$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    

# =========================================================
# RULE 72 : INFIKS -EK-
# contoh : kekembang -> kembang
# =========================================================
class DisambiguatorInfixRuleSunda72(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^([k])ek(.*)$', word)

        if matches:
            hasil = (
                matches.group(1) + matches.group(2)
            )

            suffixNotAllowed = hasil.endswith('er') or hasil.endswith('es') or hasil.endswith('mu')

            if hasil in kamus_dasar and not suffixNotAllowed:
                return hasil
        return None
    

# =========================================================
# RULE 73 : PREFIX KA-
# contoh : 
# =========================================================
class DisambiguatorPrefixRuleSunda73(object):
    def disambiguate(self, word, kamus_dasar):

        if word in kamus_dasar:
            return None
        matches = re.match(r'^ka([a-z]{3,})', word)

        if matches:
            hasil = (
                matches.group(1)
            )

            if hasil in kamus_dasar:
                return hasil
        return None
    
