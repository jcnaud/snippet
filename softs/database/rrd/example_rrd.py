cat <<EOF > example_rrd.py
import rrdtool

result = rrdtool.fetch("test.rrd", "AVERAGE")
start, end, step = result[0]
ds = result[1]
rows = result[2]
print('ds', ds)
print('rows', rows)
EOF





