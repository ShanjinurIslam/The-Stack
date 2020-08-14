#!/bin/bash

#!/bin/bash
directory=$1
mkdir $directory
mkdir $1.'/templates'
mkdir $1.'/static'
touch $1.'/main.py'
touch $1.'/run.sh'
touch $1.'/templates/index.htm'
printf "#!/bin/bash \nexport FLASK_APP=main.py \nexport FLASK_ENV=development \nflask run" >> $1.'/run.sh'
