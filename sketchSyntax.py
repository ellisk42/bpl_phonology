# DSL independent model generation code
# Focuses on generating and parsing the syntax of sketch/webppl programs

import re

class Expression:
    def __add__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return Addition(self,o)
    def __mul__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return Multiplication(self,o)
    def __sub__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return Subtraction(self,o)
    def __eq__(self,o):
        if not isinstance(o,Expression):
            o = Constant(o)
        return Equals(self,o)
    def __ne__(self,o):
        if not isinstance(o,Expression):
            o = Constant(o)
        return NotEquals(self,o)
    def __le__(self,o):
        if not isinstance(o,Expression):
            o = Constant(o)
        return LessThanOrEqual(self,o)
    def __ge__(self,o):
        if not isinstance(o,Expression):
            o = Constant(o)
        return GreaterThanOrEqual(self,o)
    def __gt__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return GreaterThan(o,self)
    def __lt__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return LessThan(self,o)
    def __str__(self): return self.sketch()
    def __radd__(self,o):
        if not isinstance(o,Expression): o = Constant(o)
        return Addition(self,o)

class FunctionCall(Expression):
    def __init__(self, f, arguments):
        self.f = f
        self.x = arguments
        assert all([isinstance(a,Expression) for a in arguments ])
    def sketch(self):
        return str(self.f) + "(" + ", ".join([a.sketch() for a in self.x ]) + ")"

class Variable(Expression):
    def __init__(self,n,definingFunction = None):
        self.n = n
        self.definingFunction = definingFunction
    def __str__(self):
        if self.definingFunction == None: return self.n
        return "#<%s : %s>"%(self.n,self.definingFunction)
    def registerDefiningFunction(self,fn):
        assert self.definingFunction == None
        self.definingFunction = fn
        return self        
    def sketch(self): return self.n

class Constant(Expression):
    def __init__(self,k): self.k = str(k)
    def sketch(self): return self.k
    def web(self): return self.k

class LessThan(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) < (%s))" % (self.a.sketch(), self.b.sketch())

class GreaterThan(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) > (%s))" % (self.a.sketch(), self.b.sketch())

class Equals(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) == (%s))" % (self.a.sketch(), self.b.sketch())

class NotEquals(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) != (%s))" % (self.a.sketch(), self.b.sketch())

class GreaterThanOrEqual(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) >= (%s))" % (self.a.sketch(), self.b.sketch())

class LessThanOrEqual(Expression):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        assert isinstance(a,Expression)
        assert isinstance(b,Expression)
    def sketch(self): return "((%s) <= (%s))" % (self.a.sketch(), self.b.sketch())

class Array(Expression):
    def __init__(self,elements):
        self.elements = elements
        assert all([isinstance(x,Expression) for x in elements ])
    def sketch(self):
        return "{%s}" % ", ".join([ e.sketch() for e in self.elements ])
    

class Minimize():
    def __init__(self,n):
        self.n = n
        assert isinstance(n,Expression)
    def sketch(self): return "minimize(%s);" % self.n.sketch()
class Maximize():
    def __init__(self,n):
        self.n = n
        assert isinstance(n,Expression)
    def sketch(self): return "minimize(10 - (%s));" % self.n.sketch()

class Definition():
    def __init__(self, ty, name, value):
        self.ty = ty
        self.name = name
        self.value = value
        assert isinstance(value,Expression)
    def sketch(self):
        return "%s %s = %s;" % (self.ty,self.name,self.value.sketch())
    def web(self):
        return "var %s = %s" % (self.name,self.value.web())

class Conditional(Expression):
    def __init__(self,t,y,n):
        self.t = t
        self.y = y
        self.n = n
        assert isinstance(t,Expression)
        assert isinstance(y,Expression)
        assert isinstance(n,Expression)
    def sketch(self):
        return "((%s) ? %s : %s)" % (self.t.sketch(),self.y.sketch(),self.n.sketch())

class And(Expression):
    def __init__(self,clauses):
        self.clauses = clauses
        assert all([isinstance(c,Expression) for c in clauses ])
    def sketch(self):
        return "(%s)" % (" && ".join([c.sketch() for c in self.clauses ]))

class Not(Expression):
    def __init__(self,clause):
        self.clause = clause
        assert isinstance(clause,Expression)
    def sketch(self):
        return "(!(%s))" % (self.clause.sketch())

