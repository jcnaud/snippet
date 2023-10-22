# RRD

Docker

# Links

Tutorial: https://oss.oetiker.ch/rrdtool/tut/rrdtutorial.en.html

Python lib: https://pypi.org/project/rrdtool/

## Vocabulary
| Accronyme | Definition | Description |
|- |- |- |
| PDP | Primary Data Point |
| RRA | Round Robin Archives |
| XFF | XFiles Factor | 0 <= xff < 1, Defines what part of a consolidation interval may be made up from UNKNOWN data while the consolidated value is still regarded as known |

## Usage

```bash
# Run the docker
docker run -it --name rrdtool haineault/rrdtool bash
```

In the docker:
```bash
cd 

# Create rrd
# Dataset named "speed", it's a "COUNTER" (i.e. like index increasing value)
# use --step 300 to change the default 5 minutes step
# Add 2 round robbin archive
# First RRA use "Average" on "1" PDP (i.e 1 data) (i.e. average change nothing) and keep last 24 samples
#   24 sample of 5 min = 2 hours
#Second RRA use "Average" on "6" PDP and keep last 10 samples
#   10 sample of 6 values (30min) = 5 hours

rrdtool create test.rrd             \
        --start 920804400          \
        DS:speed:COUNTER:600:U:U   \
        RRA:AVERAGE:0.5:1:24       \
        RRA:AVERAGE:0.5:6:10

# Add data
rrdtool update test.rrd 920804700:12345 920805000:12357 920805300:12363
rrdtool update test.rrd 920805600:12363 920805900:12363 920806200:12373
rrdtool update test.rrd 920806500:12383 920806800:12393 920807100:12399
rrdtool update test.rrd 920807400:12405 920807700:12411 920808000:12415
rrdtool update test.rrd 920808300:12420 920808600:12422 920808900:12423

#retrive data
rrdtool fetch test.rrd AVERAGE --start 920804400 --end 920809200
# Dispaly info
rrdtool info test.rrd
```

You can see le dataset ```ds[speed]``` and the to rra ```rra[0]``` and ```rra[1]```.


```bash
# create graph
rrdtool graph speed.png                                 \
    --start 920804400 --end 920808000               \
    DEF:myspeed=test.rrd:speed:AVERAGE              \
    LINE2:myspeed#FF0000
```

Dipaly inf
In your host
```bash
# Get the png result
docker cp rrdtool:/root/speed.png .
# Display it
display speed.png
```

On the docker
```bash
# Or
# create graph 2
rrdtool graph speed2.png                           \
    --start 920804400 --end 920808000               \
    --vertical-label m/s                            \
    DEF:myspeed=test.rrd:speed:AVERAGE              \
    CDEF:realspeed=myspeed,1000,\*                  \
    LINE2:realspeed#FF0000
```

In your host
```bash
# Get the png result
docker cp rrdtool:/root/speed2.png .
# Display it
display speed2.png
```


On the docker
```bash
# create graph 3
 rrdtool graph speed3.png                             \
      --start 920804400 --end 920808000               \
      --vertical-label km/h                           \
      DEF:myspeed=test.rrd:speed:AVERAGE              \
      "CDEF:kmh=myspeed,3600,*"                       \
      CDEF:fast=kmh,100,GT,kmh,0,IF                   \
      CDEF:good=kmh,100,GT,0,kmh,IF                   \
      HRULE:100#0000FF:"Maximum allowed"              \
      AREA:good#00FF00:"Good speed"                   \
      AREA:fast#FF0000:"Too fast"
```

In your host
```bash
# Get the png result
docker cp rrdtool:/root/speed3.png .
# Display it
display speed3.png
```



On the docker
```bash
# create graph 4
rrdtool graph speed4.png                           \
    --start 920804400 --end 920808000               \
    --vertical-label km/h                           \
    DEF:myspeed=test.rrd:speed:AVERAGE              \
    CDEF:nonans=myspeed,UN,0,myspeed,IF             \
    CDEF:kmh=nonans,3600,*                          \
    CDEF:fast=kmh,100,GT,100,0,IF                   \
    CDEF:over=kmh,100,GT,kmh,100,-,0,IF             \
    CDEF:good=kmh,100,GT,0,kmh,IF                   \
    HRULE:100#0000FF:"Maximum allowed"              \
    AREA:good#00FF00:"Good speed"                   \
    AREA:fast#550000:"Too fast"                     \
    STACK:over#FF0000:"Over speed"
```

In your host
```bash
# Get the png result
docker cp rrdtool:/root/speed4.png .
# Display it
display speed4.png
```


# Dispaly graph in HTML

Createa index.html
```html
<HTML><HEAD><TITLE>Speed</TITLE></HEAD><BODY>
<IMG src="speed2.png" alt="Speed in meters per second">
<BR>
<IMG src="speed3.png" alt="Speed in kilometers per hour">
<BR>
<IMG src="speed4.png" alt="Traveled too fast?">
</BODY></HTML>
```

Run python simple server on the same directory on index.html and speedX.png
```bash
python -m SimpleHTTPServer 8080
```

View the site on http://127.0.0.1:8080/

## Trick
Get the curent time
```bash
perl -e 'print time, "\n" '
```


## Using with python

```bash
cat <<EOF > example_rrd.py
import rrdtool

result = rrdtool.fetch("test.rrd", "AVERAGE")
start, end, step = result[0]
ds = result[1]
rows = result[2]
print('ds', ds)
print('rows', rows)
EOF
```


pip install python-rrdtool
