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
      {
        rel: 'apple-touch-icon',
        sizes: '180x180',
        href: '/apple-touch-icon.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '32x32',
        href: '/favicon-32x32.png',
      },
      {
        rel: 'icon',
        type: 'image/png',
        sizes: '16x16',
        href: '/favicon-16x16.png',
      },
      // { rel: 'manifest', href: '/site.webmanifest' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300i,400,400i,600,600i,700,900&display=swap&subset=latin-ext',
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
    '@nuxtjs/style-resources',
  ],
  /*
   ** Nuxt.js build modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
  ],
  /*
   ** Nuxt Style Resources
   ** See https://github.com/nuxt-community/style-resources-module
   */
  styleResources: {
    scss: ['~/assets/scss/_variables.scss'],
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: isProduction
      ? 'https://navigator.otcetnigo.mk'
      : 'http://back:8000',
  },
  /*
   ** Environment variables for webpack (via definePlugin)
   */
  env: {
    API_BASE_URL: isProduction
      ? 'https://navigator.otcetnigo.mk'
      : 'http://back:8000',
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
      config.module.rules.push({
        enforce: 'pre',
        test: /\.inc\.html$/,
        loader: 'raw-loader',
        exclude: /(node_modules)/,
      });
    },
  },
};
