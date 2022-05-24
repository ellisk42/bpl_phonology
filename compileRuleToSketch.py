from features import *
from sketch import *
from sketchSyntax import *
from rule import *

def compileRuleToSketch(b,r):
    source = compileRuleToSketch_(b,r)
    return defineFunction('Word','Word u, int unrollBound',source)

def compileRuleToSketch_(bank, rule):
    insertion = isinstance(rule.focus,EmptySpecification)
    deletion = isinstance(rule.structuralChange,EmptySpecification)
    mapping = rule.calculateMapping(bank)


    leftPrefix,leftGuard = compileLeftGuardToSketch(bank, rule.leftTriggers)
    rightPrefix,rightGuard = compileRightGuardToSketch(bank, rule.rightTriggers)

    if not insertion and not deletion:
        # introduce a function for applying the specification
        applyBody = []
        for x,y in mapping.iteritems():
            x = "phoneme_%d"%bank.phoneme2index[x]
            if y == None: applyBody.append("if (s == %s) assert 0;"%x)
            else:
                y = "phoneme_%d"%bank.phoneme2index[y]
                applyBody.append("if (s == %s) return %s;"%(x,y))
        applyBody.append('return s;')        
        ruleApplication = defineFunction('Sound','Sound s',"\n".join(applyBody))

        return leftPrefix + rightPrefix + '''
Sound[u.l] o;
for (int j = 0; j < u.l; j++) {
        assert j < unrollBound;
        o[j] = (%s && %s ? %s : u.s[j]);
}
return new Word(s = o,l = u.l);
'''%(leftGuard('j'),rightGuard('j + 1'),ruleApplication(Constant('u.s[j]')).sketch())
    
        
    if deletion:
        if rule.isGeminiRule():
            print "Sorry but I don't know how to handle Gemini rules"
            assert False
        for x,y in mapping.iteritems(): assert y == ''
        condition = " || ".join([ 'u.s[j] == phoneme_%d'%(bank.phoneme2index[x]) for x in mapping ])
        body = '''if (%s && %s && (%s)) {
assert triggered == 0; triggered = 1;
} else {
o[j - triggered] = u.s[j];
}
'''%(leftGuard('j'),rightGuard('j + 1'),condition)

        return leftPrefix + rightPrefix + '''
Sound[u.l] o;
int triggered = 0;
for (int j = 0; j < u.l; j++) {
        assert j < unrollBound;
        %s
}
return new Word(s = o[0::(u.l - triggered)],l = (u.l - triggered));
'''%(body)

    if insertion:
        insert = 'phoneme_%d'%(bank.phoneme2index[mapping['']])
        if rule.copyOffset != 0: print "I don't know how to handle copying rules"
        assert rule.copyOffset == 0

        return leftPrefix + rightPrefix + '''
Sound[u.l + 1] o;
int inserted = 0;
for (int j = 0; j <= u.l; j++) {
        assert j < unrollBound + 1;
        if (%s && %s) {
           assert inserted == 0;
           inserted = 1;
           o[j] = %s;
        }
        if (j < u.l) o[j + inserted] = u.s[j];
}
return new Word(s = o[0::(u.l + inserted)],l = u.l + inserted);
'''%(leftGuard('j'),rightGuard('j'),insert)

    assert False

def compileGuardToSketch(b,g):
    if g.side == 'R': return compileRightGuardToSketch(b,g)
    if g.side == 'L': return compileLeftGuardToSketch(b,g)
    raise Exception('Unknown guard side: %s'%g.side)

