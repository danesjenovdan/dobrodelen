<template>
  <div class="page">
    <slot />
  </div>
</template>

<style lang="scss" scoped>
.page {
  background: #f6f2f0;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8rem 13rem;

  @include media-breakpoint-down(xl) {
    padding: 6rem 10rem;
  }

  @include media-breakpoint-down(sm) {
    height: auto;
    min-height: 100vh;
    padding: 2rem 1rem;
  }
}
</style>
