# google-analytics-utils

This repository provides .

Follow the below steps to get started:

![alt CoverPic](https://github.com/nimeshkverma/google-analytics-utils/blob/master/images/cover_pic.jpg)

google-analytics-utils contains Python 2.7 utils for fetching data from Google Analytics.


## Usage

1. After cloning the repository, create a virtual enviroment and activate it.
   `virtualenv env_name`
   `source env_name/bin/activate`

2. Move into the `google-analytics-utils` directory where `requirements.txt` is. Execute the following command to install all the required `pip` packages
   `pip install -r requirements.txt`

3. Provide the neccesary credentials in `ga_utils/config.py` along with the location of `client_secrets.p12`

4. Import the `query_ga` function from `utils.py` module and provide arguments simmilar to the sample functions in `sample_ga_functions.py`


## How to Contribute

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull RequestThe scripts in this
