const isProduction = process.env.NODE_ENV === 'production';

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: '',
    titleTemplate: (titleChunk) => {
      return `${titleChunk ? `${titleChunk} - ` : ''}Dobrodelen.si`;
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: '',
      },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700,900&display=swap&subset=latin-ext',
      },
    ],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~/assets/scss/main.scss'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/eslint-module',
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: isProduction ? '/' : 'http://localhost:8000',
  },
  /*
   ** Environment variables for webpack (via definePlugin)
   */
  env: {
    API_BASE_URL: isProduction ? '/' : 'http://localhost:8000',
  },
  /*
   ** Build configuration
   */
  build: {
    // extractCSS: true,
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      // inject variables import to all scss modules
      const scssRule = config.module.rules.find((e) => e.test.toString() === '/\\.scss$/i');
      const scssUses = scssRule.oneOf ? scssRule.oneOf.map((r) => r.use) : [scssRule.use];
      scssUses.forEach((use) => {
        const sassLoader = use.find((e) => e.loader === 'sass-loader');
        if (sassLoader) {
          sassLoader.options = sassLoader.options || {};
          sassLoader.options.data = `
            @import '~/assets/scss/_variables.scss';
          `;
          // sassLoader.options.functions = scssCustomFunctions;
        }
      });
    },
  },
};
