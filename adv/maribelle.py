if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Maribelle

class Maribelle(adv.Adv):
    a1 = ('s', 0.4, 'hp100')
    a3 = ('prep','100%')
    conf = {}
    conf['acl'] = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s1, pin == 'prep'
        """

if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

