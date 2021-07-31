# Installation (python 2.7 or 3.6+)

```bash
pip install -r requirements.txt
```



# Miscellaneous File Utilities


## convert_eol.py 

### Convert text file line endings

Usage

```bash
python convert_eol.py dos2unix file
```

## parallel_cmd.py

### Apply a command in parallel to a list of file


Usage

```bash

python parallel_cmd.py --command cmd --files list [--thread 2]

ls *.txt |  python parallel_cmd.py --command gzip --files -
```


## transpose.py 

### Transpose text file columns and rows

Usage

```bash
python transpose.py file
gunzip -c file.gz | python transpose.py -
```

 
## tsv2md.py
 
### Create markdown table from the beginning of a tsv file
 
 Usage

```bash
python tsv2md.py --file name [--line 1 --transpose]
```

Output

```bash
#$ python tsv2md.py --file tsv
filename               | line count
---------------------- | ----------
test/make_eol_files.sh | 12

#$ python tsv2md.py --file tsv --transpose
column     | example
---------- | ----------------------
filename   | test/make_eol_files.sh
line count | 12
```

## tsv2xlsx.py 

### Create an excel file from a tsv file or a list of tsv files


Usage

```bash
# tsv file
python tsv2xlsx.py -f tsv_file -x excel_filename.xlsx

# list of tsv files
python tsv2xlsx.py -l tsv_list -x excel_filename.xlsx
ls *.txt | python tsvlist2xlsx.py -l - -x excel_filename.xlsx
```

Parameters

    -f FILE, --file FILE      tsv file
    -l LIST, --list LIST      list of tsv files (one per line)
    -x EXCEL, --excel EXCEL   excel file name




# Miscellaneous Networking Utilities


## echo_udp.py - UDP Echo Server

Usage

```bash
python echo_udp.py host port
```
 
Output
```bash 
#$># python echo_udp.py localhost 12345
   starting up on localhost port 12345
   
   waiting to receive message
   received 4 bytes from ('127.0.0.1', 52837)
   PING
   sent 4 bytes back to ('127.0.0.1', 52837)
     
   waiting to receive message
 ```
 
  - Based on http://pymotw.com/2/socket/udp.html



 
## head_http.py - print URL http response header

Usage

```bash 
python head_http.py url
```

Output
```bash 
#$>#  python head_http.py github.com
  http://github.com:
  
  Server: GitHub.com
  Date: Wed, 03 Jun 2015 21:03:18 GMT
  Content-Type: text/html; charset=utf-8
  Transfer-Encoding: chunked
  Connection: close
  Status: 200 OK
  ...
```



 
## ip.py - get public IP address

Usage
 
```bash
python ip.py 
```

Output

```bash
      https://duckduckgo.com/?q=what+is+my+ip&ia=answer:
      IP: x.x.x.x
      
      http://checkip.dyndns.com/: 
      IP: x.x.x.x
```

 
## ping.py - check a remote host for reachability

Usage
```bash
 python ping.py host port
```

Output

```bash 
#$># sudo python ping.py 192.168.1.99 8888
  ping 192.168.1.99 port 8888
    - icmp is reachable
    -  tcp is NOT reachable
    -  udp is reachable
```

  - Require administrator/sudo privileges
  - Use GPLv2 code from https://github.com/samuel/python-ping/blob/master/ping.py
  


# Author

  David Laperriere <dlaperriere@outlook.com>
