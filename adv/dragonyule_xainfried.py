from core.advbase import *

def module():
    return Dragonyule_Xainfried

class Dragonyule_Xainfried(Adv):
    comment = 'no s2'

    conf = {}
    conf['slots.a'] = ['A_Dogs_Day', 'Castle_Cheer_Corps']
    conf['slots.poison.a'] = conf['slots.a']
    conf['slots.d'] = 'Freyja'
    conf['acl'] = """
        `s4
        `s1
        `s3, x>2 or fsc
        `fs, x=5
        `dodge,fsc
        """
    conf['coabs'] = ['Dagger2','Bow','Tobias']
    conf['share'] = ['Marty','Tobias']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)