class Or(Expression):
    def __init__(self,clauses):
        self.clauses = clauses
        assert all([isinstance(c,Expression) for c in clauses ])
    def sketch(self):
        return "(%s)" % (" || ".join([c.sketch() for c in self.clauses ]))

class Assertion():
    def __init__(self,p):
        self.p = p
        assert isinstance(p,Expression)
    def sketch(self): return "assert %s;" % self.p.sketch()

class QuantifiedAssertion():
    def __init__(self,p,i):
        self.p = p
        self.i = i
        assert isinstance(p,Expression)
    def sketch(self): return "if (__ASSERTIONCOUNT__ == %d) assert %s;" % (self.i, str(self.p))

    
class Addition(Expression):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        assert isinstance(x,Expression)
        assert isinstance(y,Expression)
    def sketch(self): return "((%s) + (%s))" % (self.x.sketch(),self.y.sketch())
class Multiplication(Expression):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sketch(self): return "((%s) * (%s))" % (self.x.sketch(),self.y.sketch())
class Subtraction(Expression):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sketch(self): return "((%s) - (%s))" % (self.x.sketch(),self.y.sketch())

class Model():
    def __init__(self):
        self.flipCounter = 0
        self.integerSizes = []
        self.definitionCounter = 0
        self.definedFunctions = []
        self.statements = []
        self.quantifiedConditions = 0
        self.preprocessorDefinitions = {}
        self.auxiliaryHarnesses = []
        self.globalConstants = []
    def auxiliaryHarness(self,k):
        self.auxiliaryHarnesses.append(k)
    def preprocessorDefinition(self,k,v):
        self.preprocessorDefinitions[k] = v
    def flip(self, p = 0.5):
        self.flipCounter += 1
        return Variable("__FLIP__%d"%self.flipCounter)
    def unknownInteger(self, numberOfBits = None):
        self.integerSizes.append(numberOfBits)
        return Variable("__INTEGER__%d"%(len(self.integerSizes)))
    def defineFunction(self,returnValue, arguments, body):
        k = len(self.definedFunctions)
        self.definedFunctions.append("%s specialDefinedFunction_%d(%s){\n%s\n}"%(returnValue,
                                                                                 k,
                                                                                 arguments,
                                                                                 body))
        return lambda *a: FunctionCall("specialDefinedFunction_%d"%k,a)
    def globalConstant(self, ty, value):
        name = "__globalConstant_%s_%d__"%(ty,len(self.globalConstants))
        self.globalConstants.append("%s %s = %s;"%(ty,name,value.sketch()))
        return Variable(name)
    def define(self, ty, value, globalToHarnesses = False):
        name = "__DEFINITION__%d"%self.definitionCounter
        globalName = "__GLOBALDEFINITION__%d"%self.definitionCounter
        self.definitionCounter += 1
        if globalToHarnesses:
            self.definedFunctions.append('%s %s() { return %s; }'%(ty,globalName,value))
            return self.globalConstant(ty, FunctionCall(globalName, [])).registerDefiningFunction(globalName)
        else:
            self.statements.append(Definition(ty, name, value))
            return Variable(name)
    def condition(self, predicate):
        self.statements.append(Assertion(predicate))
    def quantifiedCondition(self, predicate):
        self.quantifiedConditions += 1
        self.statements.append(QuantifiedAssertion(predicate,self.quantifiedConditions))
    def minimize(self, expression):
        self.statements.append(Minimize(expression))
    def maximize(self, expression):
        self.statements.append(Maximize(expression))
    def removeSoftConstraints(self):
        '''removes all minimize and maximize statements that have been previously added.'''
        self.statements = [ s for s in self.statements if not (s is Maximize or s is Minimize) ]

    def sketch(self):
        h = ""
            
        for f in range(self.flipCounter):
            h += "bit __FLIP__%d = ??;\n" % (f + 1)
        for f,s in enumerate(self.integerSizes):
            h += "int __INTEGER__%d = ??%s;\n" % (f + 1, '' if s == None else '(%d)'%s)

        h += "\n".join(self.definedFunctions)

        globalDefinitionPrefix = "\n".join(self.globalConstants)

        h += "\nharness void main() {\n"
        h += globalDefinitionPrefix + "\n"
        for a in self.statements:
            h += "\t" + a.sketch() + "\n"
        h += "}\n"

        for j,a in enumerate(self.auxiliaryHarnesses):
            h += "\nharness void auxiliaryHarness_%d() {\n%s\n assert (%s);\n}\n"%(j,globalDefinitionPrefix, a.sketch())
            
        return h
    @staticmethod
    def Global():
        global currentModel
        currentModel = Model()
        return currentModel
    
