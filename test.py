from utilities import *

class Memory(Exception): pass


def f():
    raise Memory()
def g(n):
    try: return f()
    except Memory: return Memory()
print parallelMap(4,g,range(9))
    






# def boundedMatch(observation, pattern, k=1):
#     N = len(observation)
#     M = len(pattern)

#     S = [[None]*(2*k+1) for _ in range(N + 1) ]

#     def get(n,m):
#         m = m - n + k
#         if m < 0 or m >= 2*k+1: return False
#         v = S[n][m]
#         assert v is not None
#         return v
#     def set(n,m,v):
#         m = m - n + k
#         assert m >= 0
#         assert m < 2*k+1
#         assert S[n][m] is None
#         S[n][m] = v

#     for n in xrange(N + 1):
#         #for m in range(n - k, n + k + 1):
#         # for _m in range(-k, k + 1):
#         for _m in range(0, 2*k + 1):
#             if n == 0: # does the pattern match the empty string
#                 v = _m - k + n == 0 or (_m - k + n == 1 and pattern[0] == '?')
#             elif _m - k + n < 0 or _m - k + n > M:
#                 v = False
#             elif _m - k + n == 0: # does the empty string match the pattern
#                 v = n == 0
#             else:
#                 token = pattern[_m - k + n - 1]
#                 if token == '*':
#                     # Because the table is actually diagonal...
#                     v = S[n - 1][_m]
#                     #v = get(n - 1,_m - k + n - 1)
#                 elif token == '?':
#                     v = S[n - 1][_m] or (_m - 1 >= 0 and S[n][_m - 1])

#                 else:
#                     v = S[n - 1][_m] and observation[n - 1] == token
#             #set(n,_m + n,v)
#             S[n][_m] = v
#             assert get(n,_m - k + n) == v
#     return M - N + k >= 0 and M - N + k <= 2*k and  S[N][M - N + k] # get(N,M)
                    
    

# def match(observation, pattern):
#     N = len(observation)
#     M = len(pattern)
#     t = {}
#     for n in xrange(N + 1):
#         for m in xrange(M + 1):
#             if n == 0:
#                 v = m == 0 or (m == 1 and pattern[0] == '?')
#             elif m == 0:
#                 v = n == 0
#             else:
#                 token = pattern[m - 1]
#                 if token == '*':
#                     v = t[(n - 1,m - 1)]
#                 elif token == '?':
#                     v = t[(n - 1,m - 1)] or (n <= N and t[(n,m - 1)])
#                 else:
#                     v = t[(n - 1,m - 1)] and observation[n - 1] == token
#             t[(n,m)] = v
#     return t[(N,M)]


# def test():
#     from random import choice
#     import re
#     def randomObservation():
#         return "".join([choice(map(str,range(10))) for _ in range(choice(range(2,10))) ])
#     def randomQuestion(template):
#         return "".join([choice(['?',c]) for c in template ])
#     def randomStar(template):
#         return "".join([choice(['*',c]) for c in template ])
#     for _ in xrange(1000):
#         x = randomObservation()
#         y = randomObservation()
#         for k in xrange(4):
#             assert boundedMatch(x,x,k)
#             assert boundedMatch(x,y,k) == boundedMatch(y,x,k)
#             assert boundedMatch(x,y,k) == (x == y)
#             p = randomQuestion(x)
#             assert boundedMatch(x,p,k)
#             p = randomStar(x)
#             assert boundedMatch(x,p,k)

#     def randomSmallObservation():
#         return "".join([choice(map(str,range(2))) for _ in range(choice(range(1,4))) ])
#     def randomSmallPattern():
#         while True:
#             p = "".join(choice("*?0101") for _ in range(choice(range(1,4))) )
#             if not p.startswith("??"): return p
#     for _ in xrange(10000):
#         x = randomSmallObservation()
#         p = randomSmallPattern()
#         r = "^" + p.replace('*','.').replace('?','.?') + "$"
#         print(boundedMatch(x,p,5))
#         print(re.match(r,x))
#         assert (re.match(r,x) is not None) == boundedMatch(x,p,5), "OBSERVATION %s\tPATTERN %s\tREGEX %s\tUNBOUNDEDMATCH %s"%(x,p,r,match(x,p))
# test()
# #assert match("1","?*")
# a = '13312'
# b =  '3322'
# p = '?33*2'
# print(boundedMatch(a,p))
# print(boundedMatch(b,p))
# print(boundedMatch(b,a))
# #print(boundedMatch(b,p))

# # import os

# # displaying = True
# # for j in range(1,4):#range(1,8):
# #     os.system('python Marcus.py  -t 20 -n %d --%s experiments/abb_noSyllables_%d.p %s -d 3 --noSyllables'%(j,
# #                                                                                                            'load' if displaying else 'save',
# #                                                                                                            j,
# #                                                                                                            '--quiet' if not displaying else ''))
# #     if j < 5:
# #         os.system('python Marcus.py  -t 20 -n %d --%s experiments/abb_%d.p  -d 2 %s'%(j,
# #                                                                                       'load' if displaying else 'save',
# #                                                                                       j,
# #                                                                                       '--quiet' if not displaying else ''))
