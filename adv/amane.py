if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Amane

class Amane(adv.Adv):
    a3 = ('bk',0.2)
    a1 = ('prep','75%')
    conf = {}
    acl12 = """
        `s1, seq=5 and cancel
        `s2, seq=5 and cancel
        `s3, seq=5 and cancel
        """
    acl21 = """
        `s2, seq=5 and cancel
        `s1, seq=5 and cancel
        `s3, seq=5
        """ 
    conf['acl'] = acl21


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)


