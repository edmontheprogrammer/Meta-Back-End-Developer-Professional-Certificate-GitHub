norm = [0.908466, 0.979361, 1.98221, 0.450234, 0.589496, 0.971932, 0.399969,
        1.53483, 1.18957, 1.34351, 0.586966, 0.916839, 1.41549, 0.951392, 0.779738]
# data = norm[0][0:3], norm[0][3:6], norm[0][6:9], norm[0][9:12], norm[0][12:15]
# exclusions = [7], [11], [13]
# result = []
# for datum, exclusion in zip(data, exclusions):
#     m = mean(v for i, v in enumerate(datum) if i not in exclusion)
#     result.append(m)
# print(result)

for count, value in enumerate(norm):
    if count % 3 == 0:
        print(count)
    # print(count, value)

You need something like this. Then try to figure out what to do with the values. 
