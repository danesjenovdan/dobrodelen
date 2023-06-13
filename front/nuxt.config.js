// const isProduction = process.env.NODE_ENV === 'production';

export default defineNuxtConfig({
  /*
   ** Headers of the page
   */
  meta: {
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
        href: 'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300i,400,400i,600,600i,700,900&display=swap&subset=latin-ext',
      },
    ],
  },
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@import "~/assets/scss/_variables.scss";',
        },
      },
    },
    assetsInclude: ['**/*.inc.html'],
  },
  runtimeConfig: {
    public: {
      apiBaseServer: '', // can be overridden by NUXT_PUBLIC_API_BASE_SERVER environment variable
      apiBase: '', // can be overridden by NUXT_PUBLIC_API_BASE environment variable
    },
  },
  // baseURL: isProduction ? 'https://dobrodelen.si' : 'http://localhost:8000',
});