currentModel = None


def flip(p = 0.5):
    global currentModel
    return currentModel.flip(p)
def unknownInteger(numberOfBits = None):
    global currentModel
    return currentModel.unknownInteger(numberOfBits = numberOfBits)
def ite(condition,yes,no):
    return Conditional(condition,yes,no)

def define(ty, value, globalToHarnesses = False):
    return currentModel.define(ty, value, globalToHarnesses = globalToHarnesses)
def globalConstant(ty, value):
    return currentModel.globalConstant(ty, value)
def defineFunction(returnType,arguments,body):
    return currentModel.defineFunction(returnType,arguments,body)
def definePreprocessor(k,v):
    currentModel.preprocessorDefinition(k,v)
def currentModelPreprocessorDefinitions():
    return currentModel.preprocessorDefinitions

def condition(predicate):
    currentModel.condition(predicate)

def auxiliaryCondition(predicate):
    currentModel.auxiliaryHarness(predicate)

def quantifiedCondition(predicate):
    currentModel.quantifiedCondition(predicate)

def minimize(expression):
    currentModel.minimize(expression)

def maximize(expression):
    currentModel.maximize(expression)

def removeSoftConstraints():
    currentModel.removeSoftConstraints()

def sketchImplementation(name):
    def namedImplementation(f):
        def wrapper(*args, **kwargs):
            return FunctionCall(name, args)
        return wrapper
    return namedImplementation

def conditionMutuallyExclusive(flags):
    for j in range(len(flags) - 1):
        for k in range(j + 1,len(flags)):
            condition(Not(And([flags[j],flags[k]])))

def makeSketchSkeleton():
    return currentModel.sketch()

def parseFlip(output, variable):
    pattern = 'void glblInit_%s__ANONYMOUS_'%str(variable)
    ls = output.splitlines()
    for l in range(len(ls)):
        if pattern in ls[l]:
            return " = 1;" in ls[l + 2]
    print "Could not find",variable
    print pattern
    print output
    return None
def parseInteger(output, variable):
    pattern = 'void glblInit_%s__ANONYMOUS_'%str(variable)
    ls = output.splitlines()
    for l in range(len(ls)):
        if pattern in ls[l]:
            m = re.search(" = ([0-9]+);", ls[l + 2])
            if not m:
                raise Exception('error parsing integer')
            return int(m.group(1))
    print "Could not find",variable
    print pattern
    print output
    return None
def parseMinimalCostValue(output):
    v = None
    for l in output.splitlines():
        if '*********INSIDE minimizeHoleValue' in l:
             #*********INSIDE minimizeHoleValue, mhsize=1 current value of H__BND0=12,
             m = re.search('H__BND[0-9]=([0-9]+),',l)
             if not m:
                 raise Exception('Error parsing minimize hole value: %s'%l)
             vp = int(m.group(1))
             if v != None:
                 # Actually, this is okay due to CEGIS/auxiliary harnesses
                 #assert vp < v
                 pass
             v = vp
    return v
def parseMinimalCostValues(output):
    v = None
    for l in output.splitlines():
        if '*********INSIDE minimizeHoleValue' in l:
             #*********INSIDE minimizeHoleValue, mhsize=[0-9] current value of H__BND0=12,
             vp = [ int(m.group(1))
                    for m in re.finditer('H__BND[0-9]=([0-9]+),',l) ]
             if vp == []:
                 raise Exception('Error parsing minimize hole values: %s'%l)
             if v != None:
                 # At least one of them has to be better
                 assert any([ new < old for old,new in zip(v,vp) ])
                 # And none of them can be worse
                 assert not any([ old < new for old,new in zip(v,vp) ])
             v = vp
    return v
             
def getGeneratorDefinition(generatorName, output):
    readingGenerator = False
    body = []
    for l in output.splitlines():
        if l.startswith('void %s'%generatorName):
            readingGenerator = True
        elif readingGenerator:
            body.append(l)
            if '_out = _out' in l:
                m = re.search('_out = _(.*);',l)
                assert m
                return Variable('_' + m.group(1)), "\n".join(body)
    raise Exception('getGeneratorDefinition: %s\n%s'%(generatorName, output))
