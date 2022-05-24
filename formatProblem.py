def formatProblem(stuff, n, l = 0, r = 0, delimiter = u"	"):
    for x in stuff.splitlines():
        x = x.replace(u"#","").strip().split(delimiter)
        k = " ".join(x[n:])
        x = x[:n]
        x = (u',' + delimiter).join( u'u"%s"'%y for y in x)
        x = u"None,"*l + x + u",None"*r        
        print "(%s), # %s"%(x,k)
        
