import sys

plug_cnt, use_cnt = map(int, sys.stdin.readline().split())
if plug_cnt >= use_cnt :
  print(0)
  exit()

pull_list = list(map(int, sys.stdin.readline().split()))

plug_set = set()
cnt = 0

def pull_latest(idx) :
  result = 0
  max_idx = -1
  for num in plug_set :
    try :
      num_idx = pull_list[idx:].index(num)
    except :
      num_idx = use_cnt
    if max_idx < num_idx :
      result, max_idx = num, num_idx
  
  return result
  
for idx, num in enumerate(pull_list) :
  plug_set.add(num)
  if len(plug_set) > plug_cnt :
    cnt += 1
    latest_used = pull_latest(idx)

    plug_set.discard(latest_used)

print(cnt)