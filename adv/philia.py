from core.advbase import *

def module():
    return Philia

class Philia(Adv):
    conf = {}
    conf['slots.a'] = ['Forest_Bonds', 'Primal_Crisis']
    conf['slots.poison.a'] = ['Resounding_Rendition', 'The_Fires_of_Hate']
    conf['acl'] = """
        `dragon(c3-s-end), s4.check()
        `s3, not buff(s3)
        `s4
        `s2
        `s1, cancel
        """
    conf['coabs'] = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['share'] = ['Curran']
    conf['afflict_res.paralysis'] = 0


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)