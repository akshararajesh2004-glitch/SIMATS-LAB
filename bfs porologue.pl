% Graph edges
edge(a,b). edge(a,c). edge(b,d). edge(c,g). edge(d,g).

% Heuristic values
h(a,5). h(b,3). h(c,4). h(d,2). h(g,0).

% Best First Search
bestfs(Start,Goal,Path):- bfs([[Start]],Goal,Path).
bfs([[Goal|Rest]|_],Goal,[Goal|Rest]).
bfs([[N|Rest]|_],Goal,Path):- 
    findall([X,N|Rest],(edge(N,X),\+member(X,[N|Rest])),New),
    sort_path(New,Sorted), bfs(Sorted,Goal,Path).

sort_path(Ps,Sorted):- map_list_to_pairs(fcost,Ps,Pairs),keysort(Pairs,S),pairs_values(S,Sorted).
fcost([N|_],C):- h(N,C).
