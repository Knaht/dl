import adv_test
import adv
from slot.a import *

def module():
    return Melody

class Melody(adv.Adv):
    comment = 'RR+Bellathorna & no s2 & 5000 team dps'
    conf = {}
    a1 = ('cc',0.08,'hp100')
    import slot
    if 1:
        conf['slots.a'] = slot.a.Bellathorna()+slot.a.RR()
        #conf['slots.a'] = Halidom_Grooms() + Bellathorna()
    else:
        conf['slots.a'] = slot.a.Bellathorna()+slot.a.LC()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s3, seq=5
        """
    adv_test.team_dps = 5000
    adv_test.test(module(), conf, verbose=-2)

