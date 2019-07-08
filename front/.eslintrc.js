module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
  extends: [
    'prettier',
    'prettier/vue',
    'plugin:prettier/recommended',
    '@nuxtjs',
    'plugin:nuxt/recommended',
  ],
  plugins: ['prettier'],
  // add your custom rules here
  rules: {
    'no-console': 'warn',
    semi: ['error', 'always'],
    'comma-dangle': ['error', 'always-multiline'],
    'vue/singleline-html-element-content-newline': 'off',
    // 'vue/multiline-html-element-content-newline': 'off',
  },
};
