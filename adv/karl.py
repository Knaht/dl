if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Karl

class Karl(adv.Adv):
    a3 = ('a',0.08,'hp70')
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3,fsc
        `fs, seq=3
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)