def compileLeftGuardToSketch(bank,g):
    if g.specifications == []:
        if g.endOfString:
            return '',lambda j: '(%s == 0)'%j
        else:
            return '',lambda j: '1'

    # For each specification, build a function that takes as input a
    # sketch variable and then tells you whether that's variable
    # matches something in the extension of the specification
    def buildExtension(s):
        return lambda v: "(" + " || ".join([ "(%s == phoneme_%d)"%(v,bank.phoneme2index[p]) for p in s.extension(bank) ]) + ")"
    specificationPredicates = map(buildExtension,g.specifications)

    if not g.starred:
        if len(specificationPredicates) == 1:
            if g.endOfString:
                return '', lambda j: '(%s == 1 && %s)'%(j,specificationPredicates[0]('u.s[0]'))
            else:
                return '', lambda j: '(%s > 0 && %s)'%(j,specificationPredicates[0]('u.s[%s - 1]'%j))
    
        if len(specificationPredicates) == 2:
            if g.endOfString:
                return '', lambda j: '(%s == 2 && %s && %s)'%(j,specificationPredicates[1]('u.s[0]'),specificationPredicates[0]('u.s[1]'))
            else:
                return '', lambda j: '(%s > 1 && %s && %s)'%(j,specificationPredicates[0]('u.s[%s - 1]'%j),specificationPredicates[1]('u.s[%s - 2]'%j))


    Prelude = '''
bit[u.l + 1] left_okay;
left_okay[0] = 0;
bit left_accepting = 0;
for (int j = 1; j <= u.l; j++) {
    assert j < unrollBound + 1;
    Sound this_sound = u.s[j - 1]; 
    bit this_is_okay = 1;
    bit stay_in_accepting_state = left_accepting && %s;
'''%(specificationPredicates[0]('this_sound'))
    if not g.endOfString:
        Prelude += '''
	left_accepting = %s || stay_in_accepting_state;
'''%(specificationPredicates[1]('this_sound'))
    else:
        Prelude += '''
	left_accepting = %s &&
	  (j == 1 || stay_in_accepting_state);
      '''%(specificationPredicates[1]('u.s[0]'))
    Prelude += '''
      this_is_okay = left_accepting;
    left_okay[j] = this_is_okay;
}
'''

    return Prelude,lambda j: 'left_okay[%s]'%j

def compileRightGuardToSketch(bank,g):
    if g.specifications == []:
        if g.endOfString:
            return '',lambda j: '(%s == u.l)'%j
        else:
            return '',lambda j: '1'

    # For each specification, build a function that takes as input a
    # sketch variable and then tells you whether that's variable
    # matches something in the extension of the specification
    def buildExtension(s):
        return lambda v: "(" + " || ".join([ "(%s == phoneme_%d)"%(v,bank.phoneme2index[p]) for p in s.extension(bank) ]) + ")"
    specificationPredicates = map(buildExtension,g.specifications)

    if not g.starred:
        if len(specificationPredicates) == 1:
            if g.endOfString:
                return '', lambda j: '(%s == u.l - 1 && %s)'%(j,specificationPredicates[0]('u.s[u.l - 1]'))
            else:
                return '', lambda j: '(%s < u.l && %s)'%(j,specificationPredicates[0]('u.s[%s]'%j))
    
        if len(specificationPredicates) == 2:
            if g.endOfString:
                return '', lambda j: '(%s == u.l - 2 && %s && %s)'%(j,
                                                                    specificationPredicates[1]('u.s[u.l - 1]'),
                                                                    specificationPredicates[0]('u.s[u.l - 2]'))
            else:
                return '', lambda j: '(%s + 1 < u.l && %s && %s)'%(j,
                                                                   specificationPredicates[0]('u.s[%s]'%j),
                                                                   specificationPredicates[1]('u.s[%s + 1]'%j))


    Prelude = '''
bit[u.l + 1] right_okay;
right_okay[u.l] = 0;
bit right_accepting = 0;
for (int j = 1; j <= u.l; j++) {
    assert j < unrollBound + 1;
    Sound this_sound = u.s[u.l - 1 - (j - 1)];
    bit this_is_okay = 1;
    bit stay_in_accepting_state = right_accepting && %s;
'''%(specificationPredicates[0]('this_sound'))
    if not g.endOfString:
        Prelude += '''
	right_accepting = %s || stay_in_accepting_state;
'''%(specificationPredicates[1]('this_sound'))
    else:
        Prelude += '''
	right_accepting = %s &&
	  (j == 1 || stay_in_accepting_state);
      '''%(specificationPredicates[1]('u.s[u.l - 1]'))
    Prelude += '''
      this_is_okay = right_accepting;
    right_okay[u.l - j] = this_is_okay;
}
'''

    return Prelude,lambda j: 'right_okay[%s]'%j


if __name__ == '__main__':
    Model.Global()
    
    b = FeatureBank([u"p",u"v",u"a",u"b"])
    print b.phonemes
    
    r = Guard('R', True, False, [FeatureMatrix([])])
    l = Guard('L', False, False, [])
    ru = Rule(FeatureMatrix([]),
              ConstantPhoneme(u'b'),
              l,r,0)
    print ru
    compiledRule = compileRuleToSketch(b,
                                       ru)
    print makeSketchSkeleton()
    print compiledRule(Constant('DUMMY'),Constant('DUMMY2'))

    
    # Prelude,predicate = compileGuardToSketch(b,r)
    # print Prelude
    # print predicate('j - 1')
            

    
