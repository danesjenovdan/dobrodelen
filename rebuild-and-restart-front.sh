# exit when any command fails
set -e

BASEDIR=$(dirname "$BASH_SOURCE")

cd $BASEDIR/front

# setup node version and env
source ~/.nvm/nvm.sh
nvm use 10

export NODE_ENV=production

npm install
npm run build
pm2 startOrRestart ecosystem.config.js
