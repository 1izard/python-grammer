import gc
found_objects = gc.get_objects()
print('{} objects before'.format(len(found_objects)))

import waste_memory
x = waste_memory.run()
found_objects = gc.get_objects()
print('{} objects after'.format(len(found_objects)))
for obj in found_objects:
    print(repr(obj)[:100])



import tracemalloc
tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()
import waste_memory
x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)

stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print('\n'.join(top.traceback.format()))
