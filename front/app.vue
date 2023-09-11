<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup>
import '~/assets/scss/main.scss';

useHead({
  titleTemplate: (titleChunk) => {
    return `${titleChunk ? `${titleChunk} - ` : ''}Dobrodelen.si`;
  },
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
      rel: 'stylesheet',
      href: 'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300i,400,400i,600,600i,700,900&display=swap&subset=latin-ext',
    },
  ],
});
</script>
