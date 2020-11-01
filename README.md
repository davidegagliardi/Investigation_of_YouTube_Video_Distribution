# Multimedia Services in Internet D
## Investigation of YouTube Video Distribution

*Aalto University, School of Electrical Engineering - A.Y. 2020/2021*

Davide Gagliardi - 880563 - davide.gagliardi@aalto.fi
<br>
Davide Galvan    - 881452 - davide.galvan@aalto.fi

### Installation

Clone the repository to your own instance:
```sh
git clone https://github.com/davidegagliardi/Investigation_of_YouTube_Video_Distribution
```

Enter in the folder and set up the environment:
```sh
cd Investigation_of_YouTube_Video_Distribution
[~/Investigation_of_YouTube_Video_Distribution] sudo sh setup_env.sh
```

Start the crawl:
```sh
[~/Investigation_of_YouTube_Video_Distribution] python start_crawl.py $(cat videolist.txt)
```

The result will be saved inside the `databases` folder (SQLite file) and `logs` folder (log file)

The SQLite can be easily opened with an online tool (https://sqliteonline.com/) or parsed thanks to scripts present in the `parsing` folder.
