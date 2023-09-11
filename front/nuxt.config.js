// const isProduction = process.env.NODE_ENV === 'production';

export default defineNuxtConfig({
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
    unlockPassword: '', // can be overridden by NUXT_UNLOCK_PASSWORD environment variable
    public: {
      apiBaseServer: '', // can be overridden by NUXT_PUBLIC_API_BASE_SERVER environment variable
      apiBase: '', // can be overridden by NUXT_PUBLIC_API_BASE environment variable
    },
  },
  // baseURL: isProduction ? 'https://dobrodelen.si' : 'http://localhost:8000',
});
