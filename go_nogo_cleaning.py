def summarize_rt(rt_list, low=150, high=1000):
    n_total = len(rt_list)
    present = [v for v in rt_list if v is not None]
    valid = [v for v in present if low <= v <= high]
    n_missing = n_total - len(present)
    n_out = len(present) - len(valid)
    if len(valid) == 0:
        mean = None
    else:
        mean = sum(valid) / len(valid)
    return {'mean': mean, 'n_valid': len(valid),
            'n_missing': n_missing, 'n_out': n_out, 'n_total': n_total}

data = {
    'a': [450, 480, None, 460],
    'b': [90, 1500, None],
    'c': [500, 520, 510]
}

summary = {}
for name, rts in data.items():
    summary[name] = summarize_rt(rts)

for name in summary:
    s = summary[name]
    ok = s['n_valid'] + s['n_missing'] + s['n_out'] == s['n_total']
    print(name, s, ok)
