# Short Wumpus World Simulation (Minimal)
import collections

class WumpusEnv:
    def __init__(s, size=4, w=(3,1), pits=[(3,3),(4,4)], g=(1,3), a=(1,1)):
        s.size,s.w,s.p,s.g,s.a=size,{w},set(pits),g,a; s.w_alive=True
    def in_bounds(s,p): return 1<=p[0]<=s.size and 1<=p[1]<=s.size
    def neigh(s,p): return [(p[0]+dr,p[1]+dc) for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)] if s.in_bounds((p[0]+dr,p[1]+dc))]
    def percept(s,p): return {"stench":any(n in s.w and s.w_alive for n in s.neigh(p)),
                              "breeze":any(n in s.p for n in s.neigh(p)),
                              "glitter":p==s.g}

class Agent:
    def __init__(s,env): s.e,s.pos,s.gold,s.safe,s.vis=env,env.a,0,{env.a},set()
    def bfs(s,goals):
        q=collections.deque([(s.pos,[s.pos])]); seen={s.pos}
        while q:
            cur,path=q.popleft()
            if cur in goals: return path[1:]
            for n in s.e.neigh(cur):
                if n not in seen and n in s.safe: q.append((n,path+[n])); seen.add(n)
        return []
    def step(s):
        s.vis.add(s.pos); p=s.e.percept(s.pos)
        if p["glitter"]: s.gold=1
        if not p["breeze"]: s.safe|=set(s.e.neigh(s.pos))
        path=s.bfs(s.safe-s.vis or {s.e.a})
        if path: s.pos=path[0]

def main():
    env,agent=WumpusEnv(),Agent(WumpusEnv())
    for _ in range(30):
        if agent.gold and agent.pos==env.a: break
        agent.step()
    print("Agent at",agent.pos,"Gold:",bool(agent.gold))

if __name__=="__main__": main()
