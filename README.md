# Singapore Postal Codes


![Project screenshot](./screenshot.png)

code to list out / map out all Singapore postal codes.
<p align="left">
  <img src="https://docs.onemap.sg/maps/images/new-onemap-logo_150x150.png" />
</p>

## Disclaimer:
1. USE AT OWN DISCRETION
2. FOR EDUCATIONAL PURPOSES ONLY
3. USE OF THE DATA IS GOVERNED BY THE [OPEN DATA LICENCE](HTTPS://WWW.ONEMAP.SG/LEGAL/OPENDATALICENCE.HTML)
4. THIS DATA DUMP CONTAINS INFORMATION FROM ONEMAP.SG POSTAL CODE SEARCH ACCESSED ON 25 APR 2017, AND LATER

## Demo: 
1. (on map) \
https://www.google.com/maps/d/edit?mid=1xY0bu-Aomm-KcEXD58PxdvegZhY5Tcfv&usp=sharing
https://www.google.com/maps/d/edit?mid=19yBcM2JMVOwTZj8svFY2km1j2CXeL95y&usp=sharing
https://www.google.com/maps/d/edit?mid=1JWzJu_GFFe28B7UiSLuf52WqZ-7BhlYr&usp=sharing
2. (listed out) \
https://sg-postalcodes2017.glitch.me/


## Setup

The JSON-to-CSV utility runs on Windows and Linux. In an activated Python 3
virtual environment, install `pandas`, then explicitly select the input and output:

```sh
python -m pip install pandas
python code/jsontocsv.py "path/to/buildings.json" "path/to/buildings.csv"
```

Use `python3` if that is your Linux interpreter name. Quote paths containing
spaces. Relative paths are resolved from your current directory; no personal
Downloads folder is assumed. The output CSV is replaced if it already exists.
`python code/jsontocsv.py --help` does not read data or require pandas.

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
