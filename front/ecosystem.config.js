module.exports = {
  apps: [
    {
      name: 'dobrodelen-front',
      cwd: '/home/cnvos/dobrodelen/app/front',
      interpreter: 'node@10.16.2',
      script: 'npm',
      args: 'start',
      env: {
        NODE_ENV: 'production',
        NUXT_PORT: 3002,
        API_BASE_URL: 'http://dobrotest.djnd.si',
      },
      output: '/home/cnvos/dobrodelen/log/front.out.log',
      error: '/home/cnvos/dobrodelen/log/front.err.log',
      log: '/home/cnvos/dobrodelen/log/front.combined.log',
      log_date_format: 'YYYY-MM-DDTHH:mm:ssZ',
    },
  ],
};
