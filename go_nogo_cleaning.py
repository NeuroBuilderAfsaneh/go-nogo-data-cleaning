def summarize_rt(rt_list, low=150, high=1000):
    # low/high: example RT range in ms; set before looking at results
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


def excluded_participants(summary, max_excl=50):
    # max_excl: example cutoff (% of trials lost); set before looking at results
    result = []
    for name, s in summary.items():
        pct = (s['n_missing'] + s['n_out']) / s['n_total'] * 100
        if pct > max_excl:
            result.append(name)
    return result


# Simulated practice data (None = missing RT)
data = {
    'a': [450, 480, None, 460],
    'b': [90, 1500, None],
    'c': [500, 520, 510]
}

summary = {name: summarize_rt(rts) for name, rts in data.items()}

totals = {'n_missing': 0, 'n_out': 0, 'n_valid': 0, 'n_total': 0}
for name, s in summary.items():
    for key in totals:
        totals[key] += s[key]

print(summary)
print(totals)
print(excluded_participants(summary))

